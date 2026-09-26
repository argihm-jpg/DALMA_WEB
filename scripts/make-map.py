"""Genera imagenes-candidatas/mapa-plaza-patio.webp (1200x600) a partir de una exportacion ESTATICA de OpenStreetMap
guardada en local. Herramienta 100% local: NO hace ninguna peticion HTTP.

Source asset: map-sources/osm-export-plaza-patio.png  (openstreetmap.org > Compartir > Imagen, una sola exportacion manual,
capa Estandar, escala 1:2100). Carpeta map-sources/ NO la despliega build-site.py.
Datos (c) OpenStreetMap contributors, ODbL. La atribucion visible va superpuesta en HTML (.map-attr).

Uso: python scripts/make-map.py   (requiere Pillow solo para este paso)"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "map-sources", "osm-export-plaza-patio.png")
OUT = os.path.join(ROOT, "imagenes-candidatas", "mapa-plaza-patio.webp")
# BBox exacta de la exportacion (datos del formulario de Compartir > Imagen) y punto de Plaza Patio
MINLON, MAXLON = -109.94009971618654, -109.92668867111207
MINLAT, MAXLAT = 22.9008458668988, 22.908208640271777
LAT, LON = 22.9045296, -109.9333945
CROP_LON_SPAN = 0.0129            # grados de longitud que abarca el recorte final (contexto ~1.3 km)
OUT_W, OUT_H = 1200, 600

if not os.path.isfile(SRC):
    sys.exit(f"ERROR: falta el source asset local: {SRC}\n"
             "Exportalo en openstreetmap.org > Compartir > Imagen (PNG) y guardalo con ese nombre.")

def merc(lat): return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))

src = Image.open(SRC).convert("RGB")
W, H = src.size
px = lambda lon: (lon - MINLON) / (MAXLON - MINLON) * W
py = lambda lat: (merc(MAXLAT) - merc(lat)) / (merc(MAXLAT) - merc(MINLAT)) * H
cx, cy = px(LON), py(LAT)
cw = CROP_LON_SPAN / (MAXLON - MINLON) * W
ch = cw / 2
box = (round(cx - cw / 2), round(cy - ch / 2), round(cx + cw / 2), round(cy + ch / 2))
if box[0] < 0 or box[1] < 0 or box[2] > W or box[3] > H:
    sys.exit(f"ERROR: el recorte {box} excede la exportacion {W}x{H}")
img = src.crop(box).resize((OUT_W, OUT_H), Image.LANCZOS)
mx, my = (cx - box[0]) / cw * OUT_W, (cy - box[1]) / ch * OUT_H

S = 3  # supersampling para bordes suaves
lay = Image.new("RGBA", (OUT_W * S, OUT_H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
r = 17 * S; X, Y = mx * S, (my - 34) * S  # cabeza del pin; punta en (mx, my)
d.polygon([(X - r * .82, Y + r * .58), (X + r * .82, Y + r * .58), (mx * S, my * S)], fill="#5F5651")
d.ellipse([X - r, Y - r, X + r, Y + r], fill="#5F5651", outline="#FAF9F7", width=3 * S)
d.ellipse([X - r * .38, Y - r * .38, X + r * .38, Y + r * .38], fill="#FAF9F7")
lay = lay.resize((OUT_W, OUT_H), Image.LANCZOS)
img = Image.alpha_composite(img.convert("RGBA"), lay)
try: font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
except Exception: font = ImageFont.load_default()
d = ImageDraw.Draw(img); t = "Plaza Patio"
tw = d.textlength(t, font=font); bx, by = mx + 28, my - 34 - 17
d.rounded_rectangle([bx, by - 4, bx + tw + 24, by + 34], 8, fill="#FAF9F7", outline="#5F5651", width=2)
d.text((bx + 12, by), t, font=font, fill="#4A4340")
img.convert("RGB").save(OUT, "WEBP", quality=82, method=6)
print(OUT, os.path.getsize(OUT), "bytes", img.size, "pin px", round(mx), round(my))
