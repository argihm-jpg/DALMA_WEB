<?php
/**
 * EJEMPLO (sin valores reales) de la configuracion privada del formulario.
 *
 * El archivo REAL debe existir en el servidor FUERA de public_html:
 *     <home de la cuenta>/dalma_private/contact-config.php      (carpeta 700, archivo 600)
 * y NUNCA debe guardarse en el repositorio, en HTML ni en JS.
 */
return [
    // URL /exec del Web App de Google Apps Script (proyecto "D'ALMA Contact Form Backend"). Debe ser HTTPS.
    'apps_script_url'  => '',

    // Secreto compartido PHP -> Apps Script (clave SHARED_SECRET en Script Properties).
    'shared_secret'    => '',

    // Secret Key de Cloudflare Turnstile. OBLIGATORIO: si falta, esta vacio o no tiene un formato
    // valido, contact-submit.php rechaza TODAS las solicitudes (fail-closed, HTTP 503 generico) y
    // no llama a Apps Script. El Site Key (publico) va en mockup.html (DALMA_TURNSTILE_SITE_KEY).
    'turnstile_secret' => '',
];
