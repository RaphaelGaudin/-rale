"""Illustrations du niveau B2."""
from .kit import *  # noqa: F401,F403

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


# ── Sociedad y política ──

@art("elecciones")
def _():
    return rect(14, 40, 72, 52, BLUE, rx=6) + rect(14, 40, 72, 12, NAVY, rx=4) + rect(34, 44, 32, 4, BLACK, rx=2, stroke=False) + \
        rect(36, 10, 28, 36, WHITE, rx=2, rot=-6) + path("M42 26 l5 5 l10 -10", stroke=GREEN, sw=3.4) + \
        rect(40, 64, 20, 14, WHITE, rx=3, sw=2.2) + path("M44 71 h12", stroke=BLUE, sw=2.4)


@art("gobierno")
def _():
    cols = "".join(rect(24 + i * 14, 56, 7, 26, WHITE, sw=2.4) for i in range(4))
    return rect(46, 6, 3, 18, GREY, stroke=False) + path("M49 6 H66 V14 H49Z", GREEN, sw=1.8) + rect(54.6, 6, 5.6, 8, WHITE, stroke=False) + rect(60.2, 6, 5.8, 8, RED, stroke=False) + \
        path("M49 6 H66 V14 H49", sw=1.8) + path("M28 44 A20 20 0 0 1 68 44 Z", LGREY) + rect(18, 44, 60, 12, WHITE) + cols + \
        rect(12, 82, 72, 10, LGREY) + rect(8, 90, 80, 4, GREY, stroke=False)


@art("ley")
def _():
    return line(50, 14, 50, 82, sw=4) + rect(30, 82, 40, 8, GOLD, rx=3) + line(18, 26, 82, 26, sw=4) + circle(50, 14, 5, GOLD) + \
        path("M18 26 L8 54 M18 26 L28 54 M82 26 L72 54 M82 26 L92 54", sw=2) + \
        path("M6 54 H30 Q18 66 6 54Z", GOLD) + path("M70 54 H94 Q82 66 70 54Z", GOLD)


@art("ciudadano")
def _():
    return person(shirt=TEAL, hair_style="short", hair_color=DBROWN, skin=SKIN2) + \
        rect(66, 52, 28, 20, WHITE, rx=3) + circle(74, 61, 4, SKIN, sw=1.6) + path("M80 58 h10 M80 64 h8", stroke=GREY, sw=2) + \
        rect(66, 52, 28, 5, GREEN, rx=2, stroke=False)


@art("voto")
def _():
    return rect(18, 14, 64, 72, WHITE, rx=4, rot=-4) + rect(28, 26, 14, 14, WHITE, rx=2, sw=2.4) + rect(28, 48, 14, 14, WHITE, rx=2, sw=2.4) + \
        path("M30 32 l5 5 l12 -14", stroke=GREEN, sw=4) + path("M50 34 H72 M50 56 H70", stroke=GREY, sw=3) + \
        group("rotate(40 70 70)", rect(66, 50, 9, 40, ORANGE, rx=3), poly([(66, 90), (75, 90), (70.5, 99)], CREAM))


@art("marcha")
def _():
    return path("M20 40 L64 22 V82 L20 64Z", RED) + rect(8, 38, 14, 28, DGREY, rx=4) + rect(64, 18, 10, 68, RED, rx=4) + \
        path("M30 66 L38 88 H48 L42 68", fill=DGREY) + path("M82 36 q8 16 0 32 M90 28 q12 24 0 48", sw=3.4)


@art("presidenta")
def _():
    sash = path("M34 70 L66 104 L74 98 L42 66Z", GREEN, sw=2) + path("M38 68 L70 101", stroke=WHITE, sw=3.5)
    return person(shirt=NAVY, hair_style="long", hair_color=BLACK, skin=SKIN2, extra_front=path("M36 67 L68 104 L76 98 L44 64Z", GREEN, sw=2) +
                  path("M40 66 L73 102", stroke=WHITE, sw=3.4) + path("M43 64 L76 99", stroke=RED, sw=3)) + star(84, 16, 7, GOLD, sw=2)


@art("desigualdad")
def _():
    stack = lambda x, n: "".join(ellipse(x, 86 - i * 8, 14, 5, GOLD, sw=2.4) for i in range(n))
    return stack(28, 1) + stack(70, 8) + \
        path("M12 40 L44 40 M28 40 L28 30", stroke="none") + text(28, 66, "?", 22, GREY) + path("M8 94 H92", sw=3)


# ── Medio ambiente ──

@art("contaminacion")
def _():
    return rect(10, 50, 80, 42, GREY) + poly([(10, 50), (30, 38), (30, 50), (50, 38), (50, 50), (70, 38), (70, 50)], LGREY) + \
        rect(66, 18, 12, 32, DGREY) + rect(18, 64, 12, 10, LYELLOW, sw=2) + rect(38, 64, 12, 10, LYELLOW, sw=2) + rect(56, 64, 12, 10, LYELLOW, sw=2) + \
        circle(70, 12, 8, "#6B6B7B") + circle(82, 8, 7, "#6B6B7B") + circle(60, 8, 6, "#6B6B7B")


@art("reciclaje")
def _():
    arrow = lambda a: group(f"rotate({a} 50 54)", path("M36 30 L50 14 L64 30 Z", GREEN, sw=2.6), path("M50 26 L50 30 M42 30 L28 56", stroke=GREEN, sw=9))
    return "".join(group(f"rotate({a} 50 54)", path("M30 46 L44 22 L58 22", stroke=INK, sw=12), path("M30 46 L44 22 L58 22", stroke=GREEN, sw=6),
                         poly([(56, 12), (70, 22), (56, 32)], GREEN, sw=2.6)) for a in (0, 120, 240))


@art("sequia")
def _():
    return rect(4, 4, 92, 92, "#FFE3B0", rx=16, stroke=False) + circle(76, 24, 11, ORANGE) + \
        path("M4 60 H96 V96 H4Z", "#D9A066", stroke=False) + path("M4 60 H96", sw=3) + \
        path("M14 70 l10 6 l-4 10 M40 66 l6 10 l12 -2 l4 12 M70 68 l-6 10 l10 8", stroke=DBROWN, sw=2.6) + \
        path("M32 60 Q30 46 34 38", stroke=BROWN, sw=3) + path("M34 40 Q24 40 22 50 Q30 50 34 42", "#B5A05A", sw=2.2) + \
        path("M34 46 Q44 46 46 56 Q38 56 34 48", "#B5A05A", sw=2.2)


@art("energia-solar")
def _():
    grid = "".join(rect(18 + c * 17, 46 + r * 12, 15, 10, "#2F5FB5", sw=1.6) for r in range(3) for c in range(4))
    return circle(78, 18, 11, YELLOW) + "".join(group(f"rotate({a} 78 18)", line(78, 2, 78, 4, sw=3, color=ORANGE)) for a in range(0, 360, 45)) + \
        poly([(14, 44), (88, 44), (82, 84), (20, 84)], NAVY) + grid + rect(46, 84, 8, 10, GREY, stroke=False) + rect(34, 92, 32, 4, DGREY, rx=2)


@art("basura")
def _():
    return rect(40, 8, 20, 8, GREY, rx=3) + rect(16, 16, 68, 10, GREY, rx=4) + path("M22 26 H78 L72 92 H28Z", LGREY) + \
        path("M38 36 L40 82 M50 36 V82 M62 36 L60 82", stroke=GREY, sw=3)


@art("bosque")
def _():
    pine = lambda x, y, s, c: poly([(x, y - 40 * s), (x - 18 * s, y - 10 * s), (x - 8 * s, y - 10 * s), (x - 22 * s, y + 10 * s), (x + 22 * s, y + 10 * s), (x + 8 * s, y - 10 * s), (x + 18 * s, y - 10 * s)], c) + \
        rect(x - 4 * s, y + 10 * s, 8 * s, 10 * s, BROWN)
    return rect(0, 86, 100, 14, LGREEN, stroke=False) + pine(30, 56, 1.0, DGREEN) + pine(70, 60, 0.9, GREEN) + pine(50, 68, 0.7, "#2E9E5B") + path("M0 88 H100", sw=3)


@art("huracan")
def _():
    return path("M50 50 m-6 0 a6 6 0 1 1 12 0 a14 14 0 1 1 -26 4 a24 24 0 1 1 46 -8 a34 34 0 1 1 -58 18", stroke=INK, sw=11) + \
        path("M50 50 m-6 0 a6 6 0 1 1 12 0 a14 14 0 1 1 -26 4 a24 24 0 1 1 46 -8 a34 34 0 1 1 -58 18", stroke=LBLUE, sw=5) + circle(50, 50, 5, WHITE)


@art("calentamiento-global")
def _():
    return circle(44, 54, 36, BLUE) + path("M24 34 Q34 30 38 40 Q34 50 40 56 Q30 62 22 54 Q16 44 24 34Z", GREEN, sw=2.4) + \
        path("M52 64 Q62 58 70 66 Q66 78 56 82 Q48 76 52 64Z", GREEN, sw=2.4) + path("M50 22 Q60 20 64 30 Q58 36 50 32Z", GREEN, sw=2.2) + \
        rect(74, 8, 12, 52, WHITE, rx=6) + circle(80, 66, 10, RED) + rect(77.5, 20, 5, 44, RED, stroke=False)


# ── Arte y cultura ──

@art("mural")
def _():
    return rect(6, 14, 88, 72, "#F4E3C8", rx=4) + path("M6 60 Q30 40 50 56 T94 48 V86 H6Z", ORANGE, sw=2.4) + \
        circle(30, 36, 10, YELLOW, sw=2.4) + path("M50 56 Q58 30 72 30 Q80 40 72 56Z", GREEN, sw=2.4) + \
        circle(64, 70, 8, PINK, sw=2.2) + circle(22, 70, 6, BLUE, sw=2.2) + path("M6 86 H94", sw=3.2) + \
        group("rotate(30 86 18)", rect(82, 2, 6, 28, BROWN, rx=2), rect(81, 26, 8, 8, RED, rx=2))


@art("pintora")
def _():
    return path("M50 12 C20 12 8 34 12 54 C16 76 36 90 52 86 C62 84 58 72 66 68 C76 64 90 70 90 50 C90 28 74 12 50 12Z", TAN) + \
        circle(70, 58, 6, "#F4E3C8", sw=2.4) + circle(34, 30, 7, RED, sw=2.2) + circle(54, 26, 7, YELLOW, sw=2.2) + circle(72, 36, 7, BLUE, sw=2.2) + \
        circle(26, 52, 7, GREEN, sw=2.2) + circle(40, 70, 6, PURPLE, sw=2.2) + \
        group("rotate(45 60 60)", rect(56, 22, 8, 60, BROWN, rx=3), path("M56 22 Q60 6 64 22Z", RED, sw=2))


@art("artesania")
def _():
    weave = "".join(path(f"M{18 + i * 8} 46 V88", stroke=BROWN, sw=2) for i in range(9))
    return path("M24 40 Q50 4 76 40", sw=5) + path("M14 40 H86 L78 90 H22Z", "#E8B06A") + weave + \
        path("M16 52 H84 M18 64 H82 M20 76 H80", stroke=RED, sw=4) + \
        path("M14 40 H86 L78 90 H22Z", "none")


@art("alebrije")
def _():
    return path("M20 70 C10 60 14 40 30 40 C36 30 50 26 60 34 C70 26 88 30 88 46 C96 50 94 64 84 66 L80 86 H70 L68 72 H40 L36 86 H26Z", PURPLE) + \
        path("M30 40 C26 28 30 18 38 14 C38 22 40 30 44 34", ORANGE) + path("M60 34 C62 22 70 14 78 14 C76 22 72 30 68 34", YELLOW) + \
        circle(80, 46, 6, WHITE) + dot(81, 46, 2.6) + path("M88 56 l8 -2 l-6 4 l6 4", stroke=RED, sw=2.4) + \
        "".join(circle(x, y, r, c, sw=1.8) for x, y, r, c in [(36, 56, 5, YELLOW), (50, 48, 4, TEAL), (60, 58, 5, PINK), (46, 64, 3, LGREEN), (70, 50, 3.5, ORANGE)]) + \
        path("M20 70 C10 76 4 70 6 60", stroke=TEAL, sw=5)


@art("museo")
def _():
    return poly([(8, 34), (50, 10), (92, 34)], CREAM) + rect(10, 32, 80, 8, CREAM) + \
        "".join(rect(16 + i * 18, 40, 8, 38, WHITE, sw=2.4) for i in range(4)) + rect(28, 46, 44, 26, "none", stroke=False) + \
        rect(8, 78, 84, 8, CREAM) + rect(4, 86, 92, 6, LGREY) + circle(50, 24, 5, PINK, sw=2)


@art("poesia")
def _():
    return rect(16, 14, 56, 74, WHITE, rx=4, rot=-6) + path("M26 30 Q40 26 56 30 M26 42 Q38 38 50 42 M26 54 Q40 50 58 54 M26 66 Q36 62 46 66", stroke=GREY, sw=2.6) + \
        path("M88 8 C66 14 54 34 52 62 C62 50 74 44 80 30 C74 32 70 32 68 30 C76 26 82 20 88 8Z", LPURPLE) + path("M52 62 L72 24", sw=2) + \
        heart(36, 78, 5, RED, sw=2)


@art("escultura")
def _():
    return path("M22 50 C22 22 36 10 50 10 C64 10 78 22 78 50 C78 70 70 84 50 84 C30 84 22 70 22 50Z", "#8F9A8C") + \
        path("M22 34 Q50 18 78 34 L78 42 Q50 28 22 42Z", "#6F7A6C") + \
        ellipse(38, 48, 6, 3.4, "#5C665A") + ellipse(62, 48, 6, 3.4, "#5C665A") + path("M46 50 Q44 62 50 64 Q56 62 54 50", "#7F8A7C", sw=2.4) + \
        path("M38 70 Q50 76 62 70 Q50 68 38 70Z", "#5C665A", sw=2.4) + rect(26, 84, 48, 10, "#6F7A6C", rx=2)


@art("talavera")
def _():
    return path("M38 10 H62 V18 Q78 26 80 50 Q82 78 66 90 H34 Q18 78 20 50 Q22 26 38 18Z", WHITE) + \
        path("M30 40 Q50 32 70 40", stroke=BLUE, sw=3) + path("M26 70 Q50 78 74 70", stroke=BLUE, sw=3) + \
        circle(50, 56, 9, BLUE) + circle(50, 56, 3, YELLOW, sw=1.6) + \
        "".join(group(f"rotate({a} 50 56)", ellipse(50, 44, 3, 4, BLUE, sw=1.4)) for a in range(0, 360, 60)) + \
        rect(36, 10, 28, 6, BLUE, rx=2)


# ── Historia de México ──

@art("independencia")
def _():
    return rect(46, 4, 8, 10, BROWN, rx=2) + path("M30 64 C30 30 38 16 50 16 C62 16 70 30 70 64 L78 74 H22Z", GOLD) + \
        path("M38 30 Q40 22 46 20", stroke=LYELLOW, sw=3.4) + circle(50, 80, 7, DBROWN) + \
        path("M12 40 q-6 10 0 20 M88 40 q6 10 0 20", sw=3) + path("M18 46 q-3 4 0 8 M82 46 q3 4 0 8", sw=2.6)


@art("revolucion")
def _():
    belt = "".join(rect(28 + i * 7, 56 + i * 5.2, 4, 8, GOLD, rx=1, sw=1.6, rot=-55) for i in range(7))
    return ellipse(50, 30, 44, 12, "#C9A25A") + path("M30 30 C30 8 40 2 50 2 C60 2 70 8 70 30Z", "#C9A25A") + \
        path("M31 22 Q50 28 69 22", stroke=DBROWN, sw=3) + \
        path("M18 50 L82 96", stroke=INK, sw=10) + path("M18 50 L82 96", stroke=BROWN, sw=6) + belt


@art("imperio")
def _():
    return path("M16 72 L10 28 L32 46 L50 16 L68 46 L90 28 L84 72Z", GOLD) + rect(16, 70, 68, 14, GOLD, rx=3) + \
        circle(50, 77, 4, RED, sw=1.8) + circle(32, 77, 3, BLUE, sw=1.6) + circle(68, 77, 3, GREEN, sw=1.6) + \
        circle(10, 26, 4, YELLOW) + circle(90, 26, 4, YELLOW) + circle(50, 14, 4, YELLOW)


@art("conquista")
def _():
    return path("M10 66 H90 L78 84 H22Z", BROWN) + line(50, 10, 50, 66, sw=3.4) + \
        path("M50 14 Q70 26 50 38Z", WHITE) + path("M50 40 Q76 52 50 64Z", WHITE) + path("M48 18 Q28 34 48 60Z", CREAM) + \
        path("M50 10 L62 14 L50 18", RED, sw=2) + path("M0 88 Q12 82 24 88 T48 88 T72 88 T100 88", stroke=BLUE, sw=4) + \
        rect(56, 23, 6, 6, RED, stroke=False) + rect(56, 49, 6, 6, RED, stroke=False)


@art("codice")
def _():
    return path("M6 26 L30 20 L50 26 L70 20 L94 26 V82 L70 76 L50 82 L30 76 L6 82Z", "#F2DDB0") + \
        path("M30 20 V76 M50 26 V82 M70 20 V76", sw=2) + \
        circle(18, 44, 6, RED, sw=2) + rect(36, 38, 10, 10, BLUE, rx=2, sw=2) + path("M56 40 l6 -6 l6 6 l-6 6z", GREEN, sw=2) + \
        circle(82, 44, 6, ORANGE, sw=2) + path("M12 62 h12 M34 64 h12 M54 62 h12 M74 64 h12", stroke=DBROWN, sw=3) + \
        "".join(dot(x, 70, 1.8, DBROWN) for x in (14, 20, 40, 60, 80))


@art("bandera")
def _():
    return rect(12, 6, 5, 90, GREY, rx=2) + rect(17, 14, 24, 44, "#006847", sw=2.4) + rect(41, 14, 24, 44, WHITE, sw=2.4) + \
        rect(65, 14, 24, 44, "#CE1126", sw=2.4) + circle(53, 36, 6, "#8B5A2B", sw=1.8) + path("M47 40 Q53 46 59 40", stroke="#3E7B27", sw=2) + \
        circle(14.5, 6, 4, GOLD, sw=2)


@art("heroe")
def _():
    cape = path("M30 70 C20 80 14 94 10 104 H90 C86 94 80 80 70 70Z", RED)
    return person(shirt=BLUE, hair_style="short", hair_color=BLACK, extra_back=cape,
                  extra_front=star(50, 84, 9, GOLD, sw=2) + path("M34 36 H66 V44 Q58 48 50 44 Q42 48 34 44Z", NAVY, sw=2) +
                  circle(43.5, 41, 2.2, WHITE, stroke=False) + circle(56.5, 41, 2.2, WHITE, stroke=False))


@art("batalla")
def _():
    sword = lambda a: group(f"rotate({a} 50 50)", rect(47, 4, 6, 60, LGREY, rx=2), rect(36, 62, 28, 6, GOLD, rx=3), rect(46, 68, 8, 16, BROWN, rx=2), circle(50, 88, 4, GOLD))
    return sword(-40) + sword(40) + path("M50 28 L74 36 V54 C74 70 62 80 50 86 C38 80 26 70 26 54 V36Z", RED) + \
        path("M50 36 L66 42 V54 C66 66 58 72 50 76 C42 72 34 66 34 54 V42Z", GOLD, sw=2.4)


# ── Medios y noticias ──

@art("periodico")
def _():
    return rect(10, 16, 80, 70, WHITE, rx=3) + rect(18, 24, 64, 10, INK, stroke=False) + rect(18, 40, 30, 22, LBLUE, sw=2) + \
        path("M54 42 H82 M54 50 H82 M54 58 H76 M18 70 H82 M18 78 H70", stroke=GREY, sw=3) + \
        path("M24 56 L32 46 L40 56Z", GREEN, sw=1.8)


@art("noticiero")
def _():
    return rect(6, 14, 88, 62, DGREY, rx=8) + rect(12, 20, 76, 50, "#2F5FB5", rx=3, sw=2) + \
        person(40, 22, 0.5, shirt=RED, hair_style="short", hair_color=BLACK, skin=SKIN2) + \
        rect(12, 58, 76, 12, RED, stroke=False) + path("M18 64 H60", stroke=WHITE, sw=3) + \
        rect(66, 26, 16, 12, WHITE, rx=2, sw=2) + path("M30 76 L24 90 M70 76 L76 90", sw=4)


@art("entrevista")
def _():
    return rect(36, 10, 28, 42, DGREY, rx=14) + path("M40 22 H60 M40 30 H60 M40 38 H60", stroke=GREY, sw=2.4) + \
        path("M28 40 Q28 64 50 64 Q72 64 72 40", sw=4) + line(50, 64, 50, 84, sw=4) + rect(32, 84, 36, 8, DGREY, rx=4) + \
        path("M14 30 q-6 10 0 20 M86 30 q6 10 0 20", stroke=RED, sw=3)


@art("reportero")
def _():
    return rect(10, 30, 60, 40, DGREY, rx=8) + path("M70 40 L90 30 V70 L70 60Z", GREY) + circle(32, 50, 12, NAVY) + circle(32, 50, 6, LBLUE, sw=2) + \
        circle(56, 40, 4, RED, sw=1.8) + rect(18, 20, 22, 10, DGREY, rx=3) + rect(30, 70, 8, 20, GREY, sw=2.4)


@art("titular")
def _():
    return rect(6, 14, 88, 72, WHITE, rx=3) + text(50, 46, "¡¡!!", 30, RED) + rect(14, 54, 72, 8, INK, stroke=False) + \
        path("M14 70 H86 M14 78 H66", stroke=GREY, sw=3) + sparkle(88, 12, 7)


@art("redes-sociales")
def _():
    node = lambda x, y, c: circle(x, y, 11, c) + circle(x, y - 2, 3.4, WHITE, stroke=False) + path(f"M{x - 5} {y + 6} Q{x} {y} {x + 5} {y + 6}", stroke=WHITE, sw=2)
    return path("M50 50 L22 24 M50 50 L80 22 M50 50 L20 78 M50 50 L82 76", sw=3) + node(50, 50, PURPLE) + node(22, 24, PINK) + \
        node(80, 22, BLUE) + node(20, 78, ORANGE) + node(82, 76, GREEN) + heart(66, 40, 5, RED, sw=2)


@art("rumor")
def _():
    return person(28, 22, 0.62, shirt=PINK, hair_style="long", hair_color=DBROWN) + person(72, 22, 0.62, shirt=BLUE, hair_style="short", hair_color=BLACK, skin=SKIN2) + \
        rect(30, 10, 40, 22, WHITE, rx=10) + path("M44 32 L40 40 L52 32", WHITE) + text(50, 27, "...", 16, PURPLE) + hand(40, 58, 0.3, rot=-20)


@art("noticias-falsas")
def _():
    return rect(14, 14, 64, 72, WHITE, rx=3) + rect(22, 22, 48, 8, INK, stroke=False) + path("M22 40 H70 M22 50 H70 M22 60 H60 M22 70 H66", stroke=GREY, sw=3) + \
        circle(70, 70, 20, RED) + path("M61 61 L79 79 M79 61 L61 79", stroke=WHITE, sw=6)


# ── Economía y negocios ──

@art("empresa")
def _():
    return rect(30, 8, 40, 86, "#5C7BD9") + building_windows(36, 14, 3, 6, 8, 8, 4, 4, LBLUE) + rect(10, 44, 22, 50, "#8FA8EF") + \
        building_windows(14, 50, 2, 4, 6, 6, 3, 4, LYELLOW) + rect(68, 34, 22, 60, "#3E5CB8") + building_windows(72, 40, 2, 5, 6, 6, 3, 4, LYELLOW) + \
        rect(44, 84, 12, 10, BROWN, sw=2) + path("M4 94 H96", sw=3)


@art("inversion")
def _():
    return ellipse(50, 86, 28, 7, GOLD) + rect(22, 76, 56, 10, GOLD, stroke=False) + path("M22 76 V86 M78 76 V86", sw=3) + ellipse(50, 76, 28, 7, GOLD) + \
        path("M50 70 V30", stroke=DGREEN, sw=5) + path("M50 46 C34 46 24 36 24 24 C38 24 48 32 50 46Z", GREEN) + \
        path("M50 36 C62 36 74 26 74 14 C60 14 52 22 50 36Z", LGREEN) + text(50, 84, "$", 10, DBROWN)


@art("prestamo")
def _():
    return path("M38 30 Q32 18 40 14 Q50 20 60 14 Q68 18 62 30Z", TAN) + path("M38 30 C16 40 18 84 50 84 C82 84 84 40 62 30Z", TAN) + \
        text(50, 70, "$", 28, DBROWN) + path("M82 30 A34 34 0 0 1 86 64", stroke=GREEN, sw=5) + poly([(80, 60), (92, 62), (86, 72)], GREEN, sw=2) + \
        path("M18 70 A34 34 0 0 1 14 36", stroke=ORANGE, sw=5) + poly([(20, 40), (8, 38), (14, 28)], ORANGE, sw=2)


@art("impuesto")
def _():
    return rect(14, 8, 54, 72, WHITE, rx=4) + text(41, 46, "%", 30, RED) + path("M22 58 H60 M22 66 H50", stroke=GREY, sw=3) + \
        rect(54, 46, 36, 48, DGREY, rx=6) + rect(60, 52, 24, 10, LGREEN, rx=2, sw=2) + \
        "".join(rect(60 + c * 9, 66 + r * 9, 6, 6, WHITE, rx=1.5, sw=1.6) for r in range(3) for c in range(3))


@art("ganancia")
def _():
    return rect(10, 10, 80, 80, WHITE, rx=8) + path("M18 82 H84 M18 82 V18", sw=3) + \
        rect(26, 64, 10, 18, LGREEN, sw=2) + rect(42, 52, 10, 30, LGREEN, sw=2) + rect(58, 40, 10, 42, LGREEN, sw=2) + \
        path("M24 58 L44 44 L56 50 L78 24", stroke=GREEN, sw=5) + poly([(70, 22), (82, 20), (80, 32)], GREEN, sw=2)


@art("emprendedor")
def _():
    return group("rotate(40 50 50)", path("M50 6 C64 18 66 40 64 64 H36 C34 40 36 18 50 6Z", WHITE),
                 circle(50, 34, 7, LBLUE, sw=2.6), path("M36 50 L24 66 L36 66Z", RED), path("M64 50 L76 66 L64 66Z", RED),
                 path("M42 64 L50 88 L58 64Z", ORANGE), path("M46 64 L50 78 L54 64Z", YELLOW, sw=2), path("M42 16 Q50 6 58 16", RED, sw=2.4)) + \
        sparkle(18, 20, 6) + sparkle(84, 84, 5, LBLUE)


@art("deuda")
def _():
    return rect(10, 10, 80, 80, WHITE, rx=8) + path("M18 82 H84 M18 82 V18", sw=3) + \
        path("M24 26 L42 44 L54 38 L78 70", stroke=RED, sw=5) + poly([(70, 72), (82, 74), (80, 62)], RED, sw=2) + \
        circle(70, 30, 8, GOLD, sw=2.4) + text(70, 34, "$", 11, DBROWN)


@art("contrato")
def _():
    return rect(18, 6, 56, 80, WHITE, rx=4) + path("M26 20 H66 M26 30 H66 M26 40 H58 M26 50 H66", stroke=GREY, sw=3) + \
        path("M28 70 Q34 60 38 70 T48 68 T58 70", stroke=BLUE, sw=2.6) + \
        group("rotate(40 74 70)", rect(70, 40, 9, 46, BLACK, rx=3), poly([(70, 86), (79, 86), (74.5, 96)], GOLD))


# ── Relaciones ──

@art("noviazgo")
def _():
    return person(30, 20, 0.66, shirt=BLUE, hair_style="short", hair_color=BLACK, skin=SKIN2) + \
        person(70, 20, 0.66, shirt=PINK, hair_style="long", hair_color=BROWN) + heart(50, 18, 10, RED) + heart(78, 10, 4, PINK, sw=2)


@art("boda")
def _():
    return rect(18, 66, 64, 24, WHITE) + rect(26, 46, 48, 22, WHITE) + rect(34, 28, 32, 20, WHITE) + \
        path("M18 74 q8 6 16 0 t16 0 t16 0 t16 0 M26 54 q8 6 16 0 t16 0 t16 0", stroke=LPINK, sw=3) + \
        heart(50, 18, 8, RED) + ellipse(50, 92, 40, 5, LGREY)


@art("celos")
def _():
    return face(50, 54, 36, skin="#B8E07A", mood="bored").replace(f'<line', '<line') + \
        path("M30 40 L42 44 M70 40 L58 44", sw=3.4) + text(86, 22, "?", 20, DGREEN)


@art("confianza")
def _():
    return path("M10 80 Q14 60 30 56 L44 56 Q50 58 48 64 L36 66", SKIN) + path("M90 80 Q86 60 70 56 L56 56 Q50 58 52 64 L64 66", SKIN2) + \
        heart(50, 38, 20, RED) + path("M38 30 q3 -6 10 -5", stroke=WHITE, sw=3) + rect(0, 74, 22, 22, BLUE, rx=4) + rect(78, 74, 22, 22, ORANGE, rx=4)


@art("compromiso")
def _():
    return circle(50, 64, 26, "none", stroke=INK, sw=12) + circle(50, 64, 26, "none", stroke=GOLD, sw=6) + \
        poly([(38, 30), (44, 22), (56, 22), (62, 30), (50, 44)], LBLUE) + path("M38 30 H62 M44 22 L50 30 L56 22 M50 30 V44", sw=1.8) + \
        sparkle(74, 18, 6, WHITE) + sparkle(24, 22, 5)


@art("carino")
def _():
    return circle(26, 30, 12, BROWN) + circle(74, 30, 12, BROWN) + circle(26, 30, 6, TAN, stroke=False) + circle(74, 30, 6, TAN, stroke=False) + \
        circle(50, 50, 28, BROWN) + ellipse(50, 60, 13, 10, TAN) + dot(40, 46, 3) + dot(60, 46, 3) + ellipse(50, 56, 4, 3, BLACK) + \
        path("M46 64 Q50 67 54 64", sw=2.2) + heart(50, 88, 10, RED)


@art("pelea")
def _():
    return path("M8 20 H44 Q50 20 50 26 V46 Q50 52 44 52 H22 L14 62 L16 52 H8 Q2 52 2 46 V26 Q2 20 8 20Z", "#FF8A6B") + \
        path("M56 40 H92 Q98 40 98 46 V66 Q98 72 92 72 H84 L86 82 L76 72 H56 Q50 72 50 66 V46 Q50 40 56 40Z", LBLUE) + \
        text(26, 44, "#!", 16, WHITE) + text(74, 64, "@%", 15, WHITE) + path("M50 8 L42 30 H52 L46 50", stroke=YELLOW, sw=5)


@art("reconciliacion")
def _():
    return path("M20 54 C20 36 34 28 46 32 C54 20 70 18 78 24 C70 26 64 30 62 36 C80 34 92 44 94 56 C80 52 70 56 60 64 C50 72 32 72 20 54Z", WHITE) + \
        path("M46 32 C52 40 56 48 54 58", sw=2.4) + dot(36, 40, 2.4) + path("M22 42 L12 46 L22 48Z", ORANGE, sw=2) + \
        path("M60 64 Q70 80 86 84 M74 78 l-4 -10 M80 82 l4 -8", stroke=GREEN, sw=3) + path("M84 84 q4 -6 10 -4", LGREEN, sw=2)


# ── Dichos y modismos ──

@art("estar-en-la-luna")
def _():
    return rect(4, 4, 92, 92, NAVY, rx=18, stroke=False) + path("M44 14 A36 36 0 1 0 86 66 A29 29 0 1 1 44 14Z", LYELLOW) + \
        person(36, 34, 0.4, shirt=ORANGE, hair_style="spiky", hair_color=DBROWN, mood="sleep") + \
        star(20, 20, 4, YELLOW, sw=1.6) + star(86, 18, 3, YELLOW, sw=1.4) + star(84, 50, 3.5, YELLOW, sw=1.4)


@art("echar-la-hueva")
def _():
    return line(8, 20, 8, 90, sw=4) + line(92, 20, 92, 90, sw=4) + \
        path("M8 34 Q50 80 92 34", stroke=INK, sw=10) + path("M8 34 Q50 80 92 34", stroke=ORANGE, sw=5) + \
        circle(40, 46, 10, SKIN) + path("M34 46 q3 2 6 0 M42 46 q3 2 6 0", sw=2) + path("M30 42 C30 32 50 32 50 42 C44 38 36 38 30 42Z", DBROWN, sw=2) + \
        path("M48 54 Q60 60 74 50", stroke=GREEN, sw=9) + text(70, 30, "z", 16, NAVY) + text(80, 20, "z", 11, NAVY)


@art("dar-el-avion")
def _():
    return path("M8 54 L92 18 L60 86 L46 62Z", WHITE) + path("M46 62 L92 18 L36 58Z", LGREY) + path("M46 62 L50 80 L60 86", fill=LGREY, sw=2.4) + \
        path("M10 84 q10 -10 20 -4 q10 6 18 -4", stroke=LBLUE, sw=3, extra='stroke-dasharray="4 6"')


@art("ponerse-las-pilas")
def _():
    return rect(18, 26, 60, 48, GREEN, rx=8) + rect(78, 40, 8, 20, DGREY, rx=2) + rect(24, 32, 14, 36, LGREEN, rx=3, sw=2) + rect(42, 32, 14, 36, LGREEN, rx=3, sw=2) + \
        rect(60, 32, 12, 36, LGREEN, rx=3, sw=2) + path("M52 14 L40 34 H54 L44 54", stroke=INK, sw=8).replace('stroke-width="8"', 'stroke-width="9"') + \
        path("M52 14 L40 34 H54 L44 54", stroke=YELLOW, sw=4) + text(50, 92, "100%", 14, DGREEN)


@art("estar-de-pelos")
def _():
    return face(50, 54, 36, mood="starry") + sparkle(12, 18, 7) + sparkle(88, 16, 8, PINK) + sparkle(86, 82, 5, LBLUE)


@art("hacer-de-chivo-los-tamales")
def _():
    return ellipse(30, 30, 12, 6, WHITE, rot=-30) + ellipse(70, 30, 12, 6, WHITE, rot=30) + \
        path("M40 26 Q30 8 18 10 M60 26 Q70 8 82 10", sw=4) + path("M30 34 C30 22 70 22 70 34 L64 66 C62 78 38 78 36 66Z", WHITE) + \
        dot(42, 44, 3) + dot(58, 44, 3) + ellipse(50, 62, 8, 5, LPINK) + path("M46 76 L50 92 L54 76", fill=LGREY) + \
        group("rotate(-25 82 74)", path("M82 56 C74 64 72 76 74 90 L82 96 L90 90 C92 76 90 64 82 56Z", "#C9B26A"), path("M82 62 V88", stroke="#C9402E", sw=3))


@art("no-tener-pelos-en-la-lengua")
def _():
    return path("M12 40 Q50 20 88 40 Q86 80 50 86 Q14 80 12 40Z", "#7A2E3A") + path("M18 42 Q50 30 82 42 L80 50 Q50 40 20 50Z", WHITE, sw=2.4) + \
        path("M30 60 Q50 50 70 60 Q72 88 50 92 Q28 88 30 60Z", PINK) + path("M50 62 V84", stroke="#E0457A", sw=2.6) + \
        path("M80 14 l6 -8 M88 22 l8 -4 M90 32 h8", stroke=RED, sw=3)


@art("ser-buena-onda")
def _():
    return ellipse(50, 16, 22, 6, "none", stroke=GOLD, sw=5) + face(50, 56, 34, mood="happy") + heart(86, 78, 7, RED) + sparkle(14, 74, 6)
