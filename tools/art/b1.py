"""Illustrations du niveau B1."""
from .kit import *  # noqa: F401,F403

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


# ── La chamba ──

@art("chamba")
def _():
    return path("M18 56 C18 30 34 18 50 18 C66 18 82 30 82 56 Z", YELLOW) + rect(10, 54, 80, 10, GOLD, rx=5) + \
        rect(44, 10, 12, 12, GOLD, rx=3) + path("M34 26 Q30 40 32 54 M66 26 Q70 40 68 54", stroke="#E0A92A", sw=3) + \
        group("rotate(-35 50 82)", rect(20, 78, 56, 9, GREY, rx=4), circle(80, 82, 10, GREY), circle(80, 82, 4, WHITE, sw=2))


@art("jefe")
def _():
    tie = path("M47 66 L50 70 L53 66 Z", RED, sw=2) + path("M48 70 L44 92 L50 98 L56 92 L52 70Z", RED, sw=2.2)
    suit = path("M22 104 C22 80 34 66 50 66 C66 66 78 80 78 104 Z", NAVY) + path("M40 68 L50 96 L60 68 Q50 64 40 68Z", WHITE, sw=2)
    return person(shirt=NAVY, hair_style="short", hair_color=GREY, skin=SKIN, mustache=True, glasses=False,
                  extra_front=suit + tie) + star(84, 18, 8, GOLD, sw=2)


@art("oficina")
def _():
    return rect(8, 64, 84, 8, BROWN, rx=3) + rect(14, 72, 6, 22, DBROWN) + rect(80, 72, 6, 22, DBROWN) + \
        rect(26, 26, 40, 30, DGREY, rx=4) + rect(30, 30, 32, 22, LBLUE, rx=2, sw=2) + rect(42, 56, 8, 8, GREY, sw=2) + \
        path("M34 40 h14 M34 46 h20", stroke=WHITE, sw=2.6) + rect(70, 46, 14, 18, ORANGE, rx=3) + path("M84 50 q6 0 6 6 q0 6 -6 6", sw=2.6) + \
        rect(14, 58, 10, 6, WHITE, rx=1, sw=2)


@art("junta")
def _():
    return person(20, 20, 0.5, shirt=BLUE, hair_style="short", hair_color=BLACK) + person(50, 14, 0.5, shirt=PINK, hair_style="bun", hair_color=DBROWN, skin=SKIN2) + \
        person(80, 20, 0.5, shirt=GREEN, hair_style="long", hair_color=BROWN) + ellipse(50, 78, 46, 14, BROWN) + \
        ellipse(50, 76, 38, 9, TAN, stroke=False) + rect(36, 70, 14, 8, WHITE, rx=1, sw=2, rot=-8) + rect(56, 72, 12, 7, WHITE, rx=1, sw=2, rot=10)


@art("sueldo")
def _():
    return path("M34 26 Q28 14 36 10 Q50 18 64 10 Q72 14 66 26Z", TAN) + rect(34, 24, 32, 8, DBROWN, rx=3) + \
        path("M34 32 C10 44 12 92 50 92 C88 92 90 44 66 32Z", TAN) + text(50, 76, "$", 34, DBROWN) + \
        coin(80, 82, 10) + coin(18, 84, 8)


@art("computadora")
def _():
    return path("M20 20 H80 Q84 20 84 24 V66 H16 V24 Q16 20 20 20Z", DGREY) + rect(22, 26, 56, 34, LBLUE, rx=2, sw=2.2) + \
        path("M6 66 H94 L88 78 H12Z", LGREY) + rect(42, 68, 16, 4, GREY, rx=2, stroke=False) + \
        path("M28 34 h20 M28 42 h30 M28 50 h14", stroke=WHITE, sw=3)


@art("correo")
def _():
    return rect(10, 24, 80, 54, WHITE, rx=6) + path("M12 28 L50 56 L88 28", sw=3.2) + path("M12 76 L40 50 M88 76 L60 50", sw=2.6) + \
        circle(80, 22, 13, RED) + text(80, 28, "@", 17, WHITE)


@art("horario")
def _():
    ticks = "".join(group(f"rotate({a} 50 50)", line(50, 16, 50, 21, sw=3)) for a in range(0, 360, 30))
    return circle(50, 50, 40, BLUE) + circle(50, 50, 33, WHITE) + ticks + path("M50 50 V28 M50 50 L66 58", sw=4.4) + dot(50, 50, 4) + \
        path("M50 17 A33 33 0 0 1 83 50 L50 50Z", YELLOW, stroke=False, extra='opacity="0.6"')


# ── Hablar como chilango ──

@art("orale")
def _():
    burst = star(50, 50, 44, YELLOW, points=12, inner=0.72)
    return burst + text(50, 64, "¡!", 44, RED) + sparkle(14, 14, 6, PINK) + sparkle(88, 86, 6, LBLUE)


@art("chido")
def _():
    return face(50, 52, 36, mood="cool") + sparkle(84, 16, 8) + sparkle(14, 26, 5, LBLUE)


@art("que-onda")
def _():
    return path("M6 60 Q18 40 30 60 T54 60 T78 60 T102 60", stroke=BLUE, sw=7) + path("M6 76 Q18 56 30 76 T54 76 T78 76 T102 76", stroke=TEAL, sw=5) + \
        rect(20, 8, 60, 30, WHITE, rx=12) + path("M40 38 L36 48 L50 38", WHITE) + text(50, 30, "¿?", 20, PURPLE)


@art("cuate")
def _():
    return rect(-6, 44, 40, 20, BLUE, rx=6) + rect(66, 44, 40, 20, ORANGE, rx=6) + \
        rect(26, 38, 22, 30, SKIN, rx=9) + rect(52, 38, 22, 30, SKIN2, rx=9) + \
        path("M34 44 h10 M34 52 h10 M34 60 h10 M56 44 h10 M56 52 h10 M56 60 h10", sw=2) + \
        path("M50 22 L50 30 M38 26 L42 32 M62 26 L58 32", stroke=ORANGE, sw=3.4) + sparkle(50, 82, 6)


@art("neta")
def _():
    return path("M50 8 L84 20 V48 C84 72 66 86 50 94 C34 86 16 72 16 48 V20Z", GREEN) + \
        path("M50 16 L76 26 V48 C76 66 62 78 50 84 C38 78 24 66 24 48 V26Z", LGREEN, sw=2.2) + \
        path("M34 50 L46 62 L68 38", stroke=WHITE, sw=9) + path("M34 50 L46 62 L68 38", stroke=DGREEN, sw=3)


@art("ahorita")
def _():
    return rect(22, 8, 56, 10, BROWN, rx=4) + rect(22, 82, 56, 10, BROWN, rx=4) + \
        path("M28 18 C28 40 46 44 46 50 C46 56 28 60 28 82 H72 C72 60 54 56 54 50 C54 44 72 40 72 18Z", LBLUE) + \
        path("M34 30 C40 40 46 44 50 46 C54 44 60 40 66 30Z", GOLD, sw=2) + path("M50 50 V70", stroke=GOLD, sw=2.4) + \
        path("M32 82 C34 70 44 68 50 68 C56 68 66 70 68 82Z", GOLD, sw=2)


@art("aguas")
def _():
    return path("M50 10 L92 84 Q94 90 88 90 H12 Q6 90 8 84Z", YELLOW) + rect(45, 34, 10, 30, BLACK, rx=5, stroke=False) + circle(50, 75, 5.5, BLACK, stroke=False)


@art("padre")
def _():
    return path("M30 46 H40 L52 16 Q62 14 62 26 L58 42 H80 Q90 44 86 56 L80 80 Q78 88 70 88 H40 Q30 88 30 80Z", SKIN) + \
        rect(14, 44, 18, 46, BLUE, rx=4) + path("M60 54 H82 M60 66 H80 M60 78 H76", sw=2.4) + sparkle(84, 18, 8)


# ── Buscar depa ──

@art("departamento")
def _():
    return rect(18, 10, 64, 84, "#F28C6B") + building_windows(25, 18, 3, 5, 12, 10, 6, 5, LBLUE) + \
        "".join(rect(23 + c * 18, 28 + r * 15, 16, 3, DGREY, rx=1, stroke=False) for r in range(4) for c in range(3)) + \
        rect(42, 80, 16, 14, BROWN, sw=2.4) + rect(12, 92, 76, 4, DGREY, rx=2)


@art("renta")
def _():
    return rect(14, 46, 52, 44, CREAM) + poly([(8, 50), (40, 22), (72, 50)], BLUE) + rect(32, 66, 14, 24, BROWN, rx=2) + \
        path("M66 40 L90 40 L96 52 L90 64 H66Z", YELLOW, sw=2.6) + circle(72, 52, 3, WHITE, sw=1.8) + text(84, 57, "$", 13, DBROWN)


@art("vecino")
def _():
    return rect(6, 6, 88, 88, "#F2B66B", rx=6) + rect(18, 20, 64, 74, LBLUE) + \
        person(50, 26, 0.6, shirt=GREEN, hair_style="short", hair_color=DBROWN, skin=SKIN2) + \
        rect(14, 66, 72, 10, WHITE, rx=3) + path("M20 76 V94 M80 76 V94", sw=3) + \
        hand(78, 52, 0.38, SKIN2, rot=20) + circle(30, 62, 6, RED, sw=2) + circle(40, 60, 6, PINK, sw=2) + path("M26 66 h20", stroke=GREEN, sw=4)


@art("colonia")
def _():
    house = lambda x, y, w, c, roof: rect(x, y, w, 30, c) + poly([(x - 4, y + 2), (x + w / 2, y - 16), (x + w + 4, y + 2)], roof) + \
        rect(x + w / 2 - 4, y + 16, 8, 14, BROWN, sw=2) + rect(x + 4, y + 6, 7, 7, LBLUE, sw=2)
    return rect(0, 84, 100, 16, LGREEN, stroke=False) + house(8, 54, 26, PINK, RED) + house(38, 44, 26, YELLOW, BLUE) + house(68, 54, 26, TEAL, ORANGE) + \
        path("M0 84 H100", sw=3)


@art("recamara")
def _():
    return rect(4, 4, 92, 92, LPURPLE, rx=14, stroke=False) + rect(56, 14, 28, 26, LBLUE) + line(70, 14, 70, 40) + \
        rect(10, 56, 54, 26, WHITE, rx=4) + rect(10, 50, 8, 40, BROWN, rx=3) + rect(14, 54, 16, 10, WHITE, rx=4) + \
        path("M28 60 H60 Q64 60 64 64 V76 H28Z", PINK) + rect(74, 60, 16, 22, BROWN, rx=2) + \
        path("M76 60 L82 44 L88 60Z", YELLOW) + line(82, 44, 82, 38, sw=2.4)


@art("llave")
def _():
    return group("rotate(-40 50 50)", circle(28, 50, 18, GOLD), circle(28, 50, 7, CREAM, sw=2.4),
                 rect(44, 45, 46, 10, GOLD, rx=3), rect(72, 55, 7, 12, GOLD, rx=2), rect(84, 55, 6, 9, GOLD, rx=2))


@art("elevador")
def _():
    return rect(16, 10, 68, 84, LGREY, rx=4) + rect(24, 26, 26, 64, GREY) + rect(50, 26, 26, 64, GREY) + \
        path("M34 30 V86 M66 30 V86", stroke=WHITE, sw=1.6) + rect(36, 12, 28, 10, DGREY, rx=3) + \
        poly([(44, 19), (48, 14), (52, 19)], LGREEN, stroke=False) + poly([(56, 15), (60, 20), (64, 15)], RED, stroke=False)


@art("azotea")
def _():
    return rect(4, 4, 92, 60, LBLUE, rx=14, stroke=False) + rect(8, 64, 84, 32, "#E58B6A") + rect(4, 60, 92, 8, "#C9654A", rx=2) + \
        path("M16 40 C16 30 40 30 40 40 V56 H16Z", BLACK) + ellipse(28, 40, 12, 4, DGREY) + rect(18, 56, 4, 6, DGREY, stroke=False) + rect(34, 56, 4, 6, DGREY, stroke=False) + \
        path("M50 30 V60 M90 30 V60", sw=3) + path("M50 34 Q70 42 90 34", sw=2) + \
        rect(56, 36, 9, 13, PINK, rx=1, sw=2) + rect(70, 38, 10, 12, YELLOW, rx=1, sw=2) + \
        building_windows(16, 74, 4, 1, 12, 12, 8, 4, LYELLOW)


# ── En la fonda ──

@art("mesero")
def _():
    tray = ellipse(80, 40, 16, 4, LGREY) + path("M72 38 Q72 28 80 28 Q88 28 88 38", WHITE, sw=2.4) + circle(80, 26, 2, GREY, sw=1.6) + \
        path("M70 70 L76 44", stroke=WHITE, sw=7)
    return person(shirt=WHITE, hair_style="short", hair_color=BLACK, skin=SKIN2, mustache=True, bow=BLACK,
                  extra_front=path("M36 74 H64 V104 H36Z", BLACK, sw=2.4) + path("M43 70 L50 74 L57 70 L57 78 L50 74 L43 78Z", BLACK, sw=2)) + tray


@art("cuenta")
def _():
    return rect(20, 10, 52, 80, WHITE, rx=4) + path("M28 24 H62 M28 34 H54 M28 44 H60 M28 54 H50", stroke=GREY, sw=3) + \
        path("M28 70 H62", sw=3) + text(56, 82, "$$", 13, GREEN) + \
        group("rotate(30 76 60)", rect(72, 30, 8, 52, BLUE, rx=3), poly([(72, 82), (80, 82), (76, 92)], CREAM))


@art("propina")
def _():
    return path("M22 30 H78 V82 Q78 92 68 92 H32 Q22 92 22 82Z", "#DFF3FF", extra='fill-opacity="0.9"') + rect(18, 22, 64, 10, LGREY, rx=4) + \
        coin(40, 76, 10) + coin(60, 78, 9) + coin(50, 60, 9) + rect(36, 40, 28, 12, "#7FCB8E", rx=2, sw=2, rot=-12) + \
        heart(80, 14, 7, RED)


@art("menu")
def _():
    return path("M16 14 H50 V90 H16 Q12 90 12 86 V18 Q12 14 16 14Z", RED) + path("M50 14 H84 Q88 14 88 18 V86 Q88 90 84 90 H50Z", "#F7E7C6") + \
        path("M58 28 H80 M58 40 H76 M58 52 H80 M58 64 H74 M58 76 H78", stroke=BROWN, sw=3) + \
        circle(31, 46, 11, "none", stroke=GOLD, sw=2.6) + path("M27 42 V50 M31 40 V52 M35 42 V50", stroke=GOLD, sw=2)


@art("comida-corrida")
def _():
    return rect(6, 24, 88, 60, LGREY, rx=10) + rect(12, 30, 36, 24, "#E07A3A", rx=8, sw=2.4) + rect(52, 30, 36, 24, WHITE, rx=8, sw=2.4) + \
        "".join(circle(x, 42, 2.6, WHITE, stroke=False) for x in (60, 66, 72, 78, 64, 74)) + \
        rect(12, 58, 24, 20, "#5A2E2A", rx=6, sw=2.4) + rect(40, 58, 22, 20, "#D99A4E", rx=6, sw=2.4) + rect(66, 58, 22, 20, PINK, rx=6, sw=2.4) + \
        path("M20 40 q4 -4 8 0 q4 4 8 0", stroke=ORANGE, sw=2.4)


@art("vaso")
def _():
    return poly([(28, 14), (72, 14), (66, 90), (34, 90)], "#DFF3FF") + poly([(30, 40), (70, 40), (66, 86), (34, 86)], LBLUE, sw=2.2) + \
        path("M36 22 L40 80", stroke=WHITE, sw=4) + circle(56, 56, 3, WHITE, stroke=False) + circle(50, 70, 2, WHITE, stroke=False)


@art("cuchara")
def _():
    return group("rotate(35 50 50)", ellipse(50, 24, 15, 20, LGREY), ellipse(50, 26, 9, 13, WHITE, stroke=False),
                 rect(46, 42, 8, 52, GREY, rx=4))


@art("tenedor")
def _():
    return group("rotate(-30 50 50)", path("M34 8 V30 M44 8 V30 M56 8 V30 M66 8 V30", sw=6),
                 path("M34 28 Q34 44 50 44 Q66 44 66 28 Z", LGREY), rect(46, 42, 8, 52, GREY, rx=4))


# ── Las emociones ──

@art("feliz")
def _():
    return face(50, 52, 38, mood="happy") + sparkle(86, 16, 7)


@art("triste")
def _():
    return face(50, 52, 38, skin="#BFD8FF", mood="sad")


@art("enojado")
def _():
    return face(50, 54, 38, mood="angry") + path("M80 10 l4 8 l6 -6 l-2 10", stroke=RED, sw=3) + path("M14 14 l6 6 l2 -8", stroke=RED, sw=3)


@art("cansado")
def _():
    return face(50, 54, 38, skin=SKIN, mood="tired") + text(84, 24, "z", 18, NAVY) + text(76, 12, "z", 12, NAVY)


@art("nervioso")
def _():
    return face(50, 52, 38, skin="#D9F2C2", mood="nervous")


@art("sorprendido")
def _():
    return face(50, 54, 38, mood="surprised") + text(86, 24, "!", 22, RED)


@art("aburrido")
def _():
    return face(50, 54, 38, skin="#E5DAF7", mood="bored") + path("M86 20 q4 -4 8 0 q-4 4 -8 0", sw=2.2)


@art("orgulloso")
def _():
    return face(50, 46, 34, mood="proud") + path("M38 76 L50 96 L62 76", fill=RED) + circle(50, 92, 9, GOLD) + star(50, 92, 5, YELLOW, sw=1.6)


# ── La naturaleza ──

@art("volcan")
def _():
    return path("M2 92 L36 34 H64 L98 92Z", "#8A6A55") + path("M36 34 H64 L58 46 Q50 40 42 46Z", ORANGE, sw=2.4) + \
        path("M40 46 L34 62 L44 56 L42 72", stroke=ORANGE, sw=4) + \
        circle(44, 22, 9, LGREY) + circle(56, 16, 11, LGREY) + circle(66, 8, 7, LGREY) + path("M10 92 H90", sw=3)


@art("montana")
def _():
    return path("M0 90 L34 26 L56 62 L70 42 L100 90Z", "#6B8FBF") + path("M34 26 L44 44 L38 40 L32 46 L26 40Z", WHITE, sw=2.4) + \
        path("M70 42 L78 54 L72 52 L66 56 L62 52Z", WHITE, sw=2.2) + circle(82, 18, 8, YELLOW) + rect(0, 88, 100, 12, LGREEN, stroke=False)


@art("selva")
def _():
    def leaf(x, y, a, c, l=62):
        return group(f"rotate({a} {x} {y})",
                     path(f"M{x} {y} C{x - 20} {y - l * 0.4} {x - 12} {y - l * 0.85} {x} {y - l} C{x + 12} {y - l * 0.85} {x + 20} {y - l * 0.4} {x} {y}Z", c),
                     line(x, y, x, y - l * 0.85, sw=2.2))
    return rect(4, 4, 92, 92, "#D8F5C8", rx=16, stroke=False) + leaf(50, 98, -55, LGREEN, 56) + leaf(50, 98, 55, LGREEN, 56) + \
        leaf(50, 98, -28, DGREEN, 72) + leaf(50, 98, 28, DGREEN, 72) + leaf(50, 98, 0, GREEN, 80) + \
        circle(78, 22, 6, RED, sw=2.2) + path("M74 18 l-6 -6 M82 18 l6 -6", stroke=YELLOW, sw=3)


@art("desierto")
def _():
    return rect(4, 4, 92, 92, "#FFE3B0", rx=16, stroke=False) + circle(72, 26, 10, ORANGE) + \
        path("M0 70 Q30 50 60 70 T100 66 V100 H0Z", "#F2C57C") + path("M0 82 Q40 64 100 84 V100 H0Z", "#E8A95C") + \
        path("M26 74 V44 Q26 38 31 38 Q36 38 36 44 V74", GREEN) + path("M26 58 H20 Q16 58 16 54 V48", stroke=GREEN, sw=6)


@art("rio")
def _():
    return rect(4, 4, 92, 92, LGREEN, rx=16, stroke=False) + \
        path("M40 4 C30 30 70 40 56 62 C46 78 30 84 34 96 H66 C62 84 76 76 82 60 C92 36 58 26 66 4Z", BLUE) + \
        path("M54 20 q4 4 0 8 M62 48 q-4 4 0 8 M50 76 q4 4 0 8", stroke=WHITE, sw=3) + \
        circle(18, 30, 8, GREEN) + circle(84, 76, 8, GREEN) + circle(20, 70, 3, PINK, sw=1.6)


@art("nopal")
def _():
    pad = lambda x, y, rx, ry, a: ellipse(x, y, rx, ry, GREEN, rot=a) + "".join(dot(x + dx, y + dy, 1.3, LYELLOW) for dx, dy in [(-5, -6), (5, -2), (-2, 6), (4, 10), (-6, 2)])
    return rect(30, 86, 40, 10, "#C9653A", rx=3) + pad(50, 62, 16, 24, 0) + pad(30, 38, 11, 16, -35) + pad(70, 36, 11, 16, 35) + \
        ellipse(26, 18, 5, 6, "#D6336C", sw=2) + ellipse(76, 16, 5, 6, "#D6336C", sw=2) + ellipse(50, 34, 5, 6, "#D6336C", sw=2)


@art("mar")
def _():
    return rect(4, 4, 92, 92, LBLUE, rx=16, stroke=False) + circle(76, 24, 9, YELLOW) + \
        path("M0 56 Q12 46 24 56 T48 56 T72 56 T100 56 V100 H0Z", BLUE) + path("M0 72 Q12 62 24 72 T48 72 T72 72 T100 72 V100 H0Z", "#2563C9") + \
        path("M18 32 q4 -4 8 0 q4 -4 8 0", sw=2.4)


@art("maguey")
def _():
    leaf = lambda a, l, c: group(f"rotate({a} 50 88)", path(f"M50 88 C44 70 46 {88 - l * 0.6} 50 {88 - l} C54 {88 - l * 0.6} 56 70 50 88Z", c))
    return "".join(leaf(a, l, c) for a, l, c in [(-70, 44, "#5FA88A"), (70, 44, "#5FA88A"), (-45, 60, "#4C9A7A"), (45, 60, "#4C9A7A"), (-20, 72, "#3E8A6C"), (20, 72, "#3E8A6C"), (0, 78, "#2F7A5C")]) + \
        rect(18, 86, 64, 8, "#C9965A", rx=4)


# ── De compras ──

@art("tianguis")
def _():
    stripes = "".join(path(f"M{8 + i * 14} 30 L{14 + i * 14} 14 H{28 + i * 14} L{22 + i * 14} 30Z", PINK if i % 2 == 0 else WHITE, sw=2.2) for i in range(6))
    return path("M14 30 V92 M86 30 V92", sw=4) + stripes + path("M6 30 H94 L90 38 H10Z", "#D6336C") + \
        rect(14, 64, 72, 20, BROWN) + circle(26, 60, 7, ORANGE, sw=2.4) + circle(40, 60, 7, RED, sw=2.4) + circle(56, 60, 7, YELLOW, sw=2.4) + \
        circle(72, 60, 7, GREEN, sw=2.4)


@art("oferta")
def _():
    return path("M14 40 L40 14 H86 V60 L60 86 Z", RED) + circle(70, 30, 6, WHITE) + \
        text(50, 64, "%", 30, WHITE) + path("M76 24 Q96 6 94 30", sw=2.4)


@art("tarjeta")
def _():
    return rect(8, 24, 84, 54, PURPLE, rx=8) + rect(8, 34, 84, 10, BLACK, stroke=False) + rect(18, 52, 16, 12, GOLD, rx=2, sw=2) + \
        path("M18 70 h40", stroke=WHITE, sw=3) + circle(74, 64, 7, ORANGE, sw=2) + circle(82, 64, 7, YELLOW, sw=2, extra='fill-opacity="0.85"')


@art("efectivo")
def _():
    bill = lambda y, rot: rect(12, y, 76, 36, "#7FCB8E", rx=5, rot=rot) + ""
    return bill(46, -8) + bill(40, 4) + rect(12, 34, 76, 36, "#7FCB8E", rx=5) + rect(18, 40, 64, 24, "none", rx=3, stroke=DGREEN, sw=2) + \
        circle(50, 52, 10, LGREEN, sw=2) + text(50, 57, "$", 14, DGREEN) + rect(42, 30, 16, 44, "#F2D48A", rx=1, sw=2.2)


@art("talla")
def _():
    return path("M34 14 L18 22 L6 44 L20 52 L26 42 L26 90 H74 V42 L80 52 L94 44 L82 22 L66 14 Q50 26 34 14Z", TEAL) + \
        rect(36, 44, 28, 26, WHITE, rx=4) + text(50, 65, "M", 22, INK)


@art("descuento")
def _():
    return path("M16 30 H62 L78 50 L62 70 H16Z", YELLOW) + circle(66, 50, 4, WHITE, sw=2) + text(38, 58, "-20", 20, RED) + \
        line(10, 20, 54, 78, sw=4, color=RED)


@art("recibo")
def _():
    return path("M24 6 H76 V94 L70 88 L64 94 L58 88 L52 94 L46 88 L40 94 L34 88 L28 94 L24 90Z", WHITE) + \
        path("M32 20 H68 M32 30 H58 M32 40 H64 M32 50 H54 M32 60 H66", stroke=GREY, sw=3) + path("M32 74 H68", sw=3) + \
        path("M52 80 l4 4 l8 -8", stroke=GREEN, sw=3)


@art("tiendita")
def _():
    stripes = "".join(rect(12 + i * 12.66, 30, 12.66, 12, RED if i % 2 == 0 else WHITE, stroke=False) for i in range(6))
    return rect(12, 30, 76, 62, "#FFE38A") + stripes + rect(12, 30, 76, 12, "none") + rect(16, 14, 68, 16, BLUE, rx=3) + \
        text(50, 26, "ABARROTES", 8, WHITE) + rect(20, 50, 30, 26, LBLUE, sw=2.4) + rect(58, 50, 22, 42, BROWN, sw=2.4) + \
        circle(28, 70, 4, RED, sw=1.8) + rect(36, 64, 8, 12, ORANGE, rx=1, sw=1.8)


# ── La tecnología ──

@art("celular")
def _():
    return rect(28, 6, 44, 88, DGREY, rx=10) + rect(32, 14, 36, 68, LBLUE, rx=3, sw=2) + rect(44, 9, 12, 3, BLACK, rx=1.5, stroke=False) + \
        circle(50, 88, 3, GREY, sw=1.6) + path("M40 34 H60 M40 44 H56 M40 54 H60", stroke=WHITE, sw=3)


@art("mensaje")
def _():
    return path("M16 18 H84 Q92 18 92 26 V60 Q92 68 84 68 H40 L22 84 L26 68 H16 Q8 68 8 60 V26 Q8 18 16 18Z", GREEN) + \
        circle(32, 43, 5, WHITE, sw=2) + circle(50, 43, 5, WHITE, sw=2) + circle(68, 43, 5, WHITE, sw=2)


@art("contrasena")
def _():
    return path("M32 44 V32 Q32 14 50 14 Q68 14 68 32 V44", sw=7) + rect(18, 42, 64, 48, GOLD, rx=8) + \
        text(50, 76, "***", 22, DBROWN)


@art("cargador")
def _():
    return rect(30, 20, 40, 40, WHITE, rx=8) + rect(38, 6, 6, 16, GREY) + rect(56, 6, 6, 16, GREY) + \
        path("M50 60 V72 Q50 90 70 88 Q88 86 90 70", sw=5) + path("M52 30 L44 42 H54 L46 54", stroke=YELLOW, sw=3.6)


@art("aplicacion")
def _():
    cols = [RED, BLUE, GREEN, ORANGE, PURPLE, PINK, TEAL, YELLOW, LBLUE]
    return "".join(rect(14 + (i % 3) * 26, 14 + (i // 3) * 26, 20, 20, c, rx=6) for i, c in enumerate(cols))


@art("pantalla")
def _():
    return rect(6, 14, 88, 56, BLACK, rx=6) + rect(12, 20, 76, 44, "#5CC8FF", rx=2, sw=2) + \
        path("M12 54 L32 38 L46 50 L60 34 L88 58 V64 H12Z", GREEN, sw=2) + circle(74, 30, 5, YELLOW, sw=2) + \
        rect(44, 70, 12, 12, GREY, stroke=False) + rect(30, 82, 40, 6, DGREY, rx=3)


@art("foto")
def _():
    return rect(8, 28, 84, 58, DGREY, rx=10) + rect(30, 18, 24, 14, DGREY, rx=4) + circle(50, 56, 20, LGREY) + circle(50, 56, 12, NAVY) + \
        circle(46, 52, 4, WHITE, stroke=False) + rect(72, 36, 12, 6, YELLOW, rx=2, sw=2) + rect(16, 36, 10, 6, RED, rx=2, sw=2)


@art("red")
def _():
    return path("M10 40 A56 56 0 0 1 90 40", sw=7) + path("M10 40 A56 56 0 0 1 90 40", stroke=BLUE, sw=3) + \
        path("M24 54 A36 36 0 0 1 76 54", sw=7) + path("M24 54 A36 36 0 0 1 76 54", stroke=BLUE, sw=3) + \
        path("M38 68 A17 17 0 0 1 62 68", sw=7) + path("M38 68 A17 17 0 0 1 62 68", stroke=BLUE, sw=3) + circle(50, 82, 6, BLUE)
