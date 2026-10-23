"""Illustrations du niveau A1 (compléments et nouveaux thèmes)."""
from .kit import *  # noqa: F401,F403
from .a1 import ART as A1, number, splash

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


def day(abbr, header, highlight, color=YELLOW):
    return calendar(header=header) + cal_grid(highlight=highlight, color=color) + \
        rect(26, 10, 48, 20, WHITE, rx=6) + text(50, 26, abbr, 15, header)


# ── Saludos ──

@art("buenas-tardes")
def _():
    return path("M18 66 A32 32 0 0 1 82 66 Z", ORANGE) + path("M6 66 H94 V92 Q50 84 6 92Z", "#FF7A59") + \
        path("M14 76 h18 M60 80 h22", stroke=YELLOW, sw=3) + \
        "".join(path(f"M50 62 L{x} {y}", stroke=YELLOW, sw=3.6) for x, y in [(16, 46), (28, 26), (72, 26), (84, 46)])


@art("senor")
def _():
    return person(skin=SKIN2, shirt=NAVY, hair_style="bald", hair_color=GREY, mustache=True, glasses=True,
                  extra_front=path("M44 66 L50 76 L56 66Z", WHITE, sw=2) + path("M48 72 L50 92 L52 72Z", RED, sw=1.8))


@art("senora")
def _():
    return person(shirt=PURPLE, hair_style="bun", hair_color=GREY, glasses=True,
                  extra_front=circle(40, 78, 2.4, WHITE, sw=1.4) + circle(50, 80, 2.4, WHITE, sw=1.4) + circle(60, 78, 2.4, WHITE, sw=1.4))


@art("bienvenido")
def _():
    return rect(10, 36, 80, 34, ORANGE, rx=8) + text(50, 60, "¡Hola!", 20, WHITE) + \
        path("M10 70 L4 90 M90 70 L96 90", sw=3.6) + \
        path("M20 36 Q35 22 50 36 Q65 22 80 36", stroke=PINK, sw=3) + sparkle(14, 16, 6) + sparkle(86, 18, 7, PINK)


@art("perdon")
def _():
    return person(shirt=TEAL, mood="plead", hair_style="short", hair_color=DBROWN,
                  extra_front=hand(78, 64, 0.5, rot=-8) + path("M70 18 q-4 6 0 9 q4 -3 0 -9z", LBLUE, sw=2))


@art("de-nada")
def _():
    return person(skin=SKIN2, shirt=YELLOW, hair_style="long", hair_color=BLACK,
                  extra_front=hand(80, 62, 0.5, rot=20)) + bubble(2, 6, 34, 22) + heart(19, 17, 6, RED, sw=2)


@art("hasta-luego")
def _():
    return path("M10 92 Q50 70 90 92", LGREEN) + person(56, 22, 0.6, shirt=ORANGE, hair_style="short", hair_color=BLACK,
                                                        extra_front=hand(84, 56, 0.6, rot=14)) + \
        arrow(22, 74, 6, 74) + motion(84, 10, 2, 7, 7)


@art("nombre")
def _():
    return rect(10, 22, 80, 56, WHITE, rx=10) + path("M10 40 V32 Q10 22 20 22 H80 Q90 22 90 32 V40Z", RED) + \
        text(50, 36, "HOLA", 13, WHITE) + path("M22 62 q6 -10 12 0 t12 0 t12 0 t12 0", stroke=BLUE, sw=3)


# ── La familia ──

@art("hijo")
def _():
    return person(30, 10, 0.75, shirt=PINK, hair_style="long", hair_color=DBROWN) + \
        person(68, 40, 0.55, shirt=GREEN, hair_style="spiky", hair_color=DBROWN)


@art("hija")
def _():
    return person(30, 10, 0.75, skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=BLACK, mustache=True) + \
        person(68, 40, 0.55, skin=SKIN2, shirt=PINK, hair_style="pigtails", hair_color=BLACK)


@art("tio")
def _():
    return person(skin=SKIN2, shirt=GREEN, hair_style="short", hair_color=BLACK, mustache=True,
                  extra_front=hat("straw", 50, 24))


@art("tia")
def _():
    return person(shirt=ORANGE, hair_style="long", hair_color=BROWN,
                  extra_front=circle(31, 50, 3, GOLD, sw=1.6) + circle(69, 50, 3, GOLD, sw=1.6) + path("M36 72 Q50 82 64 72", stroke=RED, sw=3))


@art("primo")
def _():
    return person(skin=SKIN3, shirt=RED, hair_style="spiky", hair_color=BLACK, extra_front=hat("cap", 50, 26))


@art("prima")
def _():
    return person(shirt=LPURPLE, hair_style="pigtails", hair_color=ORANGE,
                  extra_front=path("M34 34 Q50 24 66 34", stroke=PINK, sw=3.6))


@art("esposo")
def _():
    return person(skin=SKIN2, shirt=NAVY, hair_style="short", hair_color=DBROWN,
                  extra_front=path("M44 66 L50 76 L56 66Z", WHITE, sw=2) + path("M46 70 L50 74 L54 70 L54 78 L50 74 L46 78Z", BLACK, sw=1.6)) + \
        circle(84, 22, 8, "none", stroke=GOLD, sw=3.2) + sparkle(90, 12, 4)


@art("esposa")
def _():
    return person(shirt=WHITE, hair_style="long", hair_color=DBROWN,
                  extra_front=path("M32 30 Q50 18 68 30", stroke=WHITE, sw=4) + circle(36, 28, 3, PINK, sw=1.4) + circle(64, 28, 3, PINK, sw=1.4)) + \
        circle(84, 22, 8, "none", stroke=GOLD, sw=3.2) + sparkle(90, 12, 4)


# ── El mercado ──

@art("manzana")
def _():
    return path("M50 32 C34 20 14 32 18 56 C22 78 38 90 50 84 C62 90 78 78 82 56 C86 32 66 20 50 32Z", RED) + \
        path("M50 32 Q50 20 56 12", stroke=DBROWN, sw=3.6) + path("M54 22 Q66 10 76 18 Q66 28 54 22Z", GREEN) + \
        path("M30 44 q4 -8 12 -8", stroke="#FF9A8F", sw=4)


@art("naranja")
def _():
    dots = "".join(dot(x, y, 1.4, "#E07B00") for x, y in [(36, 50), (60, 44), (52, 66), (68, 62), (40, 70), (46, 40)])
    return circle(50, 56, 32, ORANGE) + dots + path("M50 24 Q48 16 52 12", stroke=DBROWN, sw=3.4) + \
        path("M52 22 Q64 10 74 16 Q66 26 52 22Z", GREEN) + path("M30 46 q4 -8 12 -10", stroke=LYELLOW, sw=4)


@art("papa-tuberculo")
def _():
    return path("M22 50 C20 30 44 22 62 28 C82 34 86 54 78 68 C70 82 42 84 30 74 C22 68 22 60 22 50Z", TAN) + \
        "".join(path(f"M{x} {y} q2 -2 4 0", stroke=BROWN, sw=2.4) for x, y in [(36, 42), (58, 38), (66, 58), (44, 64), (32, 58)]) + \
        path("M30 44 q4 -8 14 -10", stroke=CREAM, sw=3.6)


@art("zanahoria")
def _():
    return path("M38 30 L70 34 Q64 60 32 92 Q26 60 38 30Z", ORANGE) + \
        path("M42 44 l8 2 M38 58 l8 2 M36 72 l6 2", stroke="#C96A00", sw=2.6) + \
        path("M50 30 Q40 14 34 8 M54 30 Q56 12 62 6 M58 32 Q70 18 80 14", stroke=GREEN, sw=4.2)


@art("fresa")
def _():
    seeds = "".join(path(f"M{x} {y} l0 3", stroke=LYELLOW, sw=2.4) for x, y in [(40, 44), (56, 42), (48, 56), (64, 54), (38, 62), (54, 68), (46, 76)])
    return path("M50 88 C30 76 18 54 24 40 C30 28 70 28 76 40 C82 54 70 76 50 88Z", RED) + seeds + \
        path("M30 36 L38 26 L44 32 L50 22 L56 32 L62 26 L70 36 Q50 44 30 36Z", GREEN) + path("M50 22 V12", stroke=GREEN, sw=3.6)


@art("pina")
def _():
    grid = "".join(path(f"M{x - 4} {y} l4 -4 l4 4", stroke="#C98A00", sw=2) for x, y in
                   [(40, 50), (50, 50), (60, 50), (35, 62), (45, 62), (55, 62), (65, 62), (40, 74), (50, 74), (60, 74), (45, 85), (55, 85)])
    return ellipse(50, 64, 24, 30, YELLOW) + grid + \
        path("M50 36 L38 10 L48 20 L50 4 L54 20 L64 10Z", GREEN)


@art("uva")
def _():
    pos = [(36, 38), (50, 38), (64, 38), (43, 51), (57, 51), (36, 64), (50, 64), (64, 64), (43, 77), (57, 77), (50, 88)]
    grapes = "".join(circle(x, y, 8, PURPLE) + circle(x - 2.5, y - 2.5, 2, LPURPLE, stroke=False) for x, y in pos)
    return path("M50 30 Q52 18 58 12", stroke=DBROWN, sw=3.6) + path("M56 20 Q72 10 80 22 Q66 30 56 20Z", GREEN) + grapes


@art("lechuga")
def _():
    return circle(50, 58, 32, LGREEN) + path("M22 58 Q30 40 50 42 Q70 40 78 58", GREEN, sw=3) + \
        path("M30 68 Q40 50 50 52 Q60 50 70 68", "#7CCB5A", sw=3) + path("M50 52 V86 M40 60 L50 72 M60 60 L50 72", stroke=DGREEN, sw=2.4)


# ── La taquería ──

@art("pollo")
def _():
    return path("M32 50 C30 36 40 26 52 26 C68 26 74 40 72 52 C70 64 58 70 46 68 C38 66 34 60 32 50Z", "#D98A3A") + \
        rect(66, 58, 8, 24, CREAM, rx=4, rot=-30) + circle(80, 80, 5, CREAM) + circle(76, 84, 5, CREAM) + \
        path("M40 38 q6 -6 14 -6", stroke=LYELLOW, sw=3.6)


@art("cerdo")
def _():
    return circle(50, 54, 30, LPINK) + path("M26 34 L22 16 L38 28Z", LPINK) + path("M74 34 L78 16 L62 28Z", LPINK) + \
        ellipse(50, 62, 13, 9, PINK) + dot(45, 62, 2.2) + dot(55, 62, 2.2) + dot(38, 46, 2.6) + dot(62, 46, 2.6)


@art("huevo")
def _():
    return path("M10 60 C10 44 30 34 50 36 C74 34 92 46 90 62 C88 78 66 84 50 82 C30 84 10 76 10 60Z", WHITE) + \
        circle(50, 58, 15, YELLOW) + path("M44 52 q3 -4 8 -4", stroke=WHITE, sw=3)


@art("arroz")
def _():
    grains = "".join(ellipse(x, y, 4, 2, WHITE, rot=20, sw=1.6) for x, y in
                     [(36, 46), (46, 42), (56, 44), (66, 48), (42, 52), (52, 50), (62, 54), (32, 54)])
    return bowl(50, 56, 70, RED, CREAM, 28) + grains + path("M24 70 h52", stroke=WHITE, sw=3)


@art("cilantro")
def _():
    leaf = lambda x, y, r: group(f"translate({x} {y}) rotate({r})",
                                 path("M0 0 C-10 -4 -12 -16 -4 -20 C0 -26 8 -22 8 -14 C14 -12 12 -2 0 0Z", GREEN, sw=2.4))
    return path("M50 92 L50 50 M50 70 L32 48 M50 64 L70 40 M50 54 L44 30", stroke=DGREEN, sw=3) + \
        leaf(32, 48, -30) + leaf(70, 40, 30) + leaf(44, 30, 0) + leaf(50, 50, 10) + leaf(26, 66, -60) + leaf(74, 62, 60)


@art("tostada")
def _():
    return ellipse(50, 60, 40, 16, GOLD) + path("M18 54 Q50 40 82 54 Q50 62 18 54Z", "#C9662F", sw=2.4) + \
        path("M24 50 Q50 36 76 50", LGREEN, sw=2.4) + circle(38, 46, 4, RED, sw=1.6) + circle(58, 44, 4, RED, sw=1.6) + \
        ellipse(48, 42, 6, 3, WHITE, sw=1.6)


@art("cerveza")
def _():
    return path("M28 30 H64 V86 Q64 90 60 90 H32 Q28 90 28 86Z", GOLD) + path("M64 42 H74 Q82 42 82 50 V64 Q82 72 74 72 H64", sw=4) + \
        path("M24 30 Q24 16 36 18 Q42 10 52 16 Q64 12 68 24 Q72 30 64 32 H28 Q22 32 24 30Z", WHITE) + \
        circle(40, 52, 2.4, WHITE, sw=1.4) + circle(50, 66, 2, WHITE, sw=1.4) + circle(44, 76, 2.4, WHITE, sw=1.4)


@art("servilleta")
def _():
    return poly([(16, 30), (84, 30), (70, 78), (30, 78)], WHITE) + path("M16 30 L50 54 L84 30", sw=2.4) + \
        path("M30 40 h8 M60 40 h8", stroke=PINK, sw=3) + rect(40, 60, 20, 8, PINK, rx=3)


# ── Los números ──

@art("cuatro")
def _():
    return number("4", ORANGE)


@art("cinco")
def _():
    return number("5", GREEN)


@art("seis")
def _():
    return number("6", PURPLE)


@art("siete")
def _():
    return number("7", TEAL)


@art("ocho")
def _():
    return number("8", PINK)


@art("nueve")
def _():
    return number("9", NAVY)


@art("veinte")
def _():
    return number("20", DGREEN, 44)


@art("mil")
def _():
    return number("1000", DRED, 30)


# ── La casa ──

@art("mesa")
def _():
    return path("M10 44 L90 44 L82 54 L18 54Z", BROWN) + rect(20, 54, 8, 36, DBROWN, rx=2) + rect(72, 54, 8, 36, DBROWN, rx=2) + \
        path("M38 44 V34 Q38 28 44 28 H56 Q62 28 62 34 V44", LBLUE) + path("M50 28 Q46 18 52 12", stroke=GREEN, sw=3) + circle(52, 12, 5, PINK, sw=2)


@art("refrigerador")
def _():
    return rect(26, 8, 48, 86, LGREY, rx=8) + line(26, 38, 74, 38) + rect(64, 18, 4, 14, DGREY, rx=2) + rect(64, 46, 4, 20, DGREY, rx=2) + \
        rect(34, 50, 12, 10, YELLOW, rx=2, rot=-8, sw=2) + circle(40, 22, 4, RED, sw=1.8)


@art("lampara")
def _():
    return path("M30 50 L40 16 H60 L70 50Z", YELLOW) + rect(46, 50, 8, 32, DGREY) + ellipse(50, 86, 20, 6, DGREY) + \
        path("M24 60 l-8 6 M76 60 l8 6 M50 58 v4", stroke=ORANGE, sw=3)


@art("jardin")
def _():
    flower = lambda x, c: path(f"M{x} 86 V60", stroke=DGREEN, sw=3) + "".join(circle(x + dx, 54 + dy, 6, c, sw=2) for dx, dy in [(-6, 0), (6, 0), (0, -6), (0, 6)]) + circle(x, 54, 4, YELLOW, sw=1.8)
    return rect(4, 82, 92, 14, GREEN, rx=4) + path("M6 82 V48 M18 82 V48 M82 82 V48 M94 82 V48 M2 56 H24 M78 56 H98", stroke=BROWN, sw=3.6) + \
        flower(36, PINK) + flower(52, RED) + flower(66, PURPLE) + circle(80, 20, 10, YELLOW)


@art("escalera")
def _():
    return path("M10 90 V74 H28 V58 H46 V42 H64 V26 H82 V10 H92 V90Z", TAN) + \
        path("M10 74 H28 M28 58 H46 M46 42 H64 M64 26 H82", stroke=BROWN, sw=2.4) + path("M14 66 L86 2", stroke=DBROWN, sw=3.6)


@art("television")
def _():
    return rect(12, 22, 76, 54, BLACK, rx=8) + rect(18, 28, 64, 42, LBLUE, rx=4) + path("M18 58 L36 44 L50 56 L62 46 L82 62 V70 H18Z", GREEN, sw=2) + \
        circle(68, 38, 5, YELLOW, sw=2) + path("M40 76 L34 90 M60 76 L66 90 M28 90 H72", sw=3.6) + path("M40 22 L30 8 M60 22 L70 8", sw=3)


@art("espejo")
def _():
    return ellipse(50, 50, 30, 40, GOLD) + ellipse(50, 50, 23, 33, LBLUE) + path("M36 32 L44 24 M36 44 L54 26", stroke=WHITE, sw=3.6) + \
        rect(40, 88, 20, 8, GOLD, rx=3)


@art("regadera")
def _():
    drops = "".join(path(f"M{x} {y} q-2 4 0 6 q2 -2 0 -6z", BLUE, sw=1.6) for x, y in [(30, 48), (44, 54), (58, 50), (36, 68), (52, 72), (64, 64), (44, 84)])
    return path("M84 96 V18 Q84 8 74 8 H56 V18", sw=4.4) + path("M40 18 H72 L66 32 H46Z", LGREY) + drops


# ── La ropa ──

@art("falda")
def _():
    return rect(32, 22, 36, 10, PINK, rx=3) + path("M32 32 H68 L84 82 Q50 90 16 82Z", PINK) + \
        path("M40 32 L32 84 M50 32 V87 M60 32 L68 84", stroke="#E0558E", sw=2.4)


@art("vestido")
def _():
    return path("M38 10 L36 30 Q30 34 32 44 L18 88 Q50 96 82 88 L68 44 Q70 34 64 30 L62 10", RED) + \
        path("M38 10 Q50 22 62 10", sw=3) + path("M32 44 H68", stroke=WHITE, sw=3.6) + \
        circle(40, 66, 3, WHITE, stroke=False) + circle(56, 74, 3, WHITE, stroke=False) + circle(62, 60, 3, WHITE, stroke=False) + circle(34, 80, 3, WHITE, stroke=False)


@art("playera")
def _():
    return path("M34 14 L10 28 L20 46 L30 40 V88 H70 V40 L80 46 L90 28 L66 14 Q50 26 34 14Z", TEAL) + \
        star(50, 56, 12, YELLOW, sw=2)


@art("chamarra")
def _():
    return path("M34 12 L12 26 L14 88 H34 V40 L36 88 H64 L66 40 V88 H86 L88 26 L66 12 L50 26Z", BROWN) + \
        path("M50 26 V88", sw=3) + path("M34 12 L44 34 L50 26 L56 34 L66 12", "#C7854E") + \
        rect(38, 60, 8, 10, DBROWN, rx=2, sw=2) + rect(54, 60, 8, 10, DBROWN, rx=2, sw=2)


@art("calcetines")
def _():
    sock = lambda x, c: path(f"M{x} 10 H{x + 20} V58 L{x + 34} 72 Q{x + 38} 84 {x + 26} 88 L{x + 4} 70 Q{x} 66 {x} 60Z", c) + \
        path(f"M{x} 20 H{x + 20} M{x} 28 H{x + 20}", stroke=WHITE, sw=3)
    return sock(14, RED) + sock(50, BLUE)


@art("negro")
def _():
    return splash(BLACK, DGREY)


@art("amarillo")
def _():
    return splash(YELLOW, LYELLOW)


@art("rosa")
def _():
    return splash(PINK, LPINK)


# ── El clima ──

@art("viento")
def _():
    return path("M10 34 H60 Q74 34 74 22 Q74 12 64 12 Q56 12 56 20", stroke=LBLUE, sw=6) + \
        path("M10 54 H78 Q90 54 90 66 Q90 78 78 78 Q70 78 70 70", stroke=BLUE, sw=6) + path("M20 72 H50", stroke=LBLUE, sw=6) + \
        path("M10 34 H60 Q74 34 74 22 Q74 12 64 12 Q56 12 56 20", stroke=WHITE, sw=2) + ellipse(30, 86, 6, 3, GREEN, rot=-20, sw=2)


@art("nube")
def _():
    return path("M22 72 Q8 72 8 58 Q8 44 24 44 Q24 24 44 24 Q58 24 62 36 Q66 30 74 30 Q88 30 88 46 Q96 50 94 62 Q92 72 80 72Z", WHITE) + \
        path("M28 60 q10 6 20 0", stroke=LGREY, sw=3)


@art("nieve")
def _():
    flake = lambda x, y, r: "".join(path(f"M{x} {y} l{round(r * c, 2)} {round(r * s, 2)}", stroke=LBLUE, sw=3.4)
                                     for c, s in [(1, 0), (-1, 0), (0.5, 0.87), (-0.5, 0.87), (0.5, -0.87), (-0.5, -0.87)])
    return flake(50, 46, 26) + circle(50, 46, 5, WHITE, sw=2) + flake(18, 82, 9) + flake(84, 80, 11) + flake(82, 16, 7)


@art("arcoiris")
def _():
    cols = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    bands = "".join(path(f"M{10 + i * 5} 76 A{40 - i * 5} {40 - i * 5} 0 0 1 {90 - i * 5} 76", stroke=c, sw=5.4) for i, c in enumerate(cols))
    return bands + path("M2 80 Q2 70 12 70 Q16 62 24 66 Q30 70 26 80Z", WHITE) + path("M74 80 Q72 70 82 70 Q88 62 94 68 Q100 74 96 80Z", WHITE)


@art("lunes")
def _():
    return day("LUN", BLUE, (0,))


@art("viernes")
def _():
    return day("VIE", PURPLE, (4,), PINK)


@art("sabado")
def _():
    return day("SÁB", ORANGE, (5,), LYELLOW)


@art("domingo")
def _():
    return day("DOM", RED, (6,), LGREEN)


# ── En la escuela ──

@art("escuela")
def _():
    return rect(14, 40, 72, 50, ORANGE) + poly([(8, 42), (50, 18), (92, 42)], RED) + rect(42, 64, 16, 26, BROWN) + \
        building_windows(20, 50, 2, 1, 14, 12, 34) + circle(50, 32, 6, WHITE, sw=2) + path("M50 29 V32 H53", sw=1.8) + \
        path("M50 18 V6", sw=2.4) + path("M50 6 H62 V12 H50", GREEN, sw=2)


@art("maestro")
def _():
    return rect(4, 14, 40, 28, DGREEN, rx=3) + text(24, 34, "a b", 13, WHITE) + \
        person(62, 18, 0.82, skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=BLACK, glasses=True, mustache=True,
               extra_front=path("M20 62 L4 30", stroke=DBROWN, sw=3))


@art("alumno")
def _():
    return person(shirt=RED, hair_style="spiky", hair_color=DBROWN,
                  extra_front=rect(24, 70, 10, 30, YELLOW, rx=3) + rect(66, 70, 10, 30, YELLOW, rx=3) + path("M34 72 L42 66 M66 72 L58 66", sw=3)) + \
        hand(84, 30, 0.42, rot=10)


@art("cuaderno")
def _():
    rings = "".join(circle(28, y, 3, WHITE, sw=2) for y in range(22, 84, 12))
    return rect(26, 12, 52, 78, BLUE, rx=5) + rect(34, 12, 44, 78, LBLUE, rx=3, sw=2) + rings + rect(42, 30, 28, 12, WHITE, rx=2, sw=2)


@art("lapiz")
def _():
    return group("rotate(-40 50 50)", rect(10, 40, 64, 20, YELLOW) + rect(6, 40, 10, 20, PINK, rx=3) + rect(16, 40, 6, 20, LGREY) +
                 poly([(74, 40), (92, 50), (74, 60)], TAN) + poly([(86, 47), (92, 50), (86, 53)], INK, sw=1.4) +
                 path("M22 47 H74 M22 53 H74", stroke=GOLD, sw=2))


@art("pluma")
def _():
    return group("rotate(-40 50 50)", rect(12, 42, 62, 16, BLUE, rx=6) + rect(16, 38, 30, 4, NAVY, rx=2, sw=2) +
                 path("M74 44 L90 50 L74 56Z", LGREY) + dot(88, 50, 1.6)) + path("M20 86 q8 -8 16 0 t16 0", stroke=BLUE, sw=3)


@art("pizarron")
def _():
    return rect(8, 14, 84, 62, BROWN, rx=4) + rect(14, 20, 72, 50, DGREEN, rx=2) + text(50, 46, "2+2=4", 16, WHITE) + \
        path("M24 58 q10 -6 22 0", stroke=WHITE, sw=2.4) + rect(60, 70, 14, 6, WHITE, rx=2, sw=1.8) + path("M30 76 L22 92 M70 76 L78 92", sw=3.6)


@art("clase")
def _():
    desk = lambda x: rect(x, 76, 26, 6, BROWN, rx=2, sw=2.4) + path(f"M{x + 4} 82 v12 M{x + 22} 82 v12", sw=2.4)
    return rect(20, 6, 60, 26, DGREEN, rx=3) + text(50, 25, "¡Hola!", 13, WHITE) + \
        person(26, 44, 0.42, shirt=RED, hair_style="pigtails", hair_color=DBROWN) + person(74, 44, 0.42, skin=SKIN2, shirt=BLUE, hair_style="spiky", hair_color=BLACK) + \
        desk(12) + desk(62)


@art("examen")
def _():
    return paper(22, 10, 56, 80, lines=4) + check(36, 40, 6) + check(36, 58, 6) + cross(36, 76, 6) + \
        text(66, 34, "A", 18, RED) + circle(66, 28, 11, "none", stroke=RED, sw=2.6)


@art("tarea")
def _():
    return rect(16, 60, 68, 30, BROWN, rx=3) + paper(26, 14, 44, 52, lines=3) + \
        group("rotate(-30 70 40)", rect(60, 36, 34, 9, YELLOW, rx=1) + poly([(94, 36), (102, 40.5), (94, 45)], TAN, sw=2)) + \
        circle(84, 18, 8, LYELLOW) + path("M84 13 V18 H88", sw=2)


@art("goma")
def _():
    return group("rotate(-20 50 50)", rect(18, 36, 64, 30, PINK, rx=6) + rect(18, 36, 26, 30, BLUE, rx=6) + rect(38, 36, 6, 30, BLUE, stroke=False) +
                 line(44, 36, 44, 66)) + path("M18 82 q6 4 12 0 M36 86 q6 4 12 0", stroke=LGREY, sw=3)


@art("tijeras")
def _():
    return circle(30, 74, 11, RED) + circle(30, 74, 5, CREAM, sw=2) + circle(70, 74, 11, RED) + circle(70, 74, 5, CREAM, sw=2) + \
        path("M36 64 L66 12 L58 10 Z", LGREY) + path("M64 64 L34 12 L42 10 Z", LGREY) + dot(50, 40, 2.6)


@art("regla")
def _():
    ticks = "".join(line(18 + i * 8, 40, 18 + i * 8, 40 + (12 if i % 2 == 0 else 7), sw=2.2) for i in range(9))
    return group("rotate(-15 50 50)", rect(10, 38, 80, 24, YELLOW, rx=3) + ticks)


@art("salon")
def _():
    desk = lambda x, y: rect(x, y, 20, 10, TAN, rx=2, sw=2.4) + path(f"M{x + 3} {y + 10} v8 M{x + 17} {y + 10} v8", sw=2.2)
    return rect(6, 8, 88, 84, CREAM, rx=6) + rect(20, 14, 60, 24, DGREEN, rx=3) + text(50, 31, "a b c", 12, WHITE) + \
        desk(14, 50) + desk(40, 50) + desk(66, 50) + desk(14, 72) + desk(40, 72) + desk(66, 72)


@art("recreo")
def _():
    return rect(0, 76, 100, 24, LGREEN, stroke=False) + line(0, 76, 100, 76) + \
        person(30, 34, 0.52, shirt=ORANGE, hair_style="pigtails", hair_color=DBROWN) + person(72, 30, 0.52, skin=SKIN2, shirt=BLUE, hair_style="spiky", hair_color=BLACK) + \
        circle(52, 20, 9, RED) + path("M44 18 Q52 24 60 18", stroke=WHITE, sw=2) + motion(38, 8, 2, 6, 6)


@art("universidad")
def _():
    cols = "".join(rect(x, 44, 8, 36, WHITE, sw=2.4) for x in (22, 38, 54, 70))
    return poly([(10, 40), (50, 14), (90, 40)], LGREY) + rect(14, 40, 72, 6, LGREY) + cols + rect(10, 80, 80, 10, LGREY) + \
        hat("grad", 50, 30)


# ── Verbos de todos los días ──

@art("hablar")
def _():
    return person(shirt=ORANGE, hair_style="long", hair_color=DBROWN) + bubble(66, 6, 32, 22) + \
        path("M72 17 h20", stroke=GREY, sw=3) + ellipse(50, 52, 4, 3.4, DBROWN, sw=1.8)


@art("escuchar")
def _():
    return person(skin=SKIN2, shirt=GREEN, hair_style="short", hair_color=BLACK, extra_front=hand(24, 54, 0.4, rot=-30)) + \
        path("M82 24 q6 8 0 16 M90 18 q10 14 0 28", sw=3) + circle(76, 32, 4, BLUE, sw=2)


@art("leer")
def _():
    return person(shirt=PURPLE, hair_style="bun", hair_color=DBROWN, glasses=True, mood="neutral",
                  extra_front=path("M20 72 L50 80 L80 72 L80 96 L50 104 L20 96Z", WHITE) + path("M50 80 V104", sw=2.4) +
                  path("M26 82 l18 4 M56 86 l18 -4", stroke=LGREY, sw=2.4))


@art("escribir")
def _():
    return paper(14, 18, 56, 72, lines=4) + group("rotate(35 70 50)", rect(64, 14, 12, 54, BLUE, rx=4) + poly([(64, 68), (70, 82), (76, 68)], LGREY)) + \
        path("M24 80 q5 -6 10 0 t10 0", stroke=BLUE, sw=2.6)


@art("beber")
def _():
    return person(skin=SKIN2, shirt=RED, hair_style="short", hair_color=DBROWN,
                  extra_front=group("rotate(-25 66 56)", path("M58 46 H76 L73 76 H61Z", LBLUE) + path("M59 56 H75", stroke=BLUE, sw=4)))


@art("correr")
def _():
    return circle(56, 18, 11, SKIN) + path("M30 18 Q44 2 62 10", DBROWN, sw=2.6) + \
        path("M54 30 L46 56", stroke=ORANGE, sw=12) + path("M46 56 L30 70 L22 64 M46 56 L60 72 L56 88", sw=5) + \
        path("M52 36 L36 42 M52 36 L68 46", sw=5) + motion(6, 36, 3, 8, 12)


@art("saltar")
def _():
    return ellipse(50, 92, 22, 4, LGREY, stroke=False) + circle(50, 22, 11, SKIN) + path("M50 33 V58", stroke=GREEN, sw=12) + \
        path("M50 38 L32 22 M50 38 L68 22", sw=5) + path("M50 58 L38 72 L44 80 M50 58 L62 72 L56 80", sw=5) + \
        path("M30 86 q6 -6 12 0 M58 86 q6 -6 12 0", sw=2.4)


@art("cantar")
def _():
    return person(shirt=PINK, hair_style="long", hair_color=BLACK, extra_front=ellipse(50, 52, 4.6, 5, DBROWN, sw=1.8)) + \
        path("M80 34 V14 L92 10 V30", sw=3) + circle(77, 34, 4, INK, stroke=False) + circle(89, 30, 4, INK, stroke=False) + \
        path("M12 22 V8", sw=3) + circle(9, 22, 3.4, INK, stroke=False)


@art("bailar")
def _():
    return circle(50, 18, 11, SKIN) + path("M38 18 Q42 2 58 6 Q66 10 62 18", DBROWN, sw=2.4) + \
        path("M50 30 L44 54", stroke=RED, sw=10) + path("M44 54 L22 90 Q50 96 74 86Z", RED) + \
        path("M48 36 L70 22 M48 36 L28 44", sw=5) + path("M84 14 V30", sw=2.6) + circle(81, 30, 3.4, INK, stroke=False) + \
        path("M14 64 q-6 -6 0 -12", sw=2.4)


@art("jugar")
def _():
    return rect(16, 36, 68, 34, DGREY, rx=16) + path("M30 46 v14 M23 53 h14", stroke=WHITE, sw=4) + \
        circle(64, 48, 4, RED, sw=1.8) + circle(72, 56, 4, BLUE, sw=1.8) + circle(56, 56, 4, YELLOW, sw=1.8) + circle(64, 62, 3, GREEN, stroke=False)


@art("comprar")
def _():
    return path("M10 22 H22 L32 66 H78 L86 34 H26", sw=3.6) + path("M28 34 H86 L78 66 H32Z", LGREY, sw=2.4) + \
        circle(38, 80, 6, DGREY) + circle(72, 80, 6, DGREY) + rect(38, 22, 16, 16, ORANGE, rx=2, sw=2.4) + circle(64, 26, 8, RED, sw=2.4)


@art("abrir")
def _():
    return rect(26, 10, 48, 82, BROWN, rx=3) + path("M26 10 L58 18 V98 L26 92Z", "#C7854E") + circle(50, 56, 3, GOLD, sw=1.6) + \
        path("M74 30 L90 24 M74 50 H94 M74 70 L90 76", stroke=YELLOW, sw=3.6)


@art("cerrar")
def _():
    return rect(26, 10, 48, 82, BROWN, rx=3) + rect(32, 16, 36, 30, "#C7854E", rx=2, sw=2.4) + rect(32, 54, 36, 32, "#C7854E", rx=2, sw=2.4) + \
        circle(64, 52, 3, GOLD, sw=1.6) + rect(76, 60, 18, 16, GOLD, rx=3) + path("M79 60 V54 Q85 46 91 54 V60", sw=3)


@art("mirar")
def _():
    return ellipse(50, 50, 42, 26, WHITE) + circle(50, 50, 18, BLUE) + circle(50, 50, 9, INK) + circle(44, 44, 4, WHITE, stroke=False) + \
        path("M14 30 L8 22 M30 22 L28 12 M50 20 V10 M70 22 L72 12 M86 30 L92 22", sw=3)


@art("llorar")
def _():
    return face(50, 50, 38, skin="#BFD8FF", mood="sad") + path("M30 52 q-4 12 0 22 q4 -6 0 -22z", BLUE, sw=2) + \
        path("M70 52 q-4 12 0 22 q4 -6 0 -22z", BLUE, sw=2)


@art("reir")
def _():
    return face(50, 52, 38, mood="starry", skin=SKIN) + path("M10 20 l8 6 M90 20 l-8 6 M6 40 h8 M94 40 h-8", sw=3) + \
        text(84, 88, "ja", 14, ORANGE)


# ── Las bebidas ──

def glass(fill, x=34, w=32, top=24, bottom=86):
    return path(f"M{x} {top} H{x + w} L{x + w - 4} {bottom} H{x + 4}Z", WHITE) + \
        path(f"M{x + 1.4} {top + 14} H{x + w - 1.4} L{x + w - 4} {bottom - 1.6} H{x + 4}Z", fill, sw=2)


@art("jugo")
def _():
    return glass(ORANGE) + path("M60 30 L72 6", stroke=RED, sw=4) + circle(68, 26, 12, ORANGE) + circle(68, 26, 8, LYELLOW, sw=2) + \
        path("M68 18 V34 M60 26 H76", stroke=ORANGE, sw=1.8)


@art("leche")
def _():
    return path("M30 34 L40 18 H60 L70 34 V88 H30Z", WHITE) + path("M40 18 V10 H60 V18", sw=3.2) + rect(30, 46, 40, 24, LBLUE, sw=2.4) + \
        path("M38 58 q6 -8 12 0 t12 0", stroke=WHITE, sw=3)


@art("te")
def _():
    return path("M22 40 H70 V60 Q70 82 46 82 Q22 82 22 60Z", GREEN) + path("M70 46 Q84 46 84 58 Q84 68 70 66", sw=3.6) + \
        path("M44 40 V22", sw=2) + rect(40, 14, 10, 10, YELLOW, rx=2, sw=2) + ellipse(46, 90, 34, 5, LGREY) + steam(34, 34, 2, 22)


@art("cafe-de-olla")
def _():
    return path("M24 40 Q22 82 50 84 Q78 82 76 40Z", "#C9662F") + ellipse(50, 40, 26, 7, DBROWN) + \
        path("M24 50 Q16 50 16 58 Q16 66 26 66 M76 50 Q84 50 84 58 Q84 66 74 66", sw=3.4) + \
        path("M30 58 q10 6 20 0 t20 0", stroke=CREAM, sw=2.6) + rect(60, 14, 6, 34, "#B5652F", rx=3, rot=25, sw=2) + steam(36, 28, 2, 14)


@art("chocolate")
def _():
    return path("M24 34 H72 V70 Q72 86 48 86 Q24 86 24 70Z", WHITE) + ellipse(48, 34, 24, 6, DBROWN) + \
        path("M72 42 Q86 42 86 54 Q86 66 72 64", sw=3.6) + path("M30 58 h36 M30 66 h36", stroke=BROWN, sw=3) + steam(38, 24, 2, 14)


@art("agua-de-jamaica")
def _():
    return path("M28 18 H72 L68 88 H32Z", WHITE) + path("M29.4 30 H70.6 L68 86.4 H32Z", "#B0174F", sw=2) + \
        rect(36, 36, 9, 9, WHITE, rx=2, rot=15, sw=1.8, extra='opacity="0.8"') + rect(52, 46, 9, 9, WHITE, rx=2, rot=-10, sw=1.8, extra='opacity="0.8"') + \
        path("M78 26 C70 18 82 8 86 18 C92 10 98 22 88 26 C96 32 86 40 82 32 C76 40 68 32 78 26Z", "#D1245E", sw=2)


@art("limonada")
def _():
    return glass(LGREEN) + circle(66, 24, 12, "#C8E86B") + circle(66, 24, 8, LYELLOW, sw=2) + \
        path("M66 16 V32 M58 24 H74", stroke=LGREEN, sw=1.8) + path("M44 30 L38 6", stroke=PINK, sw=4)


@art("licuado")
def _():
    return path("M30 30 H70 L64 88 H36Z", WHITE) + path("M31.4 42 H68.6 L64 86.4 H36Z", PINK, sw=2) + \
        path("M28 30 Q34 18 50 22 Q66 18 72 30Z", LPINK) + path("M56 24 L66 4", stroke=BLUE, sw=4) + \
        path("M34 20 C34 12 44 12 42 22", fill=YELLOW, sw=2) + circle(40, 54, 2, WHITE, stroke=False) + circle(54, 66, 2, WHITE, stroke=False)


@art("mezcal")
def _():
    return path("M38 8 H62 V20 Q74 28 74 44 V88 Q74 92 70 92 H30 Q26 92 26 88 V44 Q26 28 38 20Z", "#E8F0C8") + \
        rect(38, 4, 24, 8, BROWN, rx=2) + rect(30, 50, 40, 26, ORANGE, rx=3, sw=2.4) + \
        path("M38 70 L42 58 L46 66 L50 56 L54 66 L58 58 L62 70Z", GREEN, sw=1.8)


@art("tequila")
def _():
    return path("M28 34 H52 L48 82 H32Z", WHITE) + path("M29.2 44 H50.8 L48 80.4 H32Z", GOLD, sw=2) + \
        circle(70, 62, 14, "#C8E86B") + circle(70, 62, 10, LYELLOW, sw=2) + path("M70 52 V72 M60 62 H80", stroke=LGREEN, sw=1.8) + \
        "".join(rect(x, 22, 4, 4, WHITE, sw=1.4) for x in (60, 68, 76))


@art("michelada")
def _():
    rim = "".join(dot(x, 22, 1.6, RED) for x in range(30, 72, 5))
    return path("M28 20 H72 L66 88 H34Z", WHITE) + path("M29.6 32 H70.4 L66 86.4 H34Z", "#C9662F", sw=2) + rim + \
        circle(72, 24, 10, "#C8E86B") + circle(72, 24, 6, LYELLOW, sw=1.8)


@art("pulque")
def _():
    return path("M22 34 Q20 82 50 84 Q80 82 78 34Z", "#C9662F") + ellipse(50, 34, 28, 8, WHITE) + \
        path("M26 52 l6 10 l6 -10 l6 10 l6 -10 l6 10 l6 -10 l6 10 l6 -10", stroke=YELLOW, sw=2.6) + \
        path("M34 30 q4 -4 8 0", stroke=CREAM, sw=2)


@art("botella")
def _():
    return path("M42 6 H58 V24 Q72 32 72 48 V88 Q72 94 66 94 H34 Q28 94 28 88 V48 Q28 32 42 24Z", LBLUE) + \
        rect(40, 2, 20, 8, BLUE, rx=2) + rect(28, 50, 44, 24, WHITE, sw=2.4) + path("M36 40 V84", stroke=WHITE, sw=3.4, extra='opacity="0.7"')


@art("taza")
def _():
    return path("M20 30 H70 V62 Q70 84 45 84 Q20 84 20 62Z", RED) + path("M70 38 Q86 38 86 52 Q86 66 70 64", sw=4) + \
        ellipse(45, 30, 25, 6, DBROWN) + heart(45, 58, 8, WHITE, sw=2) + ellipse(45, 90, 36, 5, LGREY)


@art("hielo")
def _():
    cube = lambda x, y, r: group(f"translate({x} {y}) rotate({r})", rect(-14, -14, 28, 28, LBLUE, rx=5) +
                                 path("M-8 -8 l6 -2", stroke=WHITE, sw=3))
    return cube(36, 62, -12) + cube(64, 64, 14) + cube(50, 36, 4) + sparkle(84, 20, 6, WHITE)


@art("popote")
def _():
    return glass(LBLUE) + group("rotate(20 60 40)", rect(57, 0, 7, 62, WHITE, sw=2.4) +
                                "".join(path(f"M57 {y} l7 -5", stroke=RED, sw=2.4) for y in range(10, 62, 9)))


# ── Las personas ──

@art("alto")
def _():
    return person(34, -8, 1.0, shirt=BLUE, hair_style="short", hair_color=DBROWN) + rect(72, 6, 6, 88, LGREY, sw=2) + \
        "".join(line(72, y, 78, y, sw=2) for y in range(14, 94, 10)) + arrow(88, 80, 88, 10, RED, 3)


@art("bajo")
def _():
    return person(42, 44, 0.56, shirt=ORANGE, hair_style="spiky", hair_color=BLACK) + rect(72, 6, 6, 88, LGREY, sw=2) + \
        "".join(line(72, y, 78, y, sw=2) for y in range(14, 94, 10)) + path("M64 66 H86", stroke=RED, sw=3.4)


@art("joven")
def _():
    return person(shirt=GREEN, hair_style="spiky", hair_color=ORANGE, extra_front=hat("cap", 50, 26)) + sparkle(86, 18, 6)


@art("viejo")
def _():
    return person(shirt=BROWN, hair_style="bald", hair_color=WHITE, glasses=True, mustache=True) + \
        path("M86 50 V96", stroke=DBROWN, sw=4) + path("M86 50 Q86 40 78 42", stroke=DBROWN, sw=4)


@art("delgado")
def _():
    return circle(50, 22, 13, SKIN) + path("M36 18 Q38 4 52 6 Q64 8 64 18", DBROWN, sw=2.4) + dot(45, 22) + dot(55, 22) + \
        path("M45 28 q5 4 10 0", sw=2.2) + rect(44, 36, 12, 34, TEAL, rx=4) + path("M46 70 V94 M54 70 V94", sw=5) + \
        path("M44 42 L36 62 M56 42 L64 62", sw=4) + path("M24 40 H32 M68 40 H76", stroke=RED, sw=2.6) + \
        path("M28 36 L24 40 L28 44 M72 36 L76 40 L72 44", stroke=RED, sw=2.6)


@art("pelo")
def _():
    return person(shirt=PINK, hair_style="long", hair_color=ORANGE,
                  extra_front=path("M30 50 q-6 16 2 30 M70 50 q6 16 -2 30", stroke="#E07B00", sw=2.4)) + sparkle(84, 16, 6)


@art("lentes")
def _():
    return circle(30, 52, 18, LBLUE) + circle(70, 52, 18, LBLUE) + path("M48 50 Q50 44 52 50", sw=3.6) + \
        path("M12 50 L4 40 M88 50 L96 40", sw=3.6) + path("M22 44 l6 -6 M62 44 l6 -6", stroke=WHITE, sw=3)


@art("barba")
def _():
    return person(skin=SKIN2, shirt=GREEN, hair_style="short", hair_color=DBROWN,
                  extra_front=path("M31 44 Q30 70 50 74 Q70 70 69 44 Q66 58 50 58 Q34 58 31 44Z", DBROWN, sw=2.4) +
                  path("M45 52 Q50 55 55 52", stroke=CREAM, sw=2.2))


@art("bigote")
def _():
    return path("M50 46 C40 32 22 36 16 48 C12 56 4 54 4 48 C2 60 14 66 26 62 C38 58 46 52 50 50 C54 52 62 58 74 62 "
                "C86 66 98 60 96 48 C96 54 88 56 84 48 C78 36 60 32 50 46Z", DBROWN) + path("M30 48 q8 -4 14 0", stroke=BROWN, sw=2.4)


@art("guero")
def _():
    return person(shirt=LBLUE, hair_style="short", hair_color=GOLD) + sparkle(18, 18, 6) + circle(80, 18, 8, YELLOW)


@art("moreno")
def _():
    return person(skin=SKIN3, shirt=ORANGE, hair_style="short", hair_color=BLACK)


@art("guapo")
def _():
    return person(skin=SKIN2, shirt=RED, hair_style="spiky", hair_color=BLACK) + sparkle(84, 18, 7) + sparkle(16, 30, 5) + \
        heart(82, 46, 6, PINK, sw=2)


@art("chistoso")
def _():
    return face(50, 52, 36, mood="wink") + circle(50, 58, 7, RED) + path("M22 22 l-8 -8 M78 22 l8 -8", sw=3) + text(84, 90, "ja", 14, ORANGE)


@art("serio")
def _():
    return person(shirt=NAVY, hair_style="short", hair_color=BLACK, mood="neutral",
                  extra_front=path("M38 36 L48 38 M62 36 L52 38", sw=2.6) + path("M44 66 L50 76 L56 66Z", WHITE, sw=2) +
                  path("M48 72 L50 92 L52 72Z", DRED, sw=1.8))


@art("timido")
def _():
    return face(50, 52, 36, mood="nervous", skin=SKIN) + path("M18 74 Q30 66 36 76 M82 74 Q70 66 64 76", sw=3) + \
        circle(28, 60, 6, CHEEK, stroke=False) + circle(72, 60, 6, CHEEK, stroke=False)


@art("amable")
def _():
    return person(shirt=YELLOW, hair_style="bun", hair_color=BROWN,
                  extra_front=path("M60 104 V78 Q60 70 68 72 L86 76", SKIN, sw=3) + heart(80, 58, 7, RED, sw=2))
