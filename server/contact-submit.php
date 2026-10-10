<?php
/**
 * D'ALMA CLINIC - endpoint del formulario de contacto.
 *
 * Flujo: navegador (fetch JSON) -> este PHP -> Google Apps Script -> correo a la clinica.
 * La configuracion privada (URL HTTPS del Apps Script, secreto compartido y secreto de
 * Turnstile; los tres obligatorios) vive FUERA de public_html:
 *     <home de la cuenta>/dalma_private/contact-config.php
 * y devuelve un array. Ver server/contact-config.example.php para su forma (sin valores).
 *
 * Respuestas: SOLO {"ok":true} o {"ok":false}. Nunca se devuelve ni se registra ningun dato
 * del visitante, secreto, URL interna ni detalle de error.
 */

declare(strict_types=1);

ini_set('display_errors', '0');
ini_set('log_errors', '0');

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex, nofollow');
header('X-Content-Type-Options: nosniff');

function dalma_fail(int $status = 200): void
{
    http_response_code($status);
    echo '{"ok":false}';
    exit;
}

/** URL https absoluta, con host y sin credenciales embebidas. */
function dalma_https_url_ok($url): bool
{
    if (!is_string($url) || $url === '' || strlen($url) > 2048) {
        return false;
    }
    $p = parse_url($url);
    return is_array($p)
        && isset($p['scheme'], $p['host'])
        && strtolower((string) $p['scheme']) === 'https'
        && $p['host'] !== ''
        && !isset($p['user'])
        && !isset($p['pass']);
}

/** Secreto de Turnstile: cadena no vacia con el alfabeto de las claves de Cloudflare. */
function dalma_turnstile_secret_ok($secret): bool
{
    return is_string($secret) && preg_match('/^[A-Za-z0-9_-]{16,128}$/', $secret) === 1;
}

/** Opciones cURL comunes: verificacion TLS explicita y solo HTTPS (tambien en redirecciones). */
function dalma_curl_secure_opts(): array
{
    $opts = [
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_SSL_VERIFYHOST => 2,
    ];
    if (defined('CURLOPT_PROTOCOLS') && defined('CURLPROTO_HTTPS')) {
        $opts[CURLOPT_PROTOCOLS] = CURLPROTO_HTTPS;
    }
    if (defined('CURLOPT_REDIR_PROTOCOLS') && defined('CURLPROTO_HTTPS')) {
        $opts[CURLOPT_REDIR_PROTOCOLS] = CURLPROTO_HTTPS;
    }
    return $opts;
}

// ---------------------------------------------------------------------------
// Rate limiting basico por origen (sin base de datos, sin PII en claro).
//
//  - Origen: IP del visitante resuelta detras de Cloudflare / CDN de Hostinger (ver
//    dalma_client_ip_bin). Nunca se guarda ni se registra en claro: solo un HMAC-SHA256
//    (clave derivada de shared_secret) truncado, que es el nombre del archivo de estado.
//  - Estado: un archivo JSON diminuto por origen en <cuenta>/dalma_private/rate-limit/
//    (fuera de public_html, carpeta 700) con marcas de tiempo, sin datos del mensaje.
//  - Limites por ventana deslizante: DALMA_RL_MAX_SENDS envios (reservados antes de llamar
//    a Apps Script; se liberan si el envio falla) y DALMA_RL_MAX_ATTEMPTS intentos que
//    llegan a verificacion externa (Turnstile/Apps Script). Los rechazos por validacion
//    o honeypot ocurren antes y no consumen cupo.
//  - Caducidad: cada escritura poda lo vencido y ~1 de cada 20 peticiones borra archivos
//    sin actividad hace mas de la ventana (+60 s).
// ---------------------------------------------------------------------------
const DALMA_RL_WINDOW       = 900; // segundos (15 min)
const DALMA_RL_MAX_SENDS    = 3;   // envios por origen y ventana
const DALMA_RL_MAX_ATTEMPTS = 8;   // intentos por origen y ventana

// Proxies cuyo X-Forwarded-For se considera confiable: rangos publicados de Cloudflare
// (https://www.cloudflare.com/ips) y rangos privados/loopback. Si Cloudflare agrega rangos,
// actualizar esta lista; si no, el origen caeria al proxy y compartiria cupo.
const DALMA_TRUSTED_PROXY_RANGES = [
    '173.245.48.0/20', '103.21.244.0/22', '103.22.200.0/22', '103.31.4.0/22',
    '141.101.64.0/18', '108.162.192.0/18', '190.93.240.0/20', '188.114.96.0/20',
    '197.234.240.0/22', '198.41.128.0/17', '162.158.0.0/15', '104.16.0.0/13',
    '104.24.0.0/14', '172.64.0.0/13', '131.0.72.0/22',
    '2400:cb00::/32', '2606:4700::/32', '2803:f800::/32', '2405:b500::/32',
    '2405:8100::/32', '2a06:98c0::/29', '2c0f:f248::/32',
    '10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '127.0.0.0/8', '::1/128', 'fc00::/7',
];

/** Texto de IP -> binario (4 u 16 bytes; IPv4-mapeada se reduce a 4) o null si no es valida. */
function dalma_parse_ip(string $text): ?string
{
    $bin = @inet_pton($text);
    if ($bin === false) {
        return null;
    }
    if (strlen($bin) === 16 && substr($bin, 0, 12) === "\0\0\0\0\0\0\0\0\0\0\xff\xff") {
        return substr($bin, 12);
    }
    return $bin;
}

function dalma_ip_in_range(string $bin, string $cidr): bool
{
    [$net, $bits] = explode('/', $cidr, 2);
    $netBin = dalma_parse_ip($net);
    if ($netBin === null || strlen($netBin) !== strlen($bin)) {
        return false;
    }
    $bits  = (int) $bits;
    $bytes = intdiv($bits, 8);
    if ($bytes > 0 && substr($bin, 0, $bytes) !== substr($netBin, 0, $bytes)) {
        return false;
    }
    $rem = $bits % 8;
    if ($rem === 0) {
        return true;
    }
    $mask = (0xFF << (8 - $rem)) & 0xFF;
    return (ord($bin[$bytes]) & $mask) === (ord($netBin[$bytes]) & $mask);
}

function dalma_is_trusted_proxy(string $bin): bool
{
    foreach (DALMA_TRUSTED_PROXY_RANGES as $cidr) {
        if (dalma_ip_in_range($bin, $cidr)) {
            return true;
        }
    }
    return false;
}

/**
 * IP del visitante (binaria) o null. Solo se lee X-Forwarded-For cuando el par TCP
 * (REMOTE_ADDR) es un proxy de confianza; la lista se recorre de derecha a izquierda y se
 * toma la primera entrada que NO es proxy de confianza. Lo que el cliente antepone a la
 * cadena queda a la izquierda de lo que agregan Cloudflare/Hostinger, por lo que no puede
 * elegir otra IP. Si el par no es de confianza, se usa REMOTE_ADDR y se ignora cualquier header.
 */
function dalma_client_ip_bin(): ?string
{
    $peer = dalma_parse_ip((string) ($_SERVER['REMOTE_ADDR'] ?? ''));
    if ($peer === null) {
        return null;
    }
    if (dalma_is_trusted_proxy($peer)) {
        $xff = (string) ($_SERVER['HTTP_X_FORWARDED_FOR'] ?? '');
        if ($xff !== '' && strlen($xff) <= 512) {
            foreach (array_reverse(explode(',', $xff)) as $entry) {
                $ip = dalma_parse_ip(trim($entry));
                if ($ip === null) {
                    break;
                }
                if (!dalma_is_trusted_proxy($ip)) {
                    return $ip;
                }
            }
        }
    }
    return $peer;
}

/** Clave del origen: HMAC no reversible; IPv6 se agrupa por /64. */
function dalma_rl_key(string $bin, string $secret): string
{
    if (strlen($bin) === 16) {
        $bin = substr($bin, 0, 8);
    }
    $key = hash('sha256', 'dalma-rl-v1|' . $secret, true);
    return substr(hash_hmac('sha256', $bin, $key), 0, 40);
}

/** Lee y poda el estado; el llamador ya tiene el flock. @return array{0:int[],1:int[]} */
function dalma_rl_load($fh, int $now): array
{
    rewind($fh);
    $st   = json_decode((string) stream_get_contents($fh), true);
    $keep = static function ($list) use ($now): array {
        $out = [];
        if (is_array($list)) {
            foreach ($list as $t) {
                if (is_int($t) && $t > $now - DALMA_RL_WINDOW) {
                    $out[] = $t;
                }
            }
        }
        return $out;
    };
    return [$keep($st['a'] ?? null), $keep($st['s'] ?? null)];
}

function dalma_rl_save($fh, array $a, array $s): bool
{
    $json = (string) json_encode(['a' => $a, 's' => $s]);
    if (!ftruncate($fh, 0) || !rewind($fh)) {
        return false;
    }
    $written = fwrite($fh, $json);
    return $written !== false && $written === strlen($json) && fflush($fh);
}

/** Reserva un envio. @return array{0:string,1:int} ['ok'|'blocked'|'skip' (almacenamiento no disponible), marca de tiempo] */
function dalma_rl_reserve(string $file, int $now): array
{
    $fh = @fopen($file, 'c+');
    if ($fh === false) {
        return ['skip', 0];
    }
    if (!flock($fh, LOCK_EX)) {
        fclose($fh);
        return ['skip', 0];
    }
    [$a, $s] = dalma_rl_load($fh, $now);
    if (count($s) >= DALMA_RL_MAX_SENDS || count($a) >= DALMA_RL_MAX_ATTEMPTS) {
        flock($fh, LOCK_UN);
        fclose($fh);
        return ['blocked', 0];
    }
    $a[] = $now;
    $s[] = $now;
    $saved = dalma_rl_save($fh, $a, $s);
    flock($fh, LOCK_UN);
    fclose($fh);
    if (!$saved) {
        return ['skip', 0]; // no se pudo registrar el cupo: el llamador rechaza
    }
    @chmod($file, 0600);
    return ['ok', $now];
}

/** Devuelve el cupo de envio (el intento sigue contando) cuando el envio no se completo. */
function dalma_rl_release(string $file, int $slot, int $now): void
{
    $fh = @fopen($file, 'c+');
    if ($fh === false) {
        return;
    }
    if (flock($fh, LOCK_EX)) {
        [$a, $s] = dalma_rl_load($fh, $now);
        $i = array_search($slot, $s, true);
        if ($i !== false) {
            array_splice($s, (int) $i, 1);
        }
        dalma_rl_save($fh, $a, $s);
        flock($fh, LOCK_UN);
    }
    fclose($fh);
}

/** Borra archivos de estado sin actividad hace mas de la ventana (+60 s). */
function dalma_rl_purge(string $dir, int $now): void
{
    $names = @scandir($dir);
    if (!is_array($names)) {
        return;
    }
    $limit = $now - DALMA_RL_WINDOW - 60;
    foreach ($names as $name) {
        if (!preg_match('/^[0-9a-f]{40}$/', $name)) {
            continue;
        }
        $mtime = @filemtime($dir . '/' . $name);
        if ($mtime !== false && $mtime < $limit) {
            @unlink($dir . '/' . $name);
        }
    }
}

// 1. Solo POST.
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    dalma_fail(405);
}

// 2. Solo application/json.
$contentType = strtolower((string) ($_SERVER['CONTENT_TYPE'] ?? ''));
if (strpos($contentType, 'application/json') !== 0) {
    dalma_fail(415);
}

// 3. Tamano maximo de la peticion.
const DALMA_MAX_BODY = 12288;
$declared = (int) ($_SERVER['CONTENT_LENGTH'] ?? 0);
if ($declared > DALMA_MAX_BODY) {
    dalma_fail(413);
}
$raw = (string) file_get_contents('php://input', false, null, 0, DALMA_MAX_BODY + 1);
if ($raw === '' || strlen($raw) > DALMA_MAX_BODY) {
    dalma_fail(413);
}

// 4. JSON valido y objeto.
$data = json_decode($raw, true);
if (!is_array($data) || (array_values($data) === $data && $data !== [])) {
    dalma_fail();
}

// 5. Solo campos esperados.
$allowed = ['name', 'phone', 'email', 'treatment', 'message', 'lang', 'marketing_consent', 'website', 'tt'];
foreach (array_keys($data) as $key) {
    if (!is_string($key) || !in_array($key, $allowed, true)) {
        dalma_fail();
    }
}

// 6. Honeypot: si trae valor, se rechaza sin llamar a Apps Script ni enviar correo.
if (isset($data['website']) && $data['website'] !== '') {
    dalma_fail();
}

// 7. Validacion de campos.
function dalma_clean($value, int $max, bool $multiline)
{
    if (!is_string($value)) {
        return null;
    }
    $s = str_replace(["\r\n", "\r"], "\n", $value);
    if ($multiline) {
        $s = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', '', $s);
    } else {
        $s = preg_replace('/[\x00-\x1F\x7F]/', ' ', $s);
    }
    if ($s === null) {
        return null;
    }
    $s = trim($s);
    $len = function_exists('mb_strlen') ? mb_strlen($s, 'UTF-8') : strlen($s);
    if ($len > $max) {
        return null;
    }
    return $s;
}

const DALMA_TREATMENTS = [
    'botox',
    'fillers',
    'hydrafacial',
    'microneedling',
    'pdrn_exosomes',
    'hair',
    'laser_hair_removal',
    'warts_keloids',
    'plasma_pen',
    'weight_control',
    'other',
];

$name      = dalma_clean($data['name'] ?? null, 120, false);
$phone     = dalma_clean($data['phone'] ?? null, 40, false);
$treatment = dalma_clean($data['treatment'] ?? null, 80, false);
$message   = array_key_exists('message', $data) && $data['message'] !== null && $data['message'] !== ''
    ? dalma_clean($data['message'], 2000, true)
    : '';
$lang      = $data['lang'] ?? null;

if ($name === null || $name === '' || $phone === null || $phone === '' || $treatment === null || $treatment === '' || $message === null) {
    dalma_fail();
}
if ($lang !== 'es' && $lang !== 'en') {
    dalma_fail();
}
if (!in_array($treatment, DALMA_TREATMENTS, true)) {
    dalma_fail();
}
if (!preg_match('/^[0-9+()\-.\s]+$/', $phone)) {
    dalma_fail();
}
$digits = strlen((string) preg_replace('/\D/', '', $phone));
if ($digits < 7 || $digits > 20) {
    dalma_fail();
}

// Correo electronico: opcional; si viene, formato valido (ASCII, local <= 64, total <= 254).
$email = '';
if (array_key_exists('email', $data) && $data['email'] !== null && $data['email'] !== '') {
    $email = dalma_clean($data['email'], 254, false);
    if ($email === null || $email === '' || strlen($email) > 254
        || strpos($email, '..') !== false
        || !preg_match('/^[^\s@,;<>()\[\]"]{1,64}@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/', $email)
        || filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
        dalma_fail();
    }
}

// Autorizacion promocional: solo un booleano explicito (ausente = false). true exige correo valido.
$marketing = false;
if (array_key_exists('marketing_consent', $data)) {
    if (!is_bool($data['marketing_consent'])) {
        dalma_fail();
    }
    $marketing = $data['marketing_consent'];
}
if ($marketing && $email === '') {
    dalma_fail();
}

// 8. Configuracion privada (fuera de public_html).
$cfgFile = dirname(__DIR__, 3) . '/dalma_private/contact-config.php';
$cfg = is_file($cfgFile) ? include $cfgFile : null;
// Fail-closed: sin configuracion completa y valida NO se procesa nada (ni se llama a servicios externos).
if (
    !is_array($cfg)
    || !function_exists('curl_init')
    || !is_string($cfg['shared_secret'] ?? null) || $cfg['shared_secret'] === ''
    || !dalma_https_url_ok($cfg['apps_script_url'] ?? null)
    || !dalma_turnstile_secret_ok($cfg['turnstile_secret'] ?? null)
) {
    dalma_fail(503);
}

// 9. Rate limiting: antes de cualquier llamada externa (Turnstile / Apps Script). Fail-closed:
//    si no se puede resolver el origen o crear/escribir el almacenamiento privado, el envio se
//    rechaza con un error generico (503) en lugar de continuar sin limite.
$rlDone = false;
$rlIp   = dalma_client_ip_bin();
$rlDir  = dirname(__DIR__, 3) . '/dalma_private/rate-limit';
if ($rlIp === null || !(is_dir($rlDir) || @mkdir($rlDir, 0700, true)) || !is_dir($rlDir) || !is_writable($rlDir)) {
    dalma_fail(503);
}
$rlNow  = time();
$rlFile = $rlDir . '/' . dalma_rl_key($rlIp, (string) $cfg['shared_secret']);
[$rlState, $rlSlot] = dalma_rl_reserve($rlFile, $rlNow);
if ($rlState === 'blocked') {
    dalma_fail(429);
}
if ($rlState !== 'ok') {
    dalma_fail(503);
}
if (mt_rand(1, 20) === 1) {
    dalma_rl_purge($rlDir, $rlNow);
}
register_shutdown_function(static function () use ($rlFile, $rlSlot, &$rlDone): void {
    if (!$rlDone) {
        dalma_rl_release($rlFile, $rlSlot, time());
    }
});

// 10. Turnstile OBLIGATORIO (fail-closed): sin token valido verificado por Cloudflare no se llama a
//     Apps Script. Cualquier fallo (token ausente, Cloudflare caido, respuesta invalida o
//     success != true) rechaza la solicitud. A Cloudflare solo se envia secreto + token.
$token = $data['tt'] ?? null;
if (!is_string($token) || $token === '' || strlen($token) > 2048) {
    dalma_fail();
}
$ts = curl_init('https://challenges.cloudflare.com/turnstile/v0/siteverify');
curl_setopt_array($ts, dalma_curl_secure_opts() + [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => http_build_query(['secret' => $cfg['turnstile_secret'], 'response' => $token]),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => false,
    CURLOPT_CONNECTTIMEOUT => 5,
    CURLOPT_TIMEOUT        => 10,
]);
$tsResp = curl_exec($ts);
$tsCode = (int) curl_getinfo($ts, CURLINFO_RESPONSE_CODE);
curl_close($ts);
$tsJson = is_string($tsResp) ? json_decode($tsResp, true) : null;
if ($tsCode !== 200 || !is_array($tsJson) || ($tsJson['success'] ?? false) !== true) {
    dalma_fail();
}

// 11. Envio al Apps Script (HTTPS, sigue redirecciones de Google, timeouts razonables).
$payload = json_encode([
    'secret'    => $cfg['shared_secret'],
    'name'      => $name,
    'phone'     => $phone,
    'email'     => $email,
    'marketing_consent' => $marketing,
    'treatment' => $treatment,
    'message'   => $message,
    'lang'      => $lang,
], JSON_UNESCAPED_UNICODE);
if ($payload === false) {
    dalma_fail();
}

$ch = curl_init((string) $cfg['apps_script_url']);
curl_setopt_array($ch, dalma_curl_secure_opts() + [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $payload,
    CURLOPT_HTTPHEADER     => ['Content-Type: application/json'],
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_MAXREDIRS      => 5,
    CURLOPT_CONNECTTIMEOUT => 5,
    CURLOPT_TIMEOUT        => 15,
]);
$resp = curl_exec($ch);
$code = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
curl_close($ch);

if (!is_string($resp) || $code !== 200) {
    dalma_fail();
}
$json = json_decode($resp, true);
if (!is_array($json) || ($json['ok'] ?? false) !== true) {
    dalma_fail();
}

$rlDone = true; // el envio se completo: el cupo reservado queda consumido
echo '{"ok":true}';
