"""Petit kit de dessin SVG pour les illustrations d'Órale.

Style : dessins à plat, contour sombre arrondi (façon BD), palette vive.
Toutes les illustrations utilisent un viewBox 100×100.
"""

INK = "#2B2140"
SW = 3.2  # épaisseur du contour

# Palette
RED = "#EE4B3E"
DRED = "#B8322A"
ORANGE = "#FF9F1C"
YELLOW = "#FFD23F"
LYELLOW = "#FFE98A"
GREEN = "#43B866"
DGREEN = "#1F7A4C"
LGREEN = "#A6E07A"
TEAL = "#2EC4B6"
BLUE = "#3A86FF"
LBLUE = "#9CCBFF"
NAVY = "#24366B"
PURPLE = "#8E5CD9"
LPURPLE = "#C9B2F2"
PINK = "#FF6FA8"
LPINK = "#FFC2D6"
BROWN = "#A0623A"
DBROWN = "#6E3F22"
TAN = "#E8B886"
CREAM = "#FFF4DE"
SKIN = "#F6C7A0"
SKIN2 = "#D9956A"
SKIN3 = "#A86B45"
WHITE = "#FFFFFF"
GREY = "#9AA3B5"
LGREY = "#E1E6EE"
DGREY = "#5D6478"
BLACK = "#2B2140"
GOLD = "#F7C531"
CHEEK = "#FF9AA8"


def _attrs(fill=None, stroke=True, sw=None, extra=""):
    s = f' fill="{fill}"' if fill is not None else ' fill="none"'
    if stroke is False:
        s += ' stroke="none"'
    elif isinstance(stroke, str):
        s += f' stroke="{stroke}"'
    if sw is not None:
        s += f' stroke-width="{sw}"'
    if extra:
        s += " " + extra
    return s


def circle(cx, cy, r, fill=WHITE, **kw):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"{_attrs(fill, **kw)}/>'


def ellipse(cx, cy, rx, ry, fill=WHITE, rot=0, **kw):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"{_attrs(fill, **kw)}{t}/>'


def rect(x, y, w, h, fill=WHITE, rx=0, rot=0, **kw):
    t = f' transform="rotate({rot} {x + w / 2} {y + h / 2})"' if rot else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"{_attrs(fill, **kw)}{t}/>'


def path(d, fill=None, **kw):
    return f'<path d="{d}"{_attrs(fill, **kw)}/>'


def poly(points, fill=WHITE, **kw):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return f'<polygon points="{pts}"{_attrs(fill, **kw)}/>'


def line(x1, y1, x2, y2, sw=None, color=None):
    s = f' stroke="{color}"' if color else ""
    w = f' stroke-width="{sw}"' if sw else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"{s}{w}/>'


def text(x, y, s, size=30, fill=INK, weight=900, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" stroke="none" '
            f'text-anchor="{anchor}" font-family="ui-rounded, \'SF Pro Rounded\', system-ui, sans-serif">{s}</text>')


def group(transform, *els):
    return f'<g transform="{transform}">{"".join(els)}</g>'


def dot(cx, cy, r=2.2, fill=INK):
    return circle(cx, cy, r, fill, stroke=False)


def svg(*els):
    body = "".join(els)
    return (f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
            f'<g stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>')


# ───────── Visages et personnages ─────────

def face(cx=50, cy=50, r=30, skin=SKIN, mood="happy", cheeks=True):
    """Visage rond. mood : happy, sad, angry, tired, nervous, surprised, bored, proud, cool, starry, love, wink, sleep."""
    k = r / 30
    ex, ey, er = 10 * k, -3 * k, 3 * k
    els = [circle(cx, cy, r, skin)]
    if cheeks and mood not in ("angry",):
        els += [circle(cx - 17 * k, cy + 8 * k, 4.5 * k, CHEEK, stroke=False, extra='opacity="0.7"'),
                circle(cx + 17 * k, cy + 8 * k, 4.5 * k, CHEEK, stroke=False, extra='opacity="0.7"')]
    L, R = (cx - ex, cy + ey), (cx + ex, cy + ey)
    if mood in ("happy", "love", "wink"):
        if mood == "love":
            els += [heart(L[0], L[1], 5 * k, RED), heart(R[0], R[1], 5 * k, RED)]
        elif mood == "wink":
            els += [dot(*L, er), path(f"M{R[0] - 4 * k} {R[1]} q{4 * k} {-4 * k} {8 * k} 0", sw=2.6)]
        else:
            els += [dot(*L, er), dot(*R, er)]
        els.append(path(f"M{cx - 11 * k} {cy + 9 * k} Q{cx} {cy + 20 * k} {cx + 11 * k} {cy + 9 * k}", sw=2.8))
    elif mood == "sad":
        els += [dot(*L, er), dot(*R, er),
                path(f"M{cx - 9 * k} {cy + 16 * k} Q{cx} {cy + 8 * k} {cx + 9 * k} {cy + 16 * k}", sw=2.8),
                path(f"M{L[0] - 1} {L[1] + 5 * k} q-3 {6 * k} 0 {9 * k} q3 {-3 * k} 0 {-9 * k}z", LBLUE, sw=2)]
    elif mood == "angry":
        els[0] = circle(cx, cy, r, "#FF8A6B")
        els += [dot(L[0], L[1] + 2 * k, er), dot(R[0], R[1] + 2 * k, er),
                line(L[0] - 6 * k, L[1] - 7 * k, L[0] + 5 * k, L[1] - 2 * k, sw=3.4),
                line(R[0] + 6 * k, R[1] - 7 * k, R[0] - 5 * k, R[1] - 2 * k, sw=3.4),
                path(f"M{cx - 9 * k} {cy + 15 * k} Q{cx} {cy + 9 * k} {cx + 9 * k} {cy + 15 * k}", sw=2.8)]
    elif mood == "tired":
        els += [path(f"M{L[0] - 5 * k} {L[1]} q{5 * k} {4 * k} {10 * k} 0", sw=2.6),
                path(f"M{R[0] - 5 * k} {R[1]} q{5 * k} {4 * k} {10 * k} 0", sw=2.6),
                path(f"M{L[0] - 4 * k} {L[1] + 6 * k} q{4 * k} {2 * k} {8 * k} 0", stroke=GREY, sw=2),
                path(f"M{R[0] - 4 * k} {R[1] + 6 * k} q{4 * k} {2 * k} {8 * k} 0", stroke=GREY, sw=2),
                ellipse(cx, cy + 14 * k, 4 * k, 3 * k, DBROWN, sw=2)]
    elif mood == "nervous":
        els += [circle(*L, er * 1.4, WHITE, sw=2), circle(*R, er * 1.4, WHITE, sw=2), dot(*L, er * 0.6), dot(*R, er * 0.6),
                path(f"M{cx - 10 * k} {cy + 13 * k} l{4 * k} {-3 * k} l{4 * k} {3 * k} l{4 * k} {-3 * k} l{4 * k} {3 * k} l{4 * k} {-3 * k}", sw=2.6),
                path(f"M{cx + r * 0.75} {cy - r * 0.55} q-3 6 0 9 q3 -3 0 -9z", LBLUE, sw=2)]
    elif mood == "surprised":
        els += [circle(*L, er * 1.3, WHITE, sw=2.2), circle(*R, er * 1.3, WHITE, sw=2.2), dot(*L, er * 0.7), dot(*R, er * 0.7),
                path(f"M{L[0] - 4 * k} {L[1] - 8 * k} q{4 * k} {-3 * k} {8 * k} 0", sw=2.4),
                path(f"M{R[0] - 4 * k} {R[1] - 8 * k} q{4 * k} {-3 * k} {8 * k} 0", sw=2.4),
                ellipse(cx, cy + 14 * k, 5 * k, 6.5 * k, DBROWN, sw=2.4)]
    elif mood == "bored":
        els += [line(L[0] - 4 * k, L[1], L[0] + 4 * k, L[1], sw=2.8), line(R[0] - 4 * k, R[1], R[0] + 4 * k, R[1], sw=2.8),
                ellipse(cx, cy + 13 * k, 7 * k, 5 * k, DBROWN, sw=2.4)]
    elif mood == "proud":
        els += [path(f"M{L[0] - 4 * k} {L[1] + 1} q{4 * k} {-5 * k} {8 * k} 0", sw=2.6),
                path(f"M{R[0] - 4 * k} {R[1] + 1} q{4 * k} {-5 * k} {8 * k} 0", sw=2.6),
                path(f"M{cx - 8 * k} {cy + 10 * k} Q{cx} {cy + 17 * k} {cx + 8 * k} {cy + 10 * k}", sw=2.8)]
    elif mood == "cool":
        els += [path(f"M{cx - 22 * k} {cy - 7 * k} h{44 * k} l{-3 * k} {10 * k} q{-7 * k} {3 * k} {-14 * k} 0 l{-2 * k} {-5 * k} h{-6 * k} l{-2 * k} {5 * k} q{-7 * k} {3 * k} {-14 * k} 0z", BLACK, sw=2),
                path(f"M{cx - 10 * k} {cy + 11 * k} Q{cx + 2 * k} {cy + 19 * k} {cx + 12 * k} {cy + 8 * k}", sw=2.8)]
    elif mood == "starry":
        els += [star(L[0], L[1], 6 * k, GOLD, sw=1.8), star(R[0], R[1], 6 * k, GOLD, sw=1.8),
                path(f"M{cx - 12 * k} {cy + 8 * k} Q{cx} {cy + 24 * k} {cx + 12 * k} {cy + 8 * k}z", DBROWN, sw=2.6)]
    elif mood == "sleep":
        els += [path(f"M{L[0] - 4 * k} {L[1]} q{4 * k} {4 * k} {8 * k} 0", sw=2.6),
                path(f"M{R[0] - 4 * k} {R[1]} q{4 * k} {4 * k} {8 * k} 0", sw=2.6),
                ellipse(cx, cy + 12 * k, 3 * k, 2.4 * k, DBROWN, sw=2)]
    return "".join(els)


def heart(cx, cy, s, fill=RED, **kw):
    """Cœur centré en (cx, cy), demi-largeur s."""
    d = (f"M{cx} {cy + s * 0.9} C{cx - s * 1.6} {cy - s * 0.1} {cx - s * 0.9} {cy - s * 1.3} {cx} {cy - s * 0.45} "
         f"C{cx + s * 0.9} {cy - s * 1.3} {cx + s * 1.6} {cy - s * 0.1} {cx} {cy + s * 0.9}Z")
    return path(d, fill, **kw)


def star(cx, cy, r, fill=GOLD, points=5, inner=0.45, **kw):
    import math
    pts = []
    for i in range(points * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.pi / points * i - math.pi / 2
        pts.append((round(cx + rr * math.cos(a), 2), round(cy + rr * math.sin(a), 2)))
    return poly(pts, fill, **kw)


def hair(style, color, cx=50, cy=42, r=19):
    """Cheveux : renvoie (derrière, devant)."""
    k = r / 19
    top = (f"M{cx - 19.5 * k} {cy + 1 * k} C{cx - 20 * k} {cy - 23 * k} {cx + 20 * k} {cy - 23 * k} {cx + 19.5 * k} {cy + 1 * k} "
           f"C{cx + 14 * k} {cy - 8 * k} {cx + 4 * k} {cy - 11 * k} {cx - 3 * k} {cy - 9 * k} C{cx - 9 * k} {cy - 8 * k} {cx - 15 * k} {cy - 5 * k} {cx - 19.5 * k} {cy + 1 * k}Z")
    if style == "none":
        return "", ""
    if style == "short":
        return "", path(top, color)
    if style == "long":
        back = path(f"M{cx - 21 * k} {cy} C{cx - 23 * k} {cy - 26 * k} {cx + 23 * k} {cy - 26 * k} {cx + 21 * k} {cy} L{cx + 23 * k} {cy + 26 * k} L{cx - 23 * k} {cy + 26 * k}Z", color)
        return back, path(top, color)
    if style == "bun":
        return circle(cx, cy - 21 * k, 8 * k, color), path(top, color)
    if style == "pigtails":
        back = circle(cx - 22 * k, cy + 4 * k, 7 * k, color) + circle(cx + 22 * k, cy + 4 * k, 7 * k, color)
        return back, path(top, color)
    if style == "bald":
        sides = (path(f"M{cx - 19 * k} {cy + 4 * k} q-2 {-12 * k} {6 * k} {-14 * k} l1 {10 * k}z", color) +
                 path(f"M{cx + 19 * k} {cy + 4 * k} q2 {-12 * k} {-6 * k} {-14 * k} l-1 {10 * k}z", color))
        return "", sides
    if style == "curl":
        return "", path(f"M{cx} {cy - r + 1} c-3 -8 6 -10 7 -4", sw=2.6)
    if style == "spiky":
        spikes = (f"M{cx - 19 * k} {cy} L{cx - 17 * k} {cy - 16 * k} L{cx - 10 * k} {cy - 13 * k} L{cx - 7 * k} {cy - 22 * k} "
                  f"L{cx} {cy - 15 * k} L{cx + 6 * k} {cy - 23 * k} L{cx + 9 * k} {cy - 13 * k} L{cx + 17 * k} {cy - 17 * k} "
                  f"L{cx + 19 * k} {cy} C{cx + 10 * k} {cy - 9 * k} {cx - 10 * k} {cy - 9 * k} {cx - 19 * k} {cy}Z")
        return "", path(spikes, color)
    raise ValueError(style)


def person(x=50, y=0, s=1.0, skin=SKIN, hair_style="short", hair_color=DBROWN, shirt=BLUE, mood="happy",
           glasses=False, mustache=False, extra_front="", extra_back="", bow=None):
    """Personnage en buste. (x, y) = décalage, s = échelle (référence : tête en 50,42 r19, buste jusqu'en bas)."""
    back, front = hair(hair_style, hair_color)
    els = [back, extra_back,
           path("M22 104 C22 80 34 66 50 66 C66 66 78 80 78 104 Z", shirt),
           circle(50, 42, 19, skin), front]
    # visage
    els += [circle(38.5, 49, 3.2, CHEEK, stroke=False, extra='opacity="0.7"'),
            circle(61.5, 49, 3.2, CHEEK, stroke=False, extra='opacity="0.7"')]
    if mood == "happy":
        els += [dot(43.5, 43, 2.3), dot(56.5, 43, 2.3), path("M44.5 50 Q50 55.5 55.5 50", sw=2.6)]
    elif mood == "sleep":
        els += [path("M40.5 43 q3 2.5 6 0", sw=2.4), path("M53.5 43 q3 2.5 6 0", sw=2.4), ellipse(50, 51.5, 2.2, 1.8, DBROWN, sw=1.8)]
    elif mood == "plead":
        els += [circle(43.5, 43, 3.6, WHITE, sw=2), circle(56.5, 43, 3.6, WHITE, sw=2), dot(43.5, 43.6, 2.2), dot(56.5, 43.6, 2.2),
                path("M46 52 Q50 50 54 52", sw=2.4)]
    elif mood == "neutral":
        els += [dot(43.5, 43, 2.3), dot(56.5, 43, 2.3), line(46, 51, 54, 51, sw=2.6)]
    if glasses:
        els += [circle(43.5, 43, 5, sw=2), circle(56.5, 43, 5, sw=2), line(48.5, 43, 51.5, 43, sw=2)]
    if mustache:
        els.append(path("M42 49 Q46 46 50 48.5 Q54 46 58 49 Q55 53 50 50.5 Q45 53 42 49Z", hair_color if hair_color != "none" else DBROWN, sw=1.8))
    if bow:
        els.append(path("M43 70 L50 74 L57 70 L57 78 L50 74 L43 78Z", bow, sw=2))
    els.append(extra_front)
    inner = "".join(els)
    if s == 1.0 and x == 50 and y == 0:
        return inner
    return group(f"translate({x - 50 * s} {y}) scale({s})", inner)


def hand(cx, cy, s=1.0, fill=SKIN, rot=0):
    """Main ouverte (paume), doigts vers le haut."""
    inner = "".join([
        rect(-5, -34, 8, 22, fill, rx=4), rect(4, -36, 8, 24, fill, rx=4), rect(13, -32, 8, 21, fill, rx=4),
        rect(-14, -28, 8, 18, fill, rx=4),
        path("M-15 -14 Q-16 8 0 10 Q20 10 21 -14 Z", fill),
        rect(15, -12, 8, 18, fill, rx=4, rot=-35),
    ])
    return group(f"translate({cx} {cy}) rotate({rot}) scale({s})", inner)


def sparkle(cx, cy, r, fill=YELLOW):
    return path(f"M{cx} {cy - r} Q{cx + r * 0.2} {cy - r * 0.2} {cx + r} {cy} Q{cx + r * 0.2} {cy + r * 0.2} {cx} {cy + r} "
                f"Q{cx - r * 0.2} {cy + r * 0.2} {cx - r} {cy} Q{cx - r * 0.2} {cy - r * 0.2} {cx} {cy - r}Z", fill, sw=2)


def motion(x, y, n=3, gap=7, length=8, angle_dir=1):
    """Petits traits de mouvement."""
    return "".join(path(f"M{x} {y + i * gap} q{4 * angle_dir} -3 {length * angle_dir} 0", sw=2.6) for i in range(n))


def calendar(cx=50, cy=54, w=64, h=58, header=RED):
    x, y = cx - w / 2, cy - h / 2
    return "".join([
        rect(x, y, w, h, WHITE, rx=8),
        path(f"M{x} {y + 16} V{y + 8} Q{x} {y} {x + 8} {y} H{x + w - 8} Q{x + w} {y} {x + w} {y + 8} V{y + 16}Z", header),
        rect(x + 12, y - 6, 5, 12, LGREY, rx=2.5), rect(x + w - 17, y - 6, 5, 12, LGREY, rx=2.5),
    ])


def cal_grid(cx=50, cy=54, w=64, h=58, highlight=(), color=YELLOW, cols=7, rows=3, arrow=None):
    """Cases d'un calendrier ; highlight = indices des cases colorées."""
    x0, y0 = cx - w / 2 + 6, cy - h / 2 + 22
    cw, ch = (w - 12) / cols, (h - 28) / rows
    els = []
    for r in range(rows):
        for c in range(cols):
            i = r * cols + c
            fill = color if i in highlight else LGREY
            els.append(rect(round(x0 + c * cw + 1, 2), round(y0 + r * ch + 1, 2), round(cw - 2, 2), round(ch - 2, 2), fill, rx=1.5,
                            stroke=INK if i in highlight else False, sw=1.6))
    return "".join(els)


def bowl(cx=50, cy=58, w=70, fill=LBLUE, food=RED, depth=28):
    x = cx - w / 2
    return "".join([
        ellipse(cx, cy, w / 2, 8, food),
        path(f"M{x} {cy} Q{x + 2} {cy + depth} {cx} {cy + depth} Q{x + w - 2} {cy + depth} {x + w} {cy} Q{cx} {cy + 10} {x} {cy}Z", fill),
    ])


def plate(cx=50, cy=62, rx=40, ry=14, fill=WHITE):
    return ellipse(cx, cy, rx, ry, fill) + ellipse(cx, cy - 1, rx - 9, ry - 5, LGREY, stroke=False)


def steam(x, y, n=3, gap=10):
    return "".join(path(f"M{x + i * gap} {y} q-4 -5 0 -10 q4 -5 0 -10", stroke=GREY, sw=2.6) for i in range(n))


def coin(cx, cy, r=12, fill=GOLD, sign="$"):
    return circle(cx, cy, r, fill) + circle(cx, cy, r - 4, fill, sw=1.8) + text(cx, cy + r * 0.38, sign, r * 1.05, DBROWN)


def building_windows(x, y, cols, rows, w=8, h=8, gx=4, gy=4, fill=LBLUE):
    return "".join(rect(x + c * (w + gx), y + r * (h + gy), w, h, fill, rx=1.5, sw=2) for r in range(rows) for c in range(cols))


# ───────── Réutilisation et petits pictos ─────────

def inner(svg_str):
    """Contenu d'une illustration déjà générée (sans les balises <svg> et <g> extérieures)."""
    body = svg_str.split(">", 2)[2]
    return body[: -len("</g></svg>")]


def use(svg_str, x=0, y=0, s=1.0):
    """Replace une illustration existante, mise à l'échelle s, coin haut-gauche en (x, y)."""
    return group(f"translate({x} {y}) scale({s})", inner(svg_str))


def arrow(x1, y1, x2, y2, color=INK, sw=3.6, head=7):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (round(x2 - head * math.cos(a - 0.5), 2), round(y2 - head * math.sin(a - 0.5), 2))
    p2 = (round(x2 - head * math.cos(a + 0.5), 2), round(y2 - head * math.sin(a + 0.5), 2))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"/>'
            + path(f"M{p1[0]} {p1[1]} L{x2} {y2} L{p2[0]} {p2[1]}", stroke=color, sw=sw))


def check(cx, cy, r=12, fill=GREEN):
    return circle(cx, cy, r, fill) + path(f"M{cx - r * 0.45} {cy} l{r * 0.32} {r * 0.35} l{r * 0.6} {-r * 0.65}", stroke=WHITE, sw=3.4)


def cross(cx, cy, r=12, fill=RED):
    d = r * 0.4
    return circle(cx, cy, r, fill) + path(f"M{cx - d} {cy - d} L{cx + d} {cy + d} M{cx + d} {cy - d} L{cx - d} {cy + d}", stroke=WHITE, sw=3.4)


def bubble(x, y, w, h, fill=WHITE, tail="left"):
    tx = x + 12 if tail == "left" else x + w - 12
    d = 8 if tail == "left" else -8
    return rect(x, y, w, h, fill, rx=min(12, h / 2)) + \
        path(f"M{tx} {y + h - 1.5} l{d * 0.2} 10 l{d} -10", fill) + \
        path(f"M{tx - 1.5 * (1 if d > 0 else -1)} {y + h - 2} h{d * 1.3}", stroke=fill, sw=3.4)


def paper(x=24, y=14, w=52, h=72, fill=WHITE, lines=5, line_color=LGREY):
    els = [path(f"M{x} {y} H{x + w - 12} L{x + w} {y + 12} V{y + h} H{x}Z", fill),
           path(f"M{x + w - 12} {y} V{y + 12} H{x + w}", LGREY, sw=2.4)]
    for i in range(lines):
        els.append(line(x + 8, y + 22 + i * 9, x + w - 8 - (12 if i == lines - 1 else 0), y + 22 + i * 9, sw=3, color=line_color))
    return "".join(els)


def swatch(color, label=None):
    """Tache de peinture (couleurs)."""
    d = ("M50 14 C64 12 70 24 80 26 C92 30 90 46 86 54 C82 64 92 74 80 82 C70 90 60 82 50 86 "
         "C38 90 28 92 20 82 C12 72 18 62 14 52 C10 40 14 28 26 24 C36 20 40 16 50 14Z")
    return path(d, color) + circle(28, 88, 5, color) + circle(84, 18, 4, color) + \
        path("M34 34 q6 -6 14 -6", stroke=WHITE, sw=3.6, extra='opacity="0.7"') + (text(50, 60, label, 18, WHITE) if label else "")


def tag(x, y, w, s, fill=YELLOW, size=15, color=INK):
    """Étiquette avec un texte court."""
    return rect(x, y, w, 24, fill, rx=8) + text(x + w / 2, y + 17, s, size, color)


def sign_post(s, fill=GREEN, color=WHITE, size=16, y=24):
    return rect(46, y + 20, 8, 64 - y, BROWN) + rect(14, y, 72, 30, fill, rx=6) + text(50, y + 21, s, size, color)


def hat(kind, cx=50, cy=26, s=1.0):
    """Couvre-chefs posés sur la tête d'un person() (tête en 50,42 r19)."""
    if kind == "cap":
        return path(f"M{cx - 19} {cy + 6} Q{cx} {cy - 20} {cx + 19} {cy + 6}Z", BLUE) + path(f"M{cx + 10} {cy + 4} h20 q-2 5 -20 5z", BLUE)
    if kind == "helmet":
        return path(f"M{cx - 22} {cy + 8} Q{cx} {cy - 22} {cx + 22} {cy + 8}Z", YELLOW) + rect(cx - 26, cy + 4, 52, 7, YELLOW, rx=3) + \
            rect(cx - 4, cy - 12, 8, 14, ORANGE, rx=3)
    if kind == "chef":
        return circle(cx - 11, cy - 10, 9, WHITE) + circle(cx + 11, cy - 10, 9, WHITE) + circle(cx, cy - 15, 11, WHITE) + \
            rect(cx - 17, cy - 6, 34, 14, WHITE, rx=3)
    if kind == "police":
        return path(f"M{cx - 20} {cy + 6} L{cx - 22} {cy - 10} Q{cx} {cy - 22} {cx + 22} {cy - 10} L{cx + 20} {cy + 6}Z", NAVY) + \
            rect(cx - 22, cy + 2, 44, 7, BLACK, rx=2) + star(cx, cy - 6, 5, GOLD, sw=1.6)
    if kind == "straw":
        return ellipse(cx, cy + 6, 32, 7, TAN) + path(f"M{cx - 16} {cy + 5} Q{cx - 15} {cy - 16} {cx} {cy - 16} Q{cx + 15} {cy - 16} {cx + 16} {cy + 5}Z", TAN) + \
            path(f"M{cx - 16} {cy} H{cx + 16}", stroke=RED, sw=3.6)
    if kind == "grad":
        return poly([(cx - 26, cy - 4), (cx, cy - 14), (cx + 26, cy - 4), (cx, cy + 6)], BLACK) + \
            path(f"M{cx + 20} {cy - 2} v14", stroke=GOLD, sw=2.6) + circle(cx + 20, cy + 13, 2.4, GOLD, sw=1.4)
    if kind == "fire":
        return path(f"M{cx - 26} {cy + 8} Q{cx - 22} {cy - 20} {cx} {cy - 20} Q{cx + 22} {cy - 20} {cx + 26} {cy + 8}Z", RED) + \
            rect(cx - 6, cy - 14, 12, 14, GOLD, rx=3)
    raise ValueError(kind)
