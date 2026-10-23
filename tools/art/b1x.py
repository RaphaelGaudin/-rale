"""Illustrations du niveau B1 (compléments et nouveaux thèmes)."""
from .kit import *  # noqa: F401,F403
from .a1 import ART as A1
from .a2 import ART as A2
from .b1 import ART as B1
from .b2 import ART as B2
from .a2x import ART as A2X
from .a1x import ART as A1X

ART = {}
X = {**A1, **A2, **B1, **B2, **A1X, **A2X}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


def screen(x=10, y=14, w=80, h=56, fill=LBLUE):
    return rect(x, y, w, h, DGREY, rx=6) + rect(x + 5, y + 5, w - 10, h - 10, fill, rx=3, sw=2) + \
        path(f"M{x - 6} {y + h + 6} H{x + w + 6} L{x + w} {y + h} H{x}Z", GREY)


def bill(x, y, w=40, rot=0, fill="#9ED69A"):
    return rect(x, y, w, w * 0.5, fill, rx=3, rot=rot) + circle(x + w / 2, y + w / 4, w * 0.14, "none", stroke=DGREEN, sw=2)


# ── La chamba ──

@art("curriculum")
def _():
    return paper(18, 8, 58, 84, lines=0) + rect(26, 18, 16, 18, LBLUE, rx=2, sw=2) + circle(34, 25, 4, SKIN, sw=1.6) + \
        path("M48 22 h18 M48 30 h12 M26 46 h40 M26 56 h34 M26 66 h40 M26 76 h28", stroke=GREY, sw=3) + star(76, 82, 8, GOLD, sw=2)


@art("vacante")
def _():
    return rect(12, 20, 76, 50, WHITE, rx=6) + text(50, 44, "SE", 14, RED) + text(50, 62, "BUSCA", 14, RED) + \
        path("M30 20 L50 6 L70 20", sw=2.6) + circle(50, 6, 3, GOLD, sw=1.6) + person(78, 56, 0.4, shirt=BLUE)


@art("companero-de-trabajo")
def _():
    return rect(0, 78, 100, 22, BROWN) + person(28, 18, 0.62, shirt=BLUE, hair_style="short", hair_color=BLACK) + \
        person(72, 18, 0.62, skin=SKIN2, shirt=PURPLE, hair_style="long", hair_color=DBROWN) + rect(4, 66, 30, 14, DGREY, rx=2) + rect(66, 66, 30, 14, DGREY, rx=2)


@art("vacaciones")
def _():
    return rect(0, 70, 100, 30, "#FFE3A3", stroke=False) + path("M0 70 q12 -6 25 0 t25 0 t25 0 t25 0", LBLUE, sw=2.4) + \
        path("M72 92 Q70 50 78 30", stroke=BROWN, sw=5) + path("M78 30 Q60 20 52 32 M78 30 Q90 16 98 26 M78 30 Q70 10 60 12 M78 30 Q96 34 96 46", stroke=GREEN, sw=5) + \
        circle(26, 24, 12, YELLOW) + path("M14 90 L44 76 L28 70Z", RED) + path("M28 70 L36 94", sw=2.4)


@art("aguinaldo")
def _():
    return use(X["regalo"], 0, 6, 0.8) + bill(52, 54, 40, -12) + coin(80, 26, 11) + sparkle(16, 16, 6)


@art("renuncia")
def _():
    return paper(16, 10, 54, 76, lines=4) + text(43, 28, "ADIÓS", 11, RED) + path("M28 74 q8 -10 14 0 t14 -4", stroke=BLUE, sw=2.6) + \
        arrow(70, 60, 94, 60, RED, 4) + rect(80, 40, 14, 14, BROWN, rx=2, sw=2)


@art("ascenso")
def _():
    return rect(10, 70, 22, 22, LBLUE) + rect(38, 50, 22, 42, BLUE) + rect(66, 30, 22, 62, NAVY) + \
        person(77, -12, 0.42, shirt=ORANGE, hair_style="short", hair_color=BLACK) + arrow(14, 58, 50, 28, GREEN, 4) + star(20, 18, 7, GOLD, sw=2)


@art("home-office")
def _():
    return rect(6, 6, 88, 88, CREAM, rx=6) + rect(14, 14, 28, 24, LBLUE, sw=2.4) + path("M28 14 V38 M14 26 H42", sw=2) + \
        screen(44, 28, 42, 30) + rect(26, 64, 68, 6, BROWN, rx=2) + path("M32 70 V92 M88 70 V92", sw=3) + \
        path("M26 50 H38 V64 H26Z", RED) + path("M38 54 q6 0 6 4 q0 4 -6 4", sw=2.4) + use(X["gato"], 0, 64, 0.32)


def note_small(x, y):
    return path(f"M{x} {y} V{y - 14} L{x + 8} {y - 16}", sw=2.4) + circle(x - 3, y, 3.2, INK, stroke=False)


# ── El caló chilango ──

@art("guey")
def _():
    return person(30, 22, 0.66, shirt=RED, hair_style="spiky", hair_color=BLACK) + person(70, 22, 0.66, skin=SKIN2, shirt=TEAL, hair_style="short", hair_color=DBROWN) + \
        path("M44 64 L56 56", sw=5) + bubble(30, 2, 40, 20) + text(50, 16, "¡güey!", 11, INK)


@art("raza")
def _():
    return person(18, 40, 0.42, shirt=RED) + person(38, 30, 0.46, skin=SKIN2, shirt=YELLOW, hair_style="long", hair_color=BLACK) + \
        person(62, 30, 0.46, skin=SKIN3, shirt=GREEN, hair_style="spiky", hair_color=BLACK) + person(82, 40, 0.42, shirt=PURPLE, hair_style="bun", hair_color=DBROWN) + \
        heart(50, 16, 7, RED, sw=2)


@art("chavo")
def _():
    return person(skin=SKIN2, shirt=ORANGE, hair_style="spiky", hair_color=BLACK, extra_front=hat("cap", 50, 26)) + \
        rect(70, 64, 12, 20, BLACK, rx=3, sw=2) + path("M76 64 V54", sw=2)


@art("desmadre")
def _():
    return use(X["papel-picado"], 0, -16, 1.0) + person(30, 34, 0.5, shirt=RED, hair_style="long", hair_color=BLACK) + \
        person(70, 34, 0.5, skin=SKIN2, shirt=BLUE, hair_style="spiky", hair_color=BLACK) + \
        "".join(rect(x, y, 4, 6, c, rot=r, stroke=False) for x, y, c, r in [(10, 60, PINK, 20), (50, 50, YELLOW, -30), (88, 64, GREEN, 40), (46, 86, BLUE, 10)]) + \
        motion(4, 34, 2, 6, 6)


@art("no-manches")
def _():
    return face(50, 54, 36, mood="surprised") + hand(16, 82, 0.4, rot=-20) + hand(84, 82, 0.4, rot=20) + \
        text(50, 14, "¡NO!", 14, RED)


@art("fresa-snob")
def _():
    return person(shirt=PINK, hair_style="long", hair_color=GOLD, extra_front=path("M28 34 h44 l-3 8 q-8 3 -14 0 l-2 -4 h-6 l-2 4 q-6 3 -14 0z", BLACK, sw=1.8)) + \
        path("M80 54 C72 48 72 38 80 36 C88 38 88 48 80 54Z", RED, sw=2) + path("M76 36 L80 30 L84 36", stroke=GREEN, sw=2) + sparkle(16, 20, 6)


@art("lana")
def _():
    return bill(14, 50, 52, -10) + bill(30, 36, 52, 8, "#B9E4A8") + coin(76, 74, 12) + coin(84, 50, 9)


@art("antro")
def _():
    return rect(0, 0, 100, 100, "#2A1E4A", stroke=False) + circle(50, 18, 12, LGREY) + "".join(rect(x, y, 4, 4, WHITE, sw=1) for x, y in [(44, 12), (52, 16), (46, 22)]) + \
        path("M50 6 V0", sw=2) + path("M50 30 L10 90 M50 30 L50 96 M50 30 L90 90", stroke=PINK, sw=3, extra='opacity="0.6"') + \
        person(30, 46, 0.46, shirt=TEAL, hair_style="long", hair_color=BLACK) + person(70, 46, 0.46, skin=SKIN2, shirt=ORANGE, hair_style="spiky", hair_color=BLACK)


# ── La vivienda ──

@art("casero")
def _():
    return person(skin=SKIN2, shirt=GREY, hair_style="bald", hair_color=DGREY, mustache=True) + use(X["llave"], 62, 52, 0.38)


@art("deposito")
def _():
    return use(X["casa"], 0, 0, 0.6) + arrow(58, 40, 76, 40) + bill(54, 60, 40, -6) + coin(84, 20, 9)


@art("mudanza")
def _():
    box = lambda x, y, w: rect(x, y, w, w * 0.8, TAN) + path(f"M{x} {y + 6} H{x + w} M{x + w / 2} {y} V{y + 6}", sw=2) + rect(x + w / 2 - 4, y, 8, w * 0.8, "#F0D9B0", stroke=False, extra='opacity="0.6"')
    return path("M4 30 H62 V78 H4Z", ORANGE) + path("M62 44 H82 L94 58 V78 H62Z", ORANGE) + rect(68, 48, 14, 10, LBLUE, sw=2) + \
        circle(20, 80, 8, DGREY) + circle(78, 80, 8, DGREY) + box(12, 42, 18) + box(34, 46, 16)


@art("roomie")
def _():
    return rect(48, 10, 4, 84, GREY, stroke=False) + person(26, 22, 0.6, shirt=GREEN, hair_style="short", hair_color=BLACK) + \
        person(74, 22, 0.6, skin=SKIN2, shirt=PINK, hair_style="pigtails", hair_color=DBROWN) + use(X["llave"], 36, 0, 0.28)


@art("servicios")
def _():
    return circle(24, 30, 15, YELLOW) + path("M18 30 l6 -10 v8 h6 l-6 10 v-8z", ORANGE, sw=1.8) + \
        circle(76, 30, 15, LBLUE) + path("M76 20 q-8 10 0 16 q8 -6 0 -16z", BLUE, sw=2) + \
        circle(50, 72, 15, "#FFD6C2") + path("M50 62 q-8 10 -2 18 q4 -4 2 -8 q6 4 2 10 q8 -6 -2 -20z", ORANGE, sw=2)


@art("portero")
def _():
    return rect(4, 60, 92, 36, BROWN) + rect(10, 66, 34, 24, LBLUE, sw=2.4) + person(50, 4, 0.8, skin=SKIN3, shirt=NAVY, hair_style="short", hair_color=GREY, mustache=True,
                                                                                    extra_front=hat("cap", 50, 26)) + rect(70, 70, 18, 14, WHITE, rx=2, sw=2)


@art("calentador")
def _():
    return rect(30, 10, 40, 72, WHITE, rx=14) + rect(38, 34, 24, 16, LGREY, rx=4, sw=2) + text(50, 46, "60°", 10, RED) + \
        path("M40 82 V94 M60 82 V94", stroke=GREY, sw=4) + path("M50 62 q-6 8 0 14 q6 -6 0 -14z", ORANGE, sw=2) + steam(74, 30, 2, 8)


@art("cocineta")
def _():
    return rect(6, 50, 88, 40, WHITE) + rect(10, 56, 36, 30, LGREY, sw=2.4) + rect(54, 56, 36, 30, LGREY, sw=2.4) + \
        ellipse(28, 48, 10, 3, DGREY, sw=2) + ellipse(28, 46, 12, 3, DGREY, sw=2) + rect(56, 18, 30, 22, LBLUE, rx=2) + rect(56, 36, 30, 6, GREY, rx=1, sw=1.8) + \
        path("M18 46 V32 L26 28", stroke=GREY, sw=3)


# ── La fonda ──

@art("sopa")
def _():
    return bowl(50, 52, 74, WHITE, "#E07A3A", 30) + "".join(circle(x, y, 3, c, stroke=False) for x, y, c in [(34, 50, GREEN), (48, 48, YELLOW), (60, 52, LGREEN), (68, 48, ORANGE)]) + \
        steam(34, 38, 3, 14) + rect(66, 18, 6, 32, LGREY, rx=3, rot=30)


@art("postre")
def _():
    return use(X["flan"], 0, 0, 1.0) + circle(66, 22, 6, RED) + path("M66 16 q2 -6 6 -6", stroke=GREEN, sw=2)


@art("guisado")
def _():
    return path("M14 44 H86 Q86 84 50 84 Q14 84 14 44Z", "#C9662F") + ellipse(50, 44, 36, 9, DRED) + \
        "".join(circle(x, y, 4, c, sw=1.6) for x, y, c in [(36, 42, TAN), (52, 40, ORANGE), (64, 44, TAN), (44, 46, GREEN)]) + \
        path("M14 50 H6 M86 50 H94", sw=4) + steam(36, 30, 3, 14)


@art("mantel")
def _():
    checks = "".join(rect(10 + c * 16, 34 + r * 16, 16, 16, RED if (r + c) % 2 == 0 else WHITE, stroke=False) for r in range(3) for c in range(5))
    return poly([(4, 30), (96, 30), (92, 84), (8, 84)], WHITE) + checks + rect(10, 34, 80, 48, "none", sw=2.4) + path("M8 84 l6 10 l6 -10 l6 10 l6 -10", stroke=RED, sw=2.4)


@art("sal")
def _():
    holes = "".join(dot(x, 22, 1.8) for x in (42, 50, 58)) + "".join(dot(x, 28, 1.8) for x in (46, 54))
    return path("M30 34 Q30 16 50 16 Q70 16 70 34 V86 Q70 92 64 92 H36 Q30 92 30 86Z", WHITE) + path("M30 34 Q30 16 50 16 Q70 16 70 34Z", LGREY) + holes + \
        text(50, 70, "S", 22, BLUE)


@art("cuchillo")
def _():
    return group("rotate(-40 50 50)", path("M44 6 Q60 10 60 40 V58 H44Z", LGREY) + rect(42, 58, 18, 6, DGREY, rx=2) + rect(44, 64, 14, 30, BROWN, rx=4) +
                 dot(51, 72, 1.8, CREAM) + dot(51, 84, 1.8, CREAM) + path("M49 14 V48", stroke=WHITE, sw=2.4))


@art("plato")
def _():
    return plate(50, 56, 42, 24) + path("M24 56 q4 -6 12 -6", stroke=WHITE, sw=3)


@art("orden")
def _():
    return rect(26, 8, 48, 80, WHITE, rx=3) + path("M26 88 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6", WHITE) + \
        path("M34 22 h32 M34 34 h24 M34 46 h28 M34 58 h20", stroke=GREY, sw=3) + text(60, 74, "$85", 12, RED) + \
        group("rotate(30 80 40)", rect(76, 20, 7, 40, YELLOW, rx=2) + poly([(76, 60), (79.5, 68), (83, 60)], TAN, sw=2))


# ── Las emociones ──

@art("preocupado")
def _():
    return face(50, 54, 36, mood="nervous") + path("M30 32 L42 36 M70 32 L58 36", sw=2.8) + text(84, 22, "?", 18, PURPLE)


@art("emocionado")
def _():
    return face(50, 54, 34, mood="starry") + hand(12, 50, 0.4, rot=-20) + hand(88, 50, 0.4, rot=20) + sparkle(20, 14, 6) + sparkle(82, 12, 6, PINK)


@art("avergonzado")
def _():
    return face(50, 54, 36, skin="#FFB3A8", mood="nervous") + circle(30, 62, 7, RED, stroke=False, extra='opacity="0.5"') + \
        circle(70, 62, 7, RED, stroke=False, extra='opacity="0.5"') + path("M18 96 Q24 74 36 80 M82 96 Q76 74 64 80", sw=3)


@art("asustado")
def _():
    return face(50, 54, 36, skin="#D8E6FF", mood="surprised") + path("M8 40 l6 4 M6 56 h8 M92 40 l-6 4 M94 56 h-8", sw=3) + \
        path("M80 18 q-3 6 0 9 q3 -3 0 -9z", LBLUE, sw=2) + path("M20 18 q-3 6 0 9 q3 -3 0 -9z", LBLUE, sw=2)


@art("tranquilo")
def _():
    return face(50, 54, 34, mood="sleep", skin="#D8F0C8") + path("M12 92 Q30 80 50 92 Q70 80 88 92", stroke=LBLUE, sw=4) + \
        path("M50 8 C40 16 40 24 50 28 C60 24 60 16 50 8Z", LGREEN, sw=2)


@art("confundido")
def _():
    return face(48, 56, 34, mood="bored") + text(80, 30, "?", 22, PURPLE) + text(18, 24, "?", 14, ORANGE) + \
        path("M22 42 q6 -6 14 -2 M62 38 q6 2 12 -2", sw=2.6) + path("M78 52 q8 -4 6 6 q-2 8 -10 4", sw=2.4)


@art("enamorado")
def _():
    return face(50, 54, 34, mood="love") + heart(84, 18, 8, PINK, sw=2) + heart(16, 22, 6, RED, sw=2) + heart(86, 84, 5, RED, sw=1.8)


@art("decepcionado")
def _():
    return face(50, 54, 34, mood="sad", skin="#E6E0F0") + arrow(84, 18, 84, 46, GREY, 3) + path("M10 20 h14", stroke=GREY, sw=3)


# ── La naturaleza ──

@art("lago")
def _():
    return path("M0 50 L22 24 L40 46 L58 18 L84 50Z", "#8FA6C9") + path("M50 26 L58 18 L66 28 Z", WHITE, sw=2) + \
        ellipse(50, 70, 46, 18, LBLUE) + path("M20 66 h14 M54 72 h20 M38 80 h12", stroke=WHITE, sw=3) + rect(0, 48, 100, 4, GREEN, stroke=False)


@art("cascada")
def _():
    return path("M0 20 H100 V30 H64 V84 H36 V30 H0Z", "#8E7A6A") + rect(38, 28, 24, 60, LBLUE, sw=2.4) + \
        path("M44 34 V80 M50 30 V84 M56 34 V80", stroke=WHITE, sw=2.4) + ellipse(50, 88, 36, 8, BLUE) + \
        circle(30, 86, 4, WHITE, sw=1.6) + circle(70, 86, 4, WHITE, sw=1.6)


@art("isla")
def _():
    return rect(0, 60, 100, 40, BLUE, stroke=False) + path("M0 66 q10 -4 20 0 t20 0 t20 0 t20 0 t20 0", stroke=LBLUE, sw=3) + \
        ellipse(50, 66, 30, 10, "#FFE3A3") + path("M50 64 Q46 40 54 24", stroke=BROWN, sw=5) + \
        path("M54 24 Q38 16 30 28 M54 24 Q66 12 78 22 M54 24 Q50 6 40 8 M54 24 Q72 30 74 42", stroke=GREEN, sw=5) + circle(18, 20, 10, YELLOW)


@art("cueva")
def _():
    return path("M2 92 Q6 30 50 18 Q94 30 98 92Z", "#9A8A7A") + path("M26 92 Q28 50 50 46 Q72 50 74 92Z", INK) + \
        path("M40 50 l3 8 l3 -8 M56 50 l2 6 l2 -6", WHITE, sw=1.6) + path("M14 60 l8 4 M84 50 l-6 6", stroke="#6E5E50", sw=2.6)


@art("arbol")
def _():
    return rect(42, 56, 16, 38, BROWN) + path("M42 70 L30 60 M58 66 L70 56", stroke=BROWN, sw=4) + \
        circle(50, 36, 26, GREEN) + circle(28, 48, 16, GREEN) + circle(72, 48, 16, GREEN) + circle(40, 30, 4, RED, sw=1.6) + circle(62, 40, 4, RED, sw=1.6) + \
        path("M36 22 q6 -6 14 -6", stroke=LGREEN, sw=3.4)


@art("flor")
def _():
    petals = "".join(ellipse(50 + 14 * c, 38 + 14 * s, 10, 10, PINK) for c, s in [(1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7)])
    return path("M50 50 V94", stroke=DGREEN, sw=4) + path("M50 76 Q34 64 28 72 Q36 82 50 76Z", GREEN) + petals + circle(50, 38, 10, YELLOW)


@art("piedra")
def _():
    return path("M10 82 Q8 60 26 50 Q34 30 56 32 Q80 34 88 56 Q96 76 86 84Z", GREY) + path("M26 52 Q40 46 46 54 M60 40 q10 2 16 12", stroke=DGREY, sw=2.4) + \
        path("M30 60 q6 -4 12 -2", stroke=LGREY, sw=3) + rect(0, 82, 100, 4, LGREEN, stroke=False)


@art("cielo")
def _():
    return rect(4, 4, 92, 92, LBLUE, rx=10) + circle(74, 26, 12, YELLOW) + \
        path("M14 62 Q8 62 8 54 Q8 46 18 46 Q20 36 32 38 Q40 32 46 42 Q56 42 54 54 Q54 62 46 62Z", WHITE, sw=2.6) + \
        path("M60 80 q4 -6 8 0 q4 -6 8 0", sw=2.4) + path("M30 22 q3 -4 6 0 q3 -4 6 0", sw=2.2)


# ── De compras ──

@art("caja")
def _():
    return rect(10, 50, 80, 42, GREY) + rect(18, 20, 46, 34, DGREY, rx=4) + rect(24, 26, 34, 14, LGREEN, rx=2, sw=2) + text(41, 37, "$120", 9, DGREEN) + \
        "".join(rect(24 + c * 12, 44, 8, 5, LGREY, rx=1, sw=1.4) for c in range(3)) + rect(20, 62, 44, 20, LGREY, rx=2, sw=2) + rect(68, 30, 18, 24, LBLUE, rx=3, sw=2)


@art("cambio")
def _():
    return hand(50, 96, 0.9, rot=0) + coin(38, 40, 11) + coin(60, 34, 10) + coin(50, 56, 9) + arrow(80, 20, 64, 20, GREEN, 3)


@art("bolsa")
def _():
    return path("M20 36 H80 L86 92 H14Z", "#C9A06A") + path("M36 36 V26 Q36 14 50 14 Q64 14 64 26 V36", sw=3.6) + \
        path("M44 40 V50 M56 40 V50", sw=2) + rect(30, 26, 12, 16, LGREEN, rx=4, rot=-10, sw=2) + rect(56, 22, 10, 18, ORANGE, rx=3, rot=8, sw=2)


@art("probador")
def _():
    rings = "".join(circle(x, 14, 3, GREY, sw=1.6) for x in range(18, 86, 12))
    return rect(8, 10, 84, 4, DGREY, stroke=False) + rings + path("M14 16 Q20 50 12 92 H56 Q48 50 56 16Z", RED) + \
        path("M24 20 Q28 50 22 90 M40 20 Q44 50 38 90", stroke=DRED, sw=2.4) + rect(60, 20, 30, 70, LBLUE, rx=3) + path("M68 30 l8 -6 M68 40 l14 -10", stroke=WHITE, sw=2.4) + \
        path("M72 90 l2 -6 l6 0 l2 6", sw=2)


@art("barato")
def _():
    return tag(16, 36, 68, "$10", GREEN, 22, WHITE) + path("M16 48 L6 48", sw=2) + circle(10, 48, 2, WHITE, sw=1.4) + \
        arrow(50, 70, 50, 92, GREEN, 4) + face(84, 18, 12, mood="happy")


@art("caro")
def _():
    return tag(8, 36, 84, "$9999", RED, 20, WHITE) + arrow(50, 92, 50, 70, RED, 4) + face(84, 16, 12, mood="surprised")


@art("devolucion")
def _():
    return path("M24 40 H76 L80 88 H20Z", "#C9A06A") + path("M38 40 V32 Q38 22 50 22 Q62 22 62 32 V40", sw=3.4) + \
        path("M70 64 A22 22 0 1 1 50 42", stroke=GREEN, sw=5) + path("M44 34 L52 42 L44 50", stroke=GREEN, sw=5)


@art("super")
def _():
    return rect(6, 36, 88, 56, WHITE) + rect(6, 24, 88, 16, RED) + text(50, 36, "SÚPER", 12, WHITE) + \
        rect(14, 50, 32, 40, LBLUE, sw=2.4) + rect(54, 50, 32, 40, LBLUE, sw=2.4) + use(X["comprar"], 26, 50, 0.44)



# ── La tecnología ──

@art("archivo")
def _():
    return path("M10 30 V82 Q10 88 16 88 H84 Q90 88 90 82 V38 Q90 32 84 32 H48 L40 22 H16 Q10 22 10 28Z", GOLD) + \
        rect(20, 30, 60, 30, WHITE, rx=2, sw=2.4) + path("M10 44 H90 V82 Q90 88 84 88 H16 Q10 88 10 82Z", YELLOW)


@art("descargar")
def _():
    return circle(50, 46, 34, BLUE) + arrow(50, 24, 50, 64, WHITE, 6, 12) + path("M18 86 H82", sw=5) + path("M18 80 V86 M82 80 V86", sw=5)


@art("usuario")
def _():
    return circle(50, 50, 40, LPURPLE) + circle(50, 40, 14, WHITE) + path("M24 78 Q26 58 50 58 Q74 58 76 78 Q64 88 50 88 Q36 88 24 78Z", WHITE)


@art("impresora")
def _():
    return rect(28, 10, 44, 24, WHITE) + rect(10, 32, 80, 38, DGREY, rx=6) + circle(78, 42, 3, GREEN, sw=1.6) + \
        paper(26, 58, 48, 36, lines=2)


@art("teclado")
def _():
    keys = "".join(rect(14 + c * 10, 34 + r * 10, 8, 8, WHITE, rx=1.6, sw=1.6) for r in range(3) for c in range(8))
    return rect(6, 26, 88, 48, DGREY, rx=6) + keys + rect(28, 64, 44, 6, WHITE, rx=2, sw=1.6)


@art("audifonos")
def _():
    return path("M18 60 V48 Q18 14 50 14 Q82 14 82 48 V60", sw=6) + rect(10, 52, 20, 32, RED, rx=8) + rect(70, 52, 20, 32, RED, rx=8) + \
        path("M16 60 v16 M76 60 v16", stroke=WHITE, sw=2, extra='opacity="0.6"') + note_small(50, 60)


@art("videollamada")
def _():
    return screen(8, 10, 84, 60, LBLUE) + person(34, 18, 0.44, shirt=ORANGE, hair_style="long", hair_color=DBROWN) + \
        rect(56, 38, 26, 22, WHITE, rx=3, sw=2) + group("translate(44 24) scale(0.36)", inner(svg(person(shirt=BLUE, hair_style="short", hair_color=BLACK)))) + \
        circle(50, 88, 7, RED) + path("M46 88 h8", stroke=WHITE, sw=2.4)


@art("liga")
def _():
    return group("rotate(-45 50 50)", rect(16, 38, 40, 24, "none", rx=12, stroke=BLUE, sw=7) + rect(44, 38, 40, 24, "none", rx=12, stroke=BLUE, sw=7))


# ── Los trámites ──

@art("cajero-automatico")
def _():
    return rect(16, 6, 68, 88, LGREY, rx=6) + rect(24, 14, 52, 32, NAVY, rx=3) + text(50, 34, "$", 14, LGREEN) + \
        "".join(rect(26 + c * 12, 52 + r * 9, 9, 6, WHITE, rx=1.4, sw=1.4) for r in range(3) for c in range(3)) + \
        rect(64, 54, 10, 4, INK, stroke=False) + rect(30, 82, 40, 6, INK, rx=2) + bill(36, 76, 28)


@art("credencial")
def _():
    return rect(8, 20, 84, 60, "#F2D7E8", rx=8) + rect(8, 20, 84, 14, PINK, rx=6) + text(50, 31, "INE", 9, WHITE) + \
        rect(16, 40, 24, 30, WHITE, rx=3, sw=2.4) + circle(28, 51, 6, SKIN, sw=2) + path("M20 68 Q28 58 36 68", NAVY, sw=2) + \
        path("M48 44 h34 M48 54 h28 M48 64 h32", stroke=GREY, sw=3)


@art("fila")
def _():
    return person(16, 36, 0.4, shirt=RED) + person(38, 36, 0.4, skin=SKIN2, shirt=BLUE, hair_style="long", hair_color=BLACK) + \
        person(60, 36, 0.4, skin=SKIN3, shirt=GREEN, hair_style="spiky", hair_color=BLACK) + person(82, 36, 0.4, shirt=PURPLE, hair_style="bun", hair_color=GREY) + \
        rect(0, 80, 100, 4, GREY, stroke=False) + text(50, 22, "· · ·", 18, GREY)


@art("formulario")
def _():
    boxes = "".join(rect(28, y, 6, 6, WHITE, rx=1, sw=1.8) + line(40, y + 3, 70, y + 3, sw=2.4, color=GREY) for y in (34, 48, 62))
    return paper(18, 10, 60, 80, lines=0) + rect(26, 18, 40, 8, LBLUE, rx=2, sw=2) + boxes  + \
        path("M28 51 l2.5 2.5 l5 -6", stroke=GREEN, sw=2.4) + path("M28 80 q6 -8 12 0 t12 -2", stroke=BLUE, sw=2.4)


@art("firma")
def _():
    return rect(6, 50, 88, 30, WHITE, rx=4) + line(14, 70, 86, 70, sw=2, color=GREY) + path("M18 66 q6 -22 12 -6 t10 -4 q6 -14 10 4 q4 8 12 -6 q4 -6 8 2", stroke=NAVY, sw=3) + \
        group("rotate(35 80 30)", rect(74, 0, 10, 48, BLUE, rx=3) + poly([(74, 48), (79, 60), (84, 48)], LGREY, sw=2))


@art("sello")
def _():
    return rect(40, 8, 20, 26, BROWN, rx=8) + rect(30, 32, 40, 12, DBROWN, rx=3) + rect(26, 44, 48, 8, RED, rx=2) + \
        circle(50, 76, 18, "none", stroke=RED, sw=3.6) + text(50, 80, "OK", 12, RED) + path("M22 76 H8 M78 76 H92", stroke=RED, sw=2.4)


@art("cita")
def _():
    return calendar(46, 54, 72, 66) + cal_grid(46, 54, 72, 66, highlight=(9,), color=PINK) + circle(80, 24, 14, WHITE) + \
        path("M80 16 V24 H86", sw=2.6)


@art("comprobante-de-domicilio")
def _():
    return paper(10, 10, 56, 80, lines=4) + text(24, 26, "CFE", 10, GREEN, anchor="start") + use(X["casa"], 50, 46, 0.48)


@art("ventanilla")
def _():
    return rect(4, 10, 92, 80, LGREY) + rect(18, 20, 64, 40, LBLUE) + person(50, 12, 0.5, shirt=PURPLE, hair_style="bun", hair_color=DBROWN, glasses=True) + \
        rect(18, 20, 64, 40, "none") + rect(38, 52, 24, 8, WHITE, rx=2, sw=2) + rect(10, 60, 80, 8, GREY) + tag(32, 70, 36, "Nº 3", YELLOW, 12)


@art("tramite")
def _():
    return paper(38, 4, 46, 58, lines=3) + paper(26, 18, 46, 58, lines=3) + paper(14, 32, 46, 58, lines=3) + \
        circle(48, 76, 10, "none", stroke=RED, sw=3) + text(48, 80, "OK", 8, RED)


@art("transferencia")
def _():
    return rect(4, 34, 30, 32, LBLUE, rx=5) + rect(66, 34, 30, 32, LGREEN, rx=5) + text(19, 56, "A", 16, NAVY) + text(81, 56, "B", 16, DGREEN) + \
        arrow(36, 50, 64, 50, ORANGE, 4) + coin(50, 30, 9)


@art("estado-de-cuenta")
def _():
    return paper(16, 8, 60, 84, lines=0) + "".join(line(24, y, 52, y, sw=2.6, color=GREY) + line(58, y, 68, y, sw=2.6, color=GREEN if i % 2 else RED) for i, y in enumerate(range(24, 70, 9))) + \
        line(24, 76, 68, 76, sw=3) + text(62, 88, "$", 10, NAVY)


@art("clave")
def _():
    return rect(12, 26, 76, 48, NAVY, rx=10) + "".join(circle(x, 50, 6, WHITE, sw=2) for x in (28, 44, 60)) + text(76, 58, "_", 16, WHITE) + \
        rect(36, 4, 28, 26, "none", rx=12, stroke=GOLD, sw=5)


@art("copia")
def _():
    return paper(40, 16, 44, 60, lines=3) + paper(16, 24, 44, 60, lines=3) + arrow(50, 92, 72, 92, BLUE, 3)


@art("acta-de-nacimiento")
def _():
    return paper(16, 6, 60, 86, fill=CREAM, lines=0) + circle(46, 28, 10, GREEN, sw=2) + path("M42 28 l3 3 l6 -6", stroke=WHITE, sw=2.4) + \
        path("M26 48 h40 M26 56 h34 M26 64 h40", stroke=GREY, sw=2.6) + use(X["bebe"], 50, 62, 0.36)


@art("retiro")
def _():
    return rect(18, 10, 64, 46, LGREY, rx=6) + rect(28, 40, 44, 6, INK, rx=2) + bill(32, 42, 36) + hand(50, 94, 0.7) + arrow(50, 62, 50, 74, GREEN, 3)


# ── El deporte ──

@art("gimnasio")
def _():
    return rect(4, 40, 92, 52, LGREY) + poly([(0, 42), (50, 14), (100, 42)], ORANGE) + rect(20, 56, 60, 6, DGREY, rx=2) + \
        rect(12, 46, 10, 26, BLACK, rx=3) + rect(78, 46, 10, 26, BLACK, rx=3) + rect(42, 72, 16, 20, BROWN, sw=2.4)


@art("nadar")
def _():
    return rect(0, 50, 100, 50, LBLUE, stroke=False) + circle(36, 50, 9, SKIN) + path("M28 46 Q36 36 44 46", RED, sw=2.4) + \
        path("M44 54 Q60 34 76 44", sw=5) + path("M0 56 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0", stroke=WHITE, sw=3.4) + \
        path("M0 72 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0", stroke=BLUE, sw=3)


@art("entrenador")
def _():
    return person(skin=SKIN2, shirt=RED, hair_style="short", hair_color=BLACK, extra_front=hat("cap", 50, 26) + path("M50 66 L40 82", sw=1.6) +
                  circle(40, 84, 4, GREY, sw=1.6)) + rect(72, 54, 22, 30, WHITE, rx=3) + path("M76 62 l6 6 M82 62 l-6 6 M86 74 a3 3 0 1 0 0.1 0", sw=1.8)


@art("cancha")
def _():
    return rect(6, 16, 88, 68, GREEN) + rect(6, 16, 88, 68, "none", stroke=WHITE, sw=2.4) + line(50, 16, 50, 84, sw=2.4, color=WHITE) + \
        circle(50, 50, 12, "none", stroke=WHITE, sw=2.4) + rect(6, 36, 14, 28, "none", stroke=WHITE, sw=2.4) + rect(80, 36, 14, 28, "none", stroke=WHITE, sw=2.4)


@art("gol")
def _():
    net = "".join(line(x, 24, x, 78, sw=1.4, color=LGREY) for x in range(18, 84, 8)) + "".join(line(14, y, 86, y, sw=1.4, color=LGREY) for y in range(30, 78, 8))
    return net + path("M14 78 V24 H86 V78", stroke=WHITE, sw=6) + path("M14 78 V24 H86 V78", sw=1.6) + use(X["futbol"], 46, 44, 0.32) + \
        text(50, 18, "¡GOL!", 13, RED)


@art("arbitro")
def _():
    return person(shirt=BLACK, hair_style="bald", hair_color=DBROWN, extra_front=path("M40 66 V104 M60 66 V104", stroke=WHITE, sw=3)) + \
        rect(74, 22, 16, 22, YELLOW, rx=2, rot=12) + rect(82, 30, 12, 18, RED, rx=2, rot=-6, sw=2.4)


@art("equipo")
def _():
    return person(20, 34, 0.48, shirt=GREEN, hair_style="short", hair_color=BLACK) + person(50, 28, 0.5, skin=SKIN2, shirt=GREEN, hair_style="spiky", hair_color=BLACK) + \
        person(80, 34, 0.48, skin=SKIN3, shirt=GREEN, hair_style="long", hair_color=DBROWN) + text(20, 88, "7", 10, WHITE) + text(50, 88, "10", 10, WHITE) + \
        text(80, 88, "9", 10, WHITE) + star(50, 12, 7, GOLD, sw=1.8)


@art("alberca")
def _():
    return rect(6, 30, 88, 60, LBLUE, rx=6) + path("M6 46 H94 M6 62 H94 M6 78 H94", stroke=WHITE, sw=2.4, extra='stroke-dasharray="4 4"') + \
        path("M76 30 V8 M88 30 V8 M76 14 H88 M76 22 H88", stroke=GREY, sw=3) + path("M14 40 q6 -4 12 0 t12 0", stroke=BLUE, sw=2.4)


@art("maraton")
def _():
    return rect(0, 76, 100, 24, GREY, stroke=False) + path("M0 88 H100", stroke=WHITE, sw=2.4, extra='stroke-dasharray="8 6"') + \
        circle(40, 18, 9, SKIN) + path("M38 28 L32 50", stroke=ORANGE, sw=10) + rect(28, 34, 12, 10, WHITE, rx=1, sw=1.6) + text(34, 42, "42", 6) + \
        path("M32 50 L20 62 L14 58 M32 50 L44 62 L42 76", sw=4.4) + path("M36 32 L24 38 M36 32 L50 40", sw=4.4) + \
        path("M70 76 V20", sw=3) + path("M70 20 H94 V40 H70", WHITE, sw=2.4) + "".join(rect(70 + c * 6, 20 + r * 5, 6, 5, INK if (r + c) % 2 else WHITE, stroke=False) for r in range(4) for c in range(4))



@art("carrera")
def _():
    lanes = "".join(path(f"M0 {y} Q50 {y - 30} 100 {y}", stroke=WHITE, sw=2) for y in (60, 76, 92))
    return rect(0, 40, 100, 60, "#D9663A", stroke=False) + lanes + rect(0, 0, 100, 40, LBLUE, stroke=False) + \
        circle(30, 46, 5, BLUE, sw=1.8) + circle(54, 62, 5, RED, sw=1.8) + circle(74, 78, 5, YELLOW, sw=1.8) + motion(10, 40, 2, 5, 8)


@art("pesas")
def _():
    return rect(14, 46, 72, 8, GREY) + rect(14, 28, 12, 44, BLACK, rx=3) + rect(74, 28, 12, 44, BLACK, rx=3) + \
        rect(4, 36, 10, 28, DGREY, rx=3) + rect(86, 36, 10, 28, DGREY, rx=3) + text(50, 84, "20 kg", 11, DGREY)


@art("beisbol")
def _():
    return circle(38, 60, 22, WHITE) + path("M22 46 q8 14 0 28 M54 46 q-8 14 0 28", stroke=RED, sw=2.4) + \
        group("rotate(40 70 40)", path("M66 4 Q74 4 74 14 L72 68 H68 L66 14Z", TAN) + rect(66, 68, 6, 18, DBROWN, rx=2))


@art("box")
def _():
    glove = lambda x, c, r: group(f"translate({x} 50) rotate({r})", path("M-16 -14 Q-16 -30 4 -30 Q22 -30 20 -8 Q20 10 4 14 H-12 Q-18 10 -16 -14Z", c) +
                                  path("M-16 -8 Q-6 -14 -2 -2", sw=2.4) + rect(-12, 14, 20, 14, WHITE, rx=3, sw=2.4))
    return glove(32, RED, -15) + glove(70, BLUE, 15) + sparkle(50, 18, 7)


@art("medalla")
def _():
    return path("M30 6 L44 46 M70 6 L56 46", stroke=BLUE, sw=8) + path("M30 6 L44 46 M70 6 L56 46", stroke=RED, sw=2.6) + \
        circle(50, 64, 24, GOLD) + circle(50, 64, 16, "none", stroke="#C98A00", sw=2.4) + star(50, 64, 9, YELLOW, sw=1.8)


@art("aficionado")
def _():
    return person(skin=SKIN2, shirt=GREEN, hair_style="spiky", hair_color=BLACK, mood="happy",
                  extra_front=path("M34 44 h8 M58 44 h8", stroke=WHITE, sw=2.4) + path("M38 50 h6 M56 50 h6", stroke=RED, sw=2.4)) + \
        path("M10 50 V12", sw=3) + path("M10 12 L34 18 L10 26Z", RED, sw=2.4) + hand(86, 38, 0.36, rot=10) + motion(78, 6, 2, 5, 6)


@art("estirarse")
def _():
    return circle(50, 28, 9, SKIN) + path("M50 38 V64", stroke=PURPLE, sw=10) + path("M50 42 L30 10 M50 42 L70 10", sw=4.4) + \
        path("M50 64 L34 92 M50 64 L66 92", sw=4.4) + rect(10, 92, 80, 4, PINK, rx=2) + path("M22 18 q-4 4 0 8 M78 18 q4 4 0 8", sw=2)


# ── Viajar por México ──

@art("carretera")
def _():
    return rect(0, 40, 100, 60, LGREEN, stroke=False) + path("M0 40 L22 22 L38 34 L58 14 L80 32 L100 22 V40Z", "#8FA6C9") + \
        path("M36 100 L48 40 H52 L64 100Z", DGREY) + path("M50 46 V54 M50 62 V72 M50 82 V96", stroke=YELLOW, sw=3)


@art("terminal")
def _():
    return rect(4, 30, 92, 60, CREAM) + rect(4, 22, 92, 12, NAVY) + text(50, 31, "TERMINAL", 8, WHITE) + \
        group("translate(10 46) scale(0.8)", rect(0, 0, 100, 40, LBLUE, rx=8) + building_windows(8, 6, 5, 1, 14, 14, 4) + circle(20, 42, 7, DGREY) + circle(80, 42, 7, DGREY))


@art("frontera")
def _():
    return rect(0, 76, 100, 24, "#E8C07A", stroke=False) + "".join(rect(x, 36, 4, 42, GREY, sw=1.6) for x in range(4, 100, 10)) + line(0, 40, 100, 40, sw=2.4) + \
        path("M18 76 V10", sw=2.6) + rect(18, 10, 24, 16, GREEN, sw=1.8) + rect(26, 10, 8, 16, WHITE, sw=1.4) + rect(34, 10, 8, 16, RED, sw=1.8)


@art("pueblo-magico")
def _():
    houses = rect(4, 60, 22, 30, PINK) + rect(26, 56, 22, 34, YELLOW) + rect(70, 62, 26, 28, TEAL) + \
        "".join(rect(x, 70, 8, 10, LBLUE, sw=2) for x in (11, 33, 79))
    return houses + rect(48, 36, 22, 54, ORANGE) + poly([(48, 36), (59, 14), (70, 36)], "#C9662F") + rect(54, 70, 10, 20, BROWN, sw=2) + \
        sparkle(18, 22, 7) + sparkle(86, 30, 6, PINK) + star(36, 14, 5, GOLD, sw=1.6)


@art("tienda-de-campana")
def _():
    return rect(0, 82, 100, 18, LGREEN, stroke=False) + poly([(10, 84), (50, 20), (90, 84)], ORANGE) + poly([(38, 84), (50, 48), (62, 84)], DBROWN, sw=2.4) + \
        path("M50 20 V12 M10 84 L4 92 M90 84 L96 92", sw=2.6) + circle(84, 16, 7, LYELLOW) + star(20, 18, 4, YELLOW, sw=1.4)


@art("hostal")
def _():
    return rect(10, 30, 80, 60, "#F2C49B") + poly([(4, 32), (50, 8), (96, 32)], RED) + rect(26, 18, 48, 14, WHITE, rx=3, sw=2) + text(50, 29, "HOSTAL", 8, NAVY) + \
        building_windows(18, 40, 4, 2, 12, 12, 6) + rect(42, 72, 16, 18, BROWN, sw=2)


@art("guia")
def _():
    return person(skin=SKIN2, shirt=YELLOW, hair_style="short", hair_color=BLACK, extra_front=hat("straw", 50, 24)) + \
        path("M84 80 V16", sw=3) + path("M84 16 L98 22 L84 28Z", RED, sw=2) + rect(10, 68, 18, 20, WHITE, rx=2, rot=-10, sw=2)


@art("excursion")
def _():
    return path("M0 92 L30 40 L50 64 L72 26 L100 76 V92Z", "#8FA6C9") + path("M64 40 L72 26 L80 40 Q72 44 64 40Z", WHITE, sw=2) + \
        path("M10 92 Q30 76 46 82 T80 70", stroke=WHITE, sw=3, extra='stroke-dasharray="5 5"') + \
        person(24, 50, 0.36, shirt=RED, extra_back=rect(36, 64, 28, 30, ORANGE, rx=4)) + rect(0, 90, 100, 10, GREEN, stroke=False)


@art("itinerario")
def _():
    return paper(14, 8, 60, 84, lines=0) + "".join(circle(26, y, 4, c, sw=2) + line(34, y, 64, y, sw=2.6, color=GREY) for y, c in [(28, RED), (46, ORANGE), (64, GREEN), (82, BLUE)]) + \
        path("M26 32 V42 M26 50 V60 M26 68 V78", sw=2, extra='stroke-dasharray="2 3"') + check(78, 20, 9)


@art("equipaje")
def _():
    return use(X["maleta"], 14, 6, 0.75) + use(X["mochila"], 50, 36, 0.6)


@art("mirador")
def _():
    return rect(0, 0, 100, 60, LBLUE, stroke=False) + path("M0 60 L20 36 L36 50 L56 26 L76 46 L100 30 V60Z", "#8FA6C9") + \
        rect(0, 60, 100, 40, GREEN, stroke=False) + path("M8 70 H92", sw=3) + "".join(line(x, 70, x, 86, sw=2.6) for x in range(14, 92, 12)) + \
        group("translate(40 56)", rect(0, 0, 20, 10, DGREY, rx=4) + rect(8, 10, 4, 20, DGREY, sw=2) + circle(2, 5, 4, LBLUE, sw=2) + circle(18, 5, 4, LBLUE, sw=2))


@art("ruta")
def _():
    return rect(6, 6, 88, 88, LGREEN, rx=8) + path("M20 80 Q20 50 44 54 T72 30 L80 18", stroke=WHITE, sw=9) + \
        path("M20 80 Q20 50 44 54 T72 30 L80 18", stroke=ORANGE, sw=3, extra='stroke-dasharray="5 5"') + circle(20, 80, 6, BLUE, sw=2) + \
        path("M80 6 C70 6 70 18 80 26 C90 18 90 6 80 6Z", RED, sw=2) + circle(80, 13, 2.4, WHITE, sw=1.2)


@art("recuerdo")
def _():
    return use(X["sombrero"], 2, 30, 0.6) + use(X["alebrije"], 44, 4, 0.56) + tag(10, 74, 40, "MX", RED, 12, WHITE)


@art("lancha")
def _():
    return rect(0, 68, 100, 32, BLUE, stroke=False) + path("M10 54 H90 L80 72 H20Z", RED) + path("M12 60 H88", stroke=WHITE, sw=3) + \
        rect(70, 44, 8, 12, DGREY, rx=2) + path("M0 74 q10 -5 20 0 t20 0 t20 0 t20 0 t20 0", stroke=LBLUE, sw=3) + \
        person(40, 24, 0.36, shirt=YELLOW, hair_style="short", hair_color=BLACK) + motion(90, 64, 2, 5, 8)


@art("temporada-alta")
def _():
    return calendar(50, 56, 76, 66, header=ORANGE) + cal_grid(50, 56, 76, 66, highlight=tuple(range(7, 21)), color=ORANGE) + \
        person(76, 46, 0.32, shirt=TEAL) + person(26, 46, 0.32, shirt=PINK, hair_style="long") + arrow(50, 30, 50, 8, RED, 3)


@art("vuelo")
def _():
    return use(X["avion"], 6, 6, 0.8) + path("M8 86 Q40 74 92 86", stroke=LBLUE, sw=3, extra='stroke-dasharray="5 6"') + \
        tag(60, 70, 34, "MX 12", YELLOW, 10)


# ── Cocinar ──

def pan(x=10, y=50, c=DGREY):
    return ellipse(x + 34, y, 34, 12, c) + ellipse(x + 34, y - 2, 28, 8, "#3A3A3A", sw=2) + rect(x + 66, y - 4, 26, 8, BLACK, rx=4)


@art("picar")
def _():
    return rect(8, 60, 84, 26, TAN, rx=6) + circle(84, 72, 3, BROWN, sw=1.4) + \
        "".join(rect(x, 64, 7, 7, GREEN if i % 2 else LGREEN, rx=1.4, sw=1.6) for i, x in enumerate(range(18, 60, 9))) + \
        group("rotate(-25 60 40)", path("M44 20 Q72 20 76 40 H44Z", LGREY) + rect(14, 34, 30, 8, BROWN, rx=3))


@art("freir")
def _():
    return pan(4, 66) + "".join(circle(x, y, 3, YELLOW, sw=1.6) for x, y in [(30, 60), (46, 58), (56, 62)]) + \
        path("M20 46 l-4 -8 M38 40 v-10 M56 42 l4 -8", stroke=ORANGE, sw=2.6) + ellipse(40, 62, 10, 4, GOLD, sw=1.8)


@art("hervir")
def _():
    return path("M16 46 H84 V82 Q84 90 76 90 H24 Q16 90 16 82Z", GREY) + ellipse(50, 46, 34, 7, LBLUE) + \
        "".join(circle(x, y, r, WHITE, sw=1.8) for x, y, r in [(36, 42, 4), (52, 38, 5), (66, 42, 3.4)]) + steam(34, 30, 3, 14) + \
        path("M16 52 H6 M84 52 H94", sw=4) + path("M30 96 q4 -6 8 0 M50 96 q4 -6 8 0", stroke=ORANGE, sw=2.6)


@art("mezclar")
def _():
    return bowl(50, 50, 76, LBLUE, CREAM, 32) + path("M36 48 q14 -10 28 0 q-14 8 -28 0", stroke=TAN, sw=2.4) + \
        group("rotate(25 60 30)", rect(56, 2, 6, 44, BROWN, rx=3) + ellipse(59, 46, 6, 9, BROWN)) + motion(10, 20, 2, 6, 6)


@art("asar")
def _():
    grill = "".join(line(18, y, 82, y, sw=2.6) for y in (56, 64, 72))
    return ellipse(50, 66, 36, 14, BLACK) + grill + rect(30, 50, 22, 12, "#A0521A", rx=4, rot=-6) + rect(56, 54, 18, 10, DRED, rx=4, rot=8) + \
        path("M34 52 l14 0 M58 56 l12 0", stroke=BLACK, sw=1.6) + path("M28 80 L22 96 M72 80 L78 96", sw=4) + \
        path("M30 40 q-4 -8 2 -14 M50 38 q-4 -8 2 -14 M70 40 q-4 -8 2 -14", stroke=ORANGE, sw=2.6)


@art("olla")
def _():
    return path("M14 40 Q12 86 50 88 Q88 86 86 40Z", "#C9662F") + ellipse(50, 40, 36, 9, "#A0521A") + \
        path("M14 48 Q4 48 6 58 Q8 66 16 64 M86 48 Q96 48 94 58 Q92 66 84 64", sw=3.6) + \
        path("M22 62 l8 10 l8 -10 l8 10 l8 -10 l8 10 l8 -10 l8 10", stroke=YELLOW, sw=2.4)


@art("comal")
def _():
    return ellipse(50, 60, 42, 16, DGREY) + ellipse(50, 58, 36, 12, "#4A4A4A", sw=2) + ellipse(50, 56, 20, 7, "#F0D28A", sw=2) + \
        path("M40 54 q4 2 8 0 M54 58 q4 2 8 0", stroke="#C9A06A", sw=2) + path("M20 82 h60", stroke=ORANGE, sw=3) + \
        path("M30 92 q-4 -6 0 -10 M50 92 q-4 -6 0 -10 M70 92 q-4 -6 0 -10", stroke=RED, sw=2.6)


@art("sarten")
def _():
    return pan(4, 52) + ellipse(36, 50, 8, 5, WHITE, sw=1.8) + circle(36, 50, 3.4, YELLOW, sw=1.4) + ellipse(54, 48, 7, 4, WHITE, sw=1.8) + circle(54, 48, 3, YELLOW, sw=1.4)


@art("licuadora")
def _():
    return path("M28 12 H72 L66 64 H34Z", "#DDEFFF") + path("M30 34 H70 L66 64 H34Z", PINK, sw=2) + rect(26, 6, 48, 8, DGREY, rx=3) + \
        path("M42 58 L58 52 M42 52 L58 58", sw=2.4) + path("M30 64 H70 L76 92 H24Z", RED) + circle(50, 80, 5, WHITE, sw=1.8)


@art("horno")
def _():
    return rect(12, 10, 76, 82, LGREY, rx=6) + rect(20, 32, 60, 50, DGREY, rx=4) + rect(26, 38, 48, 36, "#FFB36B", rx=3, sw=2) + \
        rect(30, 32, 40, 4, GREY, stroke=False) + "".join(circle(x, 20, 4, WHITE, sw=1.8) for x in (26, 40, 54)) + rect(64, 16, 16, 8, NAVY, rx=2, sw=1.6) + \
        ellipse(50, 62, 14, 6, BROWN, sw=2)


@art("cucharada")
def _():
    return group("rotate(-30 50 50)", rect(46, 50, 8, 46, LGREY, rx=4) + ellipse(50, 34, 18, 22, LGREY) + ellipse(50, 34, 13, 16, "#FFE0A3", sw=2)) + \
        text(80, 90, "1", 16, NAVY)


@art("pizca")
def _():
    return path("M22 40 Q18 24 32 22 L44 34 Q46 44 36 48 Z", SKIN) + path("M62 28 Q78 24 80 38 L66 48 Q56 46 56 36Z", SKIN) + \
        "".join(dot(x, y, 1.6, WHITE) for x, y in [(48, 52), (52, 60), (46, 66), (54, 70), (50, 78)]) + \
        "".join(circle(x, y, 1.6, WHITE, sw=1) for x, y in [(48, 52), (52, 60), (46, 66), (54, 70), (50, 78)]) + ellipse(50, 88, 22, 5, LGREY)


@art("ajo")
def _():
    return path("M50 14 Q54 24 64 30 Q84 40 80 62 Q76 84 50 86 Q24 84 20 62 Q16 40 36 30 Q46 24 50 14Z", CREAM) + \
        path("M50 30 Q40 50 44 84 M50 30 Q60 50 56 84 M36 36 Q26 58 34 80 M64 36 Q74 58 66 80", stroke=LGREY, sw=2.4) + \
        path("M44 86 l-4 6 M50 86 v8 M56 86 l4 6", stroke=TAN, sw=2)


@art("canela")
def _():
    stick = lambda y, r: group(f"rotate({r} 50 {y})", rect(14, y - 7, 72, 14, "#A0521A", rx=7) + path(f"M18 {y} H82", stroke="#6E3F22", sw=2) + ellipse(86, y, 4, 7, "#C9662F", sw=2))
    return stick(40, -12) + stick(60, 4) + stick(78, -4)


@art("aceite")
def _():
    return path("M40 6 H60 V20 Q74 28 74 42 V88 Q74 94 68 94 H32 Q26 94 26 88 V42 Q26 28 40 20Z", GOLD) + rect(40, 2, 20, 8, GREEN, rx=2) + \
        rect(30, 50, 40, 22, WHITE, rx=3, sw=2.4) + ellipse(50, 61, 7, 5, LGREEN, rot=-30, sw=1.8) + path("M34 30 V84", stroke=LYELLOW, sw=3)


@art("masa")
def _():
    return bowl(50, 56, 76, "#C9662F", "#F0D28A", 30) + circle(40, 50, 12, "#F0D28A") + circle(60, 48, 10, "#F0D28A") + \
        path("M36 44 q4 -2 8 0", stroke=WHITE, sw=2) + hand(78, 34, 0.4, rot=200)
