"""Illustrations du niveau A1."""
from .kit import *  # noqa: F401,F403

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


# ── Saludos ──

@art("hola")
def _():
    return person(shirt=ORANGE, hair_style="long", hair_color=DBROWN,
                  extra_front=hand(84, 50, 0.62, rot=12) + motion(88, 14, 2, 7, 7))


@art("adios")
def _():
    return hand(50, 70, 1.15, rot=-14) + path("M18 30 q-6 10 0 20", sw=3) + path("M10 26 q-8 14 0 28", sw=3) + \
        path("M82 30 q6 10 0 20", sw=3) + path("M90 26 q8 14 0 28", sw=3)


@art("gracias")
def _():
    return heart(50, 54, 30, RED) + path("M34 40 q4 -6 10 -4", stroke=WHITE, sw=3.5) + \
        sparkle(18, 22, 7) + sparkle(84, 20, 5) + sparkle(86, 78, 6, PINK)


@art("por-favor")
def _():
    hands = (path("M44 104 L44 76 Q44 66 50 60 Q56 66 56 76 L56 104Z", SKIN) +
             path("M50 60 L50 100", sw=2) +
             rect(40, 92, 20, 10, ORANGE, rx=3))
    return person(shirt=PURPLE, mood="plead", hair_style="short", hair_color=BLACK, extra_front=hands)


@art("buenos-dias")
def _():
    rays = "".join(path(f"M50 62 L{x} {y}", stroke=ORANGE, sw=4) for x, y in [(14, 40), (26, 22), (50, 12), (74, 22), (86, 40)])
    return rect(0, 0, 100, 100, "none", stroke=False) + rays + \
        path("M18 64 A32 32 0 0 1 82 64 Z", YELLOW) + \
        path("M6 64 H94 V92 Q50 84 6 92Z", LBLUE) + path("M14 74 h18 M60 78 h22 M36 84 h14", stroke=WHITE, sw=3)


@art("buenas-noches")
def _():
    return circle(50, 50, 42, NAVY) + path("M58 22 A26 26 0 1 0 74 66 A21 21 0 1 1 58 22Z", LYELLOW) + \
        star(30, 30, 6, YELLOW, sw=2) + star(76, 32, 4.5, YELLOW, sw=2) + star(24, 64, 4, YELLOW, sw=2) + \
        text(78, 82, "z", 14, WHITE) + text(86, 72, "z", 10, WHITE)


@art("amigo")
def _():
    return person(30, 8, 0.72, shirt=GREEN, hair_style="short", hair_color=BLACK) + \
        person(70, 8, 0.72, skin=SKIN2, shirt=ORANGE, hair_style="long", hair_color=DBROWN) + \
        heart(50, 18, 7, RED)


@art("mucho-gusto")
def _():
    return rect(-4, 46, 34, 22, BLUE, rx=4) + rect(70, 46, 34, 22, RED, rx=4) + \
        path("M28 48 Q40 40 52 46 L70 50 L70 66 Q58 74 44 70 L28 66Z", SKIN) + \
        path("M44 70 Q38 62 46 56 M52 70 Q46 62 54 56 M60 68 Q55 62 62 57", sw=2.4) + \
        path("M52 46 Q60 40 66 48", SKIN2, sw=2.6) + sparkle(50, 24, 7)


# ── La familia ──

@art("familia")
def _():
    return person(24, 18, 0.62, shirt=PINK, hair_style="long", hair_color=DBROWN) + \
        person(76, 18, 0.62, skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=BLACK, mustache=True) + \
        person(50, 42, 0.5, shirt=YELLOW, hair_style="pigtails", hair_color=DBROWN)


@art("mama")
def _():
    return person(shirt=PINK, hair_style="long", hair_color=DBROWN) + heart(80, 22, 7, RED)


@art("papa")
def _():
    return person(skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=BLACK, mustache=True,
                  extra_front=path("M47 66 L50 92 L53 66Z", RED, sw=2))


@art("hermano")
def _():
    return person(50, 14, 0.86, shirt=GREEN, hair_style="spiky", hair_color=BROWN) + \
        rect(62, 80, 20, 14, RED, rx=4) + ellipse(72, 78, 10, 4, WHITE)


@art("hermana")
def _():
    return person(50, 14, 0.86, skin=SKIN2, shirt=YELLOW, hair_style="pigtails", hair_color=BLACK) + heart(84, 26, 7, PINK)


@art("abuela")
def _():
    return person(shirt=LPURPLE, hair_style="bun", hair_color=LGREY, glasses=True,
                  extra_front=path("M36 72 Q50 82 64 72", stroke=WHITE, sw=3) + circle(50, 80, 2.5, WHITE, sw=1.5))


@art("abuelo")
def _():
    return person(shirt=TAN, hair_style="bald", hair_color=LGREY, glasses=True, mustache=True,
                  extra_front=rect(78, 56, 5, 46, BROWN, rx=2.5) + path("M80 58 q0 -10 -10 -10", BROWN, sw=4))


@art("bebe")
def _():
    els = [path("M30 104 C30 84 38 76 50 76 C62 76 70 84 70 104Z", LBLUE),
           circle(50, 48, 27, SKIN),
           path("M50 21 c-4 -8 6 -11 8 -5", sw=2.8),
           circle(36, 56, 4, CHEEK, stroke=False, extra='opacity="0.7"'), circle(64, 56, 4, CHEEK, stroke=False, extra='opacity="0.7"'),
           dot(41, 47, 2.8), dot(59, 47, 2.8),
           circle(50, 61, 7, PINK), circle(50, 61, 2.5, WHITE, sw=1.6),
           rect(40, 62, 20, 6, PINK, rx=3, stroke=False)]
    return "".join(els[:-1])


# ── En el mercado ──

@art("mango")
def _():
    return path("M24 58 C18 34 40 16 62 22 C86 30 90 62 68 80 C50 94 30 82 24 58Z", ORANGE) + \
        path("M62 22 C86 30 90 62 68 80 C78 60 76 38 62 22Z", RED, sw=2.4) + \
        path("M34 60 C30 46 38 34 50 30", stroke=YELLOW, sw=4.5) + \
        path("M58 22 q0 -8 4 -12", sw=3) + path("M62 12 C72 2 88 8 90 16 C80 22 68 20 62 12Z", GREEN)


@art("aguacate")
def _():
    return path("M50 8 C30 8 26 36 22 52 C16 78 32 94 50 94 C68 94 84 78 78 52 C74 36 70 8 50 8Z", DGREEN) + \
        path("M50 18 C36 18 34 40 31 54 C27 74 38 85 50 85 C62 85 73 74 69 54 C66 40 64 18 50 18Z", LGREEN, sw=2.4) + \
        circle(50, 62, 14, BROWN) + path("M44 56 q3 -4 8 -3", stroke=TAN, sw=3)


@art("limon")
def _():
    segs = "".join(line(50, 54, x, y, sw=2.4) for x, y in [(50, 24), (76, 39), (76, 69), (50, 84), (24, 69), (24, 39)])
    return circle(50, 54, 36, GREEN) + circle(50, 54, 29, LGREEN, sw=2.4) + segs + circle(50, 54, 4, LYELLOW, sw=2) + \
        path("M58 12 C66 4 80 6 82 12 C74 18 64 18 58 12Z", DGREEN)


@art("jitomate")
def _():
    return path("M50 26 C22 24 10 46 16 66 C22 86 40 92 50 92 C60 92 78 86 84 66 C90 46 78 24 50 26Z", RED) + \
        path("M28 50 q4 -10 14 -12", stroke="#FF8A80", sw=4) + \
        poly([(50, 34), (40, 20), (46, 28), (34, 26), (44, 32), (50, 22), (56, 32), (66, 26), (54, 28), (60, 20)], GREEN, sw=2.4) + \
        path("M50 24 q0 -10 6 -14", sw=3.4)


@art("elote")
def _():
    kernels = "".join(ellipse(40 + c * 9, 24 + r * 10, 3.6, 4.2, YELLOW, sw=1.6) for r in range(6) for c in range(3))
    return path("M50 6 C30 6 28 40 32 74 L50 90 L68 74 C72 40 70 6 50 6Z", GOLD) + kernels + \
        path("M50 94 C36 84 18 74 16 44 C26 58 36 66 44 70 Z", GREEN) + \
        path("M50 94 C64 84 82 74 84 44 C74 58 64 66 56 70 Z", LGREEN)


@art("chile")
def _():
    return path("M34 26 C26 40 30 64 46 78 C58 88 74 92 86 90 C70 82 60 70 54 52 C50 40 50 30 46 24 Z", RED) + \
        path("M38 36 C38 50 44 62 52 70", stroke="#FF8A80", sw=3.5) + \
        path("M30 26 C34 18 44 16 50 24 C46 30 36 30 30 26Z", GREEN) + path("M40 20 C38 12 42 6 50 4", sw=4)


@art("sandia")
def _():
    seeds = "".join(ellipse(x, y, 2, 3.2, BLACK, stroke=False, rot=r) for x, y, r in [(34, 44, -20), (50, 40, 0), (66, 44, 20), (42, 56, -10), (58, 56, 10), (50, 66, 0)])
    return path("M8 30 A42 42 0 0 0 92 30 Z", GREEN) + path("M15 30 A35 35 0 0 0 85 30 Z", WHITE, sw=2) + \
        path("M20 30 A30 30 0 0 0 80 30 Z", RED, sw=2.2) + seeds


@art("platano")
def _():
    return path("M20 18 C14 50 34 84 74 86 C84 86 90 82 90 78 C60 76 40 56 34 20 Z", YELLOW) + \
        path("M30 30 C34 52 46 68 66 76", stroke=GOLD, sw=3) + \
        path("M20 18 l-2 -8 l10 -2 l2 10Z", DBROWN, sw=2.4) + path("M90 78 l4 2 l-2 4 l-4 -2z", DBROWN, sw=2)


# ── La taquería ──

@art("taco")
def _():
    return path("M10 76 A40 40 0 0 1 90 76 Z", GOLD) + \
        path("M18 68 Q26 40 50 38 Q74 40 82 68", fill="none") + \
        path("M22 66 Q22 46 38 40 Q50 50 44 62 Q34 70 22 66Z", BROWN, sw=2.6) + \
        path("M40 56 Q50 34 64 40 Q72 48 66 62 Q54 66 40 56Z", DBROWN, sw=2.6) + \
        circle(36, 44, 5, LGREEN, sw=2) + circle(52, 40, 4, LGREEN, sw=2) + circle(66, 46, 5, LGREEN, sw=2) + \
        rect(44, 46, 7, 7, WHITE, rx=2, sw=2) + rect(58, 52, 6, 6, WHITE, rx=2, sw=2) + \
        path("M10 76 A40 40 0 0 1 90 76 Z", GOLD, extra='fill-opacity="0"') + path("M10 76 Q50 66 90 76", GOLD, sw=3)


@art("tortilla")
def _():
    spots = "".join(circle(x, y, r, TAN, stroke=False) for x, y, r in [(36, 40, 4), (58, 36, 3), (66, 46, 4), (44, 50, 3), (30, 50, 2.5)])
    return ellipse(50, 76, 40, 12, CREAM) + ellipse(50, 66, 40, 12, CREAM) + ellipse(50, 56, 40, 12, CREAM) + \
        ellipse(50, 46, 40, 14, CREAM) + spots


@art("salsa")
def _():
    return path("M14 44 Q14 82 50 82 Q86 82 86 44 Z", DGREY) + ellipse(50, 44, 36, 9, RED) + \
        circle(38, 43, 3, GREEN, stroke=False) + circle(58, 42, 3, LGREEN, stroke=False) + circle(48, 46, 2.5, WHITE, stroke=False) + \
        rect(24, 80, 10, 12, DGREY, rx=3) + rect(66, 80, 10, 12, DGREY, rx=3) + rect(45, 82, 10, 10, DGREY, rx=3) + rect(62, 6, 10, 38, GREY, rx=5, rot=35) + \
        circle(26, 64, 2, GREY, stroke=False) + circle(70, 62, 2, GREY, stroke=False) + circle(56, 70, 2, GREY, stroke=False)


@art("queso")
def _():
    return poly([(12, 72), (88, 72), (88, 44), (12, 72)], YELLOW) + poly([(12, 72), (88, 44), (60, 26)], LYELLOW) + \
        path("M12 72 L60 26 L88 44 L88 72 Z", YELLOW, extra='fill-opacity="0"') + \
        circle(70, 60, 5, GOLD, sw=2) + circle(52, 66, 3.5, GOLD, sw=2) + circle(80, 52, 3, GOLD, sw=2) + \
        ellipse(58, 40, 4, 2.5, GOLD, sw=1.8)


@art("carne")
def _():
    return path("M18 50 C10 26 40 14 62 22 C84 30 92 52 80 70 C68 88 36 86 26 72 C22 66 22 58 18 50Z", "#D9534F") + \
        path("M30 46 C40 36 58 34 70 44", stroke="#FFD0C8", sw=4) + path("M34 62 C46 54 60 56 70 62", stroke="#FFD0C8", sw=4) + \
        circle(64, 54, 8, WHITE, sw=2.4) + circle(64, 54, 3, LGREY, sw=1.6)


@art("cebolla")
def _():
    return path("M50 20 C24 30 16 54 24 72 C32 88 68 88 76 72 C84 54 76 30 50 20Z", "#C86BB5") + \
        path("M50 22 C38 34 34 56 40 82", stroke=WHITE, sw=2.6) + path("M50 22 C62 34 66 56 60 82", stroke=WHITE, sw=2.6) + \
        path("M50 22 L50 84", stroke=WHITE, sw=2.6) + path("M44 22 q6 -16 2 -18 M54 22 q2 -12 8 -16", sw=3) + \
        path("M40 88 q10 6 20 0", sw=2.4)


@art("agua")
def _():
    return path("M50 8 C38 30 22 46 22 64 A28 28 0 0 0 78 64 C78 46 62 30 50 8Z", LBLUE) + \
        path("M36 62 Q36 76 48 80", stroke=WHITE, sw=4.5) + circle(80, 26, 6, LBLUE, sw=2.4) + circle(20, 30, 4, LBLUE, sw=2.2)


@art("refresco")
def _():
    return poly([(26, 30), (74, 30), (66, 94), (34, 94)], RED) + rect(22, 22, 56, 10, WHITE, rx=4) + \
        path("M54 22 L62 4 L72 6", stroke=INK, sw=4) + path("M54 22 L62 4 L72 6", stroke=YELLOW, sw=1.6) + \
        path("M32 50 h36 M33 60 h34", stroke=WHITE, sw=4) + circle(46, 76, 3, WHITE, stroke=False) + circle(56, 82, 2, WHITE, stroke=False)


# ── Números y dinero ──

def number(n, fill, size=56):
    return circle(50, 50, 40, fill) + circle(50, 50, 32, "none", stroke=WHITE, sw=2.4) + text(50, 50 + size * 0.36, n, size, WHITE)


@art("uno")
def _():
    return number("1", RED)


@art("dos")
def _():
    return number("2", BLUE)


@art("tres")
def _():
    return number("3", GREEN)


@art("diez")
def _():
    return number("10", PURPLE, 46)


@art("cien")
def _():
    return number("100", ORANGE, 36)


@art("peso")
def _():
    return circle(50, 50, 40, GREEN) + text(50, 70, "$", 62, WHITE) + sparkle(84, 18, 7) + sparkle(16, 82, 5)


@art("billete")
def _():
    return rect(8, 24, 84, 52, "#7FCB8E", rx=6) + rect(15, 31, 70, 38, "none", rx=4, stroke=DGREEN, sw=2) + \
        circle(50, 50, 13, LGREEN, sw=2.4) + text(50, 57, "$", 20, DGREEN) + \
        text(24, 44, "100", 9, DGREEN) + text(76, 64, "100", 9, DGREEN)


@art("moneda")
def _():
    return ellipse(50, 80, 30, 9, GOLD) + rect(20, 70, 60, 10, GOLD, stroke=False) + ellipse(50, 70, 30, 9, GOLD) + \
        rect(20, 60, 60, 10, GOLD, stroke=False) + path("M20 60 V80 M80 60 V80", sw=3.2) + ellipse(50, 60, 30, 9, GOLD) + \
        coin(56, 34, 20)


# ── La casa ──

@art("casa")
def _():
    return rect(22, 46, 56, 44, CREAM) + poly([(12, 50), (50, 16), (88, 50)], RED) + rect(62, 20, 10, 18, DGREY, rx=1) + \
        rect(42, 62, 16, 28, BROWN, rx=3) + circle(54, 77, 1.8, YELLOW, sw=1) + \
        rect(28, 56, 10, 10, LBLUE, rx=1.5, sw=2.4) + rect(64, 56, 10, 10, LBLUE, rx=1.5, sw=2.4) + \
        path("M10 90 H90", sw=3.2)


@art("cocina")
def _():
    flames = "".join(path(f"M{x} 66 q-4 -6 0 -12 q1 5 3 5 q2 -4 0 -9 q6 6 2 16z", ORANGE, sw=2) for x in (34, 48, 62))
    return rect(14, 66, 72, 26, LGREY, rx=4) + rect(20, 74, 26, 14, DGREY, rx=2, sw=2.4) + circle(62, 80, 4, WHITE, sw=2) + circle(76, 80, 4, WHITE, sw=2) + \
        flames + path("M22 56 Q22 34 50 34 Q78 34 78 56 Z", RED) + rect(18, 52, 64, 6, DRED, rx=3) + \
        rect(44, 26, 12, 8, DRED, rx=3) + steam(38, 24, 3, 12)


@art("cama")
def _():
    return rect(10, 28, 12, 62, BROWN, rx=4) + rect(78, 50, 12, 40, BROWN, rx=4) + rect(16, 56, 70, 20, CREAM, rx=4) + \
        rect(20, 44, 24, 14, WHITE, rx=6) + path("M40 52 H82 Q86 52 86 58 V70 H40Z", BLUE) + \
        path("M50 60 h26 M50 66 h26", stroke=LBLUE, sw=2.6)


@art("puerta")
def _():
    return rect(24, 8, 52, 86, BROWN, rx=4) + rect(32, 16, 36, 30, TAN, rx=3, sw=2.4) + rect(32, 52, 36, 34, TAN, rx=3, sw=2.4) + \
        circle(64, 54, 4, YELLOW) + path("M14 94 H86", sw=3.2)


@art("ventana")
def _():
    return rect(16, 14, 68, 70, LBLUE) + line(50, 14, 50, 84) + line(16, 49, 84, 49) + \
        path("M22 20 l10 0 M22 26 l6 0", stroke=WHITE, sw=3) + \
        path("M10 10 H32 Q26 40 34 88 H10Z", RED) + path("M90 10 H68 Q74 40 66 88 H90Z", RED) + \
        rect(6, 6, 88, 8, BROWN, rx=3) + rect(12, 84, 76, 8, BROWN, rx=3)


@art("bano")
def _():
    return rect(26, 8, 34, 30, WHITE, rx=5) + rect(32, 14, 14, 4, LGREY, rx=2, stroke=False) + \
        path("M18 44 H76 Q78 70 56 74 L58 92 H32 L34 74 Q18 70 18 44Z", WHITE) + ellipse(47, 44, 29, 7, LGREY) + \
        ellipse(47, 44, 21, 4, LBLUE, sw=2) + rect(22, 36, 50, 6, WHITE, rx=3)


@art("silla")
def _():
    return rect(28, 10, 8, 82, BROWN, rx=3) + rect(64, 50, 8, 42, BROWN, rx=3) + rect(28, 50, 8, 0.1, BROWN) + \
        rect(32, 14, 34, 8, TAN, rx=3) + rect(32, 28, 34, 8, TAN, rx=3) + rect(22, 48, 56, 10, RED, rx=4) + \
        rect(30, 58, 6, 34, BROWN, rx=3) + rect(64, 58, 6, 34, BROWN, rx=3)


@art("sillon")
def _():
    return rect(14, 30, 72, 34, TEAL, rx=12) + rect(6, 46, 20, 32, TEAL, rx=8) + rect(74, 46, 20, 32, TEAL, rx=8) + \
        rect(22, 56, 56, 18, "#5FD8CC", rx=6) + line(50, 58, 50, 72, sw=2.4) + \
        rect(14, 78, 6, 10, BROWN, rx=2) + rect(80, 78, 6, 10, BROWN, rx=2) + rect(10, 74, 80, 6, TEAL, rx=3, stroke=False)


# ── Ropa y colores ──

@art("camisa")
def _():
    return path("M34 14 L18 22 L6 44 L20 52 L26 42 L26 90 H74 V42 L80 52 L94 44 L82 22 L66 14 Q50 26 34 14Z", WHITE) + \
        path("M34 14 L42 30 L50 20 L58 30 L66 14", fill=LGREY) + line(50, 22, 50, 90, sw=2.4) + \
        dot(54, 40, 2) + dot(54, 54, 2) + dot(54, 68, 2) + rect(30, 44, 12, 10, "none", rx=2, sw=2.2)


@art("pantalon")
def _():
    return path("M24 10 H76 L82 92 H58 L50 40 L42 92 H18Z", BLUE) + rect(24, 10, 52, 10, NAVY, rx=2) + \
        path("M50 20 V34", sw=2.4) + path("M30 22 q6 10 14 4 M70 22 q-6 10 -14 4", stroke=LBLUE, sw=2.4) + \
        path("M22 84 H40 M60 84 H80", stroke=LBLUE, sw=2.4)


@art("zapatos")
def _():
    shoe = lambda x, c: path(f"M{x} 46 Q{x} 36 {x + 12} 36 L{x + 16} 52 Q{x + 34} 56 {x + 38} 66 Q{x + 40} 74 {x + 30} 74 H{x - 2} Q{x - 6} 74 {x - 4} 62Z", c) + \
        path(f"M{x - 4} 68 H{x + 39}", sw=2.4) + path(f"M{x + 10} 46 l6 -2 M{x + 12} 52 l6 -2", stroke=WHITE, sw=2.2)
    return shoe(10, BROWN) + group("translate(44 14)", shoe(10, DBROWN))


@art("sombrero")
def _():
    return ellipse(50, 66, 46, 16, GOLD) + ellipse(50, 64, 30, 8, "#E0A92A", stroke=False) + \
        path("M30 64 C30 30 38 20 50 20 C62 20 70 30 70 64 Z", GOLD) + \
        path("M31 54 Q50 62 69 54 L70 62 Q50 70 30 62Z", RED, sw=2.4) + \
        path("M14 70 q6 4 12 2 M86 70 q-6 4 -12 2", stroke=RED, sw=3) + \
        dot(36, 59, 1.6, WHITE) + dot(50, 62, 1.6, WHITE) + dot(64, 59, 1.6, WHITE)


def splash(color, light=None):
    d = ("M50 14 C58 14 60 24 66 22 C76 18 84 26 80 36 C78 42 88 46 86 56 C84 66 74 64 72 72 C70 82 62 88 52 84 "
         "C44 80 40 90 30 86 C20 82 22 72 18 66 C12 58 12 48 20 44 C26 40 18 30 26 24 C34 18 40 26 44 20 C46 16 48 14 50 14Z")
    els = path(d, color) + circle(88, 20, 5, color) + circle(14, 82, 4, color) + circle(90, 82, 3.5, color)
    if light:
        els += path("M36 38 Q42 30 52 30", stroke=light, sw=4.5)
    return els


@art("rojo")
def _():
    return splash(RED, "#FF9A8F")


@art("verde")
def _():
    return splash(GREEN, LGREEN)


@art("azul")
def _():
    return splash(BLUE, LBLUE)


@art("blanco")
def _():
    return splash(WHITE, LGREY)


# ── El clima y los días ──

@art("sol")
def _():
    rays = "".join(group(f"rotate({a} 50 50)", rect(46, 4, 8, 16, ORANGE, rx=4)) for a in range(0, 360, 45))
    return rays + circle(50, 50, 26, YELLOW) + face(50, 52, 18, skin=YELLOW, cheeks=True)


@art("lluvia")
def _():
    drops = "".join(path(f"M{x} {y} q-5 8 0 11 q5 -3 0 -11z", BLUE, sw=2.2) for x, y in [(30, 66), (50, 72), (70, 66), (40, 84), (62, 86)])
    return path("M24 60 A14 14 0 0 1 26 32 A20 20 0 0 1 64 24 A16 16 0 0 1 80 58 Z", LGREY) + drops


@art("calor")
def _():
    return circle(50, 50, 38, ORANGE, stroke=False, extra='opacity="0.35"') + face(50, 50, 30, skin="#FF8A6B", mood="tired") + \
        path("M80 34 q-5 8 0 11 q5 -3 0 -11z", LBLUE, sw=2.2) + path("M18 40 q-4 7 0 10 q4 -3 0 -10z", LBLUE, sw=2.2) + \
        path("M10 16 q4 -4 8 0 t8 0 M74 12 q4 -4 8 0 t8 0", stroke=RED, sw=2.6)


@art("frio")
def _():
    arm = lambda col, w: line(50, 50, 50, 10, sw=w, color=col) + path("M41 19 L50 27 L59 19", stroke=col, sw=w - 1) + \
        path("M43 33 L50 39 L57 33", stroke=col, sw=w - 1)
    outer = "".join(group(f"rotate({a} 50 50)", arm(INK, 8.5)) for a in range(0, 360, 60))
    inner = "".join(group(f"rotate({a} 50 50)", arm(LBLUE, 3.5)) for a in range(0, 360, 60))
    return outer + inner + circle(50, 50, 7, WHITE)


@art("hoy")
def _():
    return calendar() + cal_grid(highlight=(10,), color=YELLOW) + circle(50, 62, 9, "none", stroke=RED, sw=3.6)


@art("manana")
def _():
    return calendar(header=BLUE) + cal_grid(highlight=(11,), color=LGREEN) + \
        path("M30 68 Q40 50 54 60", stroke=RED, sw=3.4) + path("M50 54 L56 61 L48 64", stroke=RED, sw=3.4)


@art("noche")
def _():
    return rect(6, 6, 88, 88, NAVY, rx=18) + circle(70, 30, 12, LYELLOW) + circle(64, 26, 3, YELLOW, stroke=False) + \
        star(26, 24, 4, YELLOW, sw=1.8) + star(46, 16, 3, YELLOW, sw=1.6) + \
        path("M6 94 V64 H20 V54 H34 V70 H46 V48 H60 V66 H72 V58 H94 V94Z", "#3D4C8C") + \
        rect(50, 54, 5, 5, YELLOW, stroke=False) + rect(24, 60, 5, 5, YELLOW, stroke=False) + rect(78, 64, 5, 5, YELLOW, stroke=False)


@art("semana")
def _():
    return calendar(header=PURPLE) + cal_grid(highlight=(7, 8, 9, 10, 11, 12, 13), color=PINK)
