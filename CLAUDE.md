# DALMA_WEB — Contexto del Proyecto

## ⚠️ RESTRICCIÓN PERMANENTE DE CUENTA GOOGLE (leer antes de cualquier tarea de Google) ⚠️
Para **cualquier** tarea de D'ALMA en Google Search Console, Google Analytics/GA4, Google Tag Manager, Google Ads, Google Business Profile, o cualquier otro servicio de Google, usar **ÚNICAMENTE**:

**`clinic.dalma@gmail.com`**

En Chrome existen otras cuentas de Google con sesión iniciada. Antes de **crear, editar, vincular, configurar o verificar** cualquier propiedad/cuenta/contenedor de Google, Claude debe **verificar visualmente** que la cuenta activa sea `clinic.dalma@gmail.com`. Si no lo es: **DETENERSE** y pedir a Bruno que cambie de cuenta. No usar ninguna otra cuenta de Google para D'ALMA bajo ninguna circunstancia.

## Estado Actual de Producción y Punto de Reanudación (actualizado 2026-09-23)
- **Arquitectura multipágina bilingüe YA DESPLEGADA en Hostinger** (`public_html/`). Producción: ES `/`, `/nosotros/`, `/servicios/`, `/contacto/`, `/aviso-de-privacidad/`; EN `/en/`, `/en/about/`, `/en/services/`, `/en/contact/`.
- **El sitio NO está públicamente lanzado (pre-lanzamiento):** `PUBLIC_LAUNCH=false` → overlay "Próximamente / Coming soon" activo por defecto, `?preview=1` permite revisar el sitio completo, `noindex, nofollow` en las 9 páginas, sin `sitemap.xml`, Testimonios desactivado (`/testimonios/` y `/en/testimonials/` → 404).
- **Próxima etapa (NO iniciada):** Google Search Console, GA4, Google Tag Manager, Google Ads, eventos `click_whatsapp` / `click_phone` / `generate_lead`, y CAPTCHA/backend del formulario cuando corresponda. La arquitectura/deploy ya no es el siguiente paso. Recordar la restricción de cuenta Google de arriba.
- **Validar en producción sin barridos rápidos con curl** (ver incidente 429 en la entrada 2026-09-23).
- **Ajustes finales de contenido/ubicación (2026-09-26): commiteados en `main` pero NO desplegados** — producción sigue con el deploy del 2026-09-23. Ver entrada 2026-09-26 más abajo. Hacer deploy solo con autorización explícita de Bruno.

## Descripción
Sitio web para **D'ALMA CLINIC**, clínica estética ubicada en Cabo San Lucas, BCS.
El proyecto lo elabora **Bruno Sandoval**. La directora del negocio es **Ana María**.

## Datos del Negocio
- **Nombre comercial:** D'ALMA CLINIC
- **Dominio:** `dalmaclinic.com.mx`
- **Dirección (CONFIRMADA, verificada externamente 2026-09-26):** Plaza Patio, De Las Brisas 2404, Brisas del Pacífico, Cabo San Lucas, Baja California Sur, C.P. 23473. **Aún sin número de local/suite** dentro de la plaza (pendiente; no inventarlo). Punto de Plaza Patio: 22.9045296, -109.9333945
- **Horario:** "Lunes a domingo, 10:00 am – 8:00 pm" aparece como texto provisional en el sitio, pero Bruno confirmó (2026-09-22) que **no es un dato real, Anita aún no lo ha definido** — no usar como fuente de verdad (p. ej. no incluir en schema.org hasta confirmación real)
- **WhatsApp:** Pendiente de definir
- **Instagram:** Pendiente

## Identidad Visual

### Paleta de colores oficial
| Nombre | Hex |
|---|---|
| Beige hueso | `#F5F1EC` |
| Arena suave | `#D8CBBE` |
| Taupe elegante | `#8B817B` |
| Gris café profundo | `#5F5651` |
| Blanco limpio | `#FAF9F7` |

### Tipografía
- **Principal:** Cormorant Garamond
- **Secundaria:** Montserrat

### Estilo visual
Minimalista, cálido, elegante, moderno y emocional. Usar iluminación cálida, tonos beige y neutros, fotografías naturales con hombres y mujeres. Evitar apariencia quirúrgica, fría o elitista.

### Frases clave de marca
- "Cuidarte también es una forma de amor propio."
- "No se trata de cambiar quién eres… se trata de volver a sentirte tú."
- "Tu piel también cuenta tu historia."
- "Queremos que venir a D'ALMA se sienta distinto."

## Tono de Comunicación
Humano · elegante · cálido · moderno · natural · accesible.
No debe percibirse como clínica fría, exclusiva o intimidante. Dirigido a hombres y mujeres.

## Estructura del Sitio (5 secciones)

### Home — estructura aprobada (2026-06-12)
1. Hero — headline "Cuidarte también es una forma de amor propio." + imagen aspiracional (bienestar/amor propio, no interior clínica) + CTAs
2. Tratamientos destacados — 4 cards de servicios destacados
3. Testimonios — carrusel con cards demo (5 testimonios); contenido final pendiente de la cliente
4. Sección oscura — cita de marca "No se trata de cambiar quién eres…"
5. ¿Por qué D'ALMA? — 3 pilares de filosofía
6. CTA + mapa — layout 2 columnas: izquierda título "Tu piel también cuenta tu historia." + botón; derecha placeholder Google Maps (Plaza Patio, Cabo San Lucas) + horario

### Nosotros
Historia de Ana María, equipo

### Servicios
Acordeones o tarjetas por categoría

### Testimonios
Pacientes reales, fotos naturales, before/after con autorización

### Contacto + FAQ
WhatsApp, Instagram, mapa, horario, preguntas frecuentes

## Servicios

### Inyectables
- **Botox** — Linurase, Otesaly, Dysport. Requiere valoración médica.
- **Fillers y armonización facial** — Rejeneusse, Revofil, Starfill, E.P.T.Q. (Fine, Plus, Ultra según zona)

### Regeneración y revitalización
- **PDRN** — ReMedium PDRN (Emport) y Otesaly PDRN
- **Exosomas, Aquashine y Natural-B** — Natural-B, Aquashine PTX, Exo-Xelle (Radiesse y Sculptra para etapa posterior)

### Faciales
- **Hydrafacial** — Ideal como tratamiento de entrada; hombres y mujeres
- **Microneedling / Despigmentantes** — Dermaheal, PTx-SB, Inbioamber, PTx-SR

### Capilares
- **Tratamientos capilares** — PTx-HL, Dermaheal P-HL, Dr. CYJ Hair Filler

### Otros
- **Depilación láser** — Para hombres y mujeres, múltiples zonas
- **Verrugas, queloides y plasmapen** — Bajo valoración médica; triamcinolona intralesional

## Requerimientos Técnicos
- **Regla obligatoria de responsividad:** toda modificación al sitio (HTML, CSS, JS, imágenes, layout, componentes nuevos) debe funcionar correctamente en cualquier tamaño de pantalla — mobile, tablet y desktop — sin excepción, sin importar de qué se trate el cambio. Antes de dar por terminada una tarea, verificar visualmente el resultado en al menos un breakpoint mobile (`≤768px`) y uno desktop.
- Responsive (mobile-first, optimizado para celular)
- Integración futura: Meta Business, Facebook Ads, Instagram, WhatsApp Business, Google Analytics, Google Search Console

## Material Pendiente
- [ ] Fotografías profesionales del equipo
- [ ] Fotografías del local (interior y exterior; se realizarán al terminar la obra)
- [ ] Before/after de pacientes (con autorización)
- [ ] WhatsApp oficial
- [ ] Número(s) de teléfono de contacto

## Pendientes Bloqueados por Anita
*(actualizado 2026-09-22 — consolida y reemplaza los listados sueltos de sesiones anteriores)*

### Contacto
- Número de local/suite dentro de Plaza Patio.
- Perfil real de Google Maps / Google Business Profile (hoy el mapa enlaza a una búsqueda de Maps; sustituir el `href` de `.map-frame-lnk` en Home y Contacto cuando exista; usar SOLO `clinic.dalma@gmail.com`).
- Horario real de atención (el que se muestra en el sitio sigue siendo PROVISIONAL).
- Número de teléfono / WhatsApp definitivo.
- Instagram y otras redes oficiales.
- Correo receptor/formulario, si corresponde.

### Aviso de privacidad
- Nombre legal completo.
- Domicilio legal completo.
- Correo de privacidad.
- Teléfono.
- Texto legal definitivo ES/EN.

### Equipo
- Copy definitivo de las frases bajo cada integrante (hoy son PLACEHOLDERS neutrales, comentario `PENDIENTE ANITA` en `mockup.html`).
- Nombre y credenciales definitivas de Doctora.
- Nombre y credenciales definitivas de Cosmetóloga.

### Testimonios
- Testimonios reales autorizados.
- Nombres/autorizaciones.
- Fotografías de antes/después autorizadas.
- Traducción EN cuando corresponda.

### Datos estructurados / SEO local
- Teléfono para schema.
- URLs oficiales de redes (`sameAs`).
- Cualquier dato de negocio que no esté confirmado todavía.
- Completar/actualizar LocalBusiness/MedicalClinic cuando se reciban esos datos.

## Assets Disponibles
Carpeta `D'ALMA_LOGOS/`:
- `DALMA_Logo.svg` — Logo vectorizado
- `DALMA_Logo.pdf` — Logo en PDF
- `DALMA_Logo.webp` / `DALMA_Logo_Black.png` / `DALMA_Logo_White.png` / `DALMA_Logo_WhiteBackground.jpg`
- `DALMA_Logo_Transparent_4000px.png` — Logo de alta resolución con fondo transparente
- `DALMA_Favicon.ico` — Favicon

## Instrucción para Claude al Finalizar Cada Sesión
Al terminar cada sesión de trabajo, agrega una entrada en la sección **Historial de Sesiones** con el formato:

```
### YYYY-MM-DD
**Actividades:**
- [descripción de cada cambio o decisión importante]
```

## Propuesta Comercial
- **Documento:** `Propuesta_Web_DAlma.md`
- **Fecha de emisión:** Abril 27, 2026 | **Vigencia:** 30 días | **Entrega:** 18 días hábiles | **Revisiones:** 3 rondas
- **Inversión:** $19,800 MXN + IVA (50% inicio · 50% entrega)
- **Incluye:** Hasta 5 secciones, dominio 1 año, SSL, WhatsApp, formulario de contacto, Google Business

## Estado Actual de Archivos (actualizado 2026-06-20)

| Archivo | Estado | Notas |
|---|---|---|
| `design-preview.html` | ✅ Estable — no modificar | Sistema de diseño v1.0. Fuente de verdad visual. |
| `design-tokens.json` | ✅ Estable — no modificar | Tokens de color, tipografía, espaciado. |
| `wireframes.html` | ✅ Aprobado | Home actualizada: testimonios + CTA+mapa. 5 páginas. |
| `mockup.html` | ✅ En desarrollo | Home + Servicios aprobados; Contacto en primera versión. |
| `DESIGN.md` | ✅ Estable | Razonamiento de decisiones de diseño. |
| `D_Alma_Clinica.md` | 📄 Referencia | Documento completo de la clínica (480 líneas). Sirve como `llms.txt` estructurado para IA. |
| `Propuesta_Web_DAlma.md` | 📄 Referencia | Propuesta comercial de Bruno para el cliente. |
| `calendario-implementacion.html` | 📄 Referencia | Calendario visual de 6 fases: Arranque → Diseño → Desarrollo → Integraciones+SEO → Revisiones → Entrega/Publicación. |
| `llms.txt` | 🌐 SEO/GEO | Archivo para rastreadores de IA (GEO). Usa URLs `dalmaclinic.com.mx`. No commitear hasta tener dominio activo. |
| `robots.txt` | 🌐 SEO | Configurado para `dalmaclinic.com.mx`. Permite todos los bots incl. IA. No commitear hasta tener dominio activo. |
| `sitemap.xml` | 🌐 SEO | 5 URLs de `dalmaclinic.com.mx`. No commitear hasta tener dominio activo. |
| `DALMA_PREVIEW/` | 🚫 Local only — no commitear | Copia estática del mockup para despliegue manual en Cloudflare. Regenerar si cambia `mockup.html`. |

### Decisiones de diseño fijadas (no revertir sin acuerdo con Bruno/cliente)
- **Hero**: imagen aspiracional de bienestar/amor propio — no interior de clínica.
- **Testimonios en Home**: carrusel con 5 cards demo. Copys finales pendientes de la cliente.
- **Sección final Home**: layout 2 columnas con imagen de fondo. Izquierda: título + CTA. Derecha: mapa + horario. El Info Strip separado fue eliminado.
- **Cards de testimonios**: `bone-100` de fondo, `border-left: 2px taupe-500`, Cormorant Garamond italic.
- **Mapa**: placeholder visual. Se integrará Google Maps real cuando esté disponible.

---

## Historial de Sesiones

### 2026-09-26 — Ajustes finales de Anita y ubicación con mapa estático (local, NO desplegado)
**Estado: cambios commiteados en `main`; producción sin cambios (sigue el deploy del 2026-09-23). Sin deploy, sin Hostinger/Cloudflare/Google. `PUBLIC_LAUNCH` sigue `false`.**

- **Ubicación confirmada:** Plaza Patio, De Las Brisas 2404, Brisas del Pacífico, Cabo San Lucas, BCS, C.P. 23473 (schema.org ya coincidía; sin cambios). Pin del mapa = "Plaza Patio" (no "D'ALMA": el local/suite exacto sigue desconocido).
- **Mapa estático local (OpenStreetMap):** asset `imagenes-candidatas/mapa-plaza-patio.webp` (1200×600, ~55 KB), generado por `scripts/make-map.py` (100% local, SIN peticiones HTTP; requiere Pillow) desde el source `map-sources/osm-export-plaza-patio.png` (exportación oficial openstreetmap.org > Compartir > Imagen, una sola vez; `map-sources/` no se despliega). Coordenadas 22.9045296, -109.9333945. **No se descargan teselas** (la política de OSM prohíbe el prefetch/offline de `tile.openstreetmap.org`). Sin requests a mapas en runtime. Atribución visible "© OpenStreetMap contributors" (enlace independiente a openstreetmap.org/copyright, superpuesto en HTML). El mapa es el enlace a Google Maps (búsqueda por dirección, `target="_blank" rel="noopener noreferrer"`); **futuro: sustituir el `href` por el perfil real de Google Business Profile.** Alt ES/EN en la clave i18n `alt.map`.
- **Home:** tarjeta de ubicación corregida (`.clinic-strip` ahora crece con su contenido: antes altura fija + `overflow:hidden` recortaba la dirección); fondo de la tarjeta ~93% opaco y textos `#5F5651` (contraste AA); frase "Tu piel también cuenta tu historia." más grande (`clamp(1.85rem,3vw,2.7rem)`) y CTA "Agenda tu valoración" algo mayor.
- **Contacto:** dirección visible una sola vez; el mapa completo es clicable (chip "Abrir en Google Maps ↗"); atribución OSM enlace independiente; se eliminó el bloque duplicado bajo el mapa.
- **Nosotros:** espacio hero → primer bloque compactado en desktop (la foto 2:3 dictaba una fila de ~895 px); foto de Ana María se muestra COMPLETA (columna 400 px, sin recorte); móvil preservado.
- **Equipo:** María José eliminada; **Estefanía Serrano añadida como Cosmetóloga** (sobre la tarjeta que ya existía, con su foto). Las frases bajo cada integrante son **PLACEHOLDERS neutrales pendientes de copy definitivo de Anita** (Doctoras siguen "Dra. ———").
- **Foto:** retirada la segunda foto de Ana María con Sculptra (Anita no manejará esa marca); reutilización TEMPORAL de la foto principal en la tarjeta del equipo. **Pendiente sustituirla tras la nueva sesión fotográfica.**
- **Legibilidad/contraste:** nuevo token `--text-body:#5F5651` para párrafos de lectura (`.bt`, `.hero-sub`, `.svc-card-txt`; antes `taupe-500` ~3.5:1, ahora ~6.4–6.8:1); `.ftx-detail` a `taupe-600`; `.bt-lt` (texto sobre fondo oscuro) a `bone-300`; etiqueta "Filtrar por categoría" a `taupe-600`. Servicios revisado para WCAG AA en los textos tratados. Sin cambio de tamaños ni negritas. Sigue sin cumplir AA: texto blanco sobre el verde de WhatsApp (~2:1, color de marca) y los eyebrows decorativos `.ew` (~2.6:1); no tocados.
- **Sigue PROVISIONAL / pendiente (NO resuelto):** horario real (el visible es provisional), teléfono/WhatsApp, Instagram/redes, local/suite, datos legales restantes del aviso de privacidad, backend real del formulario, CAPTCHA, frases definitivas del equipo, nombres/credenciales de doctoras, testimonios reales, perfil real de Google Maps/Business Profile.
- **Recordatorio:** para cualquier servicio Google de D'ALMA usar EXCLUSIVAMENTE `clinic.dalma@gmail.com`.

### 2026-09-23 — Deploy multipágina bilingüe a Hostinger (pre-lanzamiento)
**Estado: arquitectura multipágina desplegada y validada en producción. El sitio sigue en pre-lanzamiento (no público).**

**1. Deploy multipágina.** La nueva arquitectura bilingüe está en Hostinger. Producción: ES `/`, `/nosotros/`, `/servicios/`, `/contacto/`, `/aviso-de-privacidad/`; EN `/en/`, `/en/about/`, `/en/services/`, `/en/contact/`. Se hizo en dos fases: primero todo salvo el `index.html` raíz (con validación intermedia de las rutas nuevas), después el reemplazo del `index.html` raíz.

**2. Estado pre-lanzamiento.** `PUBLIC_LAUNCH=false`: overlay "Próximamente / Coming soon" activo por defecto; `?preview=1` permite revisar el sitio completo; `noindex, nofollow` en las 9 páginas; **no existe `sitemap.xml`**; Testimonios desactivado (`ENABLE_TESTIMONIALS=false`), `/testimonios/` y `/en/testimonials/` devuelven 404. **El sitio no está públicamente lanzado.**

**3. Backup / rollback.** Backup manual previo al deploy: `C:\Users\bruno\Downloads\_public_html.zip`, 24,696,825 bytes, con el `index.html` anterior y las 20 imágenes de la versión anterior (descargado directo desde el gestor de archivos; no se dejó ningún ZIP en el servidor). Backup automático adicional de Hostinger: 2026-09-21 11:32 (el backup manual desde hPanel está bloqueado por el plan). **El rollback no fue necesario.** Rollback rápido autorizado si hiciera falta: restaurar solo el `index.html` viejo desde el ZIP (las carpetas y assets nuevos pueden quedarse).

**4. Archivos desplegados.** 8 rutas nuevas con su `index.html`; nuevo `index.html` raíz; `favicon.ico`; `robots.txt`; `imagenes-candidatas/imagen-para-hero-home-horizontal.webp` y `imagenes-candidatas/home-footer-dalma-still-life-horizontal.webp`. Las otras 18 imágenes ya existentes eran idénticas por MD5 al build y no se sobrescribieron. Se conservaron `imagen-para-hero-home-horizontal.png` y `home-footer-dalma-still-life-horizontal.jpg`: ya no están referenciadas por la web nueva pero permanecen en el servidor (~9 MiB, se pueden limpiar más adelante con autorización).

**5. robots.txt.** Ahora existe físicamente `public_html/robots.txt`. Respuesta pública: HTTP 200, `User-agent: *` / `Allow: /` (25 B); ya no aparece el bloque de Content Signals de Cloudflare que se servía antes cuando no había archivo físico. Mientras `PUBLIC_LAUNCH=false`, la protección contra indexación depende del meta robots `noindex, nofollow` de cada HTML, no de `robots.txt`.

**6. Trailing slash — RESUELTO.** Verificado en producción (sin `.htaccess`; Hostinger lo gestiona automáticamente):
- `/nosotros` → 301 → `/nosotros/`
- `/servicios` → 301 → `/servicios/`
- `/contacto` → 301 → `/contacto/`
- `/aviso-de-privacidad` → 301 → `/aviso-de-privacidad/`
- `/en` → 301 → `/en/`
- `/en/about` → 301 → `/en/about/`
- `/en/services` → 301 → `/en/services/`
- `/en/contact` → 301 → `/en/contact/`
Todos terminan en HTTP 200.

**7. Cloudflare.** Sigue activa la Redirect Rule www → apex (301). Verificado después del deploy: `https://www.dalmaclinic.com.mx/?preview=1` → 301 → `https://dalmaclinic.com.mx/?preview=1` (query string preservado) → carga la Home nueva. No fue necesaria ninguna purga de caché. DNS y SSL/TLS no se tocaron.

**8. Validaciones del deploy (todas OK):** las 9 páginas; rutas ES/EN reales; navegación multipágina (URLs cambian de verdad, sin `showPg`); selector ES/EN con rutas reales; favicon; canonical; hreflang; Open Graph/Twitter; JSON-LD `MedicalClinic`; imágenes (0 rotas); `noindex, nofollow`; overlay activo sin `?preview=1`; modo preview; Testimonios 404; ausencia de `sitemap.xml`; consola sin errores; sin overflow; hero WebP nueva. El `index.html` publicado coincide byte a byte (MD5 `7e8632f271e3395bdeda8a86e863703f`, 99,148 B) con `DALMA_BUILD/index.html`.

**9. `public_html/` actual.** Antes del deploy: `index.html` e `imagenes-candidatas/`. Después se añadieron `nosotros/`, `servicios/`, `contacto/`, `aviso-de-privacidad/`, `en/`, `favicon.ico` y `robots.txt`. **No existe `.htaccess`.** En la raíz superior del hosting existe `DO_NOT_UPLOAD_HERE` (marcador de Hostinger): no subir nada ahí ni tocarlo.

**10. Incidente 429.** Durante las validaciones automatizadas hubo un HTTP 429 temporal por exceso de peticiones al borde de Hostinger (barridos rápidos con curl desde la misma IP; un bucle de sondeo en segundo plano no se detuvo a tiempo y siguió consultando). Se resolvió solo al reducir el ritmo. Sin impacto permanente ni cambios necesarios. **Para futuras validaciones en producción: evitar barridos rápidos/repetitivos con curl; una petición a la vez y con pausas.**

**11. Pendientes de Anita:** sin cambios, siguen abiertos (ver sección "Pendientes Bloqueados por Anita"): teléfono/WhatsApp, redes, datos legales, horario, nombres/credenciales faltantes, testimonios, datos adicionales para schema y backend final del formulario.

**12. Google:** mantener la restricción de arriba — usar EXCLUSIVAMENTE `clinic.dalma@gmail.com` para Search Console, GA4, GTM, Google Ads, Google Business Profile y cualquier servicio de Google de D'ALMA.

**13. Siguiente etapa (no iniciada):** Google Search Console, GA4, GTM, Google Ads, eventos `click_whatsapp` / `click_phone` / `generate_lead`, y CAPTCHA/backend del formulario cuando corresponda.

### 2026-09-22 — SEO técnico, accesibilidad, favicon, schema.org y redirect Cloudflare
**Estado al cierre de esa sesión: mejoras técnicas commiteadas y pusheadas a `main`. (Actualización: la versión multipágina fue desplegada a Hostinger el 2026-09-23 — ver la entrada de esa fecha más arriba.)**

**1. Último commit funcional:** `28054ce` — "Mejora SEO tecnico y accesibilidad Dalma" (`mockup.html` + `scripts/build-site.py`).

**2. Favicon:**
- `DALMA_Favicon.ico` (de `D'ALMA_LOGOS/`) se copia de forma reproducible a `DALMA_BUILD/favicon.ico` en cada build (`scripts/build-site.py`), no es una copia manual.
- Ruta pública: `/favicon.ico`, referenciada con `<link rel="icon">` en las 9 páginas.
- `apple-touch-icon` sigue pendiente y es opcional — no existe todavía un asset cuadrado adecuado.
- **No se modificó ni adaptó ningún logo** — Bruno no tiene autorización para tocar el logotipo.

**3. Open Graph / Twitter Cards:** implementados en las 9 páginas — `og:title`, `og:description`, `og:url`, `og:type`, `twitter:card`, `twitter:title`, `twitter:description`. **Sin `og:image` ni `twitter:image`**: Bruno no tiene autorización para modificar/adaptar el logotipo y no existe todavía un asset social aprobado para ese propósito.

**4. Imágenes / CLS:** las 24 etiquetas `<img>` del sitio (20 archivos únicos) tienen `width`/`height` intrínsecos reales (leídos del archivo, no estimados). Se agregó `height:auto` únicamente donde era necesario para conservar el `aspect-ratio` existente (`.svc-card img`, `.std-card img`, y 5 fotos de equipo en Nosotros) — sin ese ajuste, los atributos width/height rompían el recorte cuadrado/16:10/3:4 en todo navegador real (hallazgo verificado con una reproducción aislada, no un artefacto de la herramienta de pruebas). Diseño visual verificado sin cambios en desktop y mobile 390px.

**5. Accesibilidad:**
- Botón flotante de WhatsApp (`.wafloat`): `aria-label="WhatsApp"` agregado — tiene nombre accesible aunque el texto visual (`.wa-txt`) se oculte en mobile.
- El SVG decorativo dentro del botón lleva `aria-hidden="true"` para evitar que un lector de pantalla lo procese como contenido adicional (el nombre accesible ya lo da el `aria-label` del enlace).
- Filtro de categorías de Servicios (`.svc-filter-select`): agregado `:focus-visible{outline:2px solid var(--taupe-500);outline-offset:2px;}`, reutilizando el mismo criterio visual que `.svc-toggle:focus-visible`/`.fq-q:focus-visible`. El comportamiento con mouse/click no cambió.

**6. Schema.org (JSON-LD):**
- `@type: MedicalClinic`, mismo `@id: https://dalmaclinic.com.mx/#business` en las 9 páginas (ES y EN) — una sola entidad real, nunca duplicada.
- Incluye únicamente datos confirmados: `@context`, `@type`, `@id`, `name`, `url`, `description` (traducida ES/EN, reutilizando la meta description real de Home), `address` (PostalAddress con la dirección confirmada por Bruno).
- **NO incluye:** horario (`openingHours`), teléfono, email, `sameAs`, reviews/ratings, ni `logo` (no hay un logo servido públicamente en el build todavía).
- Generado desde `scripts/build-site.py` (`build_business_schema()`), no está hardcodeado por página.

**7. Datos pendientes de Anita:** ver sección **"Pendientes Bloqueados por Anita"** más arriba en este documento (Contacto, Aviso de privacidad, Equipo, Testimonios, Datos estructurados/SEO local). **El horario que aparece visualmente en el sitio NO debe tratarse como dato confirmado** (ver nota en "Datos del Negocio").

**8. Cloudflare — Redirect Rule desplegada:**
- Zona: `dalmaclinic.com.mx`.
- Regla activa: **"Redirect www a dominio raiz (301)"**.
- Comportamiento: `https://www.dalmaclinic.com.mx/*` → `https://dalmaclinic.com.mx/${path}`, status `301`, con `Preserve query string` activado.
- Verificado en producción: `https://www.dalmaclinic.com.mx/servicios/?foo=bar` → `301` → `https://dalmaclinic.com.mx/servicios/?foo=bar` (path y query string preservados).
- **DNS y SSL/TLS no se modificaron** en esta tarea — solo se agregó la Redirect Rule.

**9. Pendiente técnico de auditoría — RESUELTO el 2026-09-23:** el comportamiento de rutas sin slash final (`/nosotros` → `/nosotros/`, etc.) quedó verificado en producción tras el deploy multipágina (ver entrada 2026-09-23).

**10. Producción (al cierre de esa sesión):** la versión multipágina aún no estaba desplegada; se desplegó el 2026-09-23. Cloudflare solo había recibido la Redirect Rule www→apex (punto 8). `PUBLIC_LAUNCH` sigue `false` en la fuente (`mockup.html`).

**11. Estado Git:** commit funcional `28054ce` — "Mejora SEO tecnico y accesibilidad Dalma" (pusheado a `origin/main`). Commit de documentación de esta misma jornada aplicado por separado sobre `CLAUDE.md`.

### 2026-09-21 — Arquitectura multipágina bilingüe, auditoría técnica y cierre de jornada
**Estado: arquitectura ES/EN funcional en local, verificada y commiteada. Producción sin cambios — sigue con la publicación inicial de la sesión 2026-09-13.**

**1. Commit funcional de la jornada:** `c554398` — "Optimiza imagenes y prepara formulario de contacto" (incluye también, sobre el mismo `mockup.html`, todo el trabajo de arquitectura bilingüe del commit previo `de143f8` — "Implementa arquitectura multipagina bilingue Dalma").

**2. Arquitectura de rutas actual (generada por `scripts/build-site.py` a partir de `mockup.html`):**
- **ES:** `/`, `/nosotros/`, `/servicios/`, `/contacto/`, `/aviso-de-privacidad/`
- **EN:** `/en/`, `/en/about/`, `/en/services/`, `/en/contact/`
- Cada ruta es un archivo físico real (`index.html` en su carpeta), sin `showPg()` ni JS de por medio para la navegación cross-page — los enlaces son `href` reales.

**3. Estado de flags (en `mockup.html`):**
- `PUBLIC_LAUNCH = false`
- `ENABLE_TESTIMONIALS = false`

**4. Estado del build:**
- `scripts/build-site.py` genera `DALMA_BUILD/` a partir de `mockup.html` (fuente única).
- `DALMA_BUILD/` está en `.gitignore` — no se versiona, se regenera localmente cuando hace falta revisar el resultado.
- Sin `sitemap.xml` mientras `PUBLIC_LAUNCH=false` (se genera automáticamente al activar el flag, con las rutas ES+EN activas).
- `/testimonios/` y `/en/testimonials/` **no se generan** mientras `ENABLE_TESTIMONIALS=false` — ambas rutas devuelven 404 real (verificado), no un redirect ni un archivo vacío.

**5. SEO bilingüe:**
- Cada página EN trae el HTML ya en inglés desde el primer byte (verificado con `curl`, sin ejecutar JS) — nada de "carga en español y JS traduce después".
- `canonical` autocanónico por ruta (nunca cruza de idioma).
- `hreflang` recíproco ES↔EN en los 4 pares (Home, Nosotros/About, Servicios/Services, Contacto/Contact), con `x-default` apuntando siempre a la versión ES.
- Aviso de privacidad sigue siendo **una sola URL**: `/aviso-de-privacidad/` (decisión de proyecto). No existe ni se creará `/en/privacy-policy/` — cuando Anita entregue el documento definitivo, esa misma página incluirá el texto completo en ES + EN. Desde las páginas EN, "Privacy Notice" enlaza a esa misma URL española.

**6. Imágenes optimizadas (WebP, reemplazando PNG/JPG pesados y las 2 imágenes de Unsplash detectadas en la auditoría):**
- Hero de Home: `imagenes-candidatas/imagen-para-hero-home-horizontal.webp` (antes `.png`, ~6.7 MB → ~119 KB).
- Sección final de Home, hero de Servicios/Services y hero de Contacto/Contact: `imagenes-candidatas/home-footer-dalma-still-life-horizontal.webp` (antes `.jpg`, ~2.6 MB → ~182 KB; mismo archivo reutilizado en las 3 secciones, sin duplicar).
- Card "Fillers" de Home: `imagenes-candidatas/servicios-fillers.webp` (antes imagen externa de Unsplash).
- **0 referencias a Unsplash** en `mockup.html`, `scripts/build-site.py` y `DALMA_BUILD/` (verificado).
- Los originales pesados (`.png`/`.jpg`) se conservan intactos en `imagenes-candidatas/` como fuente — la web solo usa las versiones `.webp`.

**7. Formulario de Contacto:**
- Ahora es un `<form id="contact-form">` real (antes no existía la etiqueta `<form>`).
- Los 4 campos (nombre, teléfono, tratamiento, mensaje) tienen `id`/`name`/`label for` asociados correctamente; nombre/teléfono/tratamiento son `required`, mensaje queda opcional (su propio label ya lo indica).
- `autocomplete="name"` y `autocomplete="tel"` donde aplica.
- Validación HTML nativa conservada (sin `novalidate`).
- Corregido además un `outline:none` sin alternativa en los campos del formulario — ahora tienen `:focus-visible` visible.
- **Envío bloqueado temporalmente a propósito**: un listener de `submit` hace `preventDefault()` solo cuando el formulario ya pasó la validación nativa, y muestra un mensaje `aria-live="polite"` ("El envío del formulario estará disponible próximamente." / "Form submission will be available soon.") en vez de enviar algo.
- **No existe backend, no hay `fetch`/`XHR`, no hay CAPTCHA, no hay `generate_lead`** — nada de esto se conectó todavía.

**8. Producción:** no se hizo deploy en esta jornada. Hostinger y Cloudflare no fueron tocados. El sitio publicado sigue siendo la versión de la sesión 2026-09-13 (overlay "Próximamente" activo, arquitectura de un solo archivo). Todo lo documentado aquí existe solo en `DALMA_BUILD/` local y en el repositorio (`main`), pendiente de subirse a Hostinger.

**9. Pendientes técnicos para la próxima sesión** (todos resueltos sin depender de Anita):
- Favicon (ya existe `DALMA_Favicon.ico` en `D'ALMA_LOGOS/`, solo falta enlazarlo).
- Open Graph / Twitter Cards.
- `width`/`height` explícitos en las imágenes (riesgo de CLS).
- `aria-label="WhatsApp"` en el botón flotante (pierde su texto visible en mobile).
- `:focus-visible` en el filtro de categorías de Servicios/Services (`.svc-filter-select`, distinto del ya corregido en el formulario de Contacto).
- Página 404 personalizada.
- Datos estructurados (schema.org `LocalBusiness`/`FAQPage`) con los datos ya seguros (nombre, dirección, horario, FAQ reales).
- Revisión de redirect `www` → `non-www` (Cloudflare).
- Configurar Search Console, GA4 y GTM.
- Definir tracking de `click_whatsapp` / `click_phone` / `generate_lead`.
- Checklist y plan de rollback para el día del deploy real.

**10. Bloqueados por Anita** (no son fallas técnicas, son información pendiente):
- Número de WhatsApp / teléfono real.
- Handles reales de redes sociales (Instagram/Facebook).
- Datos legales completos del Aviso de privacidad (nombre legal, domicilio, correo de privacidad, teléfono, URL del sitio).
- Nombres/credenciales faltantes del equipo (Doctora, Cosmetóloga — siguen como "———").
- Testimonios reales y autorizados (ES + EN) para activar `ENABLE_TESTIMONIALS`.
- Backend/destino final del formulario de Contacto, en la medida en que dependa de a dónde debe llegar (correo/WhatsApp de la clínica).

**11. Estado Git:**
- Commit funcional real de hoy: `c554398` — "Optimiza imagenes y prepara formulario de contacto".
- Commit previo de la misma jornada: `de143f8` — "Implementa arquitectura multipagina bilingue Dalma".
- `DALMA_BUILD/` y `DALMA_PREVIEW/` permanecen fuera de Git (el primero vía `.gitignore`, el segundo nunca se ha agregado).
- Sin secretos ni archivos locales auxiliares incluidos en ningún commit de la jornada.

### 2026-09-13 (sesión 5) — Cierre de publicación inicial
**Estado: publicación inicial de D'ALMA en producción, cerrada y confirmada por Bruno.**

**1. Fecha de publicación inicial en Hostinger:** 2026-09-13.

**2. Dominio publicado:** [https://dalmaclinic.com.mx/](https://dalmaclinic.com.mx/)

**3. Ubicación en Hostinger:** `public_html/`

**4. Archivos finales publicados:**
- `index.html` (copia de `mockup.html` en el momento de la publicación, con Testimonios ya oculto).
- `imagenes-candidatas/` (solo las 20 imágenes locales referenciadas por el HTML).

**5. Overlay "Próximamente":** activo por defecto para el público general — bloquea visualmente el sitio (ver sesión "2026-09-13" más abajo para el detalle de implementación). No se modificó en esta sesión.

**6. Modo revisión:**
- `https://dalmaclinic.com.mx/?preview=1` desactiva el overlay y guarda la preferencia en `localStorage` de ese navegador.
- `https://dalmaclinic.com.mx/?preview=0` vuelve a activar el overlay.
- Sin parámetro, se respeta lo guardado en `localStorage`; si no hay nada guardado, se muestra el overlay.

**7. Pruebas reales confirmadas por Bruno en el dominio productivo (no solo en el entorno de pruebas local):**
- El dominio normal (sin parámetro, navegación normal) muestra el overlay "Próximamente".
- `?preview=1` muestra la web completa, sin overlay.
- En modo incógnito (sin `localStorage` previo), el dominio normal sigue mostrando el overlay — confirma que el bloqueo es el comportamiento por defecto real para cualquier visitante nuevo.

**8. Testimonios ocultos** (ver detalle completo en la sesión "2026-09-13 (sesión 4)"):
- `ENABLE_TESTIMONIALS = false`.
- Ocultos en el menú desktop (header).
- Ocultos en el menú mobile (hamburguesa) de las 6 páginas.
- Ocultos en el bloque de Home (entre Tratamientos y Filosofía).
- Ocultos en el footer (columna Páginas) de las 6 páginas.
- Página completa `pg-testimonios` (incluye "Antes y después") bloqueada: inalcanzable desde cualquier menú.
- `showPg('testimonios')` redirige de forma segura a Home si se llama manualmente.
- Confirmado en producción (`?preview=1`): no aparece en header, no aparece en Home, no aparece en footer, no aparece "Antes y después".

**9. Motivo de ocultar Testimonios:** todavía no existen testimonios reales autorizados por Anita; los testimonios y el bloque "Antes y después" actuales son contenido demo/inventado (nombres ficticios, sin fotos ni autorizaciones reales) y no deben mostrarse públicamente ni en revisión con la cliente.

**10. Estructura conservada:** todo el HTML de Testimonios (carrusel de Home, página completa, carrusel propio, bloque Antes/Después) sigue en el archivo — no se borró nada, solo se oculta mediante la bandera `ENABLE_TESTIMONIALS`.

**11. Para reactivar Testimonios cuando Anita entregue contenido real:**
1. Recibir testimonios reales autorizados de Anita (citas, nombres, tratamiento asociado).
2. Reemplazar los textos demo actuales (Sofía Arriaga, Carlos Medina, Gabriela Rojas, Laura Villanueva, Patricia Elizondo, y las citas anónimas M.R./L.G./P.M./R.A./C.V. de la página Testimonios) por el contenido real.
3. Validar permisos/autorizaciones firmadas antes de publicar fotos de "Antes y después".
4. Cambiar `ENABLE_TESTIMONIALS` a `true`.
5. Probar Home, header (desktop y mobile), footer y la página Testimonios completa.
6. Regenerar `DALMA_PREVIEW/` y volver a publicar en Hostinger.

**12. Pendientes antes del lanzamiento final (fase siguiente, no implementada — solo documentada):**
- Aprobación final de Anita para retirar el overlay "Próximamente".
- Retirar el bloque `<!-- PRELAUNCH OVERLAY -->` cuando Anita apruebe el lanzamiento público.
- Completar los placeholders legales pendientes del Aviso de privacidad (nombre legal, domicilio, correo de privacidad, teléfono, URL del sitio).
- Definir el número de WhatsApp definitivo (hoy sigue como placeholder).
- Conectar el formulario de Contacto a un backend real (hoy sigue siendo mockup visual, sin `<form>` funcional).
- Agregar CAPTCHA (ej. Cloudflare Turnstile) al formulario de contacto, con validación server-side.
- Crear y configurar los correos institucionales (`@dalmaclinic.com.mx`) en Hostinger.
- Crear y configurar Google Analytics 4 (GA4).
- Crear y configurar Google Tag Manager (GTM).
- Conectar Google Search Console.
- Definir y preparar eventos de conversión (envío de formulario, clic a WhatsApp, etc.).
- Preparar Meta Pixel y eventos hacia Meta Business Suite, una vez existan las redes sociales y el Business Manager de la clínica.

Ninguno de estos pendientes fue implementado en esta sesión — quedan únicamente documentados para la siguiente fase, según instrucción explícita de Bruno.

### 2026-09-13 (sesión 4)
**Solicitud de Bruno:** ocultar Testimonios (Home, página completa, Antes/Después, menú y footer) antes de publicar, porque los testimonios actuales son demo/inventados y no hay todavía testimonios ni fotos reales autorizadas por Anita. No se puede mostrar ni siquiera en modo revisión (`?preview=1`) con Anita. La estructura debe conservarse para reactivarla fácilmente cuando existan testimonios reales.

**Actividades:**
- **Bandera de control agregada:** `const ENABLE_TESTIMONIALS = false;`, declarada al inicio del `<script>` principal, justo antes del diccionario `I18N`, con comentario explicando que `false` = testimonios ocultos por no haber contenido real autorizado, y `true` = reactivar solo cuando Anita entregue testimonios reales y se reemplacen los textos/nombres demo.
- **Testimonios ocultos sin borrar HTML**, usando la bandera:
  - Los 18 enlaces "Testimonios" (nav desktop + menú móvil + footer, repartidos en las 6 páginas) se marcaron con el atributo `data-testimonials-link`. Al cargar, si `ENABLE_TESTIMONIALS` es `false`, un script oculta el `<li>` contenedor (nav/menú móvil) o el propio `<a>` (footer, que no tiene `<li>`), evitando huecos en el menú.
  - El bloque de Testimonios de Home se marcó con `data-testimonials-section` en su `<section>` y se oculta igual (`display:none`) cuando la bandera está en `false`. Home fluye directo de "Tratamientos" a "Nuestra filosofía".
  - La página `pg-testimonios` (incluye su propio carrusel y el bloque "Antes y después") ya no es alcanzable desde ningún menú (sus enlaces están ocultos) y además `showPg()` redirige de forma segura: si alguien llama `showPg('testimonios')` con la bandera en `false`, se convierte internamente en `showPg('home')` antes de tocar el DOM o el `<title>`/meta — nunca se activa ni se deja visible el título "Testimonios".
  - El carrusel de testimonios (`initCarousel`, usado tanto en Home como en la página Testimonios) ahora solo se inicializa cuando `ENABLE_TESTIMONIALS` es `true`, para no dejar temporizadores corriendo en segundo plano sobre secciones ocultas.
- **No se borró ningún testimonio, nombre, cita ni el bloque Antes/Después** — todo el HTML sigue en el archivo, solo oculto por la bandera.
- **Para reactivar cuando Anita envíe testimonios reales:**
  1. Reemplazar los textos demo (citas y nombres: Sofía Arriaga, Carlos Medina, Gabriela Rojas, Laura Villanueva, Patricia Elizondo, M.R./L.G./P.M./R.A./C.V. en la página Testimonios) por testimonios reales autorizados.
  2. Revisar permisos/autorizaciones de fotos para "Antes y después" antes de mostrarlas.
  3. Cambiar `ENABLE_TESTIMONIALS` a `true`.
  4. Probar Home, menú (desktop y mobile), footer y la página Testimonios completa.
  5. Volver a publicar.
- Verificado con `?preview=1` (simulado por la limitación conocida de `data:` URLs de este entorno de pruebas): sin "Testimonios" en nav desktop ni mobile, sin el bloque en Home, sin nombres inventados ni frases sensibles ("Resultados reales", "Fotos publicadas con autorización firmada") visibles en el render, footer sin Testimonios (Inicio/Nosotros/Servicios/Contacto/Aviso de privacidad intactos), `showPg('testimonios')` manual redirige a Home sin romper nada, overlay normal y `?preview=0` sin cambios (no se tocó ese bloque), sin overflow horizontal en 390/430/844/1024/1440px, sin `undefined` en ES/EN, sin errores de consola, 235/235 claves i18n y 104/104 IDs únicos.

### 2026-09-13 (sesión 3)
**Solicitud de Bruno:** quitar por completo la barra negra superior del mockup ("D'ALMA — Mockup del cliente" con los botones Home/Nosotros/Servicios/Testimonios/Contacto), ya que era solo una ayuda de navegación interna para desarrollo y el sitio está por publicarse. Debe quedar únicamente el menú blanco real como navegación oficial.

**Actividades:**
- **Barra negra (`.pbar`/`.pb`) eliminada por completo**, tanto del HTML (existía un único bloque, compartido por todas las páginas, justo antes del contenedor que envuelve las 6 páginas) como del CSS (`.pbar`, `.pbar-lbl`, `.pb`, `.pb:hover`, `.pb.on` y su override en el media query de mobile). El contenedor que envolvía todas las páginas (antes `<div class="frame">`, con `margin-top:44px` para dejar espacio a la barra) se dejó como `<div>` simple sin esa clase, ya que ese margen ya no aplica.
- **Dependencias de `.pb` resueltas:** todas las llamadas `showPg('pagina', document.querySelectorAll('.pb')[N])` repartidas en nav, menú móvil, footer, hero y CTAs de las 6 páginas se simplificaron a `showPg('pagina')`. Dentro de `showPg()` se quitó la línea que limpiaba la clase activa de `.pb` (ya no existe). `goToService()` también se actualizó para llamar `showPg('servicios')` sin el segundo argumento. `showPg()` ya aceptaba `btn` como parámetro opcional, así que no falla sin él.
- **Nav blanco reposicionado:** `.nav{top:44px}` → `top:0` (queda pegado arriba, sin espacio vacío). `.nav-mmenu{top:104px}` → `top:60px` (104px = 44px de la barra negra + 60px del nav compacto; al quitar la barra solo queda la altura del nav).
- **Overlay "Próximamente" no se tocó** — se verificó que sigue funcionando igual: normal (`mockup.html`) sigue bloqueando con el overlay; en modo revisión (overlay oculto vía `?preview=1`/localStorage, simulado en pruebas por la limitación de `data:` URLs del navegador de este entorno) el sitio se ve completo, sin barra negra y con el nav blanco pegado arriba.
- Verificado en navegador: 235/235 claves ES/EN sin huecos, 104/104 IDs únicos, sin `undefined`, sin errores de consola, sin overflow horizontal en 390/430/768/844/1024/1440px, nav sticky en `top:0` en todos los anchos, menú hamburguesa abre pegado debajo del nav (sin espacio de la barra negra) en mobile, las 6 páginas (Home/Servicios/Nosotros/Testimonios/Contacto/Aviso de privacidad) navegan correctamente con `showPg()`, `goToService()`, el botón flotante de WhatsApp y "Agenda tu valoración" siguen llevando a Contacto, y el enlace de Aviso de privacidad del footer sigue actualizando el hash (`#aviso-de-privacidad`).

### 2026-09-13 (sesión 2)
**Solicitud de Bruno:** que el overlay de "Próximamente" siga bloqueando al público general, pero que él pueda revisar la web completa sin que el overlay le aparezca cada vez que la abre.

**Actividades:**
- **Overlay convertido de bloqueo fijo a modo revisión por URL + localStorage.** Se quitó `class="launch-locked"` hardcodeada de `<html>` y `<body>` — ahora un script inline, colocado justo después del propio overlay (muy al inicio de `<body>`, antes de que el resto de la página se pinte, para que un visitante normal nunca vea un parpadeo del sitio real), decide en cada carga:
  - `?preview=1` en la URL → oculta el overlay, quita el bloqueo de scroll, y guarda `localStorage.dalmaPreviewMode = 'true'`.
  - `?preview=0` en la URL → borra ese valor de `localStorage` y vuelve a mostrar el overlay bloqueando.
  - Sin parámetro → revisa `localStorage`: si dice `'true'`, el sitio se ve completo sin overlay; si no, se muestra el overlay igual que antes.
  - Importante detalle de robustez: la decisión de *esta* carga se toma directamente del parámetro de la URL cuando está presente (no depende de releer `localStorage` después de escribir), para que funcione aunque el navegador bloquee el guardado en algún caso raro — `localStorage` solo se usa para *recordar* la próxima vez.
  - Sigue sin haber botón de cerrar, sin contraseña, sin pedir correo, sin WhatsApp, sin formularios ni tracking nuevo — el público normal no tiene ninguna forma visible de quitar el overlay.
- **Cómo usarlo:** Bruno abre una vez `mockup.html?preview=1` (o la URL publicada + `?preview=1`) → el overlay desaparece y el sitio queda navegable normalmente en ese navegador. Las siguientes veces puede entrar directo a `mockup.html` (sin el parámetro) y seguirá viendo el sitio completo, porque quedó guardado en `localStorage` de ese navegador/dispositivo. Para volver a activar el bloqueo (por ejemplo, en otro dispositivo, o si quiere volver a ver el overlay), abre `mockup.html?preview=0` una vez.
- **Antes del lanzamiento final** hay que retirar todo el bloque marcado `<!-- PRELAUNCH OVERLAY -->` / `<!-- /PRELAUNCH OVERLAY -->` (el `<div>` del overlay + el `<script>` de decisión) y el bloque CSS marcado igual — ya no hay ninguna clase hardcodeada que quitar de `<html>`/`<body>` porque ahora todo lo controla ese script.
- **Limitación del entorno de pruebas de esta sesión (no del sitio):** el navegador de previsualización sandboxed usado para verificar convierte la página en una URL `data:` al cargarla, y estas URLs `data:` tienen "origen opaco" en cualquier navegador — por diseño del navegador (no un bug), `localStorage` está deshabilitado ahí (mensaje exacto: *"Storage is disabled inside 'data:' URLs"*) y el query string (`?preview=1`) se pierde al convertir la página. Esto impidió probar el flujo real de principio a fin navegando con la URL tal cual. Se verificó en su lugar, con máximo rigor posible: (a) la función de decisión completa simulando `localStorage` con un objeto en memoria, confirmando los 5 escenarios A-E exactamente como se pidieron; (b) que mostrar/ocultar el overlay y bloquear/desbloquear el scroll funciona correctamente en ambas direcciones aplicando el estado directamente. Recomiendo a Bruno confirmar el flujo completo abriendo el archivo directamente en su navegador (doble clic, o subiendo `?preview=1` a la URL una vez publicado en Cloudflare) — ahí sí es un `file://` o `https://` normal, sin ninguna de estas restricciones.
- Verificado en navegador: 235/235 claves ES/EN sin huecos, 104/104 IDs únicos, sin `undefined`, sin errores de consola, sin overflow horizontal en 390/430/844/1024/1440px, Home/Nosotros/Servicios/Testimonios/Contacto/Aviso de privacidad visibles con el overlay desactivado.

### 2026-09-13
**Solicitud de Anita:** la web ya está casi lista para publicarse, pero los usuarios normales todavía no deben poder navegarla — quiere un overlay de "Próximamente" que bloquee visualmente el sitio mientras se preparan los últimos detalles (número de WhatsApp, correos, contenido pendiente).

**Actividades:**
- **Overlay "Próximamente" agregado (bloqueante, sin cerrar).** Vive como un bloque único justo después de `<body>`, marcado con comentarios `<!-- PRELAUNCH OVERLAY -->` / `<!-- /PRELAUNCH OVERLAY -->`, más un bloque CSS marcado igual cerca del inicio del `<style>`. Cubre toda la pantalla (`position:fixed;inset:0;z-index:999999`, por encima incluso de la barra de mockup interna), bloquea clics hacia el contenido (verificado con clics reales que no navegan nada) y bloquea el scroll vía `class="launch-locked"` en `<html>` y `<body>` (`overflow:hidden`). No tiene botón de cerrar, no pide correo, no muestra WhatsApp ni número, no carga formularios ni tracking nuevo. Texto **bilingüe fijo** (ES arriba, EN abajo) en vez de depender del selector de idioma, porque el overlay lo bloquea — decisión explícita de Bruno para este caso. **Para retirarlo cuando se publique de verdad:** quitar `class="launch-locked"` de `<html>` y de `<body>`, borrar el `<div id="launch-overlay">` completo, y borrar el bloque CSS marcado "PRELAUNCH OVERLAY" (ninguna otra parte del sitio depende de esas clases).
- **Nosotros — menos aire entre el hero y la primera foto:** el hero (`.sec-sm.sec-alt`) tenía un padding inline fijo de 72px arriba/abajo que ni siquiera respetaba el breakpoint mobile (por ser inline, ganaba sobre `.sec-sm{padding:36px 20px}`). Se reemplazó por dos clases nuevas y específicas de Nosotros: `.nos-hero` (40px/36px desktop, 28px/28px mobile) y `.nos-first-block` en la sección de Ana María (40px arriba desktop, 32px mobile, en vez de los 88px que trae `.sec` en todas las demás páginas). Total de aire entre hero y primera foto: 160px→76px en desktop, ~144px+→~60px en mobile. No se tocó `.sec`/`.sec-sm`/`.sec-alt` globales, así que Home/Servicios/Testimonios/Contacto quedan intactos.
- **Legibilidad/tipografía — subida moderada, priorizando mobile y sin tocar el nav:** se aumentaron entre 0.02 y 0.06rem (≈0.3–1px) los tamaños de: descripciones de cards (Home destacados y Servicios), textos y CTA dentro de `.ftx` (bio Ana María), footer (tagline, links, columna de horario, copyright, títulos de columna), formulario e info de Contacto (labels, inputs, valores), respuestas de FAQ (`.fq-a`, con su `max-height` ampliado de 400px a 500px para que ninguna respuesta larga quede cortada — verificado que la más larga solo necesita 215px, hay margen de sobra), el Aviso de privacidad completo (nota de pendientes, párrafos, subtítulos H3, banner EN), botones (`.bp`,`.bs`,`.bwa`), el dropdown de categorías de Servicios, las notas de rol del equipo en Nosotros, y varios textos sueltos (botón del CTA final de Home, horario/mapa). **Deliberadamente no se tocó** `.nav-cta`, `.nav-links a`, `.lang-btn` ni nada del nav — subir esos tamaños podía reabrir el bug de overflow del rango 769–1030px corregido en la sesión del 2026-08-24, así que se dejaron igual; tampoco se tocó nada dentro de Testimonios/Antes-después (instrucción explícita de esta tarea). Verificado sin overflow en los 11 anchos probados y que ninguna card/botón quedó roto.
- **Imagen del CTA final de Home cambiada** (ya no parece spa): antes usaba `home-footer-dalma-still-life-horizontal.png` (foto de still-life de spa: vela, gua sha, espejo). **Hallazgo importante:** ese archivo `.png` ya no existe en disco — en algún momento Bruno/Anita lo reemplazaron externamente por una versión `.jpg` con el mismo nombre base (fecha de modificación de hoy), lo cual dejaba **la imagen del hero de Contacto rota** (referencia a un archivo `.png` inexistente) desde antes de que empezara esta sesión. La nueva foto `.jpg` es una imagen de marca D'ALMA (con logo visible en productos y tablet) mostrando una consulta real en sala de tratamiento — exactamente el tipo de imagen "de clínica" que pedía esta tarea, y con proporción horizontal que encaja mucho mejor en la franja ancha del CTA que cualquier foto vertical disponible. Se actualizó la referencia en **ambos lugares** donde se usaba (`.png`→`.jpg`): el CTA final de Home (cambio pedido) y el hero de Contacto (arreglo del enlace roto, no pedido explícitamente pero necesario). `alt`/`data-i18n-alt` (`alt.interior`) actualizados en ES/EN para describir la nueva imagen. **Nota:** el `.png` sigue apareciendo como "deleted" en `git status` porque estaba trackeado en un commit anterior — no se hizo `git add`/`rm` en esta sesión, queda para que Bruno lo revise cuando haga commit.
- **Control de Peso y bienestar — se mantiene la imagen actual.** Se revisaron las 6 imágenes candidatas sin usar en `imagenes-candidatas/` buscando una alternativa; ninguna es temáticamente relevante a control de peso (son todas de rostro/piel: crema, microneedling, evaluación facial). **Recomendación:** cuando haya oportunidad de tomar/conseguir una foto nueva para esta card, buscar algo que transmita acompañamiento médico y bienestar (ej. una consulta cálida entre médico y paciente) en vez de solo una cinta métrica alrededor de la cintura, para reforzar el reposicionamiento ya hecho de "Control de Peso" a "Control de Peso y bienestar". No es urgente — la imagen actual es válida y ya fue aprobada.
- **Pendiente operativo — correos institucionales con Hostinger (no implementado, solo documentado):** Anita quiere correos con el dominio (`@dalmaclinic.com.mx`). Antes de poder crearlos, revisar en Hostinger/hPanel:
  1. Confirmar que el dominio `dalmaclinic.com.mx` ya está registrado y activo.
  2. Qué servicio de correo trae o se contrató (Hostinger Email, Titan Email, cPanel Email, Google Workspace u otro) y cuántos buzones permite el plan.
  3. Crear inicialmente solo las cuentas necesarias, por ejemplo `contacto@`, `hola@`, `anita@` (dominio a confirmar — no se debe inventar).
  4. Configurar/verificar registros MX, SPF, DKIM y DMARC.
  5. Probar envío y recepción con Gmail, y revisar que no caiga en spam.
  6. Configurar Webmail o cliente de correo si Anita lo pide.
  No se guardan contraseñas ni accesos aquí — eso se gestiona directamente en Hostinger.
- Verificado en navegador: 235/235 claves ES/EN sin huecos, 104/104 IDs únicos, sin `undefined`, sin errores de consola, sin overflow horizontal en 1440/1366/1280/1100/1024/844/800/768/430/390/360px, overlay probado con clics reales (no navega nada), menú hamburguesa y filtro de Servicios siguen funcionando con el overlay desactivado temporalmente para pruebas.

**Qué falta antes de publicación real** (adicional a lo ya documentado en sesiones previas — testimonios/antes-después demo, datos del equipo, formulario real, Turnstile, WhatsApp/Instagram definitivos, aviso de privacidad con placeholders):
- Quitar el overlay "Próximamente" (ver instrucciones arriba) cuando Anita confirme que se puede publicar de verdad.
- Confirmar visualmente la nueva imagen del CTA de Home y del hero de Contacto abriendo el archivo localmente (el navegador de esta sesión no pudo renderizarla, limitación ya conocida de esa herramienta).
- Decidir si vale la pena una foto nueva para Control de Peso y bienestar (no urgente).
- Avanzar el pendiente operativo de correos institucionales en Hostinger.

### 2026-09-04
**Actividades:**
- **Aviso de privacidad — enlace muerto corregido.** Fuente usada: `Docs Word/Preguntas y aviso de privacidad .docx` (única encontrada; incluye también las FAQ ya integradas antes, sin relación con este cambio). El documento trae dos versiones del aviso ("simplificado" e "integral"); se integraron **ambas, completas y sin resumir**, en una nueva página `pg-privacidad` dentro de `mockup.html`. El footer de las 5 páginas (Home, Nosotros, Servicios, Testimonios, Contacto) y el de la nueva página ahora usan `<a href="#aviso-de-privacidad" onclick="showPg('privacidad');history.replaceState(null,'','#aviso-de-privacidad');return false;">`. Se agregó `history.replaceState` (no estaba en el ejemplo original del prompt) porque con solo `showPg(...);return false;` el hash de la URL nunca cambiaba — necesario para cumplir el requisito de que la URL sí refleje `#aviso-de-privacidad`.
- **Placeholders pendientes del aviso (sin inventar datos):** el documento integral trae 5 datos sin completar por la clínica — `[NOMBRE LEGAL COMPLETO DE LA PERSONA FÍSICA O MORAL]`, `[DOMICILIO COMPLETO]`, `[CORREO DE PRIVACIDAD]` (aparece 4 veces), `[TELÉFONO]` y `[DIRECCIÓN DEL SITIO WEB]`. Se dejaron visibles tal cual en la página (con estilo itálico discreto) y se agregó una nota visible arriba del contenido avisando que el aviso no debe considerarse versión final hasta completarlos. **Este aviso no debe publicarse tal cual — falta que Bruno/Anita completen esos datos.**
- **Sin traducción legal al inglés:** el aviso completo se muestra siempre en español (en ambos idiomas del sitio), tal como pidió Bruno. En modo EN se agrega únicamente un texto breve aclaratorio: "This legal notice is currently available in Spanish." No se tradujo el documento legal por iniciativa propia.
- Home: "Tratamientos destacados" → **"Tratamientos"** (ES) / "Featured Treatments" → **"Treatments"** (EN). Solo el título de sección; las cards no se tocaron.
- Home: **eliminado el bloque oscuro "QUOTE DARK"** que aparecía entre Testimonios y Filosofía (cita "No se trata de cambiar quién eres..." + 2 CTAs "Conoce nuestra historia"/"Ver servicios"). Se quitó porque repetía casi textualmente la frase del Hero y el sentimiento de "cómodo, seguro y acompañado" que ya está en el pilar de Filosofía inmediatamente después, y sus 2 CTAs no aportaban ninguna acción que el nav, el Hero o el CTA+mapa final no cubrieran ya. Se eliminaron las 4 claves i18n que quedaron huérfanas (`home.quote.text/p/cta1/cta2`, ES y EN). No se tocó Testimonios ni Filosofía.
- Home: **"Nuestra filosofía" ahora es el H2 semántico real** de su sección (antes era un eyebrow visual sin jerarquía de encabezado). "¿Por qué D'ALMA?" pasó a ser un párrafo de apoyo (ya no H2), conservando su estilo visual grande. Se renombró la clave `home.phil.eyebrow` a `home.phil.h2` (ahora contiene "Nuestra filosofía") y se creó `home.phil.h2` → antiguo valor pasó a nueva clave `home.phil.statement` ("¿Por qué D'ALMA?"). La frase "Primero te escuchamos. Después vemos qué necesitas." se conservó sin cambios. Verificado que no quedan dos H2 compitiendo en esa sección.
- Contacto: FAQ ya no muestra "¿Tienes dudas?" duplicando el eyebrow "Preguntas frecuentes" — se eliminó el eyebrow y el H2 ahora dice directamente **"Preguntas frecuentes"** / "Frequently asked questions". Preguntas y respuestas sin cambios.
- Verificado en navegador: 235/235 claves ES/EN sin huecos, 103/103 IDs únicos, sin `undefined`, sin errores de consola, sin overflow horizontal en 1440/1366/1280/1100/1024/844/800/768/430/390/360px, los 6 enlaces "Aviso de privacidad" (5 footers + el propio) navegan y cambian el hash correctamente, menú hamburguesa funciona dentro de la nueva página.

### 2026-08-24 (sesión 3)
**Actividades:**
- Corregido el bug real de overflow del nav detectado en la auditoría (rango ~769px–1030px, incluye tablets, laptops pequeñas y mobile en horizontal): el nav de escritorio (links + selector de idioma + botón "Agenda tu valoración") no cabía en ese rango, causando overflow horizontal real (`scrollWidth > clientWidth`), el botón cortado a 2 líneas y "Contacto"/"ES" pegados sin espacio. Solución: se subió el punto donde aparece el menú hamburguesa de 768px a 1100px, agregando las mismas 3 reglas que ya existían para mobile (`.nav` compacto, ocultar `.nav-links`/`.nav-cta`, mostrar `.nav-ham`) al bloque `@media(max-width:1100px) and (min-width:769px)` que ya existía para el hero. No se tocó el resto del layout de secciones (hero, cards, footer) en ese rango — solo el nav. El `top` del menú móvil (`.nav-mmenu{top:104px}`) sigue siendo correcto porque ahora el nav mide 60px de alto en todo el rango ≤1100px, igual que en mobile. Verificado sin overflow en 1440/1366/1280/1100/1050/1024/1000/932/844/800/768/430/390/360px, y que el menú hamburguesa abre/cierra igual en todo ese rango ampliado.
- Corregido el botón verde de WhatsApp dentro de la propia página de Contacto, que antes tenía `href="#"` sin `onclick` (no hacía nada al hacer clic). Como todavía no existe el número definitivo, no se inventó ningún `wa.me`: ahora el botón hace scroll suave hasta la fila que muestra "[NÚMERO PENDIENTE]" (`id="ci-wa-row"`) y la resalta brevemente (1.6s) con un contorno sutil (`.ci-row-focus`), sin usar `alert()`. Los demás botones de WhatsApp del sitio (footer, Nosotros, Testimonios, flotante) no se tocaron — siguen redirigiendo a Contacto como antes.
- **Formulario de Contacto — documentado como pendiente crítico, sin implementar nada:** el formulario sigue siendo mockup visual (sin `<form>`, sin `name` en los campos, sin `action`, sin backend). No se agregó `fetch`, endpoints, Turnstile ni GTM en esta pasada. Pendientes antes de publicación final:
  1. Convertir Contacto en un `<form>` real con `name` en cada campo.
  2. Definir el endpoint (Cloudflare Worker, Function, u otro servicio).
  3. Validación frontend mínima (campos requeridos, formato de teléfono).
  4. Validación backend del lado servidor.
  5. Cloudflare Turnstile con validación server-side (el widget visual solo no protege nada sin esa validación).
  6. Definir feedback de éxito/error visible para el usuario.
  7. Conectar medición de conversiones (GTM/GA4/Meta) después de que el envío funcione de verdad.
- **Seguridad anti-bots — documentado, no implementado:** no se implementa todavía porque el sitio es estático, no existe endpoint de formulario, no hay `wa.me` real, y Turnstile requiere validación server-side que hoy no existe. Plan futuro, en orden: (1) formulario real primero; (2) Cloudflare Turnstile con validación server-side en Worker/backend; (3) rate limiting sobre el endpoint real; (4) posible ruta intermedia `/go/whatsapp` para medir clics y redirigir a `wa.me` una vez exista el número; (5) WAF/Managed Challenge de Cloudflare solo si aparece evidencia real de abuso, para no frenar leads legítimos.
- No se tocaron testimonios de Home, la página Testimonios, ni el bloque Antes/Después (nombres, estrellas, frases y disclaimers intactos) — sigue pendiente ocultarlos antes de publicación final, como ya estaba documentado.
- Verificado en navegador: 238/238 claves ES/EN sin huecos, 100/100 IDs únicos, sin `undefined`, sin errores de consola, nav/menú móvil/dropdown/cards/FAQ/CTAs probados con clics reales.

### 2026-08-24 (sesión 2)
**Actividades:**
- Unificado el nombre del servicio de Microneedling en todo el sitio (card de Servicios, footer de las 5 páginas, select de Contacto) a **"Microneedling / Dermapen / Manchas"** (ES) / **"Microneedling / Dermapen / Dark Spots"** (EN, reutilizando la traducción que ya existía en footer/formulario). El título de la card cambió de "Microneedling y Despigmentantes" a esta redacción; el resto ya estaba consistente. `svc-microneedling`, `goToService()` e imagen del servicio sin cambios.
- Unificados los CTAs a 2 textos en todo el sitio: **"Agenda tu valoración"** (antes también aparecía como "Agendar cita" en nav/menú móvil) y **"Escríbenos por WhatsApp"** (antes "Agenda por WhatsApp" en footer, CTAs oscuros de Nosotros/Testimonios y botón de Contacto). EN: "Book Your Consultation" y "Message us on WhatsApp". Ningún número de WhatsApp fue modificado (sigue en `href="#"`, placeholder).
- Home: subtítulo del hero y subtítulo de "Tratamientos destacados" actualizados con los nuevos textos de Anita/Bruno (ES/EN). H1 semántico sin cambios.
- Bloque "¿Por qué D'ALMA?": nueva frase de apoyo bajo el título ("Primero te escuchamos. Después vemos qué necesitas.") y los 3 pilares reescritos (Primero te escuchamos / Resultados naturales / Un espacio cercano), ES/EN.
- Servicios: agregado bloque de entrada arriba del filtro ("¿Qué te gustaría mejorar?" + texto de apoyo), verificado que no alarga demasiado la sección en mobile. Filtro de categorías reemplazado: de 8 botones-pill a un único `<select id="svc-filter-select">` (más compacto, mejor en mobile), con las nuevas categorías más claras: Líneas de expresión y armonización facial, Hidratación/manchas y textura de la piel, Regenerativos, Capilares, Depilación, Imperfecciones, Control de peso. La agrupación de tratamientos por categoría no cambió (mismos `data-cat`), solo las etiquetas visibles — verificado que las 8 opciones filtran correctamente y que Plasma Pen permanece junto a Verrugas y Queloides en "Imperfecciones", separado de Microneedling. `goToService()` actualizado mínimamente para resetear el nuevo `<select>` en vez del pill "Todos".
- "Ver más" renombrado a "Conoce el tratamiento" (ES) / "Learn about the treatment" (EN) en las 10 cards; el link ahora es más grande (.72rem→.8rem), más oscuro (taupe-600→taupe-700) y con subrayado, sin parecer botón principal.
- Contraste mejorado en textos descriptivos pequeños: `.std-card-txt` (descripción de tratamientos) y `.fq-a` (respuestas de FAQ) pasaron de `--taupe-500` a `--taupe-600` (de ~3.55:1 a ~4.9:1 de contraste, cumple AA) sin usar negro puro.
- Control de Peso renombrado a **"Control de Peso y bienestar"** en card, footer, select de Contacto y alt de imagen; nueva frase corta y nuevo texto descriptivo enfocados en acompañamiento médico y seguimiento, sin mencionar L-TRZ, retatrutide ni ninguna sustancia específica (verificado con búsqueda de texto en toda la página).
- Nosotros: reescrito el inicio de la bio de Ana María con el nuevo texto de apertura; se conservó la información profesional existente (comunicóloga/periodista, vínculo con clínicas estéticas) reordenada como segundo párrafo, y se retiró el párrafo final que quedó redundante con la nueva apertura, para no alargar el texto. No se inventó ningún dato nuevo.
- Verificado en navegador: 238/238 claves ES/EN sin huecos, sin `undefined`, sin errores de consola, sin overflow horizontal en 1440/1366/1280/1024/768/430/390/360px, exactamente un `<h1>` en Home, cards expandibles y navegación principal intactas.

**Pendientes / decisiones que requieren aprobación de Anita o de Bruno antes de publicar:**
1. **"Un espacio cercano"** (pilar de "¿Por qué D'ALMA?"): el texto usado es la adaptación neutral de Bruno sobre la propuesta original de Anita ("cómoda, segura y acompañada"). Falta que Anita apruebe este cambio de tono.
2. **Equipo (Nosotros)**: falta confirmar nombre completo, especialidad y credenciales relevantes de cada médico/staff, y una descripción breve desde la esencia de cada persona. Hoy las tarjetas de Doctora siguen con placeholder "———".
3. **Testimonios (crítico, antes de publicar)**: los 4 testimonios de Home y la sección "Antes y después" de la página Testimonios siguen siendo contenido demo/mockup (nombres inventados: Sofía Arriaga, Carlos Medina, Gabriela Rojas, Laura Villanueva). Más delicado aún: el texto fijo de "Antes y después" afirma "Resultados reales, misma luz y ángulo" y el disclaimer dice "Fotos publicadas con autorización firmada" — esto es una afirmación falsa mientras no existan fotos ni autorizaciones reales; las tarjetas en sí son solo bloques de color, no fotos. Bruno quiere avisarle a Anita que estas dos secciones no deben mostrarse al público hasta tener testimonios y autorizaciones reales. No se ocultó nada en esta pasada (para no eliminar secciones sin autorización explícita) — recomiendo decidir con Anita si se oculta la sección completa o al menos se retira el texto de "resultados reales"/"autorización firmada" antes de cualquier publicación pública.
4. **Contacto**: revisar UX en mobile (hoy puede requerir varios scrolls para llegar al CTA de WhatsApp); buscar inspiración para mejorar el diseño de la página; planear medición de conversiones (envío de formulario, clic a WhatsApp, eventos en GTM, Meta Business, Google Ads, GA4). No se implementó tracking, scripts de GTM, eventos nuevos ni integraciones en esta pasada.

### 2026-08-24
**Actividades:**
- Verificada la nueva imagen `imagenes-candidatas/control-de-peso.webp` (reemplazada manualmente por Anita/Bruno con el mismo nombre de archivo): archivo válido y completo (RIFF/WebP bien formado, sin corrupción), contenido confirmado por lectura directa (foto de midición de cintura con cinta métrica, tono cálido acorde a la marca). Proporción nativa (1312×816 ≈ 1.61) casi idéntica al recorte de card 16:10 (1.6), por lo que `object-fit:cover` recorta menos del 1% — imperceptible. No se ajustó `object-position` (no hacía falta) ni se tocó el nombre/ruta del archivo. Nota técnica: el navegador de previsualización usado en esta sesión no logró renderizar esta imagen puntual (limitación de caché de esa herramienta, no del sitio); se recomienda a Bruno hacer una verificación visual rápida al abrir el archivo localmente.
- Reducido nuevamente el tamaño de la frase emocional del Hero de Home (`.hero-statement`) porque en laptop se partía en 4 líneas en algunos casos límite: desktop `clamp(2rem,3.4vw,3.2rem)` → `clamp(1.8rem,2.85vw,2.85rem)`; mobile `clamp(1.85rem,7vw,2.4rem)` → `clamp(1.7rem,6.4vw,2.25rem)`. Verificado con medición real de líneas (Range.getClientRects) en 1440/1366/1280/1024px: exactamente 3 líneas en los cuatro, con margen real (antes el ajuste anterior dejaba 1024px al límite, con solo ~7px de holgura, lo que explica el salto a 4 líneas reportado). El H1 de negocio no se tocó.

### 2026-08-23 (sesión 3)
**Actividades:**
- Corregida la estructura semántica del hero de Home: el antiguo eyebrow ("Medicina estética & regenerativa · Cabo San Lucas") se convirtió en el `<h1>` real de la página, con texto ampliado a "Clínica de medicina estética & regenerativa · Cabo San Lucas" (conserva estilo visual pequeño/uppercase vía clase `.ew` + nueva clase `.hero-business-h1`). La frase emocional ("No se trata de cambiar quién eres...") dejó de ser `<h1>` y pasó a ser `<p class="hero-statement">`, reduciendo su tamaño visual (`clamp(2rem,3.4vw,3.2rem)` desktop / `clamp(1.85rem,7vw,2.4rem)` mobile) para verse más equilibrada junto al nuevo H1. Home ahora tiene exactamente un `<h1>` semántico.
- i18n: la key `home.hero.h1` ahora contiene el texto de negocio (antes tenía la frase emocional); nueva key `home.hero.statement` para la frase emocional; key huérfana `home.hero.eyebrow` eliminada de ambos diccionarios. De paso se corrigió un bug preexistente: el valor de este texto en el diccionario JS usaba la entidad `&amp;` pero el atributo `data-i18n` se aplica vía `textContent`, por lo que se habría visto literalmente "&amp;" en pantalla tras cualquier cambio de idioma o carga inicial; se cambió a `&` literal en el diccionario (el HTML estático sí conserva `&amp;`, que es lo correcto ahí).

### 2026-08-23 (sesión 2)
**Actividades:**
- Quitadas las etiquetas/eyebrows visibles de categoría (`Inyectables`, `Faciales`, `Regeneración`, `Capilares`, `Depilación`, `Especializados`, `Control de peso`) dentro de las 10 cards de Servicios; la card ahora va directo de imagen a nombre del tratamiento. Se conservó intacto `data-cat` en cada card, por lo que los filtros superiores siguen funcionando igual. Las 4 claves de badge que quedaron sin uso (`badge.capilares`, `badge.depilacion`, `badge.especializados`, `badge.control_peso`) se eliminaron del diccionario ES/EN; los badges del Home (Tratamientos destacados) no se tocaron y siguen mostrándose ahí.
- Footer (5 páginas) actualizado: la columna "Servicios" pasó de 5 a los 10 tratamientos completos, cada uno enlazando a su card en Servicios vía `goToService()` (ya hacía scroll automático a la card correcta, reseteando el filtro a "Todos"). Traducciones EN agregadas para los enlaces nuevos.

### 2026-08-23
**Actividades:**
- Ajustes finales de contenido en `mockup.html` a partir del documento de Bruno "Ajustes finales página D'Alma": Home (nuevo H1/subtítulo, CTAs renombrados a "Agenda tu valoración" / "Conoce nuestros tratamientos"); Servicios (las 8 tarjetas existentes se reestructuraron a un formato único: nombre + frase poética + "Ver más" → explicación ampliada + CTA, eliminando frases funcionales y los bloques de duración/recuperación/beneficio/marcas); 2 tratamientos nuevos agregados: Plasma Pen (categoría Especializados) y Control de Peso (nueva categoría, sin presentarlo como "inyecciones para adelgazar" ni mencionar L-TRZ/Peptology); filtro "Control de peso" agregado (8 categorías en total); "Verrugas, Queloides y Plasmapen" renombrado a "Verrugas y Queloides" (ya no menciona triamcinolona intralesional, y el Plasma Pen quedó como tratamiento propio).
- Contacto: formulario reducido a 4 campos (Nombre, WhatsApp, Tratamiento de interés, Mensaje opcional), encabezado simplificado a una sola frase, lista de tratamientos del select reconstruida (11 opciones, incluye Plasma Pen y Control de Peso).
- Nosotros: nueva frase de encabezado y nueva bio de Ana María (3 párrafos); sección Equipo ampliada de 4 a 5 tarjetas con una nueva tarjeta de Cosmetóloga (placeholder "———", sin nombre real) usando la imagen `cosmetologa.webp`; línea humanizante agregada bajo cada rol (excepto Ana María); "Nuestra forma de trabajar" con 3 textos nuevos (un título cambiado: "Confianza y acompañamiento" → "Cercanía y acompañamiento").
- CTAs consolidados en todo el sitio a 2 variantes principales: "Agenda tu valoración" y "Agenda por WhatsApp" (antes había varias formas distintas dispersas en Nosotros, Testimonios, Servicios, footer y Contacto).
- Imágenes nuevas incorporadas sin renombrar: `plasma-pen.webp`, `control-de-peso.webp` y `cosmetologa.webp` (el documento original la nombraba `commetologa.webp`; se usó el archivo real en disco, que está bien escrito como `cosmetologa.webp`).
- Verificado en navegador: i18n ES/EN completo (233 claves, sin huecos), sin IDs duplicados, sin imágenes rotas, sin errores de consola, sin overflow horizontal en 1440/1024/768/430/390/360px. No se tocó `DALMA_PREVIEW/`, `wireframes.html`, `design-preview.html` ni imágenes existentes. No se hizo commit ni push.

### 2026-08-09 (sesión 9)
**Actividades:**
- Agregados bloques resumidos de FAQ en Home (3 preguntas: q1, q2, q3) y Servicios (5 preguntas: q1, q7, q9, q11, q12), reutilizando las mismas claves i18n y respuestas ya integradas en Contacto (sin duplicar texto, sin nuevas traducciones). Nuevo H2 compartido `faq.shared.h2` ("Preguntas frecuentes"/"Frequently asked questions"). IDs únicos por sección (`home-fq-*`, `svc-fq-*`), Contacto conserva sus 12 FAQ e IDs originales sin cambios.

### 2026-08-09 (sesión 8)
**Actividades:**
- Integradas las 12 FAQ definitivas de `dalma_faqs_contacto.md` en Contacto, reemplazando las 8 placeholder; accordion 100% funcional (sin preguntas deshabilitadas), traducidas fielmente al inglés.
- Integrados meta titles y meta descriptions de `dalma_meta_titles_descriptions.md` para las 5 páginas internas: `<title>` y `<meta name="description">` en `<head>` para carga inicial (Home), y diccionario `PAGE_META` (ES/EN) que actualiza ambos dinámicamente en `showPg()` y `setLang()`.
- Servicios: cards rediseñadas para mostrar solo imagen, categoría, título y frase funcional de forma permanente; el resto (frase poética, descripción, datos rápidos y CTA) se agrupó en `.svc-more`, desplegable con hover/focus en desktop y con botón "Ver más / Ver menos" en mobile. Se cierra la card expandida al cambiar de filtro.
- Nosotros: actualizada la foto de encabezado de Ana María (`directora-perfil-vertical`) — Anita reemplazó el archivo por una versión editada en formato `.png`; se actualizó la referencia en `mockup.html` (mismo recorte, mismo `alt`, mismo lugar). El `.jpg` anterior queda eliminado del repositorio en este commit.

### 2026-08-02 (sesión 7)
**Actividades:**
- Retirado el botón verde de WhatsApp del hero de Home (quedaban "Agenda tu cita" y "Conoce los servicios"). Se elimina para una presentación inicial más limpia; el botón flotante de WhatsApp global y los demás botones de WhatsApp del sitio (Nosotros, Servicios, Testimonios, Contacto, footer) quedan intactos.

### 2026-08-02 (sesión 6)
**Actividades:**
- Retirada la frase "Al enviar, aceptas nuestro aviso de privacidad." / "By submitting, you agree to our Privacy Notice." debajo del formulario de Contacto, por decisión de diseño: el enlace de Aviso de privacidad vive únicamente en el footer (columna Páginas). Limpiadas las claves `cont.form.privacy_pre` y `footer.privacy_lc` (sin uso tras el retiro).

### 2026-08-02 (sesión 5)
**Actividades:**
- Servicios: agregado label discreto "Filtrar por categoría" / "Filter by category" justo arriba de la barra de filtros, con el estilo `.ew` (eyebrow) ya usado en el resto del sitio. Sin cambios de lógica de filtrado ni de layout de cards.

### 2026-08-02 (sesión 4)
**Actividades:**
- Aviso de privacidad: el enlace visible ya no vive en la barra de copyright del footer (ahí existía pero con el mismo color/tamaño que el texto de copyright, sin subrayado, por eso no se distinguía como enlace). Se movió a la columna "Páginas" del footer en las 5 páginas, con el mismo estilo que los demás enlaces de esa columna. La frase debajo del formulario de Contacto (ya existente antes de esta sesión) se dejó sin tocar.

### 2026-08-02 (sesión 3)
**Actividades:**
- Corregidos 4 bugs técnicos detectados en la auditoría del mockup, solo en `mockup.html`: (1) aviso de privacidad de Contacto ya no se destruye al cambiar ES/EN (el párrafo pasó de `data-i18n` a `data-i18n-html`, conservando el enlace); (2) navegación entre páginas internas ya no anima el scroll hacia arriba (`showPg()` usa `window.scrollTo({behavior:'instant'})`, sin tocar el `scroll-behavior:smooth` global ni el scroll suave de `goToService()`); (3) los puntos del carrusel de testimonios ahora reflejan solo posiciones reales según el ancho (3 en desktop/tablet, 5 en mobile, recalculado en resize), aplicado a las dos instancias del carrusel; (4) el logo D'ALMA en las 5 páginas ahora navega a Home y cierra el menú mobile si estaba abierto.

### 2026-08-02 (sesión 2)
**Actividades:**
- Barra de filtros de Servicios: centrada en desktop/tablet (`justify-content:center`), y en mobile pasó de wrap asimétrico (3+3+1) a grilla de 2 columnas con el 7º botón ("Especializados") centrado en su propia fila. Sin cambios de lógica, categorías ni iconos.
- Corregido detalle preexistente: el título "Depilación Láser" no tenía `data-i18n`; ahora usa `svc.depilacion.title` (ES "Depilación Láser" / EN "Laser Hair Removal") y cambia de idioma correctamente.
- FAQ de Contacto: no existía accordion funcional (solo la pregunta 1 tenía respuesta, visible de forma permanente; las preguntas 2-8 no tenían `.fq-a` en el HTML ni había JS que las abriera). Implementado accordion real y accesible (`button`, `aria-expanded`, una sola respuesta abierta a la vez, ícono `+` que rota, transición de altura). La pregunta 1 quedó funcional con su respuesta existente; las preguntas 2-8 quedan con botón deshabilitado (no se inventó contenido clínico) hasta que Anita entregue esas respuestas.

### 2026-08-02
**Actividades:**
- Ajuste UX en Servicios (post-revisión de Anita), solo en `mockup.html`: frase funcional breve agregada en cada uno de los 8 tratamientos (debajo del título, antes de la frase poética/descripción, clase nueva `.svc-functional`); CTAs variados y honestos por tratamiento (siempre hacia Contacto, sin WhatsApp ni páginas falsas); grid de Servicios (`#svc-grid`) ajustado a 2 columnas en desktop/tablet y 1 en mobile, sin tocar el `.g3` global que usan Home/Nosotros/Testimonios. Traducciones ES/EN agregadas para todo lo nuevo, selector de idioma verificado.

### 2026-07-12
**Actividades:**
- Auditoría de UX de la página Servicios: se detectaron 3 formatos de tarjeta distintos, filtros de categoría decorativos (no filtraban nada) y varios tratamientos sin botón de acción. Rediseño completo: 9 tratamientos unificados en un solo formato de tarjeta (`.std-card`), filtros funcionando de verdad vía `data-cat`, `goToService()` corregido para resetear el filtro activo. Banner "¿No sabes cuál elegir?" retirado a petición de Bruno.
- Hero de Home: corregido bug de responsividad — la imagen vivía en una columna de 42% con `object-position` fijo y se cortaba/desaparecía al redimensionar. Rediseñado como imagen de fondo completo + tarjeta de texto flotante con glassmorphism (`backdrop-filter: blur`).
- Imágenes reales incorporadas: Hydrafacial (Home), 6 tratamientos en Servicios (Botox, Fillers, Hydrafacial, Microneedling, Capilares, PDRN&Exosomas) desde `imagenes-candidatas/SERVICIOS/`, y foto de Ana María en Nosotros (`DIRECTORA 1.jpg` / `DIRECTORA 2.jpg`, comprimidas de 24 MB / 21.8 MB a ~100 KB antes de usarlas en el sitio).
- Barra de presentación del mockup (pbar): scroll horizontal en mobile en vez de desbordarse y cortar el último botón.
- Orden del menú principal cambiado a Inicio · Servicios · Nosotros · Testimonios · Contacto (Servicios antes que Nosotros, prioriza conversión sobre historia de marca).
- Reescritura de copy en tono "Humano · Elegante · Cálido · Moderno · Natural · Accesible": Hero, bio de Ana María, y las 8 descripciones de tratamientos de Servicios. Ningún dato médico, tiempo, marca o beneficio real fue alterado — solo estilo de redacción. Limpieza de em-dashes en todo el copy visible del sitio.
- Página Testimonios: la sección de testimonios pasó de grilla estática a carrusel rotativo, reutilizando (no duplicando) el componente que ya usaba Home.
- **Sitio convertido a bilingüe ES/EN**: sistema `data-i18n` vanilla JS embebido (sin dependencias ni fetch externo, por compatibilidad con `file://`), 224 strings traducidos con calidad nativa, selector "ES · EN" en nav (desktop + mobile) y footer, persistencia en `localStorage`. Cobertura verificada automáticamente contra el HTML (0 huecos). Regla permanente establecida: todo cambio de copy futuro debe sincronizarse en ambos idiomas sin que se tenga que recordar — documentada en memoria de Claude para esta sesión y las siguientes.

### 2026-07-07
**Actividades:**
- Actualización de imágenes en `mockup.html` para alinear mejor la identidad visual de D'ALMA: solo rutas, sin modificar textos, estilos ni navegación.
- Home: card Hydrafacial → `home-card-hydrafacial-aquapure-vertical.png`; bloque CTA+Mapa → `home-footer-dalma-still-life-horizontal.png`.
- Contacto: header → `home-footer-dalma-still-life-horizontal.png` (misma imagen que footer Home).
- Servicios (Más tratamientos): cards Tratamientos Capilares, Depilación Láser y Verrugas/Queloides/Plasmapen → imágenes de `imagenes-candidatas/`.

### 2026-06-29 (sesión 3)
**Actividades:**
- Habilitada navegación interna completa en `mockup.html` para mejorar la revisión de Anita. No se modificaron textos, diseño ni imágenes.
- Añadida función `goToService(id)`: navega a Servicios + hace scroll suave al bloque del tratamiento.
- Añadidos IDs en Servicios: `svc-botox`, `svc-fillers`, `svc-hydrafacial`, `svc-pdrn-exosomas`, `svc-depilacion`.
- CTAs hacia **Servicios**: "Conoce los servicios", "Ver servicios", "Conoce nuestros servicios" → `showPg('servicios',...)`.
- CTA hacia **Nosotros**: "Conoce nuestra historia" → `showPg('nosotros',...)`.
- CTAs hacia **Contacto**: todos los botones "Agendar cita" (nav-cta + mm-cta × 5 páginas), "Agenda tu cita", "Agendar valoración", "Agendar cita" (Hydrafacial), todos los links WA ("Enviar WhatsApp", "Preguntar por WhatsApp", "Agendar por WhatsApp", botón flotante).
- Cards destacadas de Home: "Ver tratamiento →" usa `goToService()` con el ID correspondiente.
- Footers (5 en total, replace_all): columna Páginas y columna Servicios con navegación interna funcional.
- Únicos `href="#"` sin destino: "Aviso de privacidad" (5 footers) y botón WhatsApp dentro de la página Contacto (número pendiente de Anita).

### 2026-06-29 (sesión 2)
**Actividades:**
- Limpieza de CTAs sin destino real en la página **Servicios** de `mockup.html`: eliminados todos los botones "Saber más →" (ftx-cards) y enlaces "Ver tratamiento →" (std-cards) dentro de Servicios. No existen páginas individuales por tratamiento, por lo que estos CTAs generaban expectativa falsa de navegación.
- Reemplazado "Agenda sin costo" por "Agendar valoración" en el bloque de valoración de Servicios — no hay confirmación de Anita de que la valoración sea gratuita.
- Eliminado "Sin compromiso." del CTA section al fondo de Servicios — condición comercial no validada por la cliente.
- Los "Ver tratamiento →" del **Home** (cards Tratamientos Destacados) se conservaron intactos.
- No se tocaron: Home, Nosotros, Testimonios, Contacto, imágenes, `wireframes.html`, `design-preview.html`, `DALMA_PREVIEW/`, `Docs Word/D´ALMA CLINIC TRATAMIENTOS.md`.

### 2026-06-29 (sesión 1)
**Actividades:**
- Integración en la página **Servicios** de `mockup.html` de los tiempos aproximados, recuperación y beneficios principales de cada tratamiento, tomados del archivo `Docs Word/D´ALMA CLINIC TRATAMIENTOS.md` (información de Anita). No se inventó ni reescribió ningún dato.
- Tratamientos con bloque `svc-meta` (3 columnas): Botox, Fillers y Armonización Facial, Hydrafacial.
- PDRN & Exosomas: bloque `svc-dual` con dos mini-bloques internos (PDRN / Exosomas). Se mantuvo como una sola sección.
- Tratamientos con bloque `svc-info` (compacto): Microneedling y Despigmentantes, Tratamientos Capilares, Depilación Láser, Verrugas/Queloides/Plasmapen.
- CSS nuevo: `.svc-meta`, `.svc-meta-lbl`, `.svc-meta-val`, `.svc-dual`, `.svc-dual-block`, `.svc-dual-name`, `.svc-info`, `.svc-info-row`. Responsive: apila a 1 columna en `max-width:768px`.
- No se modificaron: Home, Nosotros, Testimonios, Contacto, imágenes, navegación, footer, `wireframes.html`, `design-preview.html`, `DALMA_PREVIEW/`, `Docs Word/D´ALMA CLINIC TRATAMIENTOS.md`.

### 2026-06-21
**Actividades:**
- Desarrollo visual de la página **Nosotros** en `mockup.html` usando la estructura y textos de `wireframes.html`
- Mockup publicado temporalmente en Cloudflare para revisión de Anita: `https://dalma-mockup.clinic-dalma.workers.dev`
- `DALMA_PREVIEW/` es una copia local estática (no en git) usada para el despliegue manual. Si se modifica `mockup.html`, regenerar la carpeta y volver a desplegar.
- Imágenes usadas: `directora.jpg` (Ana María / bio + tarjeta equipo), `doctora.jpg` (2 tarjetas Dra. —), `recepcion.jpg` (María José)
- Se añadió botón "Nosotros" al pbar y se actualizaron los índices de pb[1]→pb[2] (Servicios) en Home y Contacto
- Desarrollo visual de la página **Testimonios** en `mockup.html` con placeholders elegantes para antes/después
- Wiring completo de los 5 links de navegación (desktop + mobile) en todas las páginas
- Merge con origin/main: se integraron limpiezas ponytail del 2026-06-20 (SVG sprite, CSS cleanup, `showPg()` fix)

### 2026-06-20
**Actividades:**
- Revisión del repositorio GitHub (`argihm-jpg/DALMA_WEB`) — repo local en sync con main, sin commits nuevos desde 2026-06-18
- Identificados 6 archivos locales no trackeados (no están en GitHub ni estaban en CLAUDE.md): `D_Alma_Clinica.md`, `Propuesta_Web_DAlma.md`, `calendario-implementacion.html`, `llms.txt`, `robots.txt`, `sitemap.xml`
- Actualización de CLAUDE.md: dominio `dalmaclinic.com.mx` agregado a Datos del Negocio; nueva sección Propuesta Comercial; tabla de archivos ampliada con los 6 archivos nuevos
- Revisión ponytail de `mockup.html` y aplicación de limpiezas: CSS muerto eliminado (`.clinic-strip-txt`, `.info-strip` y 6 reglas relacionadas + sus overrides responsive); dos bloques `@media(max-width:768px)` y dos `480px` fusionados en uno cada uno; SVG de WhatsApp definido una vez como `<symbol id="ico-wa">` y referenciado con `<use>` en los 7 lugares donde aparecía (~3 KB menos); `showPg()` ahora resetea `body.style.overflow` directamente, eliminando llamadas redundantes a `closeMenu` en los onclick de navegación
- Commit `5b00d30` — "Limpieza ponytail: reduce complejidad en mockup.html y actualiza CLAUDE.md"

### 2026-06-17 — Resumen de sesión
**Actividades:**
- Ajuste de imágenes en Home y Servicios para alinearlas mejor con los comentarios de Anita (encuadre, recorte, `object-position`)
- Reemplazo y ajuste visual de imágenes en las cards de "Tratamientos destacados" del Home (Botox, PDRN & Exosomas)
- Incorporación de imágenes de referencia desde `imagenes-candidatas/` al repositorio
- Desarrollo visual inicial de la sección/página **Contacto** en `mockup.html`, basado en la estructura existente de `wireframes.html`: hero, formulario de contacto, info + mapa placeholder, FAQ, footer
- La sección Contacto queda como primera versión visual — pendiente de revisión y ajustes posteriores

### 2026-06-17 (sesión 6)
**Actividades:**
- Card de Botox (Home): se volvió a usar `inyeccion-facial-desde-arriba-vertical.jpg` (nueva versión 640×1138). `object-fit:cover` heredado del CSS global; `object-position:center 30%` inline para centrar el encuadre en la zona relevante (rostro + inyección). La card mantiene la misma altura que las demás.

### 2026-06-17 (sesión 5)
**Actividades:**
- Card de Botox (Home): ajuste localizado de encuadre con `object-fit:contain` + `background:var(--bone-100)` inline. La imagen se muestra completa dentro del contenedor `1/1` sin zoom excesivo. La card mantiene la misma altura que las demás.

### 2026-06-17 (sesión 4)
**Actividades:**
- Card de Botox (Home): reemplazada imagen `inyeccion-facial-desde-arriba-vertical.jpg` por `preparando-rostro-para-inyeccion-horizontal.jpg`. Eliminado el `aspect-ratio:3/4` inline que quedó de la sesión anterior. La card recupera uniformidad visual con las demás.

### 2026-06-17 (sesión 3)
**Actividades:**
- Ajuste localizado en la card de Botox (Home): añadido `aspect-ratio:3/4` inline en el `<img>`. Sobrescribe el `1/1` global solo para esta imagen, reduciendo el zoom sin afectar las demás cards.

### 2026-06-17 (sesión 2)
**Actividades:**
- Ajuste de encuadre en cards de "Tratamientos destacados" (Home): cambio de `aspect-ratio:4/3` a `1/1` en `.svc-card img`. Corrige el zoom excesivo de imágenes verticales (Botox, PDRN & Exosomas). Solo afecta las 4 cards del Home.

### 2026-06-17
**Actividades:**
- Reemplazo de imágenes en `mockup.html` — solo las indicadas, sin modificar estructura, copys ni estilos
- Home: hero → `imagen-para-hero-home-horizontal.png` (object-position: right center); card Botox → `inyeccion-facial-desde-arriba-vertical.jpg`; card PDRN & Exosomas → `rostro-microneedling-frente-vertical.jpg`
- Servicios: Botox → `aplicando-tratamiento-senora-vertical.jpg`; Fillers → `preparacion-rostro-linea-vertical.jpg`; Hydrafacial → `aplicacion-crema-rostro-vertical.jpg`; PDRN & Exosomas → `tratamiento-facial-persona-recostada-vertical.jpg`
- Ajustes de `object-position` por imagen para optimizar el encuadre sin deformar

### 2026-06-16
**Actividades:**
- Modificación de `mockup.html` — únicamente secciones Hero (Home) y Botox (Servicios)
- Hero H1: reemplazado "Cuidarte también es una forma de amor propio." por "Cuidarte no es vanidad, es bienestar."
- Hero subtítulo: reemplazado "Un espacio cálido y moderno para hombres y mujeres que buscan tratamientos personalizados, tecnología actual y resultados naturales." por "Nos especializamos en medicina estética, regenerativa y bienestar integral para rostro y cuerpo."
- Botox (Servicios): eliminado el bloque "Marcas disponibles / Linurase · Otesaly · Dysport"; se conserva "Requiere valoración médica previa."
- No se modificaron: `wireframes.html`, `design-preview.html`, imágenes, estilos, estructura general

### 2026-06-12 (sesión 2)
**Actividades:**
- Modificación de `mockup.html` — únicamente la página Home (`#pg-home`)
- Nueva sección Testimonios: carrusel visual de alta fidelidad insertado entre TRATAMIENTOS y QUOTE DARK. 5 cards demo con quote, ★★★★★, nombre/apellido y tratamiento. Cards con bg bone-100, border-left taupe-500, Cormorant Garamond italic. Desktop: 3 cards visibles; mobile: 1 card. Dots + flechas prev/next. Autoscroll 4s, pausa en hover e interacción, respeta prefers-reduced-motion.
- Sección final CTA + mapa: reemplaza CLINIC STRIP simple + INFO STRIP por composición de dos columnas sobre la misma imagen de fondo (URL sin cambios). Izquierda: título "Tu piel también cuenta tu historia." + botón CTA. Derecha: card glassmorphism (backdrop-filter blur) con eyebrow "Cabo San Lucas, BCS", placeholder de mapa (📍 Google Maps · Plaza Patio), horario. Colapsa a 1 columna en mobile.
- CSS nuevo: `.tc-card`, `.tc-stars`, `.tc-quote`, `.tc-author`, `.tc-treat`, `.tco-*` (carousel), `.cs-inner`, `.cs-map-card`, `.cs-map-ph` + media queries adicionales.
- No se modificaron: `wireframes.html`, `design-preview.html`, imagen hero, imagen clinic strip, página Servicios, nav, footer, estilos globales.

### 2026-06-12 (sesión 1)
**Actividades:**
- Modificación de `wireframes.html` — únicamente la página Home (`#page-home`)
- Hero: cambio del placeholder "Foto hero — interior clínica" por "Imagen aspiracional · bienestar · confianza · amor propio" (ícono ✦ en lugar de 🌿)
- Nueva sección de testimonios: carrusel con 5 cards demo entre TRATAMIENTOS y CITA OSCURA. Autoscroll 4s, pausa en hover e interacción manual, indicadores de posición, respeta `prefers-reduced-motion`. Desktop: 3 cards visibles; mobile: 1 card. Sin librerías externas.
- Sección final CTA+Mapa: reemplaza el Info Strip por layout de dos columnas (desktop). Izquierda: título "Tu piel también cuenta tu historia." + botones CTA. Derecha: eyebrow "Cabo San Lucas, BCS" + placeholder de mapa (Google Maps · Plaza Patio) + horario. Colapsa a 1 columna en mobile con `g-half`.
- CSS mínimo agregado: estilos de carrusel, `.tcard-stars`, override mobile `.crs-slide{width:100%}`
- JS del carrusel: función `window.crsGoTo` expuesta para reset al cambiar viewport desktop↔mobile
- No se modificaron: `mockup.html`, `design-preview.html`, páginas Nosotros/Servicios/Testimonios/Contacto, navegación, footer, tokens de diseño

### 2026-06-04
**Actividades:**
- Lectura completa de los documentos de contenido y requerimientos
- Creación de `wireframes.html` — las 5 páginas interactivas con switch desktop/mobile (Home, Nosotros, Servicios, Testimonios, Contacto+FAQ)
- Creación del sistema de diseño completo:
  - `design-tokens.json` — fuente de verdad de colores, tipografía, espaciado, sombras, radios y transiciones
  - `DESIGN.md` — razonamiento de cada decisión de diseño (paleta, tipografía, componentes, accesibilidad)
  - `design-preview.html` — preview interactivo con sidebar, 14 secciones y todos los componentes reales del sitio
- Creación de `mockup.html` — mockup de alta fidelidad con imágenes reales de Unsplash, páginas Home y Servicios, diseño responsive con hamburger mobile

### 2026-06-02
**Actividades:**
- Inicialización del repositorio en GitHub (`argihm-jpg/DALMA_WEB`)
- Subida de archivos iniciales: logos (SVG, PDF, WebP, PNG, ICO), documentos Word de contenido y requerimientos
- Renombre de la carpeta de logos: `D'ALMA LOGOS ` → `D'ALMA_LOGOS` (sin espacios)
- Creación de `.gitignore` para excluir `.DS_Store`
- Creación de `CLAUDE.md` con contexto completo del proyecto extraído de los documentos
