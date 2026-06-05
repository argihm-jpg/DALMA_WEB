# DALMA_WEB — Contexto del Proyecto

## Descripción
Sitio web para **D'ALMA CLINIC**, clínica estética ubicada en Cabo San Lucas, BCS.
El proyecto lo elabora **Bruno Sandoval**. La directora del negocio es **Ana María**.

## Datos del Negocio
- **Nombre comercial:** D'ALMA CLINIC
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
1. **Home** — Hero, tratamientos destacados, botones CTA
2. **Nosotros** — Historia de Ana María, equipo
3. **Servicios** — Acordeones o tarjetas por categoría
4. **Testimonios** — Pacientes reales, fotos naturales, before/after con autorización
5. **Contacto + FAQ** — WhatsApp, Instagram, mapa, horario, preguntas frecuentes

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

---

## Historial de Sesiones

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
