# DALMA_WEB — Contexto del Proyecto

## Descripción
Sitio web para **D'ALMA CLINIC**, clínica estética ubicada en Cabo San Lucas, BCS.
El proyecto lo elabora **Bruno Sandoval**. La directora del negocio es **Ana María**.

## Datos del Negocio
- **Nombre comercial:** D'ALMA CLINIC
- **Dominio:** `dalmaclinic.com.mx`
- **Dirección:** Plaza Patio, De Las Brisas 2404, Brisas del Pacífico, Cabo San Lucas, Baja California Sur
- **Horario:** Lunes a domingo, 10:00 am – 8:00 pm
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
- Responsive (mobile-first, optimizado para celular)
- Integración futura: Meta Business, Facebook Ads, Instagram, WhatsApp Business, Google Analytics, Google Search Console

## Material Pendiente
- [ ] Fotografías profesionales del equipo
- [ ] Fotografías del local (interior y exterior; se realizarán al terminar la obra)
- [ ] Before/after de pacientes (con autorización)
- [ ] WhatsApp oficial
- [ ] Número(s) de teléfono de contacto

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
