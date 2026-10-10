# Pendientes de Meta (Pixel) para Gio — D'ALMA Clinic

**Última actualización:** 2026-10-10, tras el deploy `c446e04` (preparado para el retorno de Gio el lunes 2026-10-12).
**Responsable del tema:** Gio (CM / Meta Ads de la clínica). **Coordinación técnica y deploys:** Bruno Sandoval.
**Alcance de este documento:** explicar el estado actual del Meta Pixel en el sitio y lo que falta verificar o decidir. No contiene credenciales, tokens ni datos de la clínica.

> **Regla de oro:** este documento NO autoriza cambios. No modificar el Pixel, no crear ni cambiar eventos y no desplegar nada sin coordinarlo con Bruno. Cualquier cambio en el sitio exige commit, backup, deploy controlado y re-prueba (ver sección 8).

---

## 1. Estado en una mirada

| Tema | Estado |
|---|---|
| Pixel `1762473058207277` | Instalado **directamente en el código** del sitio (el que dejó Gio, sin modificar). En producción. |
| Eventos que envía nuestro código | `PageView` al cargar cada página y `Contact` en cada clic a un botón de WhatsApp. **No existe `Lead`.** |
| Google Tag Manager `GTM-MJGTQRV7` | Instalado en las 9 páginas, **sin etiquetas publicadas** (versión publicada = "Empty Container"). No gestiona el Pixel. |
| GA4 `G-CQ7R0YH9J1` | Configurado y probado en GTM, **SIN PUBLICAR** (borrador; la publicación quedó pendiente de un clic manual de Bruno). Todavía no hay medición GA4 real. |
| Eventos de `dataLayer` existentes | `click_whatsapp` y `generate_lead` (ver sección 3). |
| Mecanismo de desactivación del seguimiento | **EN PRODUCCIÓN desde el deploy `c446e04` (2026-10-10)**; probado con la red real en producción. |
| Aviso de cookies / Aviso de privacidad nuevo | **EN PRODUCCIÓN** (`c446e04`). El aviso de cookies solo se ve con `?preview=1` mientras el overlay esté activo. |
| Sitio | **PRE-LANZAMIENTO**: `PUBLIC_LAUNCH=false`, overlay "Próximamente / Coming soon" para visitas normales, `noindex, nofollow`, sin `sitemap.xml`. `?preview=1` permite ver el sitio completo. |
| Acceso a Meta Business Suite / Administrador de eventos | **No se ha entrado.** Todo lo de Meta marcado como "por verificar" depende de que Gio lo revise con su cuenta. |

### Qué está en producción

- **En producción (commit de código `c446e04`, 2026-10-10):** Pixel de Gio sin modificar (`PageView` + `Contact`), GTM vacío (sin etiquetas publicadas), formulario con Turnstile y **sin** casilla de promociones, aviso de cookies («Entendido»), control para desactivar/reactivar la medición y Aviso de privacidad = texto original de Anita + un párrafo mínimo de cookies.
- **Ojo:** el párrafo del Píxel de Meta que escribió Gio (commit `6eaa3e2`) fue sustituido por el párrafo mínimo ("Este sitio utiliza Google Analytics … y el Píxel de Meta, para medir y evaluar nuestras campañas publicitarias…"). Gio puede proponer ajustes a esa redacción, pero el texto legal lo valida Anita/asesoría.
- **Aún NO está en producción:** ninguna etiqueta de Google (GTM sin publicar), `Lead` de Meta, ni ningún cambio al Pixel.

---

## 2. Qué es lo que hace hoy el Pixel (hecho verificado en el código)

Ubicación en el repositorio: `mockup.html`, bloque `// META PIXEL` dentro del script compartido (justo antes del bloque `// WHATSAPP`). El `<head>` lo regenera `scripts/build-site.py` y no copia el de `mockup.html`, por eso el Pixel vive en el script compartido y sale en las 9 páginas.

- `fbq('init', '1762473058207277')` una vez por página; `fbq('track', 'PageView')` al cargar.
- Dentro del listener delegado de clics a WhatsApp (el mismo que empuja `click_whatsapp` a `dataLayer`): `if (window.fbq) fbq('track', 'Contact')`.
- Sin parámetros ni datos personales en nuestras llamadas a `fbq`.
- Sin `<noscript>` de respaldo (no cuenta visitas sin JavaScript).
- El código oficial del Pixel (`!function(f,b,e,v,n,t,s){…}`) **no ha sido modificado**; es idéntico al de `HEAD`.
- Sitio multipágina con rutas reales: no hay navegación tipo SPA, por lo que no se espera `PageView` extra por cambios de ruta.

### Eventos de `dataLayer` (para GTM/GA4, NO para Meta hoy)

| Evento | Cuándo | Contenido |
|---|---|---|
| `click_whatsapp` | Un clic = un evento, en cualquier botón de WhatsApp | `{event:'click_whatsapp', link_type:'whatsapp', placement:'<floating\|footer\|contact\|about_cta\|services_cta>'}` |
| `generate_lead` | Solo cuando el backend responde `{"ok":true}` tras un envío real del formulario | `{event:'generate_lead', form_name:'contact'}` (nada más; sin nombre, teléfono, correo, tratamiento ni mensaje) |

`generate_lead` representa un contacto recibido por correo; `click_whatsapp` representa solo **intención** (no un lead confirmado).

---

## 3. Qué está CONFIRMADO por pruebas (2026-10-10)

Estas pruebas se hicieron en un servidor local de revisión (127.0.0.1) con la librería real `fbevents.js` descargada de Meta, **interceptando en el navegador los envíos a `facebook.com/tr`** para no contaminar el Administrador de eventos. Es evidencia técnica de lo que el navegador *intenta enviar*, no de lo que Meta *recibe/acepta*.

1. **`PageView` se dispara al cargar** (un intento de envío por carga de página).
2. **`Contact` se dispara una vez por clic a WhatsApp** (validado en producción con `?preview=1` el 2026-10-10 sustituyendo `fbq` por un registrador, sin enviar un `Contact` real a Meta; `click_whatsapp` también 1 por clic).
3. **El Pixel envía eventos automáticos propios de la librería.** Observado: al pulsar «Entendido» (botón del aviso de cookies) la librería envió `SubscribedButtonClick`, sin que nuestro código llame a `fbq` ni empuje nada a `dataLayer`. Esto proviene de la configuración del Pixel en Meta (eventos automáticos activos), no de nuestro código. Ya ocurre en producción con cualquier botón del sitio.
4. **La oposición al seguimiento (control en el Aviso de privacidad) funciona:** tras desactivar, 0 envíos a Meta, `_fbp` borrada y no recreada; con la preferencia activa al cargar otra página, `fbevents.js` ni siquiera se descarga; al reactivar, el sitio recarga y el Pixel vuelve a enviar `PageView`. Se probó en las 9 páginas (ES/EN) en local y, tras el deploy, **en producción con la lista de red real del navegador**: con el seguimiento activo hubo 1 `facebook.com/tr` (`PageView`); tras desactivar, 0 peticiones nuevas a Meta (ni `Contact` ni `SubscribedButtonClick`). Detalle en la sección 4.7.
5. **El formulario y WhatsApp siguen funcionando** con el seguimiento desactivado (verificado en producción: 1 envío ficticio con 1 correo y 1 `generate_lead`).
5b. **Cada clic a un enlace de WhatsApp genera, además de `Contact`, una llamada automática interna del Pixel** (clic en enlace/botón detectado por los eventos automáticos). Observado en producción el 2026-10-10 con `fbq` sustituido por un registrador: por clic, 1 llamada `fire` (automática) + 1 `track('Contact')` (nuestra). Hay que ver en «Probar eventos» cómo la registra Meta y si debe desactivarse (4.1/4.3).
6. **Nuestro código no envía datos del formulario a Meta:** el código del formulario no llama a `fbq`; `generate_lead` solo lleva `form_name`.
7. **Configuración pública del Pixel (auditoría parcial, 2026-10-09)**, leída del endpoint público `connect.facebook.net/signals/config/<ID>` sin iniciar sesión: Advanced Matching automático **no** activado; eventos automáticos/inferidos (botones y formularios) **sí** activos; cookies propias `_fbp`/`_fbc` activas; sin plugin de microdata. *Es lectura de la configuración pública; hay que confirmarla en el Administrador de eventos.*

## 4. Pendientes (cada uno con lo que sabemos y lo que Gio debe verificar)

### 4.1 Revisar los eventos automáticos de Meta (`SubscribedButtonClick` y similares) — **PRIORIDAD ALTA**

- **Situación:** los eventos automáticos están activos en la configuración del Pixel. Un clic en cualquier botón (incluido «Entendido») genera `SubscribedButtonClick`. Según la configuración pública, los eventos inferidos pueden incluir el **texto del botón**, la URL y el título de la página y, en formularios, los **nombres/placeholders de campos** (no los valores mientras Advanced Matching siga apagado). *Esto último es inferido de la configuración y de la documentación de Meta; no se inspeccionó el contenido completo de cada petición: Gio debe confirmarlo en "Probar eventos".*
- **Por qué importa:** la clínica es del sector salud; «Entendido» no debe generar eventos analíticos y no es consentimiento. Además `Contact` podría duplicarse con el evento automático equivalente en los botones de WhatsApp (los enlaces `<a>` también podrían detectarse).
- **Verificar en Meta (Gio):** Administrador de eventos → Configuración del Pixel → eventos automáticos / detección de clics en botones y eventos inferidos. Decidir si se **desactivan**.
- **Opciones técnicas (requieren autorización de Bruno, modifican el código de Gio):** (a) desactivarlos en Meta (preferible, sin tocar el sitio); (b) añadir `fbq('set','autoConfig',false,'1762473058207277')` **antes** de `fbq('init', …)`.
- **Criterio de aceptación:** en "Probar eventos" no aparece `SubscribedButtonClick` (ni otros automáticos) al pulsar «Entendido», botones del menú o enlaces; siguen llegando `PageView` y `Contact`.

### 4.2 Advanced Matching (AAM) y su adecuación para una clínica

- **Lo que sabemos:** la configuración pública indica AAM automático **apagado**. Nuestro código no envía correo ni teléfono al Pixel.
- **A confirmar en Meta:** estado real de "Coincidencia avanzada automática" y de la coincidencia avanzada manual (si hubiera). En el formulario de contacto el sitio recoge nombre, teléfono, correo y tratamiento; con AAM encendido, la librería podría intentar leer esos campos y enviarlos con hash.
- **Recomendación a evaluar:** mantener AAM **apagado** por tratarse de una clínica (datos de salud/estética). Cualquier activación debe revisarse con asesoría legal y reflejarse en el Aviso.
- **Criterio:** confirmación documentada del estado (captura o nota) y decisión explícita.

### 4.3 Confirmar que `Contact` se registra una sola vez por clic a WhatsApp

- **Confirmado en pruebas:** 1 llamada `fbq('track','Contact')` por clic (listener delegado único, protegido contra duplicados) y 1 `click_whatsapp`.
- **Por verificar en Meta:** que en "Probar eventos" llegue **un solo** `Contact` por clic (sin sumar un evento automático equivalente o uno de GTM) y con **cada uno de los 5 puntos de WhatsApp** (flotante, footer, contacto, Nosotros, Servicios). Comprobar además la deduplicación si más adelante entra CAPI.
- **Nota:** `Contact` hoy representa intención de contacto, no un lead confirmado. Sirve como señal de campañas hacia WhatsApp.

### 4.4 Evento estándar `Lead` a partir de `generate_lead`

- **Estado:** NO implementado, a propósito. `generate_lead` ya existe en `dataLayer` y solo se emite tras `{"ok":true}`.
- **Regla acordada:** `Lead` solo después de un formulario enviado con éxito; **sin parámetros personales** (ni nombre, teléfono, correo, tratamiento ni mensaje); idealmente sin parámetros.
- **Opciones (decidir junto con 4.5):**
  - **A. En código:** añadir `if (window.fbq) fbq('track','Lead')` justo donde se hace el `dataLayer.push({event:'generate_lead',…})` (rama de éxito del formulario en `mockup.html`).
  - **B. Desde GTM:** etiqueta de Meta Pixel disparada por el activador `CE - generate_lead` (requiere que el Pixel viva en GTM; ver 4.5).
- **Pendiente de Gio:** decidir A o B, definir `Lead` como conversión de campañas y acordar si reemplaza o complementa a `Contact`. Nunca implementar A y B a la vez (duplica `Lead`).
- **Criterio:** un `Lead` por envío exitoso; ninguno si el backend responde error; sin datos personales.

### 4.5 ¿El Pixel permanece en el código o se administra desde GTM?

- **Hoy:** en el código (directo). GTM solo se usa para Google (GA4, sin publicar).
- **Regla:** **nunca dos instalaciones** (duplicaría `PageView`, `Contact` y `Lead`).
- **Opción 1 — dejarlo en el código (menor cambio):** GTM solo para Google. `Lead` se añadiría en código (4.4-A).
- **Opción 2 — migrarlo a GTM:** crear las etiquetas de Meta en GTM (PageView base, `Contact` con `CE - click_whatsapp`, `Lead` con `CE - generate_lead`) y **retirar en el MISMO deploy** el snippet y la línea `fbq('track','Contact')` del código. Ventajas: un solo punto de control; desventajas: más superficie en GTM, plantillas de comunidad/seguridad y volver a probar la oposición.
- **Impacto en la oposición (4.7):** el mecanismo actual funciona con el Pixel en el código; si se mueve a GTM debe re-probarse con red real.
- **Decisión pendiente:** Gio + Bruno.

### 4.6 ¿Es necesaria la API de Conversiones (CAPI)?

- **Hoy:** no hay CAPI. El sitio es de bajo volumen y está en pre-lanzamiento.
- **Qué implicaría:** envío servidor-a-servidor (el endpoint PHP `contact-submit.php` en Hostinger podría hacerlo), con token de acceso en la configuración privada (`dalma_private/contact-config.php`, nunca en el repositorio), `event_id` para deduplicar con el Pixel y datos de usuario con hash (correo/teléfono). Eso supone **tratar datos personales de salud/contacto con Meta** y requiere reflejarlo en el Aviso y en el consentimiento.
- **Recomendación a evaluar:** posponer CAPI hasta tener definidos el modelo de consentimiento y la validación legal; evaluar solo si Meta lo exige para optimización o por pérdida de señal.
- **Pendiente de Gio:** indicar si Meta/Administrador de eventos recomienda CAPI para las campañas previstas y qué datos se enviarían.

### 4.7 Comprobar que el Pixel respeta la oposición implementada en el Aviso

- **Cómo funciona (en producción desde `c446e04`):**
  1. Preferencia en `localStorage` clave `dalma_tracking_optout='1'`.
  2. Un guard en el `<head>` (`TRACKING_OPTOUT_GUARD` en `scripts/build-site.py`) corre **antes** de GTM y del Pixel: si la preferencia está activa, define `window.__dalmaTrackingOptOut`, `window['ga-disable-G-CQ7R0YH9J1']=true` y `window.fbq=function(){}`. El snippet de Gio sale solo (`if(f.fbq)return;`); su código no se modificó. GTM tampoco se carga.
  3. Al pulsar «Desactivar medición y publicidad» en la página: se llama `fbq('consent','revoke')` **antes** de neutralizar `fbq`, se activa `ga-disable`, y se borran las cookies `_ga*`, `_gid`, `_gat`, `_gcl_*`, `_fbp`, `_fbc`.
- **Confirmado en pruebas locales y en producción (red real):** ver sección 3, punto 4. Hubo una fuga que se corrigió (tras desactivar, la librería seguía enviando `SubscribedButtonClick` y recreaba `_fbp`; se resolvió con `consent revoke` y escuchando el clic en captura).
- **Límites (no afirmar más):** la oposición solo detiene el seguimiento **posterior**; no retira eventos ya enviados. Es por navegador/dispositivo y se pierde si se borran los datos del sitio. No cubre cookies de terceros ni honra Global Privacy Control.
- **Pendiente de Gio:** ya desplegado; en "Probar eventos" comprobar que con la oposición activa **no llega ningún evento** (ni `PageView`, ni `Contact`, ni automáticos) y que al reactivar vuelven. Revisar también que no se estén enviando eventos desde otras fuentes (CAPI, integraciones).

### 4.8 Restricciones de Meta para datos de salud y campañas de clínicas

*No es asesoría legal; solo puntos a revisar en las políticas vigentes de Meta (pueden cambiar).*

- **Datos de salud/sensibles y herramientas de negocio:** revisar los Términos de las herramientas empresariales y las políticas de datos sensibles/salud de Meta: restringen enviar información de salud o sensible por Pixel/API, y pueden limitar optimización, audiencias personalizadas y eventos. El sitio recoge *tratamiento de interés* (puede revelar información de salud/estética): **no debe enviarse a Meta**, ni como parámetro ni en URLs.
- **Políticas publicitarias:** revisar "procedimientos cosméticos y control de peso" (restricciones de edad, imágenes antes/después, lenguaje que implique atributos personales o condiciones de salud) y atributos personales. D'ALMA ofrece, entre otros, inyectables, regenerativos, capilares, depilación y *Control de Peso y bienestar*.
- **Audiencias y retargeting:** definir si habrá audiencias personalizadas desde visitas al sitio y su reflejo en el Aviso; recordar que `PageView` por URL (p. ej. páginas de servicios concretos) puede inferir intereses de salud.
- **A confirmar:** categoría del negocio y cumplimiento de la cuenta publicitaria; si Meta ya limitó funciones por el sector.
- **Relación con GA4:** la propiedad de Google está en sector Salud y Google tampoco permite datos proporcionados por el usuario; mantener criterios coherentes entre Meta y Google.

---

## 5. Lo que Gio debe verificar en Meta Business Suite / Administrador de eventos (no verificado por nosotros)

Checklist (nada de esto ha sido comprobado desde Meta; no tuvimos acceso):

- [ ] Propietario del Pixel y de la cuenta publicitaria; ID `1762473058207277` correcto y asociado al dominio `dalmaclinic.com.mx`.
- [ ] Estado de eventos automáticos / detección de clics en botones / eventos inferidos (4.1).
- [ ] Estado de Advanced Matching automático y manual (4.2).
- [ ] Nivel de uso compartido de datos y cookies propias (`_fbp`, `_fbc`).
- [ ] Eventos que realmente llegan (PageView, Contact, SubscribedButtonClick, otros) y su origen/dominio. Las visitas de validación del 2026-10-10 con `?preview=1` (deploy anterior y deploy `c446e04`) enviaron `PageView` reales; no se envió ningún `Contact` ni `Lead` de prueba. Las pruebas locales (127.0.0.1) se interceptaron y no llegaron a Meta.
- [ ] Verificación del dominio y configuración de eventos agregados (AEM) si aplica.
- [ ] Integraciones, CAPI o socios que también envíen eventos al mismo Pixel (duplicados).
- [ ] Políticas aplicables al sector salud/cosmético (4.8).

## 6. Dependencias y decisiones fuera del alcance técnico

- **Modelo de consentimiento (Anita / asesoría legal):** hoy GA4 (cuando se publique) y el Pixel cargan **sin consentimiento previo**, con oposición posterior (opt-out). El botón «Entendido» **no** es consentimiento expreso. Si se decide opt-in, habría que añadir un banner con aceptar/rechazar y Consent Mode; eso cambia el diseño aprobado y requiere autorización.
- **Overlay de pre-lanzamiento:** mientras esté activo, el visitante normal **no ve** el aviso de cookies ni el Aviso de privacidad, pero el Pixel sí carga para él. Decidir si se acepta o se evita cargar medición durante el overlay.
- **Datos legales pendientes de Anita:** nombre legal, domicilio, correo de privacidad, teléfono, URL, plazos de conservación, vigencia, versión EN, consentimiento para datos sensibles. El correo de privacidad sigue como placeholder (`[CORREO DE PRIVACIDAD]`); no inventarlo.
- **Publicación de GA4/GTM:** el contenedor sigue SIN publicar. Bruno eligió el modelo "aviso informativo + oposición" (no es validación jurídica) y la publicación quedó pendiente de un clic manual. **No publicar ni modificar el contenedor GTM** sin coordinarlo con Bruno; las etiquetas de Meta, si llegan, se acuerdan con él (4.5).

## 7. Reglas de trabajo

- No modificar el bloque del Pixel ni el listener de WhatsApp sin acuerdo con Bruno; si cambia, **re-probar la oposición con red real**.
- No añadir `Lead`, parámetros ni datos personales sin autorización.
- No dos instalaciones del Pixel (código + GTM).
- Los secretos (tokens de CAPI, etc.) **nunca** en el repositorio, `mockup.html`, JS ni documentación; solo en `dalma_private/` (fuera de `public_html`).
- Cualquier servicio de Google de D'ALMA solo con `clinic.dalma@gmail.com`.
- Probar en producción de forma secuencial y con pausas (una vez hubo 429 por barridos rápidos).

## 8. Cómo probar (sin contaminar datos)

1. **Meta:** Administrador de eventos → "Probar eventos" con la URL `https://dalmaclinic.com.mx/?preview=1` (el overlay oculta el sitio sin ese parámetro). Revisar que cada acción produzca exactamente los eventos esperados.
2. **Red:** DevTools → Network, filtrar `facebook.com/tr` y `google-analytics.com` / `google.com/g/collect`. Ojo: GA4 también envía a `www.google.com/g/collect`.
3. **Oposición (cuando esté desplegada):** Aviso de privacidad → "Cookies y tecnologías de navegación" → «Desactivar medición y publicidad»; luego navegar, pulsar botones y WhatsApp y comprobar 0 peticiones a Meta y a Google; reactivar y confirmar que vuelven.
4. **Tráfico de prueba:** separar el tráfico interno/de pruebas de la medición real (ver CLAUDE.md, sección F) y no generar `Contact`/`Lead` falsos en campañas.
5. **Despliegue:** cualquier cambio de código requiere commit, backup de `public_html`, deploy de los HTML afectados con verificación SHA-256 y re-validación. Lo coordina Bruno.

## 9. Referencias en el repositorio

- `mockup.html` — bloque `// META PIXEL`, listener de WhatsApp (`click_whatsapp` + `Contact`), rama de éxito del formulario (`generate_lead`), manejador del control de desactivación, texto del Aviso y aviso de cookies.
- `scripts/build-site.py` — `GTM_ID`, `GTM_HEAD`/`GTM_NOSCRIPT`, `TRACKING_OPTOUT_GUARD`, `GA_MEASUREMENT_ID`.
- `CLAUDE.md` — matriz de estado (secciones A–F) y entradas del Historial: "Cookies", "GA4", "Aviso simplificado + Apps Script v5" y "Verificación final pre-deploy" (2026-10-10).
- Auditoría parcial previa del Pixel (2026-10-09): resumida en la sección 3, punto 7.
