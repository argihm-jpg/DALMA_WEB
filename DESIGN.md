# Sistema de Diseño — D'ALMA CLINIC

**Versión:** 1.0.0 · **Fecha:** 2026-06-04

---

## Principios

1. **Calidez antes que frialdad** — Cada decisión visual refuerza que D'ALMA es una clínica accesible, no intimidante.
2. **Elegancia sin ostentación** — Minimalismo con carácter. Pocas cosas, bien hechas.
3. **Mobile-first** — El 80%+ del tráfico llegará desde celular. Se diseña primero para 375px.
4. **Confianza a través de consistencia** — Un solo sistema visual en todo el sitio genera credibilidad.

---

## Paleta de Color

### Paleta base
La paleta parte de los 5 colores oficiales de la marca y se extiende con tints y shades para generar jerarquía sin introducir colores nuevos.

| Token | Hex | Uso |
|-------|-----|-----|
| `bone-100` | `#FAF9F7` | Background de página — el "aire" del diseño |
| `bone-200` | `#F5F1EC` | Cards, secciones alternadas — calidez suave |
| `bone-300` | `#EDE6DC` | Dividers internos, fills de inputs |
| `bone-400` | `#D8CBBE` | Bordes estándar, separadores |
| `bone-500` | `#C4B4A3` | Acentos sutiles |
| `taupe-400` | `#A89992` | Texto placeholder, íconos inactivos |
| `taupe-500` | `#8B817B` | Texto secundario, labels, captions |
| `taupe-600` | `#736A64` | Texto de énfasis en superficie clara |
| `taupe-700` | `#5F5651` | Texto primario, botones, links |
| `taupe-800` | `#4A4340` | Hover de botones, texto oscuro |
| `taupe-900` | `#352F2D` | Máximo contraste, active states |

**Por qué no hay color de acento brillante:**
D'ALMA no necesita un azul, verde o coral llamativo. La sofisticación de la marca viene de la coherencia en la paleta tierra. Introducir un acento vivo rompería la sensación de calma y elegancia.

### Tokens semánticos
Se usan nombres de propósito en el CSS (no colores directos), para poder cambiar la paleta sin tocar componentes:
- `--color-bg-base` → fondo de página
- `--color-bg-surface` → fondo de cards
- `--color-text-primary` → texto principal
- `--color-text-secondary` → texto de apoyo
- `--color-border` → bordes
- `--color-interactive` → botones y links

---

## Tipografía

### Decisión de fuentes
**Cormorant Garamond** (display) + **Montserrat** (body) es la combinación que mejor representa el carácter de D'ALMA:

- **Cormorant Garamond** — Serifada, con modulación de trazo, evoca lujo accesible y calidez. Ideal para headlines y frases de marca. Se usa en peso Light (300) y Regular (400) para mantener elegancia sin rigidez.
- **Montserrat** — Geométrica humanista. Legible, moderna y neutral. Perfecta para body text, labels, CTAs y navegación.

### Jerarquía tipográfica

| Rol | Familia | Tamaño | Peso | Uso |
|-----|---------|--------|------|-----|
| `hero-title` | Cormorant | 60px | Light | Frase principal del Hero |
| `section-title` | Cormorant | 36px | Light | Título de cada sección |
| `card-title` | Cormorant | 24px | Regular | Nombre de servicio, tarjeta |
| `quote` | Cormorant | 20px | Light | Citas de marca, testimonios |
| `label` | Montserrat | 12px | Semibold | Etiquetas de categoría (MAYÚSCULAS + tracking) |
| `nav` | Montserrat | 14px | Medium | Navegación principal |
| `body` | Montserrat | 16px | Regular | Texto de párrafos |
| `body-sm` | Montserrat | 14px | Regular | Texto secundario, notas |
| `cta` | Montserrat | 14px | Semibold | Botones, calls to action |
| `caption` | Montserrat | 12px | Regular | Metadata, disclaimers |

**Regla de uso de Cormorant:** Solo para contenido editorial (frases, títulos, citas). Nunca para UI funcional (labels, botones, formularios).

---

## Espaciado

Sistema basado en múltiplos de 4px. Esto garantiza alineación perfecta en cualquier pantalla.

```
4px   → micro (iconos, gaps internos)
8px   → xs (padding de badges, gaps mínimos)
12px  → sm
16px  → base (padding de inputs, gaps entre elementos)
24px  → md (padding interno de cards)
32px  → lg (gap entre cards)
48px  → xl (padding de secciones en mobile)
64px  → 2xl
80px  → 3xl (padding de secciones en desktop)
96px  → 4xl
128px → section (margen entre secciones grandes)
```

---

## Bordes y Radios

La clínica no es una app de startup. Bordes suaves pero no excesivamente redondeados.

| Token | Valor | Uso |
|-------|-------|-----|
| `none` | 0 | Líneas de separación, dividers |
| `sm` | 2px | Badges de texto |
| `md` | 4px | Inputs, selects |
| `lg` | 8px | Cards de servicio |
| `xl` | 12px | Cards de testimonios |
| `2xl` | 16px | Cards hero, modales |
| `full` | 9999px | Botones pill, tags |

**Regla:** Los botones primarios usan `full` (pill shape) para suavidad. Las cards usan `lg` o `xl` para estructura limpia.

---

## Sombras

Sombras cálidas (ligeramente tintadas de taupe, no gris frío):

| Token | Uso |
|-------|-----|
| `sm` | Input focus, elementos en hover |
| `md` | Cards en estado normal |
| `lg` | Cards en hover, dropdowns |
| `xl` | Modales, drawers |
| `inner` | Inputs activos |

---

## Componentes

### Botones

**Primario** — fondo `taupe-700`, texto blanco, forma pill
- Hover: `taupe-800`
- Active: `taupe-900`
- Uso: CTAs principales ("Agenda tu cita", "Conoce los servicios")

**Secundario** — borde `taupe-700`, texto `taupe-700`, sin fondo
- Hover: fondo `bone-200`
- Uso: CTAs secundarios, acciones alternativas

**Ghost** — solo texto `taupe-700`, sin borde ni fondo
- Hover: subrayado
- Uso: links de navegación, "Ver más"

**WhatsApp** — fondo `#25D366`, texto blanco, ícono de WhatsApp
- Siempre presente en mobile como botón fijo (floating)

### Cards

**Service Card** — fondo `bone-200`, borde `bone-400`, radio `lg`, sombra `md`
- Estructura: label de categoría → título → descripción corta → CTA
- Hover: sombra `lg`, ligero lift (translateY -2px)

**Team Card** — foto cuadrada (aspect-ratio 1:1) + nombre + rol
- Fondo `bone-100`, sin borde, sombra `sm`

**Testimonial Card** — comillas decorativas (Cormorant, grande) + texto + nombre
- Fondo `bone-200`, borde izquierdo 2px `taupe-500`

### Navegación

**Desktop:** Logo a la izquierda, links centrados, CTA botón a la derecha. Fondo transparente sobre hero, cambia a `bone-100/95%` con blur al hacer scroll.

**Mobile:** Logo centrado, hamburger a la derecha. Menú desplegable full-width con fondo `bone-100`, links en `2xl`.

### Acordeón (Servicios)

Estilo minimalista: título de servicio + icono `+` / `−`. Sin fondo en item cerrado. Al abrir: fondo `bone-200`, transición suave 300ms.

### Formulario de Contacto

- Inputs: fondo `bone-200`, borde `bone-400`, radio `md`, height 48px
- Focus: borde `taupe-600`, sombra `inner`
- Labels: Montserrat 12px, semibold, uppercase, tracking widest

---

## Accesibilidad

- Contraste WCAG AA: `taupe-700` (#5F5651) sobre `bone-100` (#FAF9F7) → ratio 7.2:1 ✓
- `taupe-500` (#8B817B) sobre `bone-100` → ratio 3.8:1 ✓ (texto grande)
- Todos los botones tienen estados `:focus-visible` con outline `taupe-700`
- Tamaño mínimo de touch target: 44×44px
- Nunca usar color como único indicador de estado

---

## Animaciones

**Principio:** Movimiento sutil que refuerza elegancia. Nada que distraiga.

| Elemento | Animación | Duración |
|----------|-----------|----------|
| Nav al scroll | opacity + blur | 250ms |
| Cards hover | translateY(-2px) + shadow | 250ms |
| Botones hover | background-color | 150ms |
| Acordeón open/close | max-height + opacity | 300ms |
| Fade in secciones | opacity + translateY(16px) | 400ms |
| Menú mobile | translateX | 300ms |

Sin parallax, sin scroll-triggered animations exageradas, sin rotaciones.

---

## Archivos del Sistema

| Archivo | Propósito |
|---------|-----------|
| `design-tokens.json` | Fuente de verdad de todos los tokens |
| `DESIGN.md` | Este documento — razonamiento y guía |
| `design-preview.html` | Vista interactiva de todos los componentes |
