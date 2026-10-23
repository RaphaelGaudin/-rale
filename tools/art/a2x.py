"""Illustrations du niveau A2 (compléments et nouveaux thèmes)."""
from .kit import *  # noqa: F401,F403
from .a1 import ART as A1
from .a2 import ART as A2
from .a1x import ART as A1X

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


def wheel(cx, cy, r=8):
    return circle(cx, cy, r, DGREY) + circle(cx, cy, r * 0.4, LGREY, sw=2)


# ── La ciudad ──

@art("semaforo")
def _():
    return rect(46, 76, 8, 20, DGREY) + rect(32, 6, 36, 74, BLACK, rx=10) + circle(50, 22, 9, RED) + \
        circle(50, 43, 9, "#6B5A2A") + circle(50, 64, 9, "#2C5A3A") + path("M44 18 q3 -3 7 -3", stroke=WHITE, sw=2.4)


@art("puente")
def _():
    return rect(0, 70, 100, 30, LBLUE, stroke=False) + path("M0 80 q10 -4 20 0 t20 0 t20 0 t20 0 t20 0", stroke=WHITE, sw=2.4) + \
        path("M4 54 Q50 10 96 54", stroke=RED, sw=4) + rect(0, 52, 100, 8, GREY) + \
        "".join(line(x, 52, x, 52 - (20 - abs(x - 50) * 0.4) if abs(x - 50) < 46 else 52, sw=2) for x in range(14, 90, 12)) + \
        rect(16, 60, 8, 30, GREY) + rect(76, 60, 8, 30, GREY)


@art("mercado")
def _():
    stripes = "".join(path(f"M{x} 26 h12 v12 q-6 5 -12 0z", c, sw=2.2) for x, c in zip(range(8, 92, 12), [RED, WHITE, GREEN] * 3))
    return rect(12, 38, 76, 48, CREAM) + stripes + rect(18, 58, 64, 26, TAN) + \
        circle(30, 56, 6, RED, sw=2) + circle(42, 56, 6, ORANGE, sw=2) + circle(58, 56, 6, GREEN, sw=2) + circle(70, 56, 6, YELLOW, sw=2) + \
        path("M8 26 H92 L88 18 H12Z", ORANGE)


@art("plaza")
def _():
    return rect(4, 70, 92, 22, LGREY, rx=4) + rect(36, 40, 28, 32, CREAM) + poly([(30, 42), (50, 24), (70, 42)], RED) + \
        rect(44, 54, 12, 18, BROWN) + circle(18, 50, 13, GREEN) + rect(16, 60, 4, 12, BROWN, sw=2) + circle(82, 50, 13, GREEN) + \
        rect(80, 60, 4, 12, BROWN, sw=2) + path("M50 24 V12", sw=2.4) + path("M50 12 H60 V18 H50", GREEN, sw=2)


@art("hospital")
def _():
    return rect(14, 24, 72, 66, WHITE) + rect(36, 6, 28, 28, RED, rx=4) + path("M50 12 V28 M42 20 H58", stroke=WHITE, sw=5) + \
        building_windows(20, 42, 4, 2, 10, 10, 6) + rect(42, 72, 16, 18, LBLUE)


@art("edificio")
def _():
    return rect(26, 6, 48, 88, "#8AA4D6") + building_windows(32, 12, 3, 6, 9, 9, 6, 4, LYELLOW) + rect(44, 80, 12, 14, DBROWN) + \
        rect(4, 50, 22, 44, LPURPLE) + building_windows(9, 56, 2, 3, 5, 7, 2, 4) + rect(74, 34, 22, 60, LGREEN) + building_windows(79, 40, 2, 4, 5, 7, 2, 4)


@art("cuadra")
def _():
    return rect(4, 4, 92, 92, LGREY, rx=6) + rect(20, 20, 60, 60, GREEN, rx=4) + \
        rect(28, 28, 18, 18, ORANGE, sw=2.4) + rect(54, 28, 18, 18, PINK, sw=2.4) + rect(28, 54, 18, 18, YELLOW, sw=2.4) + rect(54, 54, 18, 18, LBLUE, sw=2.4) + \
        path("M10 12 H90 M88 10 V90", stroke=WHITE, sw=2, extra='stroke-dasharray="6 6"')


@art("banqueta")
def _():
    return rect(0, 66, 100, 34, DGREY, stroke=False) + path("M10 84 h14 M40 84 h14 M70 84 h14", stroke=WHITE, sw=3) + \
        rect(0, 50, 100, 16, LGREY) + "".join(line(x, 50, x, 66, sw=2) for x in (20, 40, 60, 80)) + \
        person(36, 4, 0.48, shirt=ORANGE, hair_style="long", hair_color=DBROWN) + rect(70, 18, 4, 32, DGREY, sw=2) + circle(72, 16, 6, YELLOW, sw=2)


# ── De viaje ──

@art("mochila")
def _():
    return path("M28 30 Q28 14 50 14 Q72 14 72 30 V82 Q72 90 64 90 H36 Q28 90 28 82Z", ORANGE) + \
        path("M40 14 Q40 4 50 4 Q60 4 60 14", sw=3.6) + rect(36, 54, 28, 24, "#E07B00", rx=5) + line(36, 62, 64, 62, sw=2.4) + \
        rect(46, 36, 8, 6, GOLD, rx=2, sw=2)


@art("mapa")
def _():
    return poly([(8, 22), (36, 14), (64, 22), (92, 14), (92, 80), (64, 88), (36, 80), (8, 88)], LGREEN) + \
        path("M36 14 V80 M64 22 V88", sw=2.4) + path("M18 70 Q34 40 50 56 T80 34", stroke=RED, sw=3, extra='stroke-dasharray="5 5"') + \
        path("M80 22 C72 22 72 32 80 40 C88 32 88 22 80 22Z", RED, sw=2.2) + circle(80, 28, 2.4, WHITE, sw=1.4)


@art("aeropuerto")
def _():
    return rect(6, 54, 88, 36, LGREY) + path("M6 54 Q50 36 94 54", LBLUE) + rect(14, 64, 72, 14, LBLUE, sw=2.4) + \
        rect(72, 20, 10, 36, WHITE) + rect(66, 12, 22, 12, NAVY, rx=3) + \
        group("translate(10 6) rotate(-15 20 20) scale(0.5)", path("M0 20 L60 16 Q72 16 72 22 Q72 28 60 26 L0 24Z", WHITE) +
              path("M28 18 L18 0 H26 L42 18Z", BLUE) + path("M28 24 L18 42 H26 L42 24Z", BLUE))


@art("habitacion")
def _():
    return rect(8, 8, 84, 84, CREAM, rx=6) + rect(14, 18, 26, 20, LBLUE, sw=2.4) + line(27, 18, 27, 38, sw=2) + \
        use(A1["cama"], 22, 30, 0.7) + rect(64, 16, 22, 30, GOLD, rx=4) + text(75, 37, "12", 14, DBROWN)


@art("reservacion")
def _():
    return paper(16, 10, 50, 70, lines=3) + calendar(70, 66, 40, 36, GREEN) + check(70, 70, 8) + text(41, 30, "OK", 12, GREEN)


@art("turista")
def _():
    return person(shirt=TEAL, hair_style="short", hair_color=GOLD, extra_front=hat("straw", 50, 24) +
                  rect(38, 74, 24, 16, BLACK, rx=4) + circle(50, 82, 5, LBLUE, sw=2) + path("M38 74 L32 66 M62 74 L68 66", sw=2.4))


@art("bloqueador")
def _():
    return rect(34, 26, 32, 64, ORANGE, rx=8) + rect(40, 10, 20, 18, WHITE, rx=3) + circle(50, 56, 10, YELLOW) + \
        text(50, 82, "50", 12, WHITE) + circle(84, 18, 10, YELLOW) + "".join(path(f"M84 18 l{x} {y}", stroke=YELLOW, sw=3) for x, y in [(0, -16), (-14, 4), (0, 16), (12, 10)])


@art("traje-de-bano")
def _():
    return path("M22 30 H78 V44 Q66 46 60 60 H40 Q34 46 22 44Z", BLUE) + path("M40 60 Q50 70 60 60", BLUE) + \
        path("M22 36 H78", stroke=WHITE, sw=3) + circle(36, 50, 3, YELLOW, stroke=False) + circle(64, 50, 3, YELLOW, stroke=False) + \
        path("M10 84 q10 -6 20 0 t20 0 t20 0 t20 0", stroke=LBLUE, sw=4)


# ── La rutina ──

@art("levantarse")
def _():
    return use(A1["cama"], 0, 18, 0.9) + person(62, 0, 0.55, shirt=LBLUE, hair_style="spiky", hair_color=DBROWN) + \
        circle(86, 18, 9, YELLOW) + arrow(30, 30, 30, 6, ORANGE, 3)


@art("lavarse-los-dientes")
def _():
    return face(42, 52, 32, mood="happy") + rect(56, 58, 40, 7, BLUE, rx=3.5, rot=-10) + rect(56, 50, 14, 8, WHITE, rx=2, rot=-10, sw=2) + \
        circle(26, 30, 5, WHITE, sw=2) + circle(18, 40, 3.6, WHITE, sw=2) + circle(64, 24, 4, WHITE, sw=2)


@art("vestirse")
def _():
    return person(shirt=WHITE, hair_style="short", hair_color=BLACK,
                  extra_front=path("M34 64 L18 76 L24 88 L30 84 V104 H70 V84 L76 88 L82 76 L66 64Z", RED) + path("M50 66 V104", sw=2)) + \
        arrow(84, 30, 84, 56, ORANGE, 3)


@art("peinarse")
def _():
    teeth = "".join(line(x, 32, x, 42, sw=2) for x in range(52, 82, 5))
    return person(shirt=PINK, hair_style="long", hair_color=ORANGE) + group("rotate(-20 66 30)", rect(50, 22, 34, 10, BROWN, rx=3) + teeth) + sparkle(18, 18, 6)


@art("estudiar")
def _():
    return rect(6, 70, 88, 8, BROWN) + person(40, 10, 0.72, shirt=GREEN, hair_style="short", hair_color=DBROWN, glasses=True) + \
        path("M20 70 L40 62 L60 70Z", WHITE) + path("M40 62 V70", sw=2) + rect(70, 50, 16, 20, BLUE, rx=2) + sparkle(84, 20, 7)


@art("cocinar")
def _():
    return path("M18 52 H82 V76 Q82 86 72 86 H28 Q18 86 18 76Z", DGREY) + rect(14, 46, 72, 8, GREY, rx=3) + \
        path("M82 54 H96 M18 54 H4", sw=4) + steam(36, 40, 3, 14) + \
        group("rotate(20 70 20)", rect(66, 4, 6, 40, BROWN, rx=3) + ellipse(69, 46, 7, 9, BROWN))


@art("descansar")
def _():
    return rect(0, 78, 100, 22, LGREEN, stroke=False) + path("M10 60 Q50 76 90 60", stroke=BROWN, sw=3) + path("M10 60 L6 92 M90 60 L94 92", stroke=DBROWN, sw=3.6) + \
        path("M14 62 Q50 82 86 62 Q50 72 14 62Z", ORANGE, sw=2) + face(40, 50, 13, mood="sleep") + text(64, 30, "z", 14, BLUE) + text(74, 20, "z", 10, BLUE)


@art("caminar")
def _():
    return circle(50, 16, 10, SKIN) + path("M40 14 Q42 2 54 4 Q62 6 60 14", DBROWN, sw=2.4) + path("M50 26 V56", stroke=BLUE, sw=11) + \
        path("M50 32 L38 50 M50 32 L62 48", sw=5) + path("M50 56 L38 74 L34 90 M50 56 L60 74 L68 88", sw=5) + \
        path("M14 94 h10 M36 94 h10 M70 94 h10", stroke=GREY, sw=3)


# ── La salud ──

@art("ojo")
def _():
    return path("M6 50 Q50 6 94 50 Q50 94 6 50Z", WHITE) + circle(50, 50, 18, "#6E3F22") + circle(50, 50, 8, INK) + circle(44, 44, 4, WHITE, stroke=False) + \
        path("M20 32 L14 24 M36 22 L32 12 M64 22 L68 12 M80 32 L86 24", sw=3)


@art("nariz")
def _():
    return circle(50, 50, 40, SKIN) + path("M52 22 Q50 50 38 62 Q44 72 56 68 Q62 70 64 62 Q60 56 54 58", SKIN2, sw=3) + \
        dot(46, 64, 2.4) + dot(58, 64, 2.4)


@art("boca")
def _():
    return path("M10 50 Q30 26 50 36 Q70 26 90 50 Q70 82 50 82 Q30 82 10 50Z", RED) + path("M10 50 Q50 62 90 50", sw=3) + \
        path("M20 52 Q50 64 80 52 L76 58 Q50 68 24 58Z", WHITE, sw=2) + path("M28 38 q8 -4 14 0", stroke="#FF9A8F", sw=3)


@art("oreja")
def _():
    return path("M38 20 C38 4 76 4 76 34 C76 54 60 56 60 72 C60 90 40 94 34 80", SKIN) + \
        path("M46 30 C48 18 66 20 66 34 C66 46 54 46 52 56", SKIN2, sw=2.6) + path("M14 40 q-6 10 0 20 M6 34 q-8 16 0 32", stroke=BLUE, sw=3)


@art("espalda")
def _():
    return circle(50, 22, 14, SKIN) + path("M36 14 Q50 0 64 14 Q66 24 64 26 Q50 18 36 26 Q34 24 36 14Z", DBROWN, sw=2.4) + \
        path("M20 96 C20 50 32 38 50 38 C68 38 80 50 80 96Z", SKIN) + path("M50 44 V92", stroke=SKIN2, sw=3) + \
        path("M36 52 q6 6 0 12 M64 52 q-6 6 0 12", stroke=SKIN2, sw=2.4)


@art("brazo")
def _():
    return path("M10 80 C14 64 30 60 44 62 L56 34 Q60 22 72 24 Q80 28 76 38 L64 74 Q60 86 46 86 L14 92Z", SKIN) + \
        path("M56 34 Q66 30 72 40", SKIN2, sw=2.6) + circle(76, 22, 11, SKIN) + path("M40 64 Q50 56 58 62", stroke=SKIN2, sw=2.4) + sparkle(20, 22, 7)


@art("gripa")
def _():
    return face(48, 54, 34, mood="tired", skin="#D8F0C8") + circle(48, 58, 6, RED) + rect(70, 20, 22, 20, WHITE, rx=4, rot=12) + \
        path("M76 24 q4 6 10 2", stroke=LGREY, sw=2) + text(22, 22, "¡ah-", 12, BLUE) + text(32, 34, "chú!", 12, BLUE)


@art("receta")
def _():
    return paper(16, 8, 56, 80, lines=4) + text(24, 22, "Rx", 14, BLUE, anchor="start") + use(A2["pastilla"], 52, 52, 0.46)


# ── Las fiestas ──

@art("posada")
def _():
    return rect(0, 0, 100, 100, NAVY, rx=0, stroke=False) + star(80, 18, 8, GOLD, sw=2) + star(20, 22, 5, YELLOW, sw=1.6) + \
        person(30, 40, 0.5, shirt=BLUE, hair_style="long", hair_color=DBROWN) + person(70, 40, 0.5, skin=SKIN2, shirt=BROWN, hair_style="short", hair_color=BLACK) + \
        rect(46, 62, 4, 16, WHITE, sw=1.6) + path("M48 62 q-3 -4 0 -8 q3 4 0 8z", ORANGE, sw=1.4) + \
        rect(86, 62, 4, 16, WHITE, sw=1.6) + path("M88 62 q-3 -4 0 -8 q3 4 0 8z", ORANGE, sw=1.4)


@art("pastel")
def _():
    return rect(18, 54, 64, 34, PINK, rx=6) + path("M18 64 q8 8 16 0 t16 0 t16 0 t16 0", WHITE, sw=2.4) + rect(28, 34, 44, 22, LPINK, rx=5) + \
        "".join(rect(x, 18, 5, 16, LBLUE, rx=2, sw=1.8) + path(f"M{x + 2.5} 18 q-4 -5 0 -10 q4 5 0 10z", ORANGE, sw=1.4) for x in (38, 48, 58)) + \
        ellipse(50, 90, 40, 5, LGREY)


@art("regalo")
def _():
    return rect(18, 44, 64, 46, RED, rx=4) + rect(14, 34, 72, 14, RED, rx=4) + rect(44, 34, 12, 56, YELLOW, sw=2.4) + \
        path("M50 34 C30 14 22 30 40 34 M50 34 C70 14 78 30 60 34", stroke=YELLOW, sw=4)


@art("globo")
def _():
    return ellipse(42, 36, 22, 26, RED) + path("M38 62 L42 58 L46 62Z", RED, sw=2) + path("M42 62 Q36 76 46 86 T44 98", sw=2.2) + \
        ellipse(70, 46, 16, 20, BLUE) + path("M68 66 L70 64 L73 66Z", BLUE, sw=2) + path("M70 66 Q76 80 66 90", sw=2.2) + \
        path("M32 24 q4 -6 10 -6", stroke=WHITE, sw=3.4)


@art("mascara")
def _():
    return path("M10 34 Q50 20 90 34 Q92 60 70 70 Q60 72 50 62 Q40 72 30 70 Q8 60 10 34Z", PURPLE) + \
        ellipse(32, 46, 9, 7, INK) + ellipse(68, 46, 9, 7, INK) + path("M10 34 L4 20 M90 34 L96 20", sw=2.4) + \
        star(50, 32, 5, GOLD, sw=1.6) + path("M60 64 Q76 90 68 98", stroke=PINK, sw=3)


@art("papel-picado")
def _():
    flag = lambda x, c: path(f"M{x} 24 H{x + 24} V60 L{x + 18} 56 L{x + 12} 62 L{x + 6} 56 L{x} 60Z", c) + \
        circle(x + 12, 38, 4, CREAM, sw=1.6) + path(f"M{x + 6} 48 h12", stroke=CREAM, sw=2.4)
    return path("M2 22 Q50 34 98 22", sw=2.4) + flag(4, PINK) + flag(38, YELLOW) + flag(72, TEAL)


@art("navidad")
def _():
    return poly([(50, 8), (78, 50), (64, 50), (86, 82), (14, 82), (36, 50), (22, 50)], GREEN) + rect(44, 82, 12, 12, BROWN) + \
        star(50, 10, 9, GOLD, sw=2) + circle(40, 44, 4, RED, sw=1.8) + circle(60, 64, 4, BLUE, sw=1.8) + circle(36, 72, 4, YELLOW, sw=1.8) + circle(64, 40, 3, PINK, sw=1.6)


@art("desfile")
def _():
    flagp = lambda x: path(f"M{x} 70 V20", sw=2.6) + rect(x, 20, 18, 12, GREEN, sw=1.8) + rect(x + 6, 20, 6, 12, WHITE, sw=1.4) + rect(x + 12, 20, 6, 12, RED, sw=1.8)
    return rect(0, 84, 100, 16, LGREY, stroke=False) + person(22, 44, 0.42, shirt=RED) + person(50, 44, 0.42, skin=SKIN2, shirt=BLUE, hair_style="long", hair_color=BLACK) + \
        person(78, 44, 0.42, skin=SKIN3, shirt=GREEN, hair_style="spiky", hair_color=BLACK) + flagp(28) + flagp(84) + motion(4, 10, 2, 6, 6)


# ── El tiempo libre ──

@art("videojuego")
def _():
    return rect(10, 12, 80, 50, BLACK, rx=6) + rect(16, 18, 68, 38, NAVY, rx=3) + rect(26, 40, 10, 10, GREEN, sw=2) + \
        circle(64, 34, 6, RED, sw=2) + path("M16 50 H84", stroke=LBLUE, sw=2) + \
        rect(26, 68, 48, 22, DGREY, rx=10) + path("M36 74 v10 M31 79 h10", stroke=WHITE, sw=3) + circle(64, 76, 3, RED, sw=1.4) + circle(58, 82, 3, YELLOW, sw=1.4)


@art("pelicula")
def _():
    holes = "".join(rect(x, 22, 6, 6, WHITE, rx=1, sw=1.6) + rect(x, 72, 6, 6, WHITE, rx=1, sw=1.6) for x in range(14, 90, 12))
    return rect(8, 16, 84, 68, BLACK, rx=4) + holes + rect(14, 34, 32, 32, LBLUE, rx=2, sw=2) + rect(54, 34, 32, 32, LYELLOW, rx=2, sw=2) + \
        path("M26 44 l10 6 l-10 6z", RED, sw=1.8)


@art("concierto")
def _():
    heads = "".join(circle(x, 88, 8, c, sw=2.4) for x, c in [(12, DBROWN), (30, BLACK), (48, BROWN), (66, BLACK), (84, DBROWN)])
    return rect(0, 0, 100, 100, NAVY, stroke=False) + path("M20 0 L40 70 H60 L80 0Z", "#FFF3A0", stroke=False, extra='opacity="0.35"') + \
        rect(0, 66, 100, 10, PURPLE) + person(50, 8, 0.6, shirt=RED, hair_style="long", hair_color=BLACK) + heads + \
        hand(20, 76, 0.32, rot=-10) + hand(76, 76, 0.32, rot=10)


@art("teatro")
def _():
    return rect(4, 6, 92, 88, "#B0174F", rx=4) + path("M4 6 Q24 50 10 94 H4Z", DRED) + path("M96 6 Q76 50 90 94 H96Z", DRED) + \
        path("M4 6 H96 V18 Q50 30 4 18Z", GOLD) + face(38, 56, 12, mood="happy", skin=WHITE) + face(62, 60, 12, mood="sad", skin=WHITE)


@art("serie")
def _():
    return use(A1X["television"], 0, 0, 1.0) + rect(30, 40, 40, 14, WHITE, rx=4, sw=2) + text(50, 51, "EP 2", 10, RED)


@art("dibujo")
def _():
    return rect(14, 10, 60, 76, WHITE, rx=3) + circle(36, 34, 8, YELLOW, sw=2.4) + path("M20 76 L36 52 L48 64 L58 50 L70 76Z", GREEN, sw=2.4) + \
        group("rotate(35 78 60)", rect(74, 30, 8, 50, ORANGE, rx=2) + poly([(74, 80), (78, 90), (82, 80)], TAN, sw=2))


@art("cancion")
def _():
    return path("M34 74 V22 L78 12 V64", sw=4.4) + path("M34 30 L78 20", sw=6) + ellipse(26, 76, 10, 8, PURPLE, rot=-20) + \
        ellipse(70, 66, 10, 8, PURPLE, rot=-20) + sparkle(14, 18, 6) + sparkle(88, 84, 5, PINK)


@art("juego-de-mesa")
def _():
    cells = "".join(rect(10 + c * 16, 10 + r * 16, 16, 16, YELLOW if (r + c) % 2 else WHITE, sw=1.8) for r in range(5) for c in range(5))
    return cells + rect(10, 10, 80, 80, "none") + rect(54, 52, 28, 28, WHITE, rx=6) + dot(62, 60, 3) + dot(74, 72, 3) + dot(68, 66, 3) + \
        circle(26, 26, 6, RED, sw=2) + circle(42, 58, 6, BLUE, sw=2)


# ── La cocina mexicana ──

@art("guacamole")
def _():
    return bowl(50, 52, 72, "#3A3A3A", "#8BC34A", 32) + circle(38, 50, 3, RED, stroke=False) + circle(56, 48, 3, WHITE, stroke=False) + \
        circle(64, 52, 3, RED, stroke=False) + poly([(74, 30), (92, 22), (86, 44)], GOLD) + poly([(14, 36), (28, 20), (32, 42)], GOLD)


@art("tlayuda")
def _():
    return circle(50, 54, 40, "#E8C07A") + circle(50, 54, 32, "#6E3F22", sw=2) + \
        path("M30 46 q10 -6 18 2 q8 8 20 -2", stroke=WHITE, sw=4) + circle(40, 64, 5, LGREEN, sw=2) + circle(62, 64, 5, RED, sw=2) + \
        path("M34 36 h10 M56 40 h12", stroke="#C9662F", sw=4)


@art("pambazo")
def _():
    return path("M10 56 Q10 30 50 30 Q90 30 90 56Z", RED) + path("M10 62 H90 Q90 76 50 78 Q10 76 10 62Z", DRED) + \
        path("M8 58 H92", stroke=LGREEN, sw=5) + path("M14 56 q8 4 16 0 t16 0 t16 0 t16 0 t12 0", stroke=WHITE, sw=3) + \
        path("M28 40 q6 -4 12 -2", stroke="#FF9A8F", sw=3)


@art("churros")
def _():
    churro = lambda x, r: group(f"rotate({r} {x} 60)", rect(x - 7, 14, 14, 76, GOLD, rx=7) + "".join(line(x - 4, y, x + 4, y, sw=2, color="#C98A00") for y in range(22, 86, 8)))
    return churro(36, -18) + churro(64, 14) + churro(50, 0) + "".join(dot(x, y, 1.4, WHITE) for x, y in [(34, 30), (52, 22), (60, 34), (48, 46)])


@art("atole")
def _():
    return path("M22 34 H74 V66 Q74 86 48 86 Q22 86 22 66Z", "#C9662F") + ellipse(48, 34, 26, 6, LPINK) + \
        path("M74 42 Q88 42 88 54 Q88 66 74 64", sw=3.6) + path("M26 54 l6 8 l6 -8 l6 8 l6 -8 l6 8 l6 -8 l6 8", stroke=YELLOW, sw=2.4) + steam(38, 26, 2, 14)


@art("flan")
def _():
    return ellipse(50, 80, 40, 9, LBLUE) + path("M24 78 L30 40 Q50 32 70 40 L76 78 Q50 86 24 78Z", GOLD) + \
        path("M30 40 Q50 48 70 40 Q50 32 30 40Z", "#A0521A") + path("M32 42 Q30 54 34 58 M50 46 Q48 58 52 62 M66 42 Q68 52 64 56", stroke="#A0521A", sw=3)


@art("enchiladas")
def _():
    roll = lambda y: rect(16, y, 68, 16, "#F0D28A", rx=8)
    return plate(50, 62, 44, 22) + roll(42) + roll(54) + path("M18 46 Q50 36 82 50 Q50 76 18 60Z", RED, sw=2.4, extra='opacity="0.9"') + \
        path("M28 52 h10 M48 48 h12 M66 56 h8", stroke=WHITE, sw=3) + circle(40, 58, 2.6, GREEN, stroke=False) + circle(60, 60, 2.6, GREEN, stroke=False)


@art("sope")
def _():
    return ellipse(50, 66, 38, 14, "#E8C07A") + ellipse(50, 60, 34, 12, "#E8C07A") + ellipse(50, 58, 28, 9, DBROWN, sw=2) + \
        path("M32 56 q8 -6 16 0 t16 0", stroke=LGREEN, sw=4) + path("M36 60 h8 M54 62 h8", stroke=WHITE, sw=3) + circle(50, 54, 3, RED, sw=1.4)


# ── Los animales ──

@art("caballo")
def _():
    return path("M28 92 V60 Q24 40 40 30 L54 12 L58 24 Q72 24 80 40 L76 46 Q70 40 64 44 Q66 60 60 92 H52 V66 H38 V92Z", BROWN) + \
        path("M40 30 Q42 18 54 12 L46 38 Q40 40 36 46", DBROWN, sw=2.6) + dot(64, 32, 2.6) + dot(76, 42, 1.6)


@art("vaca")
def _():
    return ellipse(50, 56, 32, 28, WHITE) + path("M28 40 Q20 46 26 56 Q34 50 34 40Z", BLACK, sw=2) + path("M66 66 Q76 60 78 70 Q70 78 64 72Z", BLACK, sw=2) + \
        ellipse(50, 72, 18, 12, LPINK) + dot(44, 72, 2.4) + dot(56, 72, 2.4) + dot(38, 50, 2.6) + dot(62, 50, 2.6) + \
        path("M24 36 Q12 30 14 22 M76 36 Q88 30 86 22", stroke=CREAM, sw=5) + path("M24 36 Q12 30 14 22 M76 36 Q88 30 86 22", sw=1.6)


@art("pajaro")
def _():
    return ellipse(48, 54, 28, 22, BLUE) + circle(70, 40, 14, BLUE) + poly([(82, 38), (94, 42), (82, 46)], ORANGE, sw=2) + dot(72, 36, 2.6) + \
        path("M30 50 Q40 34 58 52 Q44 62 30 50Z", LBLUE) + path("M22 56 L6 50 L10 62Z", NAVY) + path("M44 76 v10 M54 76 v10", stroke=ORANGE, sw=3)


@art("pez")
def _():
    return path("M14 50 Q40 18 72 50 Q40 82 14 50Z", ORANGE) + path("M70 50 L92 32 V68Z", ORANGE) + circle(30, 46, 4, WHITE, sw=2) + dot(30, 46, 2) + \
        path("M40 38 Q46 50 40 62 M52 38 Q58 50 52 62", stroke="#E07B00", sw=2.4) + circle(8, 30, 3, WHITE, sw=1.6) + circle(14, 20, 2.4, WHITE, sw=1.6)


@art("perico")
def _():
    return path("M40 92 L50 64 L60 92Z", BLUE) + ellipse(50, 54, 18, 24, GREEN) + circle(50, 28, 15, GREEN) + \
        path("M54 28 Q66 28 62 42 Q58 36 54 36Z", YELLOW, sw=2) + circle(46, 24, 4, WHITE, sw=1.8) + dot(46, 24, 2) + \
        path("M36 48 Q30 62 40 72 Q44 58 36 48Z", RED) + path("M42 76 h16", stroke=BROWN, sw=4)


@art("tortuga")
def _():
    return ellipse(48, 58, 34, 22, LGREEN) + circle(84, 58, 9, LGREEN) + dot(86, 56, 1.8) + \
        path("M18 58 A30 30 0 0 1 78 58Z", DGREEN) + poly([(38, 40), (48, 34), (58, 40), (56, 50), (40, 50)], GREEN, sw=2) + \
        path("M24 58 L32 50 M72 58 L64 50", sw=2) + ellipse(28, 76, 6, 4, LGREEN, sw=2) + ellipse(66, 76, 6, 4, LGREEN, sw=2)


@art("conejo")
def _():
    return ellipse(38, 24, 7, 20, WHITE, rot=-10) + ellipse(62, 24, 7, 20, WHITE, rot=10) + ellipse(38, 24, 3, 14, LPINK, rot=-10, stroke=False) + \
        ellipse(62, 24, 3, 14, LPINK, rot=10, stroke=False) + circle(50, 58, 26, WHITE) + dot(41, 54, 2.6) + dot(59, 54, 2.6) + \
        path("M47 62 L50 65 L53 62Z", PINK, sw=1.6) + path("M50 65 V69 M44 70 Q50 74 56 70", sw=2) + path("M30 64 H16 M70 64 H84", sw=1.6)


@art("colibri")
def _():
    return ellipse(46, 54, 18, 11, TEAL, rot=-30) + circle(62, 38, 9, GREEN) + path("M68 36 L94 30", sw=2.4) + dot(64, 36, 1.8) + \
        path("M44 48 Q26 14 18 22 Q24 40 44 50Z", LBLUE) + path("M30 66 L12 80 L22 66Z", DGREEN) + path("M56 48 Q60 54 52 58", RED, sw=2) + \
        circle(88, 74, 8, PINK) + circle(88, 74, 3, YELLOW, sw=1.4)


# ── El transporte ──

def car(x=0, y=0, c=RED, s=1.0, roof=None):
    inner_ = path("M10 64 V52 Q10 46 18 44 L30 28 H66 L80 44 Q90 46 90 54 V64Z", c) + path("M34 32 H48 V44 H24Z", LBLUE, sw=2.4) + \
        path("M52 32 H64 L74 44 H52Z", LBLUE, sw=2.4) + wheel(28, 66, 9) + wheel(72, 66, 9) + rect(84, 52, 6, 4, YELLOW, sw=1.6)
    if roof:
        inner_ += roof
    return group(f"translate({x} {y}) scale({s})", inner_)


@art("taxi")
def _():
    return car(0, 6, "#E8B4C8", roof=rect(38, 18, 22, 10, WHITE, rx=2, sw=2.2) + text(49, 26, "TAXI", 7, INK) + path("M10 54 H90", stroke=GOLD, sw=3))


@art("bicicleta")
def _():
    return circle(24, 66, 16, "none", stroke=INK, sw=3.4) + circle(76, 66, 16, "none", stroke=INK, sw=3.4) + dot(24, 66, 3) + dot(76, 66, 3) + \
        path("M24 66 L40 40 H66 L76 66 M40 40 L52 66 L66 40 M52 66 H24", stroke=RED, sw=3.6) + path("M36 32 H46 M66 40 L62 28 H72", sw=3.4)


@art("coche")
def _():
    return car(0, 8, BLUE)


@art("moto")
def _():
    return circle(22, 68, 14, DGREY) + circle(22, 68, 6, LGREY, sw=2) + circle(78, 68, 14, DGREY) + circle(78, 68, 6, LGREY, sw=2) + \
        path("M22 68 L38 46 H64 L78 68", stroke=INK, sw=3.6) + path("M34 48 Q44 34 66 42 L60 54 H40Z", RED) + \
        path("M64 42 L70 26 H80", sw=3.6) + rect(28, 40, 20, 6, BLACK, rx=3, sw=2)


@art("pesero")
def _():
    return rect(6, 26, 88, 46, LGREEN, rx=10) + rect(6, 56, 88, 8, WHITE, sw=2) + building_windows(14, 34, 4, 1, 14, 14, 6) + \
        rect(82, 34, 8, 20, LBLUE, rx=2, sw=2) + wheel(26, 74, 9) + wheel(74, 74, 9) + rect(30, 18, 40, 10, WHITE, rx=3, sw=2) + text(50, 26, "RUTA 5", 7)


@art("tren")
def _():
    return rect(0, 84, 100, 4, BROWN, stroke=False) + "".join(rect(x, 86, 6, 6, DBROWN, stroke=False) for x in range(4, 100, 12)) + \
        rect(10, 30, 70, 46, RED, rx=10) + rect(80, 50, 12, 26, RED, rx=4) + building_windows(18, 38, 3, 1, 14, 14, 6) + \
        rect(16, 62, 58, 6, WHITE, sw=2) + wheel(26, 80, 7) + wheel(64, 80, 7) + circle(88, 60, 4, YELLOW, sw=1.8)


@art("estacion")
def _():
    return rect(10, 38, 80, 52, CREAM) + path("M4 40 L50 14 L96 40Z", BROWN) + rect(40, 60, 20, 30, LBLUE) + \
        circle(50, 30, 7, WHITE, sw=2.4) + path("M50 26 V30 H54", sw=1.8) + rect(16, 50, 16, 14, LBLUE, sw=2.4) + rect(68, 50, 16, 14, LBLUE, sw=2.4)


@art("gasolinera")
def _():
    return rect(24, 22, 36, 70, RED, rx=6) + rect(30, 30, 24, 16, WHITE, rx=2, sw=2.4) + text(42, 42, "$", 12, GREEN) + \
        path("M60 40 Q76 40 76 54 V78 Q76 84 82 84", sw=3.6) + rect(78, 76, 10, 14, DGREY, rx=2) + rect(18, 88, 48, 6, DGREY, rx=2) + \
        path("M42 56 q-6 10 0 16 q6 -6 0 -16z", YELLOW, sw=2)


@art("trafico")
def _():
    return car(-2, -16, RED, 0.56) + car(46, -16, BLUE, 0.56) + car(-2, 30, GOLD, 0.56) + car(46, 30, GREEN, 0.56) + \
        path("M84 8 l4 -4 M90 14 l6 -2", stroke=RED, sw=2.6) + text(84, 28, "!", 14, RED)


@art("parada")
def _():
    return rect(16, 30, 6, 64, GREY, sw=2) + circle(19, 22, 12, BLUE) + text(19, 27, "P", 13, WHITE) + \
        path("M34 34 H92 V40 H34Z", GREEN) + rect(38, 40, 4, 54, GREY, sw=2) + rect(84, 40, 4, 54, GREY, sw=2) + rect(42, 72, 42, 6, BROWN, rx=2) + \
        person(62, 34, 0.42, shirt=ORANGE, hair_style="long", hair_color=BLACK)


@art("aventon")
def _():
    return car(20, 30, ORANGE, 0.75) + group("translate(6 12) scale(0.7)", path("M18 30 Q14 30 14 36 V54 Q14 60 22 60 H34 V36 Q34 30 28 30Z", SKIN) +
                                                 rect(18, 4, 10, 30, SKIN, rx=5)) + motion(84, 40, 3, 7, 8)


@art("casco")
def _():
    return path("M14 66 Q14 20 54 20 Q90 20 90 56 V66Z", RED) + path("M50 40 H90 V60 H56 Q50 60 50 54Z", NAVY, sw=2.6) + \
        path("M24 40 Q30 28 44 26", stroke=WHITE, sw=4) + path("M14 66 H90", sw=3)


@art("licencia-de-manejo")
def _():
    return rect(8, 22, 84, 56, LBLUE, rx=8) + rect(16, 34, 24, 32, WHITE, rx=3, sw=2.4) + circle(28, 46, 6, SKIN, sw=2) + \
        path("M20 64 Q28 54 36 64", BLUE, sw=2) + path("M48 40 h34 M48 50 h26 M48 60 h30", stroke=NAVY, sw=3) + rect(8, 22, 84, 8, BLUE, rx=4, sw=2)


@art("volante")
def _():
    return circle(50, 50, 38, "none", stroke=INK, sw=9) + circle(50, 50, 38, "none", stroke=DGREY, sw=4) + circle(50, 50, 12, DGREY) + \
        path("M14 50 H38 M62 50 H86 M50 62 V86", stroke=DGREY, sw=7) + text(50, 54, "★", 10, GOLD)


@art("llanta")
def _():
    return circle(50, 50, 40, BLACK) + circle(50, 50, 22, LGREY) + circle(50, 50, 7, DGREY) + \
        "".join(path(f"M{50 + 30 * c} {50 + 30 * s} l{4 * c} {4 * s}", stroke=DGREY, sw=4) for c, s in [(1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7)])


@art("caseta")
def _():
    return rect(0, 76, 100, 24, DGREY, stroke=False) + rect(8, 40, 30, 40, WHITE) + path("M4 40 H42 V32 H4Z", ORANGE) + \
        rect(14, 48, 18, 14, LBLUE, sw=2.4) + path("M38 66 H96", stroke=RED, sw=7) + path("M38 66 H96", stroke=WHITE, sw=2.4, extra='stroke-dasharray="8 8"') + \
        coin(78, 34, 12)


# ── Las profesiones ──

@art("policia")
def _():
    return person(skin=SKIN2, shirt=NAVY, hair_style="short", hair_color=BLACK, extra_front=hat("police", 50, 24) + star(38, 80, 5, GOLD, sw=1.6))


@art("cocinero")
def _():
    return person(shirt=WHITE, hair_style="short", hair_color=DBROWN, mustache=True, extra_front=hat("chef", 50, 24) +
                  circle(46, 78, 2, INK, stroke=False) + circle(54, 78, 2, INK, stroke=False) + circle(46, 88, 2, INK, stroke=False) + circle(54, 88, 2, INK, stroke=False))


@art("enfermera")
def _():
    return person(shirt=TEAL, hair_style="bun", hair_color=DBROWN,
                  extra_front=path("M36 24 Q50 16 64 24 L62 30 H38Z", WHITE, sw=2.4) + path("M50 20 V28 M46 24 H54", stroke=RED, sw=2) +
                  path("M36 66 Q30 84 44 90 M64 66 Q70 84 56 90", stroke=DGREY, sw=2.6) + circle(50, 92, 5, LGREY, sw=2))


@art("albanil")
def _():
    bricks = "".join(rect(x, y, 14, 8, "#D9663A", rx=1, sw=1.8) for y, xs in [(78, (2, 16)), (70, (8,)), (86, (8,))] for x in xs)
    return person(skin=SKIN3, shirt=ORANGE, hair_style="short", hair_color=BLACK, extra_front=hat("helmet", 50, 24)) + bricks + \
        poly([(76, 70), (94, 62), (90, 80)], LGREY) + rect(70, 74, 12, 4, BROWN, rot=-25, sw=1.6)


@art("taxista")
def _():
    return person(skin=SKIN2, shirt=LBLUE, hair_style="short", hair_color=BLACK, mustache=True, extra_front=hat("cap", 50, 26)) + \
        circle(84, 76, 13, "none", stroke=INK, sw=5) + path("M74 76 H94 M84 76 V88", sw=3)


@art("abogada")
def _():
    return person(shirt=NAVY, hair_style="long", hair_color=BLACK, glasses=True, extra_front=path("M44 66 L50 76 L56 66Z", WHITE, sw=2)) + \
        path("M78 30 V62 M66 34 H90", sw=3) + path("M62 34 L58 46 H74 Z", GOLD, sw=2) + path("M86 34 L82 46 H98Z", GOLD, sw=2)


@art("vendedor")
def _():
    return rect(6, 70, 88, 26, TAN) + person(50, -4, 0.8, shirt=RED, hair_style="short", hair_color=DBROWN, mustache=True, extra_front=rect(36, 70, 28, 34, WHITE, rx=3, sw=2)) + \
        circle(18, 66, 7, RED, sw=2) + circle(30, 66, 7, ORANGE, sw=2) + circle(72, 66, 7, GREEN, sw=2) + circle(84, 66, 7, YELLOW, sw=2)


@art("bombero")
def _():
    return person(shirt=RED, hair_style="none", extra_front=hat("fire", 50, 24) + path("M30 80 H70 M30 90 H70", stroke=YELLOW, sw=3.6)) + \
        path("M84 10 q-8 12 0 20 q10 -8 0 -20z", ORANGE, sw=2) + path("M84 18 q-3 5 0 8 q4 -3 0 -8z", YELLOW, sw=1.4)


@art("ingeniera")
def _():
    return person(skin=SKIN2, shirt=PURPLE, hair_style="long", hair_color=DBROWN, extra_front=hat("helmet", 50, 24)) + \
        rect(70, 60, 26, 34, LBLUE, rx=3, rot=-8) + path("M74 72 h16 M74 80 h12", stroke=WHITE, sw=2.4)


@art("carpintero")
def _():
    return person(shirt=GREEN, hair_style="short", hair_color=BROWN, extra_front=path("M30 70 V104 H70 V70", BROWN, sw=2.4)) + \
        group("rotate(-30 80 40)", rect(76, 22, 8, 36, DBROWN, rx=2) + rect(68, 14, 24, 10, GREY, rx=2))


@art("mecanico")
def _():
    return person(skin=SKIN3, shirt=NAVY, hair_style="spiky", hair_color=BLACK, extra_front=path("M38 46 q-2 4 2 6", stroke=BLACK, sw=2) + hat("cap", 50, 26)) + \
        group("rotate(40 80 60)", rect(76, 40, 8, 40, GREY, rx=3) + path("M72 40 Q72 30 80 30 Q88 30 88 40 L84 40 V34 H76 V40Z", GREY, sw=2.4))


@art("cantante")
def _():
    return person(shirt=PINK, hair_style="long", hair_color=BLACK, extra_front=ellipse(50, 52, 4.6, 5, DBROWN, sw=1.8) +
                  rect(66, 52, 8, 26, DGREY, rx=3) + circle(70, 48, 7, GREY)) + path("M84 20 V6 L94 4 V18", sw=2.6) + circle(82, 20, 3, INK, stroke=False)


@art("campesino")
def _():
    return rect(0, 86, 100, 14, LGREEN, stroke=False) + person(shirt=WHITE, skin=SKIN3, hair_style="short", hair_color=BLACK, mustache=True,
                                                              extra_front=hat("straw", 50, 22) + path("M30 70 L36 104 M70 70 L64 104", stroke=RED, sw=3)) + \
        path("M88 96 V44", stroke=GREEN, sw=3) + path("M88 58 Q76 50 74 40 M88 70 Q100 62 98 52", stroke=GREEN, sw=3) + ellipse(88, 40, 4, 8, GOLD, sw=2)


@art("dentista")
def _():
    return person(shirt=WHITE, hair_style="short", hair_color=BLACK, glasses=True,
                  extra_front=rect(38, 50, 24, 12, LBLUE, rx=4, sw=2) + path("M38 54 L31 46 M62 54 L69 46", sw=1.8)) + \
        path("M76 54 Q76 44 84 46 Q92 44 92 54 Q92 66 88 74 L86 64 L82 64 L80 74 Q76 66 76 54Z", WHITE, sw=2.4) + sparkle(94, 40, 4)


@art("plomero")
def _():
    return person(skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=DBROWN, mustache=True, extra_front=hat("cap", 50, 26) + path("M36 70 V104 M64 70 V104", stroke=RED, sw=4)) + \
        path("M74 96 V76 H90 V60", stroke=GREY, sw=7) + path("M74 96 V76 H90 V60", stroke=LGREY, sw=3) + path("M90 56 q-3 4 0 6 q3 -2 0 -6z", BLUE, sw=1.4)


@art("cientifica")
def _():
    return person(shirt=WHITE, hair_style="bun", hair_color=ORANGE, glasses=True, extra_front=path("M44 66 L50 80 L56 66", stroke=LGREY, sw=2.4)) + \
        path("M78 46 V58 L68 80 Q66 86 72 86 H92 Q96 86 94 80 L84 58 V46Z", WHITE, sw=2.6) + path("M72 74 H90 L94 82 Q94 86 90 86 H72 Q66 86 68 82Z", GREEN, sw=2) + \
        circle(80, 38, 2.4, GREEN, sw=1.4) + circle(86, 30, 2, GREEN, sw=1.4)


# ── Los quehaceres ──

def broom(cx=50, rot=-20, head=GOLD):
    return group(f"rotate({rot} {cx} 50)", rect(cx - 3, 4, 6, 60, BROWN, rx=3) + path(f"M{cx - 16} 90 L{cx - 8} 60 H{cx + 8} L{cx + 16} 90Z", head) +
                 path(f"M{cx - 8} 70 H{cx + 8}", stroke=RED, sw=3) + "".join(line(cx + d, 76, cx + d * 1.6, 88, sw=2) for d in (-6, 0, 6)))


def mop(cx=50, rot=-20):
    return group(f"rotate({rot} {cx} 50)", rect(cx - 3, 4, 6, 64, BLUE, rx=3) + rect(cx - 14, 64, 28, 6, DGREY, rx=2) +
                 "".join(path(f"M{cx + d} 70 q-2 10 {d * 0.3} 22", stroke=LGREY, sw=4) for d in (-11, -5, 1, 7, 12)))


def bucket(x=50, y=60, c=BLUE):
    return path(f"M{x - 20} {y} H{x + 20} L{x + 16} {y + 32} H{x - 16}Z", c) + path(f"M{x - 20} {y} Q{x} {y - 26} {x + 20} {y}", sw=2.6) + \
        ellipse(x, y, 20, 4, LBLUE, sw=2)


@art("barrer")
def _():
    return broom(44, -24) + "".join(circle(x, y, 2.4, GREY, stroke=False) for x, y in [(70, 88), (78, 84), (84, 90), (74, 94)]) + motion(80, 64, 2, 7, 8)


@art("trapear")
def _():
    return rect(0, 86, 100, 14, LBLUE, stroke=False, extra='opacity="0.6"') + mop(40, -20) + bucket(78, 62) + sparkle(16, 80, 5, WHITE)


@art("lavar-los-trastes")
def _():
    return rect(6, 58, 88, 36, LGREY, rx=4) + rect(14, 58, 72, 18, LBLUE, sw=2.4) + ellipse(40, 56, 18, 6, WHITE) + ellipse(40, 52, 16, 5, WHITE) + \
        path("M76 58 V30 Q76 22 66 22 H60 V28", sw=4) + "".join(circle(x, y, r, WHITE, sw=1.8) for x, y, r in [(26, 40, 5), (36, 34, 4), (60, 42, 6), (54, 32, 3)])


@art("tender-la-cama")
def _():
    return use(A1["cama"], 0, 4, 1.0) + sparkle(86, 18, 7) + sparkle(14, 20, 5)


@art("planchar")
def _():
    return path("M4 78 H96 L88 70 H12Z", LBLUE) + path("M20 78 L14 96 M80 78 L86 96", sw=3) + \
        path("M26 68 Q26 44 54 40 H78 V68Z", RED) + rect(26, 62, 52, 8, LGREY, rx=2) + path("M48 40 Q48 26 60 26 H70 Q76 26 76 32 V40", sw=4) + steam(30, 30, 2, 8)


@art("sacar-la-basura")
def _():
    return path("M24 38 H66 L62 92 H28Z", GREY) + rect(20, 30, 50, 10, DGREY, rx=3) + path("M38 50 V82 M50 50 V82", stroke=LGREY, sw=3) + \
        path("M70 46 C66 30 90 30 88 46 C96 60 90 88 78 90 C66 92 62 66 70 46Z", BLACK) + path("M78 34 L74 26 L84 26Z", BLACK, sw=2) + arrow(84, 70, 98, 70, RED, 3)


@art("escoba")
def _():
    return broom(50, -10, GOLD)


@art("trapeador")
def _():
    return mop(50, 0)


@art("cubeta")
def _():
    return bucket(50, 40, ORANGE) + path("M40 34 q4 -6 8 0", stroke=WHITE, sw=2.6) + circle(62, 28, 4, WHITE, sw=1.6) + circle(68, 20, 3, WHITE, sw=1.6)


@art("jabon")
def _():
    return rect(18, 42, 64, 38, PINK, rx=14) + path("M28 52 q8 -4 16 -2", stroke=WHITE, sw=3.4) + \
        "".join(circle(x, y, r, WHITE, sw=2) for x, y, r in [(30, 32, 7), (46, 26, 5), (60, 30, 8), (76, 22, 4), (70, 38, 4)])


@art("ropa-sucia")
def _():
    return path("M18 46 H82 L76 92 H24Z", TAN) + path("M18 46 H82", sw=3.4) + "".join(line(30 + i * 10, 50, 32 + i * 9, 88, sw=1.8, color=BROWN) for i in range(5)) + \
        path("M26 46 Q30 24 46 30 L50 46Z", BLUE) + path("M50 46 Q56 18 74 34 L72 46Z", RED) + \
        circle(42, 36, 2, DBROWN, stroke=False) + circle(64, 32, 2.4, DBROWN, stroke=False) + path("M84 20 q4 -4 8 0 M88 30 q4 -4 8 0", stroke=GREEN, sw=2)


@art("tendedero")
def _():
    pin = lambda x: rect(x - 2, 26, 4, 10, BROWN, rx=1, sw=1.4)
    return path("M4 92 V20 M96 92 V20", stroke=BROWN, sw=4) + path("M4 28 Q50 38 96 28", sw=2) + \
        path("M14 30 H36 L34 62 H16Z", PINK) + pin(18) + pin(32) + path("M44 33 L40 40 L46 42 V70 H66 V42 L72 40 L68 33Z", BLUE) + pin(48) + pin(64) + \
        rect(76, 31, 14, 26, YELLOW, sw=2.4) + pin(83)


@art("aspiradora")
def _():
    return ellipse(34, 74, 22, 16, PURPLE) + circle(24, 86, 5, DGREY) + circle(46, 86, 5, DGREY) + \
        path("M50 70 Q70 64 70 46 V20", stroke=DGREY, sw=4) + path("M66 20 H82", sw=5) + rect(62, 84, 32, 8, DGREY, rx=3) + path("M70 46 V84", stroke=LGREY, sw=4)


@art("regar-las-plantas")
def _():
    return path("M14 50 H50 L46 80 H18Z", LGREY) + path("M50 54 L78 36", stroke=LGREY, sw=6) + path("M50 54 L78 36", sw=1.4) + \
        path("M14 54 Q4 54 6 66 Q8 74 16 72", sw=3) + "".join(path(f"M{x} {y} q-2 4 0 6 q2 -2 0 -6z", BLUE, sw=1.4) for x, y in [(82, 44), (86, 54), (80, 58)]) + \
        path("M66 96 L70 76 H90 L94 96Z", "#C9662F") + path("M80 76 V62 M80 70 Q72 64 72 58 M80 66 Q88 60 90 54", stroke=GREEN, sw=3)


@art("polvo")
def _():
    return rect(10, 64, 80, 8, BROWN) + rect(18, 72, 6, 24, DBROWN) + rect(76, 72, 6, 24, DBROWN) + \
        "".join(circle(x, y, r, GREY, stroke=False, extra='opacity="0.6"') for x, y, r in [(30, 50, 9), (44, 44, 12), (62, 48, 10), (74, 40, 7), (54, 30, 6)]) + \
        "".join(dot(x, y, 1.6, DGREY) for x, y in [(24, 60), (40, 60), (58, 61), (70, 60)])


@art("lavadora")
def _():
    return rect(18, 10, 64, 82, WHITE, rx=8) + line(18, 26, 82, 26) + circle(32, 18, 3, RED, sw=1.6) + rect(54, 15, 20, 6, LGREY, rx=2, sw=1.6) + \
        circle(50, 58, 24, LGREY) + circle(50, 58, 18, LBLUE) + path("M34 62 q8 -6 16 0 t16 0", stroke=BLUE, sw=3) + circle(44, 54, 3, WHITE, sw=1.4)


# ── La música mexicana ──

def note(x, y, c=INK):
    return path(f"M{x} {y} V{y - 18} L{x + 10} {y - 21}", sw=2.6) + circle(x - 3, y, 3.6, c, stroke=False)


@art("ranchera")
def _():
    return use(A1["sombrero"], 0, -6, 1.0) + note(18, 90) + note(80, 92)


@art("cumbia")
def _():
    return person(30, 30, 0.6, shirt=RED, hair_style="long", hair_color=BLACK, mood="happy") + person(70, 30, 0.6, skin=SKIN2, shirt=WHITE, hair_style="short", hair_color=BLACK) + \
        path("M40 70 Q50 60 60 70", sw=3) + note(14, 26) + note(80, 20) + motion(4, 50, 2, 6, 6)


@art("corrido")
def _():
    return use(A2["guitarra"], 0, 8, 0.85) + paper(58, 8, 36, 46, lines=3) + note(76, 92, RED)


@art("acordeon")
def _():
    folds = "".join(path(f"M{x} 26 L{x + 5} 50 L{x} 74", sw=2.2) for x in range(32, 66, 8))
    return rect(10, 22, 20, 56, RED, rx=4) + rect(70, 22, 20, 56, RED, rx=4) + rect(30, 26, 40, 48, "#FFB3A8") + folds + \
        "".join(circle(20, y, 2.6, WHITE, sw=1.4) for y in range(32, 74, 9)) + "".join(rect(76, y, 8, 5, WHITE, rx=1, sw=1.4) for y in range(30, 74, 9))


@art("trompeta")
def _():
    return path("M10 50 H60 L88 30 V70 L60 56 H10Z", GOLD) + rect(26, 34, 6, 16, GOLD, rx=2, sw=2) + rect(36, 34, 6, 16, GOLD, rx=2, sw=2) + \
        rect(46, 34, 6, 16, GOLD, rx=2, sw=2) + path("M20 56 Q36 72 56 56", stroke=GOLD, sw=4) + ellipse(88, 50, 4, 20, "#C98A00")


@art("violin")
def _():
    return group("rotate(-25 50 50)", path("M50 22 C34 22 34 40 42 46 C30 52 30 80 50 80 C70 80 70 52 58 46 C66 40 66 22 50 22Z", BROWN) +
                 rect(47, 2, 6, 40, DBROWN, rx=2) + path("M44 58 q-2 4 0 8 M56 58 q2 4 0 8", sw=2) + rect(44, 68, 12, 4, DBROWN, rx=1, sw=1.6)) + \
        path("M14 90 L86 22", stroke=TAN, sw=3)


@art("grupo")
def _():
    return person(20, 30, 0.5, shirt=RED, hair_style="short", hair_color=BLACK) + person(50, 22, 0.5, skin=SKIN2, shirt=PURPLE, hair_style="long", hair_color=DBROWN) + \
        person(80, 30, 0.5, skin=SKIN3, shirt=GREEN, hair_style="spiky", hair_color=BLACK) + note(48, 18) + star(84, 16, 5, GOLD, sw=1.6)


@art("escenario")
def _():
    return rect(0, 70, 100, 30, BROWN) + path("M0 0 H100 V12 Q50 20 0 12Z", DRED) + path("M0 0 Q18 40 6 70 H0Z", RED) + path("M100 0 Q82 40 94 70 H100Z", RED) + \
        path("M30 0 L18 70 H82 L70 0Z", "#FFF3A0", stroke=False, extra='opacity="0.5"') + rect(46, 40, 8, 30, DGREY) + circle(50, 36, 6, GREY)


@art("disco")
def _():
    return rect(6, 16, 60, 68, PURPLE, rx=4) + circle(36, 50, 18, PINK, sw=2.4) + circle(66, 50, 30, BLACK) + circle(66, 50, 20, "none", stroke=DGREY, sw=1.8) + \
        circle(66, 50, 10, RED) + dot(66, 50, 2.4, WHITE)


@art("ritmo")
def _():
    return path("M6 54 L22 54 L30 30 L40 76 L50 20 L60 70 L68 44 L76 54 H94", stroke=RED, sw=4) + \
        circle(30, 30, 4, YELLOW, sw=1.8) + circle(50, 20, 4, YELLOW, sw=1.8) + note(84, 30) + text(18, 90, "1 2 3", 12, NAVY, anchor="start")


@art("letra")
def _():
    return paper(16, 8, 58, 82, lines=0) + note(30, 34, PURPLE) + path("M42 26 h24 M26 46 h40 M26 56 h34 M26 66 h40 M26 76 h28", stroke=GREY, sw=3) + \
        group("rotate(35 82 54)", rect(78, 28, 8, 44, ORANGE, rx=2) + poly([(78, 72), (82, 80), (86, 72)], TAN, sw=2))


@art("bolero")
def _():
    return person(32, 26, 0.6, shirt=NAVY, hair_style="short", hair_color=BLACK, mustache=True) + person(68, 26, 0.6, shirt=RED, hair_style="long", hair_color=DBROWN) + \
        heart(50, 18, 9, PINK) + rect(0, 0, 100, 100, "none", stroke=False) + note(86, 26, PURPLE)


@art("son-jarocho")
def _():
    return rect(0, 80, 100, 20, BROWN) + "".join(line(x, 80, x, 100, sw=2) for x in (25, 50, 75)) + \
        person(50, 0, 0.8, shirt=WHITE, hair_style="bun", hair_color=BLACK,
               extra_front=circle(64, 30, 6, RED, sw=1.8) + path("M20 104 Q50 86 80 104", stroke=RED, sw=3)) + \
        note(14, 40) + note(84, 34) + motion(6, 66, 2, 6, 6)


@art("jarana")
def _():
    return group("rotate(30 50 50)", path("M50 36 C38 36 36 48 42 54 C34 60 34 84 50 84 C66 84 66 60 58 54 C64 48 62 36 50 36Z", TAN) +
                 circle(50, 66, 6, DBROWN) + rect(47, 4, 6, 40, DBROWN, rx=2) + path("M48 6 V82 M52 6 V82", stroke=WHITE, sw=1)) + \
        path("M12 80 q4 -6 8 0", stroke=RED, sw=2.4) + note(84, 30)


@art("arpa")
def _():
    strings = "".join(line(28 + i * 8, 20 + i * 5.5, 28 + i * 8, 86, sw=1.6) for i in range(7))
    return path("M22 92 L22 14 Q24 6 32 10 Q70 30 86 58 L92 72 L22 92", "none", sw=5) + path("M22 92 L22 14", stroke=BROWN, sw=7) + \
        path("M24 10 Q70 30 90 70", stroke=BROWN, sw=6) + path("M22 90 L90 70", stroke=BROWN, sw=6) + strings


@art("microfono")
def _():
    return rect(42, 42, 16, 40, DGREY, rx=6) + circle(50, 30, 18, GREY) + "".join(line(38, y, 62, y, sw=1.6) for y in (24, 30, 36)) + \
        path("M50 82 V94 M36 94 H64", sw=4) + path("M18 26 q-6 6 0 12 M82 26 q6 6 0 12", sw=3)
