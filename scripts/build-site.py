# -*- coding: utf-8 -*-
"""
Generador estatico bilingue (ES/EN) de D'ALMA CLINIC.

Fuente unica editable: mockup.html
Salida: DALMA_BUILD/ (no se commitea)

Lee ENABLE_TESTIMONIALS y PUBLIC_LAUNCH directamente del texto de mockup.html
(no se duplican como configuracion aparte, para evitar estados contradictorios).

Las traducciones EN se toman siempre del diccionario I18N y de PAGE_META ya
existentes en mockup.html (fuente de verdad unica). Si falta una clave EN
necesaria para generar una pagina, el build se detiene con un error claro en
vez de inventar contenido.

Uso:
    python scripts/build-site.py
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "mockup.html")
OUT_DIR = os.path.join(ROOT, "DALMA_BUILD")
DOMAIN = "https://dalmaclinic.com.mx"

PAGE_ORDER = ["home", "nosotros", "servicios", "testimonios", "contacto", "privacidad"]

# Rutas por idioma. "privacidad" solo existe en ES (no hay traduccion legal
# real todavia); se mantiene tambien en el dict "en" para que cualquier link
# cross-page hacia privacidad desde una pagina EN resuelva al mismo documento
# espanol, en vez de fallar.
ROUTES = {
    "es": {
        "home": "/",
        "nosotros": "/nosotros/",
        "servicios": "/servicios/",
        "contacto": "/contacto/",
        "privacidad": "/aviso-de-privacidad/",
        "testimonios": "/testimonios/",
    },
    "en": {
        "home": "/en/",
        "nosotros": "/en/about/",
        "servicios": "/en/services/",
        "contacto": "/en/contact/",
        "privacidad": "/aviso-de-privacidad/",
        "testimonios": "/en/testimonials/",
    },
}

OUT_PATH = {
    "es": {
        "home": "index.html",
        "nosotros": "nosotros/index.html",
        "servicios": "servicios/index.html",
        "contacto": "contacto/index.html",
        "privacidad": "aviso-de-privacidad/index.html",
        "testimonios": "testimonios/index.html",
    },
    "en": {
        "home": "en/index.html",
        "nosotros": "en/about/index.html",
        "servicios": "en/services/index.html",
        "contacto": "en/contact/index.html",
        "testimonios": "en/testimonials/index.html",
        # privacidad: sin archivo EN, no se genera.
    },
}

# Paginas que SI tienen (o tendran) version EN real. privacidad queda fuera:
# el aviso legal completo solo existe en espanol.
PAGES_WITH_EN = ["home", "nosotros", "servicios", "contacto", "testimonios"]

HTML_LANG_ATTR = {"es": "es", "en": "en"}

COMMENT_LABEL = {
    "home": "home",
    "nosotros": "nosotros",
    "servicios": "servicios",
    "testimonios": "testimonios",
    "contacto": "contacto",
    "privacidad": "privacidad",
}

# Solo para /servicios/ y /en/services/: si se llega con un hash real (p.ej.
# /servicios/#svc-botox desde el link de otra pagina), algunos navegadores/
# entornos no saltan de forma fiable al fragmento en la navegacion inicial,
# asi que se fuerza el scroll aqui. Es identico en ambos idiomas.
SERVICIOS_HASH_SCROLL_JS = """
(function(){
  if (!location.hash) return;
  var el = document.getElementById(location.hash.slice(1));
  if (!el) return;
  setTimeout(function(){ el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 80);
})();
"""


def fail(msg):
    print("ERROR:", msg, file=sys.stderr)
    sys.exit(1)


def langs_for_page(name, enable_testimonials):
    if name == "privacidad":
        return ["es"]
    if name == "testimonios":
        return ["es", "en"] if enable_testimonials else []
    return ["es", "en"]


def read_source():
    with open(SOURCE, encoding="utf-8") as f:
        return f.read()


def get_flag(src, name):
    m = re.search(r"const\s+" + name + r"\s*=\s*(true|false)\s*;", src)
    if not m:
        fail("No se encontro la constante %s en mockup.html" % name)
    return m.group(1) == "true"


def extract(src, start_marker, end_marker, label):
    i = src.find(start_marker)
    if i == -1:
        fail("No se encontro el marcador de inicio: %s" % label)
    j = src.find(end_marker, i)
    if j == -1:
        fail("No se encontro el marcador de fin: %s" % label)
    j += len(end_marker)
    return src[i:j], i, j


def extract_page_fragment(src, name, comment_label):
    """Extrae el contenido INTERNO del <div class="pg ..." id="pg-NAME">...</div><!-- /NAME --> """
    open_re = re.compile(r'<div class="pg[^"]*" id="pg-' + name + r'">')
    m = open_re.search(src)
    if not m:
        fail("No se encontro la apertura de la pagina: %s" % name)
    inner_start = m.end()
    close_marker = "</div><!-- /%s -->" % comment_label
    close_idx = src.find(close_marker, inner_start)
    if close_idx == -1:
        fail("No se encontro el cierre de la pagina: %s" % name)
    return src[inner_start:close_idx]


def extract_page_meta(src):
    """Parsea PAGE_META (bloque es/en) directamente del script fuente."""
    block, _, _ = extract(src, "const PAGE_META = {", "\n};", "PAGE_META")
    meta = {"es": {}, "en": {}}
    for lang in ("es", "en"):
        lang_m = re.search(r"\n  " + lang + r": \{(.*?)\n  \},?\n", block, re.S)
        if not lang_m:
            fail("No se pudo aislar el bloque %s de PAGE_META" % lang)
        body = lang_m.group(1)
        for pm in re.finditer(
            r'(\w+): \{ title: "((?:[^"\\]|\\.)*)", desc: "((?:[^"\\]|\\.)*)" \}',
            body,
        ):
            meta[lang][pm.group(1)] = {"title": pm.group(2), "desc": pm.group(3)}
    for lang in ("es", "en"):
        for name in ROUTES["es"]:
            if name not in meta[lang]:
                fail("Falta PAGE_META[%s][%s]" % (lang, name))
    return meta


def unescape_js_string(value):
    """Convierte escapes de string JS ( \\" -> " , \\\\ -> \\ , etc.) a texto literal."""
    return re.sub(r"\\(.)", r"\1", value)


def extract_i18n(src):
    """Parsea el diccionario I18N (bloques es/en) a un dict Python {lang: {key: value}}."""
    block, _, _ = extract(src, "const I18N = {", "\n};", "I18N")
    i18n = {"es": {}, "en": {}}
    for lang in ("es", "en"):
        lang_m = re.search(r'\n  "' + lang + r'": \{(.*?)\n  \}', block, re.S)
        if not lang_m:
            fail("No se pudo aislar el bloque I18N['%s']" % lang)
        body = lang_m.group(1)
        for entry in re.finditer(r'"([\w.]+)":\s*"((?:[^"\\]|\\.)*)"', body):
            i18n[lang][entry.group(1)] = unescape_js_string(entry.group(2))
    return i18n


# ---------------------------------------------------------------------------
# Traduccion estatica (ES ya viene correcto en el HTML fuente; para EN se
# reemplaza el contenido de cada elemento data-i18n* con el valor real de
# I18N['en'] en tiempo de build, para que el HTML servido ya venga en ingles
# desde el primer byte, sin depender de JS).
# ---------------------------------------------------------------------------

DATA_I18N_HTML_RE = re.compile(
    r'<(\w+)([^>]*?)data-i18n-html="([\w.]+)"([^>]*?)>(.*?)</\1>', re.S
)
DATA_I18N_TEXT_RE = re.compile(
    r'<(\w+)([^>]*?)data-i18n="([\w.]+)"([^>]*?)>(.*?)</\1>', re.S
)
DATA_I18N_ATTR_RE = re.compile(
    r'<(\w+)([^>]*?)data-i18n-(ph|alt|aria)="([\w.]+)"([^>]*?)>'
)
ATTR_NAME_FOR_KIND = {"ph": "placeholder", "alt": "alt", "aria": "aria-label"}


def apply_i18n_static(html, lang, i18n):
    dict_ = i18n.get(lang, {})

    def text_sub(m, attr_name):
        tag, before, key, after = m.group(1), m.group(2), m.group(3), m.group(4)
        if key not in dict_:
            fail(
                "Falta traduccion I18N['%s']['%s'] (usada con %s) - no se genera "
                "contenido inventado. Agrega la clave en mockup.html antes de "
                "generar la version %s." % (lang, key, attr_name, lang)
            )
        return '<%s%s%s="%s"%s>%s</%s>' % (
            tag, before, attr_name, key, after, dict_[key], tag,
        )

    html = DATA_I18N_HTML_RE.sub(lambda m: text_sub(m, "data-i18n-html"), html)
    html = DATA_I18N_TEXT_RE.sub(lambda m: text_sub(m, "data-i18n"), html)

    def attr_sub(m):
        tag, before, kind, key, after = m.groups()
        if key not in dict_:
            fail(
                "Falta traduccion I18N['%s']['%s'] (usada con data-i18n-%s) - no "
                "se genera contenido inventado." % (lang, key, kind)
            )
        attr_name = ATTR_NAME_FOR_KIND[kind]
        whole = '<%s%sdata-i18n-%s="%s"%s>' % (tag, before, kind, key, after)
        new_whole, n = re.subn(
            attr_name + r'="[^"]*"', '%s="%s"' % (attr_name, dict_[key]), whole, count=1
        )
        if n == 0:
            fail(
                "No se encontro el atributo %s a reemplazar para data-i18n-%s=\"%s\""
                % (attr_name, kind, key)
            )
        return new_whole

    html = DATA_I18N_ATTR_RE.sub(attr_sub, html)
    return html


# ---------------------------------------------------------------------------
# Reescritura de navegacion cross-page (consciente del idioma)
# ---------------------------------------------------------------------------

SHOWPG_A_RE = re.compile(
    r'<a\s+([^>]*?)onclick="(?:closeMenu\([^"]*\);)?showPg\(\'(\w+)\'\)(?:;return false;?)?"([^>]*?)>'
)

SHOWPG_BUTTON_RE = re.compile(
    r'<button\s+([^>]*?)onclick="(?:closeMenu\([^"]*\);)?showPg\(\'(\w+)\'\)"([^>]*?)>(.*?)</button>',
    re.S,
)

PRIVACIDAD_FOOTER_RE = re.compile(
    r'<a href="#aviso-de-privacidad" onclick="showPg\(\'privacidad\'\);history\.replaceState\([^"]*\);return false;"([^>]*)>'
)

GOTOSERVICE_RE = re.compile(
    r'<a\s+([^>]*?)onclick="goToService\(\'([\w-]+)\'\);return false;"([^>]*?)>'
)


def route_for(name, lang, enable_testimonials):
    if name == "testimonios" and not enable_testimonials:
        fail("Se intento generar un link a testimonios estando ENABLE_TESTIMONIALS=false")
    if name not in ROUTES[lang]:
        fail("No existe ruta para '%s' en idioma '%s'" % (name, lang))
    return ROUTES[lang][name]


def rewrite_links(html, is_servicios_page, enable_testimonials, lang):
    # 1) Caso especial: footer "Aviso de privacidad" (usaba history.replaceState + hash).
    #    Siempre apunta al documento espanol, sin importar el idioma de la pagina actual.
    def priv_sub(m):
        rest = m.group(1)
        return '<a href="%s"%s>' % (ROUTES["es"]["privacidad"], rest)

    html = PRIVACIDAD_FOOTER_RE.sub(priv_sub, html)

    # 2) goToService(...) — contextual segun la pagina/idioma que se esta generando
    def goto_sub(m):
        before, svc_id, after = m.group(1), m.group(2), m.group(3)
        attrs = (before + after)
        attrs = re.sub(r'href="#"\s*', "", attrs)
        if is_servicios_page:
            return '<a href="#%s" onclick="goToService(\'%s\');return false;" %s>' % (
                svc_id,
                svc_id,
                attrs.strip(),
            )
        else:
            return '<a href="%s#%s" %s>' % (ROUTES[lang]["servicios"], svc_id, attrs.strip())

    html = GOTOSERVICE_RE.sub(goto_sub, html)

    # 3) <a href="#" onclick="showPg('x')...">  (nav, mobile menu, footer, CTAs de contenido)
    def a_sub(m):
        before, name, after = m.group(1), m.group(2), m.group(3)
        route = route_for(name, lang, enable_testimonials)
        attrs = before + after
        attrs = re.sub(r'href="#"\s*', "", attrs)
        return '<a href="%s" %s>' % (route, attrs.strip())

    html = SHOWPG_A_RE.sub(a_sub, html)

    # 4) <button onclick="showPg('x')">Texto</button>  -> <a href="ruta">Texto</a>
    def btn_sub(m):
        before, name, after, text = m.group(1), m.group(2), m.group(3), m.group(4)
        route = route_for(name, lang, enable_testimonials)
        attrs = (before + after).strip()
        return '<a href="%s" %s>%s</a>' % (route, attrs, text)

    html = SHOWPG_BUTTON_RE.sub(btn_sub, html)

    return html


def strip_testimonials_markup(html):
    """Quita por completo (no oculta) los links/bloques de Testimonios cuando el flag esta en false."""
    html = re.sub(r"<li>\s*<a[^>]*data-testimonials-link[^>]*>.*?</a>\s*</li>", "", html, flags=re.S)
    html = re.sub(r"<a[^>]*data-testimonials-link[^>]*>.*?</a>", "", html, flags=re.S)
    html = re.sub(
        r'<section class="sec sec-alt" data-testimonials-section>.*?</section>',
        "",
        html,
        flags=re.S,
    )
    return html


TESTIMONIALS_I18N_RE = re.compile(
    r'^\s*"(?:test\.[\w.]+|home\.testi\.[\w.]+)":\s*".*?",?\n', re.M
)


def strip_testimonials_i18n(script_text):
    """Quita del diccionario I18N las claves exclusivas de Testimonios (incluye textos
    sensibles como 'autorizacion firmada' / 'resultados reales') para que ningun HTML
    publico, ni siquiera en el <script>, contenga ese contenido demo mientras el flag
    siga en false."""
    return TESTIMONIALS_I18N_RE.sub("", script_text)


def absolutize_images(html):
    html, n = re.subn(r'src="imagenes-candidatas/', 'src="/imagenes-candidatas/', html)
    return html, n


# ---------------------------------------------------------------------------
# Selector de idioma: navega a la ruta equivalente real, no traduce en sitio.
# ---------------------------------------------------------------------------

LANG_SWITCH_RE = re.compile(
    r'<button class="lang-btn" data-lang="es" onclick="setLang\((?:\'es\'|&#39;es&#39;)\)">([^<]*)</button>'
    r'<span class="lang-sep">&middot;</span>'
    r'<button class="lang-btn" data-lang="en" onclick="setLang\((?:\'en\'|&#39;en&#39;)\)">([^<]*)</button>'
)


def rewrite_lang_switch(html, name, cur_lang):
    has_en = name in PAGES_WITH_EN

    def sub(m):
        label_es, label_en = m.group(1), m.group(2)
        # Lado ES
        if cur_lang == "es":
            es_html = '<span class="lang-btn on" aria-current="true">%s</span>' % label_es
        else:
            es_route = ROUTES["es"][name]
            es_html = (
                '<a class="lang-btn" href="%s" '
                'onclick="location.href=this.getAttribute(\'href\')+location.hash;return false;">%s</a>'
                % (es_route, label_es)
            )
        # Lado EN
        if cur_lang == "en":
            en_html = '<span class="lang-btn on" aria-current="true">%s</span>' % label_en
        elif has_en:
            en_route = ROUTES["en"][name]
            en_html = (
                '<a class="lang-btn" href="%s" '
                'onclick="location.href=this.getAttribute(\'href\')+location.hash;return false;">%s</a>'
                % (en_route, label_en)
            )
        else:
            en_html = '<span class="lang-btn" aria-disabled="true">%s</span>' % label_en
        return es_html + '<span class="lang-sep">&middot;</span>' + en_html

    return LANG_SWITCH_RE.sub(sub, html)


# ---------------------------------------------------------------------------
# Ensamblado de documento
# ---------------------------------------------------------------------------

def build_hreflang_block(name):
    if name not in PAGES_WITH_EN:
        return ""
    es_url = DOMAIN + ROUTES["es"][name]
    en_url = DOMAIN + ROUTES["en"][name]
    return (
        '  <link rel="alternate" hreflang="es-MX" href="%s">\n'
        '  <link rel="alternate" hreflang="en" href="%s">\n'
        '  <link rel="alternate" hreflang="x-default" href="%s">\n'
    ) % (es_url, en_url, es_url)


def build_head(style_block, fonts_block, meta, name, lang, public_launch, canonical):
    title = meta[lang][name]["title"]
    desc = meta[lang][name]["desc"]
    robots = "index, follow" if public_launch else "noindex, nofollow"
    hreflang_block = build_hreflang_block(name)
    return """<!DOCTYPE html>
<html lang="%s">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%s</title>
  <meta name="description" content="%s">
  <meta name="robots" content="%s">
  <link rel="canonical" href="%s">
%s%s
  <style>
%s
  </style>
</head>
""" % (
        HTML_LANG_ATTR[lang],
        title,
        desc,
        robots,
        canonical,
        hreflang_block,
        fonts_block,
        style_block,
    )


def main():
    src = read_source()

    enable_testimonials = get_flag(src, "ENABLE_TESTIMONIALS")
    public_launch = get_flag(src, "PUBLIC_LAUNCH")

    print("ENABLE_TESTIMONIALS =", enable_testimonials)
    print("PUBLIC_LAUNCH =", public_launch)

    # ---- piezas compartidas -------------------------------------------------
    style_full, _, _ = extract(src, "  <style>", "\n  </style>", "style block")
    style_full = style_full[len("  <style>"):-len("\n  </style>")]

    overlay_css, _, _ = extract(
        src,
        "    /* PRELAUNCH OVERLAY:",
        "/* /PRELAUNCH OVERLAY */",
        "overlay css",
    )
    pg_css = ".pg{display:none;}.pg.on{display:block;}"
    if pg_css not in style_full:
        fail("No se encontro la regla .pg/.on esperada en el CSS")
    style_full = style_full.replace(pg_css, "")

    if not public_launch:
        style_block = style_full
    else:
        style_block = style_full.replace(overlay_css, "")

    fonts_block = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">"""

    overlay_html, _, _ = extract(
        src,
        "<!-- PRELAUNCH OVERLAY: remove this whole block",
        "<!-- /PRELAUNCH OVERLAY -->",
        "overlay html+script",
    )

    svg_symbol, _, _ = extract(
        src, '<svg style="display:none">', "</svg>", "svg symbol block"
    )

    wafloat_raw, _, _ = extract(
        src, '<a class="wafloat"', "</a>", "wafloat block"
    )
    wafloat_by_lang = {
        lang: rewrite_links(wafloat_raw, is_servicios_page=False, enable_testimonials=enable_testimonials, lang=lang)
        for lang in ("es", "en")
    }

    script_full, _, _ = extract(src, "<script>\n// FEATURE FLAG", "</script>\n</body>", "shared trailing script")
    script_full = script_full[len("<script>\n"):-len("</script>\n</body>")]

    # --- El idioma y la pagina ya quedan fijos en el HTML estatico; el motor
    #     de traduccion en vivo (applyI18n/setLang/updatePageMeta/PAGE_META) y
    #     el selector de "recordar idioma en localStorage" dejan de hacer
    #     falta en produccion y se retiran del bundle generado. mockup.html
    #     (fuente de edicion, un solo archivo) conserva todo esto intacto.
    page_meta_block, _, _ = extract(script_full, "const PAGE_META = {", "\n};", "PAGE_META (script)")
    script_full = script_full.replace(page_meta_block, "")

    old_update_meta = """function updatePageMeta(name, lang) {
  var meta = PAGE_META[lang] && PAGE_META[lang][name];
  if (!meta) return;
  document.title = meta.title;
  var descEl = document.querySelector('meta[name="description"]');
  if (descEl) descEl.setAttribute('content', meta.desc);
}

"""
    if old_update_meta not in script_full:
        fail("No se encontro la funcion updatePageMeta() a eliminar")
    script_full = script_full.replace(old_update_meta, "")

    old_setlang = """function setLang(lang) {
  if (!I18N[lang]) return;
  applyI18n(lang);
  document.documentElement.lang = lang;
  try { localStorage.setItem('dalma-lang', lang); } catch (e) {}
  document.querySelectorAll('.lang-btn').forEach(function(b) {
    b.classList.toggle('on', b.dataset.lang === lang);
  });
  var currentPg = document.querySelector('.pg.on');
  if (currentPg) updatePageMeta(currentPg.id.replace('pg-', ''), lang);
}

"""
    if old_setlang not in script_full:
        fail("No se encontro la funcion setLang() a eliminar")
    script_full = script_full.replace(old_setlang, "")

    old_apply_i18n = """function applyI18n(lang) {
  var dict = I18N[lang];
  if (!dict) return;
  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.getAttribute('data-i18n');
    if (dict[key] !== undefined) el.textContent = dict[key];
  });
  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-html');
    if (dict[key] !== undefined) el.innerHTML = dict[key];
  });
  document.querySelectorAll('[data-i18n-ph]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-ph');
    if (dict[key] !== undefined) el.setAttribute('placeholder', dict[key]);
  });
  document.querySelectorAll('[data-i18n-alt]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-alt');
    if (dict[key] !== undefined) el.setAttribute('alt', dict[key]);
  });
  document.querySelectorAll('[data-i18n-aria]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-aria');
    if (dict[key] !== undefined) el.setAttribute('aria-label', dict[key]);
  });
}

"""
    if old_apply_i18n not in script_full:
        fail("No se encontro la funcion applyI18n() a eliminar")
    script_full = script_full.replace(old_apply_i18n, "")

    old_showpg = """  function showPg(name, btn) {
    if (name === 'testimonios' && !ENABLE_TESTIMONIALS) {
      name = 'home';
      btn = null;
    }
    document.querySelectorAll('.nav-mmenu').forEach(m => m.classList.remove('open'));
    document.querySelectorAll('.nav-ham').forEach(h => h.classList.remove('open'));
    document.body.style.overflow = '';
    document.querySelectorAll('.pg').forEach(p => p.classList.remove('on'));
    document.getElementById('pg-' + name).classList.add('on');
    if (btn) btn.classList.add('on');
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    updatePageMeta(name, document.documentElement.lang || 'es');
  }

"""
    if old_showpg not in script_full:
        fail("No se encontro la funcion showPg() a eliminar")
    script_full = script_full.replace(old_showpg, "")

    old_goto = """  function goToService(id) {
    showPg('servicios');
    var sel = document.getElementById('svc-filter-select');
    if (sel && sel.value !== 'todos') {
      sel.value = 'todos';
      sel.dispatchEvent(new Event('change'));
    }
    setTimeout(function() {
      var el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 80);
  }"""
    new_goto = """  function goToService(id) {
    var el = document.getElementById(id);
    if (!el) { location.href = SERVICIOS_ROUTE + '#' + id; return; }
    var sel = document.getElementById('svc-filter-select');
    if (sel && sel.value !== 'todos') {
      sel.value = 'todos';
      sel.dispatchEvent(new Event('change'));
    }
    setTimeout(function() { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 80);
  }"""
    if old_goto not in script_full:
        fail("No se encontro la funcion goToService() a adaptar")
    script_full = script_full.replace(old_goto, new_goto)

    old_lang_init = """  // LANGUAGE INIT
  (function(){
    var saved = 'es';
    try { saved = localStorage.getItem('dalma-lang') || 'es'; } catch (e) {}
    setLang(saved);
  })();"""
    if old_lang_init not in script_full:
        fail("No se encontro el IIFE de LANGUAGE INIT a eliminar")
    script_full = script_full.replace(old_lang_init, "")

    if not enable_testimonials:
        before_keys = len(re.findall(r'"\w[\w.]*":', script_full))
        script_full = strip_testimonials_i18n(script_full)
        after_keys = len(re.findall(r'"\w[\w.]*":', script_full))
        print("I18N: %d claves de Testimonios removidas del bundle compartido" % (before_keys - after_keys))

    page_meta = extract_page_meta(src)
    i18n = extract_i18n(src)

    # ---- por pagina / por idioma ---------------------------------------------
    os.makedirs(OUT_DIR, exist_ok=True)

    generated = []  # lista de (name, lang)
    img_warnings = []
    used_images = set()

    for name in PAGE_ORDER:
        for lang in langs_for_page(name, enable_testimonials):
            fragment = extract_page_fragment(src, name, COMMENT_LABEL[name])
            if not enable_testimonials:
                fragment = strip_testimonials_markup(fragment)
            if lang == "en":
                fragment = apply_i18n_static(fragment, "en", i18n)
            fragment = rewrite_links(
                fragment,
                is_servicios_page=(name == "servicios"),
                enable_testimonials=enable_testimonials,
                lang=lang,
            )
            fragment = rewrite_lang_switch(fragment, name, lang)
            fragment, n_img = absolutize_images(fragment)

            remaining_rel = re.findall(r'src="imagenes-candidatas/', fragment)
            if remaining_rel:
                img_warnings.append((name, lang, len(remaining_rel)))

            for m in re.finditer(r'/imagenes-candidatas/([^"\'\)\s]+)', fragment):
                used_images.add(m.group(1))

            canonical = DOMAIN + ROUTES[lang][name]
            head = build_head(style_block, fonts_block, page_meta, name, lang, public_launch, canonical)

            page_script = "const SERVICIOS_ROUTE = '%s';\n%s" % (ROUTES[lang]["servicios"], script_full)
            if name == "servicios":
                page_script += "\n" + SERVICIOS_HASH_SCROLL_JS

            body_parts = []
            if not public_launch:
                body_parts.append(overlay_html)
            body_parts.append("<div>\n")
            body_parts.append(fragment)
            body_parts.append("\n</div>\n")
            body_parts.append(svg_symbol + "\n")
            body_parts.append(wafloat_by_lang[lang] + "\n")
            body_parts.append("<script>\n%s\n</script>\n" % page_script)

            doc = head + "<body>\n" + "\n".join(body_parts) + "</body>\n</html>\n"

            out_path = os.path.join(OUT_DIR, OUT_PATH[lang][name])
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(doc)
            generated.append((name, lang))
            print("Generado:", OUT_PATH[lang][name])

    if img_warnings:
        for name, lang, count in img_warnings:
            print("ADVERTENCIA: %s/%s tiene %d rutas de imagen relativas sin convertir" % (name, lang, count))

    # ---- limpiar testimonios/ y en/testimonials/ huerfanos de una corrida anterior
    if not enable_testimonials:
        for stale_path in (
            os.path.join(OUT_DIR, "testimonios"),
            os.path.join(OUT_DIR, "en", "testimonials"),
        ):
            if os.path.isdir(stale_path):
                shutil.rmtree(stale_path)
                print("Limpiado %s huerfano de una corrida anterior (ENABLE_TESTIMONIALS=false)" % os.path.relpath(stale_path, OUT_DIR))

    # ---- copiar SOLO las imagenes realmente referenciadas por el build (ES+EN comparten carpeta)
    src_img_dir = os.path.join(ROOT, "imagenes-candidatas")
    dst_img_dir = os.path.join(OUT_DIR, "imagenes-candidatas")
    if os.path.isdir(dst_img_dir):
        shutil.rmtree(dst_img_dir)
    os.makedirs(dst_img_dir, exist_ok=True)

    missing_images = []
    for filename in sorted(used_images):
        src_file = os.path.join(src_img_dir, filename)
        if not os.path.isfile(src_file):
            missing_images.append(filename)
            continue
        shutil.copy2(src_file, os.path.join(dst_img_dir, filename))

    if missing_images:
        fail(
            "Estas imagenes estan referenciadas en el HTML pero no existen en %s: %s"
            % (src_img_dir, ", ".join(missing_images))
        )

    total_source = len(os.listdir(src_img_dir)) if os.path.isdir(src_img_dir) else 0
    print(
        "Copiadas %d/%d imagenes referenciadas a imagenes-candidatas/ (%d sin usar, no copiadas)"
        % (len(used_images), total_source, total_source - len(used_images))
    )

    # ---- robots.txt ------------------------------------------------------------
    robots_lines = ["User-agent: *", "Allow: /"]
    if public_launch:
        robots_lines.append("")
        robots_lines.append("Sitemap: %s/sitemap.xml" % DOMAIN)
    robots_txt = "\n".join(robots_lines) + "\n"
    with open(os.path.join(OUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print("Generado: robots.txt")

    # ---- sitemap.xml (solo si PUBLIC_LAUNCH) -----------------------------------
    if public_launch:
        urls = "\n".join(
            '  <url><loc>%s%s</loc></url>' % (DOMAIN, ROUTES[lang][name]) for name, lang in generated
        )
        sitemap = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + urls
            + "\n</urlset>\n"
        )
        with open(os.path.join(OUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sitemap)
        print("Generado: sitemap.xml (%d rutas)" % len(generated))
    else:
        sitemap_path = os.path.join(OUT_DIR, "sitemap.xml")
        if os.path.exists(sitemap_path):
            os.remove(sitemap_path)
        print("sitemap.xml NO generado (PUBLIC_LAUNCH=false)")

    print("\nBuild completo en:", OUT_DIR)
    print("Paginas generadas:", ", ".join("%s(%s)" % (n, l) for n, l in generated))
    if not enable_testimonials:
        print("testimonios/ y en/testimonials/ NO generados (ENABLE_TESTIMONIALS=false) -> ambos deben dar 404")


if __name__ == "__main__":
    main()
