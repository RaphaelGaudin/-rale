"""Illustrations du niveau B2 (compléments et nouveaux thèmes)."""
from .kit import *  # noqa: F401,F403
from .a1 import ART as A1
from .a2 import ART as A2
from .b1 import ART as B1
from .b2 import ART as B2
from .a1x import ART as A1X
from .a2x import ART as A2X
from .b1x import ART as B1X, screen, bill

ART = {}
X = {**A1, **A2, **B1, **B2, **A1X, **A2X, **B1X}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


def flag_mx(x, y, w=24):
    h = w * 0.66
    return rect(x, y, w, h, WHITE, sw=1.8) + rect(x, y, w / 3, h, GREEN, sw=1.8) + rect(x + 2 * w / 3, y, w / 3, h, RED, sw=1.8) + \
        circle(x + w / 2, y + h / 2, w * 0.08, BROWN, stroke=False)


def scale_icon(cx=50, cy=50, tilt=0, c=GOLD):
    return path(f"M{cx} {cy - 30} V{cy + 30} M{cx - 18} {cy + 30} H{cx + 18}", sw=4) + \
        group(f"rotate({tilt} {cx} {cy - 24})", path(f"M{cx - 32} {cy - 24} H{cx + 32}", sw=3.6) +
              path(f"M{cx - 42} {cy} Q{cx - 32} {cy + 10} {cx - 22} {cy}Z M{cx - 32} {cy - 24} L{cx - 42} {cy} M{cx - 32} {cy - 24} L{cx - 22} {cy}", c, sw=2.4) +
              path(f"M{cx + 22} {cy} Q{cx + 32} {cy + 10} {cx + 42} {cy}Z M{cx + 32} {cy - 24} L{cx + 22} {cy} M{cx + 32} {cy - 24} L{cx + 42} {cy}", c, sw=2.4))


def crack(x, y, s=1.0, c=INK):
    return group(f"translate({x} {y}) scale({s})", path("M0 0 L8 10 L2 18 L12 30 L6 40", stroke=c, sw=3.4))


# ── La sociedad ──

@art("corrupcion")
def _():
    return hand(28, 90, 0.6, rot=30) + hand(72, 90, 0.6, rot=-30, fill=SKIN2) + bill(32, 30, 36, -10) + text(80, 22, "$", 14, DGREEN)


@art("encuesta")
def _():
    return rect(10, 10, 80, 80, WHITE, rx=6) + rect(20, 60, 12, 22, BLUE, sw=2) + rect(38, 40, 12, 42, RED, sw=2) + rect(56, 50, 12, 32, GREEN, sw=2) + \
        rect(74, 28, 8, 54, GOLD, sw=2) + text(30, 30, "%", 18, NAVY)


@art("partido")
def _():
    return path("M20 92 V14", sw=3.4) + path("M20 14 Q44 6 60 16 Q76 24 90 16 V52 Q76 60 60 52 Q44 42 20 50Z", PURPLE) + \
        star(54, 32, 9, GOLD, sw=2) + person(70, 58, 0.36, shirt=PURPLE) + person(44, 60, 0.32, shirt=PURPLE, skin=SKIN2, hair_style="long", hair_color=BLACK)


@art("diputado")
def _():
    return rect(6, 70, 88, 24, BROWN) + person(50, 0, 0.82, skin=SKIN2, shirt=NAVY, hair_style="short", hair_color=GREY, glasses=True,
                                                extra_front=path("M44 66 L50 76 L56 66Z", WHITE, sw=2) + path("M48 72 L50 92 L52 72Z", RED, sw=1.8)) + \
        rect(72, 50, 6, 22, DGREY, sw=1.6) + circle(75, 48, 5, GREY, sw=1.6) + flag_mx(10, 46, 22)


@art("seguridad")
def _():
    return path("M50 8 L84 20 V48 Q84 76 50 92 Q16 76 16 48 V20Z", BLUE) + path("M50 18 L74 26 V48 Q74 68 50 80Z", LBLUE, sw=2) + \
        rect(38, 46, 24, 22, GOLD, rx=3) + path("M42 46 V38 Q50 28 58 38 V46", sw=3.4) + dot(50, 56, 3)


@art("justicia")
def _():
    return scale_icon(50, 52, 0)


@art("reforma")
def _():
    return paper(14, 8, 56, 82, lines=4) + text(42, 24, "LEY", 11, NAVY) + group("rotate(30 74 50)", rect(68, 18, 12, 54, ORANGE, rx=3) + poly([(68, 72), (74, 84), (80, 72)], TAN, sw=2)) + \
        path("M24 62 L56 62", stroke=RED, sw=3) + path("M24 72 q8 -6 16 0 t16 0", stroke=GREEN, sw=3)


@art("candidata")
def _():
    return person(shirt=RED, hair_style="long", hair_color=BLACK, extra_front=path("M44 66 L50 74 L56 66", stroke=WHITE, sw=2.4)) + \
        rect(66, 12, 30, 22, WHITE, rx=3, sw=2.4) + text(81, 28, "¡Vota!", 8, RED) + path("M81 34 V52", sw=2.4) + star(14, 18, 7, GOLD, sw=2)


# ── El medio ambiente ──

@art("escasez-de-agua")
def _():
    return rect(0, 70, 100, 30, "#E8C07A", stroke=False) + crack(30, 72, 0.6, BROWN) + crack(66, 74, 0.5, BROWN) + \
        path("M50 10 Q30 40 30 52 Q30 70 50 70 Q70 70 70 52 Q70 40 50 10Z", "none", stroke=BLUE, sw=3, extra='stroke-dasharray="6 5"') + \
        path("M50 50 q-6 8 0 12 q6 -4 0 -12z", BLUE, sw=2) + cross(78, 22, 10)


@art("emisiones")
def _():
    return rect(14, 46, 20, 50, GREY) + rect(40, 30, 18, 66, GREY) + rect(4, 84, 92, 12, DGREY) + \
        circle(24, 34, 10, DGREY, extra='opacity="0.8"') + circle(36, 22, 13, DGREY, extra='opacity="0.8"') + circle(54, 16, 12, GREY, extra='opacity="0.8"') + \
        circle(70, 10, 9, LGREY, extra='opacity="0.8"') + text(78, 60, "CO₂", 14, DGREY)


@art("plastico")
def _():
    return rect(0, 60, 100, 40, BLUE, stroke=False) + path("M0 64 q10 -5 20 0 t20 0 t20 0 t20 0 t20 0", stroke=LBLUE, sw=3) + \
        use(X["botella"], 10, 30, 0.5) + group("rotate(70 64 68)", path("M54 56 H74 L78 82 H50Z", "#DDEFFF", sw=2.4)) + \
        path("M60 20 Q48 30 52 44 Q66 46 72 34 Q76 24 60 20Z", "#DDEFFF", sw=2.4) + cross(86, 18, 9)


@art("deforestacion")
def _():
    return rect(0, 80, 100, 20, "#C9A06A", stroke=False) + use(X["arbol"], 0, 0, 0.6) + \
        rect(52, 66, 16, 16, BROWN) + ellipse(60, 66, 8, 3, TAN) + rect(76, 70, 14, 12, BROWN) + ellipse(83, 70, 7, 3, TAN) + \
        group("rotate(-30 70 40)", rect(66, 24, 6, 34, BROWN, rx=2) + path("M60 22 H80 V32 Q70 36 60 32Z", LGREY))


@art("incendio-forestal")
def _():
    tree = lambda x: poly([(x, 30), (x + 14, 70), (x - 14, 70)], DGREEN) + rect(x - 3, 70, 6, 14, BROWN, sw=2)
    flame = lambda x, y, s: group(f"translate({x} {y}) scale({s})", path("M0 0 Q-16 -14 -6 -36 Q0 -20 6 -26 Q18 -8 12 0Z", ORANGE) + path("M0 -2 Q-6 -10 -2 -18 Q4 -10 6 -6Z", YELLOW, sw=1.8))
    return rect(0, 0, 100, 100, "#FFD6C2", stroke=False) + tree(24) + tree(52) + tree(80) + flame(30, 84, 1.1) + flame(60, 80, 1.3) + flame(84, 86, 0.9) + \
        rect(0, 84, 100, 16, "#8E7A6A", stroke=False)


@art("biodiversidad")
def _():
    return circle(50, 50, 40, LGREEN) + use(X["mariposa"], 4, 6, 0.4) + use(X["ajolote"], 50, 10, 0.42) + use(X["jaguar"], 8, 50, 0.42) + \
        use(X["colibri"], 52, 52, 0.42)


@art("smog")
def _():
    return rect(0, 0, 100, 100, "#C8C0A8", stroke=False) + use(X["edificio"], 0, 20, 0.8) + \
        rect(0, 0, 100, 100, "#B0A888", stroke=False, extra='opacity="0.5"') + circle(78, 22, 10, "#E8D8A0", stroke=False) + \
        path("M0 40 q20 -8 40 0 t40 0 t40 0", stroke=WHITE, sw=4, extra='opacity="0.6"') + path("M0 60 q20 -8 40 0 t40 0 t40 0", stroke=WHITE, sw=4, extra='opacity="0.5"')


@art("composta")
def _():
    return path("M14 40 H86 L80 92 H20Z", "#6E3F22") + rect(10, 32, 80, 10, DGREEN, rx=3) + \
        path("M30 56 q4 -6 10 -2 M54 66 q6 -4 10 2 M36 78 q4 -4 10 0", stroke="#C9A06A", sw=3) + \
        path("M50 32 V14 M50 22 Q40 12 34 16 Q40 26 50 22 M50 18 Q60 8 66 12 Q60 22 50 18", stroke=GREEN, sw=3) + \
        path("M60 50 c4 -4 8 4 12 0", stroke=PINK, sw=3)


# ── El arte ──

@art("exposicion")
def _():
    return rect(0, 76, 100, 24, TAN, stroke=False) + rect(8, 16, 34, 28, GOLD) + rect(12, 20, 26, 20, LBLUE, sw=2) + circle(20, 28, 4, YELLOW, sw=1.6) + \
        rect(56, 10, 36, 40, GOLD) + rect(60, 14, 28, 32, PINK, sw=2) + path("M62 42 L72 28 L84 42Z", GREEN, sw=2) + \
        person(30, 46, 0.36, shirt=BLUE) + person(70, 46, 0.36, skin=SKIN2, shirt=RED, hair_style="long", hair_color=BLACK)


@art("grabado")
def _():
    return rect(10, 10, 80, 80, CREAM) + rect(18, 18, 64, 64, INK, stroke=False) + use(X["calavera"], 22, 22, 0.56) + \
        rect(18, 18, 64, 64, "none", stroke=CREAM, sw=1.4)


@art("muralismo")
def _():
    return rect(4, 14, 92, 64, "#F2C49B") + path("M4 78 V50 Q26 40 40 56 Q56 30 72 46 Q86 54 96 40 V78Z", ORANGE, sw=2) + \
        person(28, 28, 0.42, skin=SKIN3, shirt=RED, hair_style="short", hair_color=BLACK) + person(64, 22, 0.46, skin=SKIN2, shirt=BLUE, hair_style="long", hair_color=BLACK) + \
        circle(84, 26, 7, YELLOW, sw=2) + rect(0, 78, 100, 6, DGREY) + path("M84 84 V96 M90 84 V96", sw=2.4)


@art("fotografia")
def _():
    return rect(10, 28, 80, 54, DGREY, rx=8) + rect(30, 18, 24, 12, DGREY, rx=3) + circle(50, 56, 20, LGREY) + circle(50, 56, 13, NAVY) + \
        circle(45, 51, 4, WHITE, stroke=False) + rect(72, 34, 10, 6, YELLOW, rx=1.4, sw=1.6) + sparkle(86, 14, 7)


@art("danza")
def _():
    return circle(50, 16, 9, SKIN) + path("M42 12 Q50 2 58 10", BLACK, sw=2.4) + path("M50 26 L48 48", stroke=PINK, sw=8) + \
        path("M48 48 Q30 54 24 70 Q48 62 72 70 Q66 54 48 48Z", PINK) + path("M50 30 L24 20 M50 30 L80 14", sw=4) + \
        path("M46 64 L38 94 M52 64 L74 82", sw=4) + motion(84, 40, 2, 6, 6)


@art("novela")
def _():
    return rect(20, 10, 56, 80, RED, rx=4) + rect(20, 10, 10, 80, DRED, rx=3) + rect(36, 24, 32, 24, CREAM, rx=2, sw=2) + \
        path("M42 32 h20 M42 40 h14", stroke=GREY, sw=2.4) + rect(76, 14, 6, 72, CREAM, sw=2) + path("M60 10 V34 L64 30 L68 34 V10", GOLD, sw=1.8)


@art("galeria")
def _():
    frame = lambda x, y, w, h, c: rect(x, y, w, h, WHITE) + rect(x + 4, y + 4, w - 8, h - 8, c, sw=2)
    return rect(0, 0, 100, 100, CREAM, stroke=False) + rect(0, 82, 100, 18, BROWN, stroke=False) + \
        frame(6, 20, 26, 34, LBLUE) + frame(38, 12, 26, 26, PINK) + frame(70, 20, 24, 40, LGREEN) + frame(38, 44, 26, 24, YELLOW) + \
        path("M0 82 H100", sw=2.4)


@art("barro-negro")
def _():
    return path("M38 10 H62 V20 Q86 34 84 60 Q82 88 50 90 Q18 88 16 60 Q14 34 38 20Z", "#2B2A30") + \
        path("M24 54 Q50 64 76 54", stroke=GREY, sw=2.4) + "".join(circle(x, 60, 2.4, "none", stroke=GREY, sw=1.6) for x in (34, 44, 56, 66)) + \
        path("M28 36 q4 -6 10 -8", stroke=DGREY, sw=3.4)


# ── La historia ──

@art("virreinato")
def _():
    return use(X["iglesia"], 0, 14, 0.8) + path("M66 18 L72 6 L78 14 L84 4 L90 14 L96 6 L100 18Z", GOLD) + rect(66, 18, 34, 6, GOLD)


@art("tlatoani")
def _():
    feathers = "".join(path(f"M50 30 L{50 + 34 * c} {30 - 26 * s}", stroke=cc, sw=6) for c, s, cc in
                       [(-1, 0.2, GREEN), (-0.7, 0.7, TEAL), (-0.3, 1, GREEN), (0.3, 1, TEAL), (0.7, 0.7, GREEN), (1, 0.2, TEAL)])
    return feathers + person(skin=SKIN3, shirt=TEAL, hair_style="short", hair_color=BLACK,
                             extra_front=rect(30, 24, 40, 8, GOLD, rx=2) + path("M30 70 Q50 86 70 70", stroke=GOLD, sw=4) + circle(50, 80, 4, RED, sw=1.6))


@art("guerra")
def _():
    sword = lambda r: group(f"rotate({r} 50 50)", path("M48 8 L52 8 L54 66 H46Z", LGREY) + rect(36, 64, 28, 6, GOLD, rx=2) + rect(46, 70, 8, 18, BROWN, rx=2))
    return sword(-35) + sword(35) + path("M20 90 l6 -8 l6 8 M70 90 l6 -8 l6 8", stroke=ORANGE, sw=3)


@art("constitucion")
def _():
    return path("M18 14 H74 V86 H18Z", CREAM) + ellipse(18, 50, 6, 38, TAN) + ellipse(76, 50, 6, 38, TAN) + \
        text(46, 30, "1917", 11, DBROWN) + path("M28 42 h36 M28 50 h30 M28 58 h36 M28 66 h26", stroke=BROWN, sw=2.4) + \
        circle(60, 76, 7, RED, sw=2) + path("M56 82 l-2 10 M64 82 l2 10", stroke=RED, sw=2.4)


@art("templo")
def _():
    return poly([(6, 90), (94, 90), (82, 70), (18, 70)], "#C9A06A") + poly([(18, 70), (82, 70), (72, 52), (28, 52)], "#D9B47A") + \
        poly([(28, 52), (72, 52), (64, 36), (36, 36)], "#E8C88A") + rect(38, 18, 24, 18, "#B5652F") + rect(46, 24, 8, 12, INK, stroke=False) + \
        path("M50 90 V36", stroke="#8E6A3A", sw=6) + path("M36 18 L50 8 L64 18Z", RED)


@art("mestizaje")
def _():
    return circle(36, 50, 26, SKIN3, extra='opacity="0.85"') + circle(64, 50, 26, SKIN, extra='opacity="0.85"') + \
        path("M50 28 Q60 50 50 72 Q40 50 50 28Z", SKIN2, sw=2.4) + heart(50, 50, 6, RED, sw=1.8)


@art("caudillo")
def _():
    return person(skin=SKIN2, shirt=BROWN, hair_style="short", hair_color=BLACK, mustache=True,
                  extra_front=use(X["sombrero"], 14, -4, 0.72) + path("M26 70 L74 100", stroke=DBROWN, sw=4) +
                  "".join(rect(28 + i * 9, 72 + i * 5.6, 5, 7, GOLD, rot=33, sw=1.4) for i in range(5)))


@art("petroleo")
def _():
    return rect(0, 84, 100, 16, "#8E7A6A", stroke=False) + path("M22 84 L40 20 L58 84", sw=3.6) + path("M28 62 H52 M33 44 H47", sw=2.4) + \
        path("M62 50 L92 34", stroke=DGREY, sw=6) + path("M74 44 V84", sw=4) + rect(60, 70, 28, 14, DGREY, rx=2) + \
        path("M86 16 Q76 32 76 40 Q76 50 86 50 Q96 50 96 40 Q96 32 86 16Z", BLACK, sw=2)


# ── Los medios ──

@art("censura")
def _():
    return paper(14, 10, 60, 80, lines=0) + "".join(rect(22, y, 44 if i % 2 else 34, 7, BLACK if i in (1, 3) else LGREY, stroke=False) for i, y in enumerate(range(24, 80, 11))) + \
        rect(56, 54, 36, 16, RED, rx=3, rot=-20) + text(74, 66, "NO", 11, WHITE)


@art("periodista")
def _():
    return person(shirt=TAN, hair_style="short", hair_color=DBROWN, glasses=True,
                  extra_front=rect(64, 58, 24, 30, WHITE, rx=2, sw=2.4) + path("M68 66 h16 M68 74 h12", stroke=GREY, sw=2) +
                  rect(28, 74, 20, 14, BLUE, rx=2, sw=2) + text(38, 84, "PRENSA", 4, WHITE))


@art("fuente")
def _():
    return paper(10, 20, 44, 60, lines=3) + circle(66, 44, 18, LBLUE) + circle(66, 44, 18, "none", sw=4) + \
        path("M78 58 L92 74", sw=7) + check(66, 44, 8)


@art("portada")
def _():
    return rect(14, 6, 72, 88, WHITE, rx=2) + rect(20, 12, 60, 12, BLACK, rx=1, stroke=False) + text(50, 22, "EL DIARIO", 8, WHITE) + \
        rect(20, 30, 60, 12, RED, rx=1, stroke=False) + rect(20, 48, 30, 26, LBLUE, sw=2) + \
        path("M56 50 h22 M56 58 h22 M56 66 h18 M20 82 h58", stroke=GREY, sw=2.4)


@art("algoritmo")
def _():
    nodes = [(20, 20), (50, 20), (80, 20), (35, 50), (65, 50), (50, 80)]
    edges = [(0, 3), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
    return "".join(line(*nodes[a], *nodes[b], sw=2.6) for a, b in edges) + "".join(circle(x, y, 9, c) for (x, y), c in zip(nodes, [BLUE, PURPLE, BLUE, TEAL, TEAL, ORANGE])) + \
        text(50, 84, "1", 9, WHITE)


@art("meme")
def _():
    return rect(10, 8, 80, 84, WHITE, rx=4) + text(50, 22, "CUANDO...", 9) + face(50, 54, 22, mood="cool") + text(50, 86, "JAJA", 10) + \
        rect(10, 8, 80, 84, "none", rx=4)


@art("audiencia")
def _():
    heads = "".join(circle(x, y, 7, c, sw=2) for x, y, c in [(14, 80, DBROWN), (30, 82, BLACK), (46, 80, BROWN), (62, 82, BLACK), (78, 80, DBROWN), (92, 82, BLACK),
                                                             (22, 66, BLACK), (38, 66, DBROWN), (54, 66, BROWN), (70, 66, BLACK), (86, 66, DBROWN)])
    return rect(20, 8, 60, 40, DGREY, rx=4) + rect(24, 12, 52, 32, LBLUE, rx=2, sw=2) + path("M40 28 l10 -6 l10 6 v-12", stroke=RED, sw=3) + heads


@art("chisme")
def _():
    return person(30, 26, 0.6, shirt=PINK, hair_style="long", hair_color=DBROWN, extra_front=hand(70, 56, 0.4, rot=-10)) + \
        person(72, 26, 0.6, skin=SKIN2, shirt=YELLOW, hair_style="bun", hair_color=BLACK, mood="plead") + \
        bubble(26, 4, 32, 18) + text(42, 17, "psst", 9, PURPLE)


# ── La economía ──

@art("ahorro")
def _():
    return ellipse(48, 58, 34, 26, PINK) + circle(80, 52, 10, PINK) + ellipse(82, 54, 5, 4, LPINK, sw=2) + dot(70, 44, 2.6) + \
        path("M36 34 L30 22 L44 30Z", PINK) + rect(26, 78, 8, 12, PINK, sw=2.4) + rect(58, 78, 8, 12, PINK, sw=2.4) + \
        rect(40, 30, 16, 4, DRED, rx=2, sw=1.6) + coin(48, 16, 10)


@art("salario-minimo")
def _():
    return paper(12, 10, 52, 74, lines=3) + text(38, 72, "$ mín.", 10, DGREEN) + bill(46, 56, 42, -8) + arrow(86, 18, 86, 40, RED, 3)


@art("inflacion")
def _():
    return use(X["tiendita"], 0, 22, 0.6) + tag(54, 20, 38, "$20", LGREY, 12, GREY) + path("M56 32 H90", stroke=RED, sw=2.4) + \
        tag(54, 54, 38, "$35", RED, 13, WHITE) + arrow(30, 18, 50, 4, RED, 3)


@art("tipo-de-cambio")
def _():
    return circle(30, 40, 20, "#9ED69A") + text(30, 47, "$", 20, DGREEN) + circle(70, 60, 20, LBLUE) + text(70, 67, "€", 20, NAVY) + \
        path("M52 28 Q70 20 76 36", stroke=ORANGE, sw=3.4) + path("M72 32 L76 38 L80 30", stroke=ORANGE, sw=3) + \
        path("M48 72 Q30 80 24 64", stroke=ORANGE, sw=3.4) + path("M28 68 L24 62 L20 70", stroke=ORANGE, sw=3)


@art("exportacion")
def _():
    return rect(0, 70, 100, 30, BLUE, stroke=False) + path("M10 56 H90 L82 76 H18Z", DGREY) + \
        rect(20, 40, 18, 16, RED, sw=2.4) + rect(40, 40, 18, 16, ORANGE, sw=2.4) + rect(60, 40, 18, 16, GREEN, sw=2.4) + rect(30, 24, 18, 16, TEAL, sw=2.4) + \
        flag_mx(70, 14, 20) + arrow(84, 86, 100, 86, WHITE, 3)


@art("quiebra")
def _():
    return path("M10 30 L30 46 L50 36 L70 66 L90 86", stroke=RED, sw=5) + arrow(80, 76, 92, 88, RED, 5) + \
        use(X["empresa"], 4, 50, 0.44) + crack(20, 62, 0.6, RED) + text(76, 30, "$0", 16, RED)


@art("socio")
def _():
    return rect(0, 0, 100, 100, "none", stroke=False) + person(26, 20, 0.6, shirt=NAVY, hair_style="short", hair_color=BLACK) + \
        person(74, 20, 0.6, skin=SKIN2, shirt=GREY, hair_style="long", hair_color=DBROWN) + \
        path("M38 76 Q50 66 62 76", SKIN, sw=2.6) + rect(36, 10, 28, 16, WHITE, rx=3, sw=2) + text(50, 22, "50/50", 8, NAVY)


@art("factura")
def _():
    return rect(22, 6, 56, 84, WHITE, rx=2) + path("M22 90 l7 -6 l7 6 l7 -6 l7 6 l7 -6 l7 6 l7 -6 l7 6", WHITE) + \
        text(50, 22, "FACTURA", 8, NAVY) + path("M30 34 h24 M30 44 h30 M30 54 h20", stroke=GREY, sw=2.4) + \
        path("M30 66 H70", sw=2) + text(62, 78, "$1,200", 9, DGREEN) + rect(56, 30, 16, 16, LGREY, sw=1.6)


# ── Las relaciones ──

@art("ligue")
def _():
    return person(30, 24, 0.62, shirt=BLUE, hair_style="spiky", hair_color=BLACK) + \
        person(72, 24, 0.62, skin=SKIN2, shirt=RED, hair_style="long", hair_color=DBROWN) + \
        path("M38 18 Q50 4 62 18", stroke=PINK, sw=2.6, extra='stroke-dasharray="4 4"') + heart(50, 10, 6, PINK, sw=1.8) + use(X["celular"], 2, 60, 0.3)


@art("beso")
def _():
    return path("M10 50 Q30 26 50 36 Q70 26 90 50 Q70 74 50 74 Q30 74 10 50Z", RED) + path("M10 50 Q50 58 90 50", sw=3) + \
        heart(80, 18, 8, PINK, sw=2) + heart(18, 82, 6, PINK, sw=1.8) + path("M30 38 q8 -4 14 0", stroke="#FF9A8F", sw=3)


@art("divorcio")
def _():
    return path("M50 92 C20 72 6 50 14 32 C22 16 42 18 50 32", RED) + path("M50 32 C58 18 78 16 86 32 C94 50 80 72 50 92", RED) + \
        path("M50 32 L44 46 L54 56 L46 70 L50 92", stroke=CREAM, sw=5) + path("M50 32 L44 46 L54 56 L46 70 L50 92", sw=2.4)


@art("pareja")
def _():
    return person(34, 18, 0.66, shirt=TEAL, hair_style="short", hair_color=BLACK) + person(66, 18, 0.66, skin=SKIN2, shirt=PINK, hair_style="long", hair_color=DBROWN) + \
        heart(50, 14, 8, RED, sw=2)


@art("apapacho")
def _():
    return person(40, 18, 0.7, shirt=ORANGE, hair_style="long", hair_color=DBROWN) + person(62, 22, 0.66, skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=BLACK,
                                                                                         extra_front=path("M22 80 Q4 76 14 60 Q24 70 34 72", SKIN2, sw=2.6)) + \
        heart(86, 16, 7, PINK, sw=2) + heart(14, 22, 5, RED, sw=1.6)


@art("desamor")
def _():
    return face(50, 58, 32, mood="sad", skin="#D8E6FF") + path("M50 22 C38 10 20 16 26 28 L50 44 L74 28 C80 16 62 10 50 22Z", RED, sw=2) + \
        path("M50 22 L46 30 L54 36 L50 44", stroke=WHITE, sw=2.4) + use(X["lluvia"], 66, 62, 0.34)


@art("infidelidad")
def _():
    return person(50, 16, 0.66, shirt=NAVY, hair_style="short", hair_color=BLACK, mood="neutral") + \
        path("M68 42 C60 36 62 26 68 30 C74 26 76 36 68 42Z", PINK, sw=2) + text(18, 30, "?", 20, RED) + text(84, 24, "!", 18, RED)


@art("amistad")
def _():
    return use(X["amigo"], 0, 0, 1.0) + sparkle(14, 16, 6) + sparkle(86, 14, 5, PINK)


# ── Modismos ──

@art("ser-un-cero-a-la-izquierda")
def _():
    return text(28, 66, "0", 54, GREY) + text(68, 66, "7", 54, BLUE) + arrow(30, 84, 10, 84, RED, 3)


@art("tirar-la-toalla")
def _():
    return rect(0, 0, 100, 100, "none", stroke=False) + path("M6 80 H94", stroke=RED, sw=4) + path("M6 70 H94", stroke=WHITE, sw=4) + path("M6 70 H94", sw=1.4) + \
        group("rotate(25 54 40)", path("M36 20 H72 V60 Q60 66 54 58 Q46 66 36 60Z", WHITE) + path("M36 28 H72", stroke=BLUE, sw=3)) + motion(22, 14, 2, 6, 6) + \
        hand(20, 52, 0.38, rot=-30)


@art("aventar-los-perros")
def _():
    return person(30, 22, 0.62, shirt=RED, hair_style="spiky", hair_color=BLACK) + use(X["perro"], 48, 52, 0.4) + \
        person(78, 22, 0.56, skin=SKIN2, shirt=PURPLE, hair_style="long", hair_color=DBROWN, mood="neutral") + heart(52, 18, 7, PINK, sw=2)


@art("sacar-de-onda")
def _():
    return face(50, 56, 32, mood="surprised") + path("M8 22 q8 -8 16 0 t16 0 t16 0 t16 0 t16 0", stroke=BLUE, sw=3.4) + text(86, 50, "?!", 14, RED)


@art("hacerse-bolas")
def _():
    return circle(50, 56, 32, "none", stroke=RED, sw=4) + path("M24 44 Q50 70 76 44 M26 70 Q50 30 76 68 M34 28 Q60 60 44 86 M66 28 Q42 60 58 86", stroke=RED, sw=3) + \
        path("M80 30 Q92 22 96 30", stroke=RED, sw=3) + text(16, 22, "?", 16, PURPLE)


@art("estar-en-chino")
def _():
    return rect(10, 14, 80, 60, WHITE, rx=8) + text(50, 54, "中文", 28, RED) + face(80, 80, 14, mood="nervous") + text(22, 92, "?", 16, PURPLE)


@art("dar-lata")
def _():
    return path("M30 20 H70 V84 H30Z", LGREY) + ellipse(50, 20, 20, 5, GREY) + ellipse(50, 84, 20, 5, GREY) + rect(30, 38, 40, 26, RED, sw=2.4) + \
        path("M14 30 l-8 -4 M14 50 h-10 M86 30 l8 -4 M86 50 h10", sw=3) + text(50, 56, "!", 16, WHITE)


@art("irsele-el-santo-al-cielo")
def _():
    return face(50, 64, 28, mood="bored") + circle(50, 18, 12, "none", stroke=GOLD, sw=4) + arrow(50, 32, 50, 4, LBLUE, 2.4) + \
        bubble(66, 14, 30, 22) + text(81, 30, "...", 14, GREY)


# ── La vida urbana ──

@art("gentrificacion")
def _():
    return rect(4, 56, 26, 36, PINK) + rect(10, 64, 8, 10, LBLUE, sw=2) + rect(36, 30, 26, 62, "#C8D4E8") + building_windows(40, 36, 2, 4, 8, 8, 2, 4, LBLUE) + \
        rect(68, 58, 28, 34, YELLOW) + rect(74, 64, 8, 10, LBLUE, sw=2) + arrow(30, 18, 70, 18, RED, 3) + text(76, 22, "$$$", 10, DGREEN)


@art("ciclovia")
def _():
    return rect(0, 50, 100, 50, DGREY, stroke=False) + rect(0, 50, 100, 22, GREEN) + path("M0 72 H100", stroke=WHITE, sw=3) + \
        use(X["bicicleta"], 24, 30, 0.5) + path("M10 86 h12 M40 86 h12 M70 86 h12", stroke=WHITE, sw=3)


@art("embotellamiento")
def _():
    return use(A2X["trafico"], 0, 10, 0.9) + path("M10 10 l6 6 M24 6 v8", stroke=RED, sw=2.6) + text(84, 14, "¡pi!", 10, RED)


@art("rascacielos")
def _():
    return rect(36, 6, 28, 88, "#8AA4D6") + path("M50 6 V0", sw=2) + building_windows(40, 12, 2, 8, 8, 6, 4, 4, LYELLOW) + \
        rect(8, 40, 24, 54, LPURPLE) + building_windows(12, 46, 2, 5, 6, 6, 4, 4) + rect(68, 26, 24, 68, TEAL) + building_windows(72, 32, 2, 6, 6, 6, 4, 4) + \
        rect(0, 92, 100, 8, DGREY, stroke=False)


@art("periferia")
def _():
    return circle(50, 50, 42, LGREEN) + circle(50, 50, 22, LGREY, sw=2.4) + use(X["edificio"], 36, 34, 0.28) + \
        "".join(rect(x, y, 8, 8, c, sw=1.8) for x, y, c in [(16, 30, ORANGE), (80, 34, PINK), (20, 70, YELLOW), (74, 72, TEAL), (48, 84, ORANGE), (48, 12, PINK)])


@art("vendedor-ambulante")
def _():
    return person(40, 18, 0.66, skin=SKIN3, shirt=ORANGE, hair_style="short", hair_color=BLACK, extra_front=hat("straw", 50, 22)) + \
        path("M66 70 H96 L92 90 H70Z", RED) + "".join(circle(x, 66, 5, c, sw=1.8) for x, c in [(72, YELLOW), (82, GREEN), (90, PINK)]) + \
        circle(72, 94, 4, DGREY, sw=1.6) + circle(90, 94, 4, DGREY, sw=1.6)


@art("segundo-piso")
def _():
    return rect(0, 76, 100, 24, DGREY, stroke=False) + rect(0, 34, 100, 12, GREY) + rect(14, 46, 10, 30, LGREY) + rect(76, 46, 10, 30, LGREY) + \
        use(A2X["coche"], 30, 6, 0.36) + use(A2X["coche"], 54, 54, 0.36) + path("M0 40 H100", stroke=YELLOW, sw=1.6, extra='stroke-dasharray="6 5"')


@art("transporte-publico")
def _():
    return use(X["metro"], 0, 10, 0.55) + use(A2X["pesero"], 44, 40, 0.56) + use(X["camion"], 0, 50, 0.48)


@art("vivienda")
def _():
    return rect(10, 40, 34, 52, ORANGE) + poly([(6, 42), (27, 22), (48, 42)], RED) + rect(20, 70, 12, 22, BROWN, sw=2) + rect(16, 50, 10, 10, LBLUE, sw=2) + \
        rect(52, 20, 40, 72, "#C8D4E8") + building_windows(56, 26, 3, 5, 8, 8, 4, 5, LYELLOW) + rect(66, 80, 12, 12, BROWN, sw=2)


@art("colonia-popular")
def _():
    houses = [(2, 50, PINK), (22, 42, YELLOW), (42, 54, TEAL), (62, 44, ORANGE), (80, 52, LPURPLE)]
    return path("M0 96 Q50 40 100 96Z", "#C9A06A") + "".join(rect(x, y, 18, 18, c, sw=2.4) + rect(x + 6, y + 6, 6, 6, LBLUE, sw=1.6) +
                                                         rect(x + 2, y - 4, 4, 4, GREY, stroke=False) for x, y, c in houses) + \
        path("M0 30 Q30 24 60 30 T100 26", stroke=INK, sw=1.4) + rect(60, 24, 18, 6, PINK, rx=1, sw=1.4)


@art("metrobus")
def _():
    return rect(0, 76, 100, 24, DGREY, stroke=False) + rect(4, 34, 92, 40, RED, rx=10) + building_windows(12, 42, 5, 1, 12, 14, 4) + \
        rect(4, 60, 92, 6, WHITE, sw=1.6) + circle(26, 76, 8, BLACK) + circle(74, 76, 8, BLACK) + rect(34, 22, 32, 12, WHITE, rx=3, sw=2) + text(50, 31, "MB", 9, RED)


@art("bache")
def _():
    return rect(0, 40, 100, 60, DGREY, stroke=False) + path("M0 70 H30 M44 70 H70 M84 70 H100", stroke=YELLOW, sw=3) + \
        path("M30 58 Q24 50 40 46 Q60 42 70 54 Q78 66 60 70 Q40 74 30 58Z", BLACK) + path("M36 56 Q50 50 62 58", stroke="#4A4A4A", sw=2.4) + \
        poly([(80, 40), (92, 18), (104, 40)], ORANGE) + path("M84 32 H100", stroke=WHITE, sw=3)


@art("ruido")
def _():
    return rect(4, 40, 24, 30, DGREY, rx=4) + path("M28 40 L52 22 V88 L28 70Z", GREY) + \
        path("M60 36 q10 18 0 36 M70 28 q16 26 0 52 M80 20 q22 34 0 68", sw=4) + text(84, 96, "¡!", 12, RED)


@art("plusvalia")
def _():
    return use(X["casa"], 0, 30, 0.6) + path("M60 80 L70 60 L80 66 L94 34", stroke=GREEN, sw=4) + arrow(84, 44, 94, 30, GREEN, 4) + coin(70, 24, 10)


@art("espacio-publico")
def _():
    return use(A2X["plaza"], 0, 0, 1.0) + person(16, 60, 0.3, shirt=RED) + person(84, 60, 0.3, skin=SKIN2, shirt=BLUE, hair_style="long", hair_color=BLACK)


@art("desarrollo-inmobiliario")
def _():
    return rect(30, 30, 34, 64, LGREY) + building_windows(34, 36, 3, 5, 6, 6, 4, 6, LBLUE) + path("M64 30 H70 V94", sw=2.4, extra='stroke-dasharray="4 3"') + \
        path("M80 94 V8 M80 12 H30 M80 12 L92 20", stroke=YELLOW, sw=4) + path("M80 94 V8 M80 12 H30", sw=1.4) + path("M40 12 V24", sw=1.6) + \
        rect(34, 24, 12, 6, ORANGE, sw=1.6) + rect(0, 94, 100, 6, DGREY, stroke=False)


# ── Los desastres naturales ──

@art("sismo")
def _():
    return use(X["edificio"], 0, 0, 1.0) + crack(42, 34, 0.9) + path("M4 96 L14 88 L24 96 L34 88 L44 96 L54 88 L64 96 L74 88 L84 96 L94 88", stroke=RED, sw=3.4) + \
        path("M2 30 q-4 6 0 12 M98 30 q4 6 0 12", sw=3)


@art("alerta-sismica")
def _():
    return rect(30, 40, 40, 50, GREY) + path("M20 40 Q50 0 80 40Z", RED) + circle(50, 30, 6, YELLOW, sw=2) + \
        path("M14 22 q-8 10 0 20 M86 22 q8 10 0 20 M6 14 q-12 18 0 34 M94 14 q12 18 0 34", stroke=RED, sw=3) + \
        rect(38, 54, 24, 20, DGREY, rx=3) + "".join(dot(x, y, 1.6, LGREY) for x in (44, 50, 56) for y in (60, 66))


@art("simulacro")
def _():
    return rect(6, 6, 88, 40, GREEN, rx=6) + path("M20 26 H50", stroke=WHITE, sw=4) + arrow(50, 26, 66, 26, WHITE, 4) + \
        circle(78, 18, 4, WHITE, stroke=False) + path("M78 22 L74 34 M76 26 L82 30 M74 34 L70 40 M74 34 L80 40", stroke=WHITE, sw=2.6) + \
        person(28, 52, 0.38, shirt=ORANGE) + person(52, 52, 0.38, skin=SKIN2, shirt=BLUE, hair_style="long", hair_color=BLACK) + person(76, 52, 0.38, shirt=PURPLE)


@art("inundacion")
def _():
    return use(X["casa"], 10, 0, 0.8) + rect(0, 56, 100, 44, BLUE, extra='opacity="0.85"') + \
        path("M0 60 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0", stroke=LBLUE, sw=3.4) + path("M0 78 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0", stroke=LBLUE, sw=3)


@art("incendio")
def _():
    flame = lambda x, y, s: group(f"translate({x} {y}) scale({s})", path("M0 0 Q-16 -14 -6 -36 Q0 -20 6 -26 Q18 -8 12 0Z", ORANGE) + path("M0 -2 Q-6 -10 -2 -18 Q4 -10 6 -6Z", YELLOW, sw=1.8))
    return use(X["casa"], 4, 20, 0.78) + flame(30, 46, 1.0) + flame(56, 34, 1.4) + flame(72, 52, 0.9) + \
        circle(70, 10, 8, GREY, extra='opacity="0.7"') + circle(84, 6, 6, GREY, extra='opacity="0.7"')


@art("escombros")
def _():
    return poly([(4, 92), (20, 60), (36, 70), (50, 44), (66, 66), (82, 56), (96, 92)], GREY) + \
        rect(24, 66, 18, 10, "#D9663A", rot=-20, sw=2) + rect(54, 58, 22, 10, "#D9663A", rot=15, sw=2) + rect(40, 78, 16, 8, LGREY, rot=-8, sw=2) + \
        path("M60 44 L74 30 M66 46 L84 38", stroke=DGREY, sw=4) + circle(24, 30, 8, LGREY, stroke=False, extra='opacity="0.7"') + circle(40, 22, 10, LGREY, stroke=False, extra='opacity="0.7"')


@art("rescatista")
def _():
    return person(shirt=ORANGE, hair_style="none", extra_front=hat("helmet", 50, 24) + path("M30 80 H70 M30 90 H70", stroke=WHITE, sw=3.4) +
                  rect(42, 76, 16, 10, WHITE, rx=2, sw=1.6) + path("M50 77 V85 M46 81 H54", stroke=RED, sw=2)) + use(X["perro"], 64, 58, 0.36)


@art("zona-de-menor-riesgo")
def _():
    return rect(10, 10, 80, 80, GREEN, rx=8) + text(50, 34, "ZONA", 10, WHITE) + circle(50, 60, 20, WHITE) + \
        "".join(circle(50 + 10 * c, 60 + 10 * s, 3.4, GREEN, stroke=False) for c, s in [(0, -1), (0.87, 0.5), (-0.87, 0.5)]) + \
        dot(50, 60, 3.4, GREEN) + path("M50 50 V60 M50 60 L58 66 M50 60 L42 66", stroke=GREEN, sw=2.4)


@art("mochila-de-emergencia")
def _():
    return use(A2X["mochila"], 0, 0, 1.0) + circle(50, 66, 10, WHITE, sw=2) + path("M50 60 V72 M44 66 H56", stroke=RED, sw=3.4) + \
        rect(72, 50, 10, 30, YELLOW, rx=3, sw=2) + circle(77, 48, 5, LYELLOW, sw=1.6)


@art("damnificado")
def _():
    return person(shirt=GREY, hair_style="short", hair_color=DBROWN, mood="plead",
                  extra_front=path("M20 104 Q20 74 34 70 L66 70 Q80 74 80 104", "#9ED6C9", sw=2.6) + path("M30 76 L70 100 M70 76 L30 100", stroke="#7CB8A8", sw=2)) + \
        crack(80, 14, 0.5)


@art("albergue")
def _():
    return poly([(4, 60), (50, 20), (96, 60)], LBLUE) + rect(14, 58, 72, 34, WHITE) + rect(42, 66, 16, 26, BROWN, sw=2) + \
        circle(50, 42, 10, WHITE, sw=2) + path("M50 36 V48 M44 42 H56", stroke=RED, sw=3.4) + rect(20, 66, 14, 12, LBLUE, sw=2) + rect(66, 66, 14, 12, LBLUE, sw=2)


@art("grieta")
def _():
    return rect(6, 6, 88, 88, "#E8DCC8", rx=4) + path("M40 6 L48 26 L38 40 L54 56 L44 72 L56 94", "none", stroke=INK, sw=5) + \
        path("M48 26 L62 30 M38 40 L26 44 M54 56 L66 62 M44 72 L32 76", sw=2.4)


@art("derrumbe")
def _():
    return rect(0, 86, 100, 14, "#8E7A6A", stroke=False) + path("M10 86 V36 H40 L46 50 L38 60 L48 86Z", LGREY) + building_windows(16, 42, 2, 2, 7, 7, 4, 6) + \
        rect(56, 74, 16, 10, LGREY, rot=-25) + rect(74, 70, 14, 10, LGREY, rot=20) + rect(60, 56, 10, 8, LGREY, rot=40, sw=2) + \
        circle(70, 30, 10, LGREY, stroke=False, extra='opacity="0.7"') + circle(84, 40, 8, LGREY, stroke=False, extra='opacity="0.7"')


@art("viveres")
def _():
    return path("M14 46 H86 V90 H14Z", TAN) + path("M14 46 L24 34 H76 L86 46", "#F0D9B0") + \
        use(X["botella"], 18, 6, 0.42) + rect(50, 26, 18, 22, RED, rx=3, sw=2.4) + rect(68, 30, 14, 18, YELLOW, rx=2, sw=2.4) + \
        circle(50, 68, 10, WHITE, sw=2) + path("M50 62 V74 M44 68 H56", stroke=RED, sw=3)


@art("voluntario")
def _():
    return person(skin=SKIN2, shirt=YELLOW, hair_style="long", hair_color=BLACK, extra_front=heart(50, 84, 8, RED, sw=2)) + hand(84, 34, 0.42, rot=8)


@art("replica")
def _():
    return use(X["casa"], 14, 10, 0.72) + path("M6 88 L14 82 L22 88 L30 82 L38 88 L46 82 L54 88 L62 82 L70 88 L78 82 L86 88 L94 82", stroke=ORANGE, sw=3) + \
        path("M4 30 q-4 6 0 12 M96 30 q4 6 0 12", sw=2.6) + text(84, 16, "2", 14, RED)


# ── La migración ──

@art("migrante")
def _():
    return person(skin=SKIN3, shirt=GREEN, hair_style="short", hair_color=BLACK, extra_back=rect(18, 64, 64, 40, ORANGE, rx=8), extra_front=hat("cap", 50, 26)) + \
        arrow(70, 20, 96, 20, BLUE, 3)


@art("remesa")
def _():
    return rect(0, 0, 100, 100, "none", stroke=False) + use(X["casa"], 52, 40, 0.48) + bill(4, 20, 36, -8) + \
        path("M24 50 Q40 80 64 64", stroke=GREEN, sw=3, extra='stroke-dasharray="5 4"') + arrow(56, 70, 64, 64, GREEN, 3) + coin(80, 20, 10)


@art("muro")
def _():
    return rect(0, 0, 100, 100, LBLUE, stroke=False) + "".join(rect(x, 24, 8, 76, "#9A8A7A", sw=2) for x in range(2, 100, 12)) + \
        path("M0 30 H100", sw=2.4) + rect(0, 88, 100, 12, "#E8C07A", stroke=False)


@art("visa")
def _():
    return use(X["pasaporte"], 0, 0, 0.8) + circle(70, 64, 20, "none", stroke=BLUE, sw=3.4) + text(70, 69, "VISA", 10, BLUE) + check(86, 20, 8)


@art("sueno-americano")
def _():
    return path("M14 76 Q4 76 4 64 Q4 52 18 52 Q18 34 38 34 Q50 26 62 36 Q82 32 84 50 Q96 52 96 64 Q96 76 84 76Z", WHITE) + \
        use(X["casa"], 26, 30, 0.46) + star(76, 18, 6, GOLD, sw=1.8) + coin(80, 60, 7)


@art("pocho")
def _():
    return person(skin=SKIN2, shirt=BLUE, hair_style="short", hair_color=BLACK) + bubble(62, 4, 36, 22) + text(80, 18, "¿Qué?", 8) + \
        bubble(2, 4, 36, 22, tail="right") + text(20, 18, "What?", 8)


@art("retorno")
def _():
    return use(A2["maleta"], 46, 30, 0.54) + use(X["casa"], 0, 30, 0.5) + path("M88 26 Q60 0 30 26", stroke=GREEN, sw=3.4) + \
        path("M36 18 L30 26 L40 30", stroke=GREEN, sw=3.4) + heart(56, 12, 5, RED, sw=1.6)


@art("deportacion")
def _():
    return use(A2["avion"], 0, 0, 0.7) + arrow(90, 80, 30, 80, RED, 4) + paper(68, 50, 26, 26, lines=2) + text(81, 70, "×", 12, RED)


@art("coyote")
def _():
    return path("M20 30 L28 8 L42 26 Z M80 30 L72 8 L58 26 Z", "#C9A06A") + path("M18 30 Q14 60 50 88 Q86 60 82 30 Q50 18 18 30Z", "#C9A06A") + \
        path("M36 60 Q50 74 64 60 L50 88Z", CREAM) + ellipse(50, 76, 6, 4, INK) + dot(36, 44, 3) + dot(64, 44, 3) + \
        path("M30 38 l10 4 M70 38 l-10 4", sw=2.6)


@art("asilo")
def _():
    return path("M50 8 L86 20 V46 Q86 74 50 90 Q14 74 14 46 V20Z", LBLUE) + person(50, 26, 0.48, skin=SKIN3, shirt=ORANGE, hair_style="long", hair_color=BLACK) + \
        path("M14 46 Q14 74 50 90 Q86 74 86 46", "none", sw=3.4)


@art("caravana")
def _():
    walker = lambda x, s, c, sk: person(x, 100 - 100 * s, s, skin=sk, shirt=c, hair_style="short", hair_color=BLACK)
    return rect(0, 84, 100, 16, "#E8C07A", stroke=False) + walker(14, 0.34, RED, SKIN3) + walker(32, 0.38, BLUE, SKIN2) + \
        walker(50, 0.42, GREEN, SKIN3) + walker(70, 0.38, ORANGE, SKIN2) + walker(88, 0.34, PURPLE, SKIN3) + arrow(20, 14, 80, 14, NAVY, 3)


@art("ciudadania")
def _():
    return rect(14, 10, 72, 80, CREAM, rx=4) + flag_mx(36, 18, 28) + path("M24 50 h52 M24 60 h40 M24 70 h46", stroke=GREY, sw=2.6) + \
        circle(70, 78, 10, GOLD, sw=2) + star(70, 78, 5, YELLOW, sw=1.4)


@art("jornalero")
def _():
    rows = "".join(path(f"M0 {y} Q50 {y - 6} 100 {y}", stroke=GREEN, sw=4) for y in (74, 84, 94))
    return rect(0, 68, 100, 32, "#A0623A", stroke=False) + rows + person(50, 0, 0.72, skin=SKIN3, shirt=WHITE, hair_style="short", hair_color=BLACK,
                                                                          extra_front=hat("straw", 50, 22)) + \
        path("M80 70 L70 40", stroke=BROWN, sw=3) + path("M66 40 Q70 32 78 36", stroke=GREY, sw=4)


@art("diaspora")
def _():
    return circle(50, 50, 40, LBLUE) + path("M18 34 Q30 26 40 36 Q44 50 32 56 Q22 54 18 34Z M56 22 Q72 18 80 34 Q72 42 60 38Z M58 58 Q70 54 76 66 Q70 78 60 74Z", LGREEN, sw=2) + \
        "".join(path(f"M30 46 Q{(30 + x) / 2} {min(46, y) - 18} {x} {y}", stroke=RED, sw=2, extra='stroke-dasharray="3 3"') + circle(x, y, 3, RED, sw=1.4) for x, y in [(68, 28), (68, 66), (50, 84)]) + \
        circle(30, 46, 4, GREEN, sw=1.6)


@art("bracero")
def _():
    return person(skin=SKIN3, shirt=TAN, hair_style="short", hair_color=BLACK, mustache=True, extra_front=hat("straw", 50, 22) +
                  path("M30 70 V104 M70 70 V104", stroke=BLUE, sw=4)) + text(80, 96, "1942", 9, DBROWN)



@art("chicano")
def _():
    return person(skin=SKIN2, shirt=WHITE, hair_style="short", hair_color=BLACK, mustache=True,
                  extra_front=path("M30 30 Q50 16 70 30 L70 34 H30Z", NAVY) + path("M24 36 H76", stroke=NAVY, sw=4)) + \
        flag_mx(4, 70, 20) + rect(76, 70, 20, 13, LBLUE, sw=1.8) + path("M76 74 h20 M76 78 h20", stroke=RED, sw=1.4)


# ── México indígena ──

@art("nahuatl")
def _():
    return bubble(10, 12, 80, 50) + text(50, 46, "Niltze!", 18, DGREEN) + \
        path("M18 76 q6 -6 12 0 M36 82 q6 -8 12 0", stroke=TEAL, sw=3) + use(X["codice"], 58, 58, 0.36)


@art("maya")
def _():
    glyph = lambda x, y, c: rect(x, y, 30, 30, c, rx=8) + circle(x + 10, y + 12, 4, CREAM, sw=1.6) + path(f"M{x + 6} {y + 22} h18", stroke=CREAM, sw=2.4) + \
        path(f"M{x + 18} {y + 8} q6 2 4 8", stroke=CREAM, sw=2.4)
    return glyph(12, 12, "#C9662F") + glyph(56, 12, TEAL) + glyph(12, 56, TEAL) + glyph(56, 56, "#C9662F")


@art("comunidad")
def _():
    return circle(50, 54, 34, "none", stroke=GOLD, sw=3, extra='stroke-dasharray="6 5"') + \
        "".join(person(50 + 32 * c, 22 + 32 * s, 0.3, skin=SKIN3, shirt=cc, hair_style=h, hair_color=BLACK)
                for c, s, cc, h in [(0, -0.4, RED, "long"), (0.9, 0.2, TEAL, "short"), (0.6, 0.9, PURPLE, "bun"), (-0.6, 0.9, GREEN, "short"), (-0.9, 0.2, ORANGE, "long")]) + \
        heart(50, 54, 8, RED, sw=2)


@art("bordado")
def _():
    flower = lambda x, y, c: "".join(circle(x + 7 * cc, y + 7 * ss, 4.6, c, sw=1.6) for cc, ss in [(1, 0), (-1, 0), (0, 1), (0, -1)]) + circle(x, y, 3.4, YELLOW, sw=1.4)
    return rect(8, 8, 84, 84, WHITE, rx=6) + rect(14, 14, 72, 72, "none", stroke=PINK, sw=2, extra='stroke-dasharray="3 3"') + \
        flower(32, 34, RED) + flower(66, 32, PURPLE) + flower(48, 64, BLUE) + path("M32 44 Q40 56 48 54 M66 42 Q60 56 52 56", stroke=GREEN, sw=2.4) + \
        path("M80 10 L92 2", sw=2) + path("M92 2 Q98 30 84 50", stroke=RED, sw=1.6)


@art("telar")
def _():
    threads = "".join(line(x, 20, x, 70, sw=2, color=c) for x, c in zip(range(22, 80, 6), [RED, YELLOW, TEAL, PINK] * 3))
    return rect(12, 10, 76, 12, BROWN) + rect(12, 70, 76, 12, BROWN) + threads + \
        path("M18 40 H82 M18 50 H82", stroke=PURPLE, sw=4) + path("M18 46 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4", stroke=ORANGE, sw=2.4) + \
        path("M8 82 L4 96 M92 82 L96 96", stroke=DBROWN, sw=4)


@art("milpa")
def _():
    return rect(0, 80, 100, 20, "#8E5A3A", stroke=False) + use(X["elote"], 2, 0, 0.6) + \
        path("M60 80 V50", stroke=GREEN, sw=3) + path("M60 60 Q46 50 50 40 Q62 46 60 60Z", GREEN, sw=2) + \
        circle(80, 70, 12, ORANGE) + path("M76 62 q4 -4 8 0", stroke=GREEN, sw=2.4) + path("M50 80 q4 -14 14 -16", stroke=LGREEN, sw=2.4) + \
        circle(40, 84, 5, "#6E3F22", sw=1.6) + circle(54, 88, 4, RED, sw=1.6)


@art("tradicion")
def _():
    return person(30, 26, 0.6, skin=SKIN3, shirt=PURPLE, hair_style="bun", hair_color=GREY, glasses=True) + \
        person(72, 42, 0.46, skin=SKIN3, shirt=PINK, hair_style="pigtails", hair_color=BLACK) + \
        use(X["vela"], 40, 50, 0.32) + path("M44 30 Q60 10 76 28", stroke=GOLD, sw=2.6, extra='stroke-dasharray="4 4"')


@art("rebozo")
def _():
    stripes = "".join(path(f"M{x} 26 L{x - 6} 80", stroke=c, sw=3) for x, c in zip(range(26, 84, 8), [PURPLE, PINK, TEAL] * 3))
    return path("M14 20 H86 L80 82 H20Z", "#5A3A8A") + stripes + "".join(line(x, 82, x, 94, sw=2) for x in range(22, 82, 5))


@art("huipil")
def _():
    return path("M20 14 H80 V90 H20Z", WHITE) + path("M40 14 Q50 26 60 14", sw=2.6) + rect(30, 30, 40, 28, "none", stroke=RED, sw=3) + \
        "".join(circle(40 + 10 * i, 44, 4, c, sw=1.4) for i, c in enumerate([RED, PURPLE, ORANGE])) + \
        path("M20 70 H80", stroke=TEAL, sw=4) + path("M20 78 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4", stroke=PINK, sw=2.4) + \
        path("M20 14 L6 34 M80 14 L94 34", sw=3)


@art("lengua-indigena")
def _():
    return bubble(4, 8, 54, 34) + text(31, 31, "Ba'ax", 12, DGREEN) + bubble(42, 48, 54, 34, tail="right") + text(69, 71, "Niltze", 12, "#C9662F")


@art("temazcal")
def _():
    return rect(0, 82, 100, 18, LGREEN, stroke=False) + path("M10 84 Q10 30 50 30 Q90 30 90 84Z", "#C9662F") + \
        path("M38 84 Q38 64 50 64 Q62 64 62 84Z", INK) + path("M20 60 h12 M68 52 h12 M46 44 h10", stroke="#A0521A", sw=3) + steam(40, 26, 3, 10)


@art("curandero")
def _():
    return person(skin=SKIN3, shirt=WHITE, hair_style="long", hair_color=GREY,
                  extra_front=path("M26 74 Q50 84 74 74", stroke=RED, sw=3)) + \
        path("M84 92 V50", stroke=GREEN, sw=3) + path("M84 60 Q74 54 72 46 M84 70 Q94 64 96 56 M84 52 Q90 44 88 36", stroke=GREEN, sw=3)


@art("asamblea")
def _():
    return rect(0, 0, 100, 100, "none", stroke=False) + person(50, 0, 0.48, skin=SKIN3, shirt=RED, hair_style="short", hair_color=BLACK) + \
        "".join(person(x, 46, 0.34, skin=SKIN3, shirt=c, hair_style=h, hair_color=BLACK) for x, c, h in [(14, TEAL, "long"), (38, ORANGE, "short"), (62, PURPLE, "bun"), (86, GREEN, "short")]) + \
        hand(24, 50, 0.26, rot=-10) + hand(72, 50, 0.26, rot=10)


@art("tequio")
def _():
    return rect(0, 80, 100, 20, "#C9A06A", stroke=False) + person(24, 30, 0.5, skin=SKIN3, shirt=RED, hair_style="short", hair_color=BLACK) + \
        person(50, 30, 0.5, skin=SKIN3, shirt=TEAL, hair_style="long", hair_color=BLACK) + person(76, 30, 0.5, skin=SKIN3, shirt=ORANGE, hair_style="short", hair_color=BLACK) + \
        rect(10, 74, 80, 8, BROWN, rx=3) + heart(50, 14, 6, RED, sw=1.8)


@art("cosmovision")
def _():
    return circle(50, 50, 42, NAVY) + circle(50, 50, 30, "none", stroke=GOLD, sw=2.4) + circle(50, 50, 16, YELLOW) + \
        "".join(path(f"M{50 + 30 * c} {50 + 30 * s} l{8 * c} {8 * s}", stroke=GOLD, sw=3) for c, s in [(1, 0), (-1, 0), (0, 1), (0, -1)]) + \
        path("M66 34 A18 18 0 1 0 66 66 A14 14 0 1 1 66 34Z", LYELLOW, sw=2) + star(30, 28, 3, WHITE, sw=1)


@art("copal")
def _():
    return path("M22 62 H78 L70 86 H30Z", "#C9662F") + path("M30 86 L26 94 H74 L70 86", "#A0521A") + \
        ellipse(50, 62, 28, 6, "#A0521A") + "".join(circle(x, 58, 4, CREAM, sw=1.6) for x in (40, 50, 60)) + \
        path("M44 54 q-8 -12 2 -22 q8 -10 0 -24 M56 54 q8 -10 0 -20 q-6 -8 2 -18", stroke=GREY, sw=3)
