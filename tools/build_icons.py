#!/usr/bin/env python3
"""Génère les icônes de l'app (bulle de BD + drapeau mexicain) dans icons/.

Usage : python3 tools/build_icons.py   (nécessite Pillow)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "icons")
S = 2048  # rendu en haute définition puis réduit (anticrénelage)


def arc(cx, cy, r, a0, a1, steps=24):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / steps)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / steps))) for i in range(steps + 1)]


def bubble_points():
    """Même tracé que le SVG du logo (viewBox 120×112)."""
    pts = []
    pts += arc(92, 28, 22, -90, 0)       # coin haut droit
    pts += arc(92, 62, 22, 0, 90)        # coin bas droit
    pts += [(54, 84), (26, 106), (32, 84)]  # queue de la bulle
    pts += arc(28, 62, 22, 90, 180)      # coin bas gauche
    pts += arc(28, 28, 22, 180, 270)     # coin haut gauche
    return pts


def draw_logo(size, scale):
    """Renvoie une image RGBA carrée de `size` avec le logo centré, occupant `scale` de la largeur."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    k = size * scale / 120
    ox = (size - 120 * k) / 2
    oy = (size - 112 * k) / 2 + 4 * k
    tf = lambda p: (ox + p[0] * k, oy + p[1] * k)
    pts = [tf(p) for p in bubble_points()]

    # Ombre portée
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).polygon([(x, y + 5 * k) for x, y in pts], fill=(0, 0, 0, 110))
    img = Image.alpha_composite(img, shadow.filter(ImageFilter.GaussianBlur(4 * k)))

    # Drapeau découpé dans la bulle
    flag = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    fd = ImageDraw.Draw(flag)
    fd.rectangle([0, 0, ox + 42 * k, size], fill="#006847")
    fd.rectangle([ox + 42 * k, 0, ox + 78 * k, size], fill="#FFFFFF")
    fd.rectangle([ox + 78 * k, 0, size, size], fill="#CE1126")
    # Emblème simplifié : aigle brun sur un nopal, entouré d'une couronne verte
    cx, cy = tf((60, 43))
    fd.ellipse([cx - 5 * k, cy - 7 * k, cx + 5 * k, cy + 7 * k], fill="#8B5A2B")
    fd.polygon([tf((56, 41)), tf((47, 33)), tf((50, 42)), tf((57, 46))], fill="#8B5A2B")
    fd.polygon([tf((64, 41)), tf((73, 33)), tf((70, 42)), tf((63, 46))], fill="#8B5A2B")
    fd.ellipse([cx - 3 * k, cy - 12 * k, cx + 3 * k, cy - 6 * k], fill="#8B5A2B")
    fd.ellipse([cx - 4 * k, cy + 6 * k, cx + 4 * k, cy + 10 * k], fill="#3E7B27")
    a, b = tf((47, 34)), tf((73, 60))
    fd.arc([a[0], a[1], b[0], b[1]], 15, 165, fill="#3E7B27", width=int(2.6 * k))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).polygon(pts, fill=255)
    img.paste(flag, (0, 0), mask)

    # Contour façon BD
    ImageDraw.Draw(img).line(pts + [pts[0]], fill="#1B1B1F", width=int(5 * k), joint="curve")
    return img


def background(size):
    """Dégradé rose mexicain → violet."""
    top, bottom = (255, 46, 147), (123, 44, 191)
    grad = Image.new("RGB", (1, size))
    for y in range(size):
        t = y / (size - 1)
        grad.putpixel((0, y), tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return grad.resize((size, size)).convert("RGBA")


def main():
    os.makedirs(OUT, exist_ok=True)
    full = Image.alpha_composite(background(S), draw_logo(S, 0.74)).convert("RGB")
    maskable = Image.alpha_composite(background(S), draw_logo(S, 0.56)).convert("RGB")
    for name, img, px in [
        ("apple-touch-icon.png", full, 180),
        ("icon-192.png", full, 192),
        ("icon-512.png", full, 512),
        ("icon-maskable-512.png", maskable, 512),
    ]:
        img.resize((px, px), Image.LANCZOS).save(os.path.join(OUT, name), optimize=True)
    # Logo seul, transparent (pour le README)
    draw_logo(S, 0.95).resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, "logo.png"), optimize=True)
    print("Icônes générées dans", OUT)


if __name__ == "__main__":
    main()
