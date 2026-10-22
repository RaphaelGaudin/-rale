"""Illustrations du niveau A2."""
from .kit import *  # noqa: F401,F403

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


# ── En la ciudad ──

@art("calle")
def _():
    return rect(0, 50, 100, 50, LGREEN, stroke=False) + path("M0 50 H100", sw=3) + \
        path("M36 50 L8 100 H92 L64 50Z", DGREY) + \
        path("M50 56 V64 M50 72 V82 M50 90 V100", stroke=WHITE, sw=4) + \
        circle(18, 34, 12, GREEN) + rect(16, 44, 4, 8, BROWN, sw=2) + circle(84, 30, 14, GREEN) + rect(82, 42, 4, 10, BROWN, sw=2) + \
        circle(70, 14, 7, YELLOW)


@art("esquina")
def _():
    return rect(38, 8, 24, 58, DGREY, rx=7) + circle(50, 20, 7, RED) + circle(50, 37, 7, "#7A6A3A") + circle(50, 54, 7, "#2F5D3A") + \
        rect(46, 66, 8, 28, GREY) + rect(34, 90, 32, 6, DGREY, rx=3) + \
        path("M32 14 h-8 M32 30 h-8 M68 14 h8 M68 30 h8", sw=3)


@art("metro")
def _():
    return rect(18, 10, 64, 74, ORANGE, rx=14) + rect(26, 20, 48, 30, LBLUE, rx=5) + \
        circle(32, 64, 5, YELLOW) + circle(68, 64, 5, YELLOW) + rect(40, 58, 20, 10, WHITE, rx=3) + \
        text(50, 66, "M", 9, ORANGE) + path("M28 84 L18 96 M72 84 L82 96", sw=4) + path("M10 96 H90", sw=3.2) + \
        line(50, 20, 50, 50, sw=2.4)


@art("camion")
def _():
    return rect(6, 24, 88, 50, "#2EB872", rx=10) + rect(6, 56, 88, 8, WHITE, stroke=False) + path("M6 56 H94 M6 64 H94", sw=2) + \
        rect(14, 32, 16, 16, LBLUE, rx=3, sw=2.4) + rect(36, 32, 16, 16, LBLUE, rx=3, sw=2.4) + rect(58, 32, 16, 16, LBLUE, rx=3, sw=2.4) + \
        rect(80, 32, 10, 30, LBLUE, rx=3, sw=2.4) + circle(28, 76, 9, DGREY) + circle(28, 76, 3.5, LGREY, sw=1.8) + \
        circle(72, 76, 9, DGREY) + circle(72, 76, 3.5, LGREY, sw=1.8)


@art("parque")
def _():
    return rect(0, 70, 100, 30, LGREEN, stroke=False) + path("M0 70 H100", sw=3) + \
        circle(30, 36, 22, GREEN) + circle(18, 46, 12, GREEN) + circle(42, 48, 12, GREEN) + rect(26, 52, 8, 22, BROWN) + \
        rect(54, 58, 38, 6, BROWN, rx=2) + rect(54, 48, 38, 5, BROWN, rx=2) + rect(58, 64, 4, 12, DBROWN) + rect(84, 64, 4, 12, DBROWN) + \
        circle(80, 20, 4, PINK, sw=2) + circle(14, 82, 3, YELLOW, sw=1.8) + circle(70, 86, 3, PINK, sw=1.8)


@art("iglesia")
def _():
    return rect(18, 46, 64, 46, CREAM) + poly([(14, 48), (50, 26), (86, 48)], RED) + rect(38, 14, 24, 40, CREAM) + \
        poly([(36, 16), (50, 2), (64, 16)], RED) + \
        path("M44 34 A6 6 0 0 1 56 34 V44 H44Z", GOLD, sw=2.2) + \
        path("M40 92 V74 A10 10 0 0 1 60 74 V92Z", BROWN) + rect(24, 58, 8, 12, LBLUE, rx=4, sw=2.2) + rect(68, 58, 8, 12, LBLUE, rx=4, sw=2.2)


@art("banco")
def _():
    cols = "".join(rect(22 + i * 15, 42, 8, 36, WHITE, sw=2.6) for i in range(4))
    return poly([(10, 36), (50, 12), (90, 36)], LGREY) + rect(12, 34, 76, 8, WHITE) + cols + rect(10, 78, 80, 8, WHITE) + rect(6, 86, 88, 6, LGREY) + \
        circle(50, 26, 6, GOLD, sw=2) + text(50, 29.5, "$", 9, DBROWN)


@art("farmacia")
def _():
    return rect(12, 12, 76, 76, WHITE, rx=18) + path("M40 22 H60 V40 H78 V60 H60 V78 H40 V60 H22 V40 H40Z", GREEN)


# ── De viaje ──

@art("playa")
def _():
    return rect(0, 58, 100, 42, LBLUE, stroke=False) + path("M0 58 H100", sw=3) + path("M0 66 q12 -5 24 0 t24 0 t24 0 t28 0", stroke=WHITE, sw=3) + \
        path("M0 100 V80 Q40 70 100 84 V100Z", "#F7D58B") + \
        path("M54 84 L66 26", sw=3.4) + path("M30 34 Q62 4 96 30 Q80 24 72 32 Q62 22 52 32 Q44 26 30 34Z", RED) + \
        path("M52 32 Q62 22 72 32", fill=WHITE, sw=2.4) + circle(18, 18, 9, YELLOW)


@art("hotel")
def _():
    return rect(20, 14, 60, 80, BLUE) + rect(14, 8, 72, 10, NAVY, rx=3) + building_windows(27, 24, 3, 4, 12, 9, 5, 5, LYELLOW) + \
        rect(42, 76, 16, 18, LBLUE, sw=2.4) + rect(32, 0, 36, 12, RED, rx=3) + text(50, 9.5, "HOTEL", 8.5, WHITE)


@art("maleta")
def _():
    return rect(36, 12, 28, 14, "none", rx=6, sw=5) + rect(16, 24, 68, 60, ORANGE, rx=10) + \
        path("M34 24 V84 M66 24 V84", stroke=DRED, sw=5) + \
        circle(28, 90, 5, DGREY) + circle(72, 90, 5, DGREY) + rect(40, 44, 20, 12, CREAM, rx=3, sw=2.2)


@art("boleto")
def _():
    return path("M10 30 H90 V44 A6 6 0 0 0 90 56 V70 H10 V56 A6 6 0 0 0 10 44Z", YELLOW) + \
        path("M66 30 V70", sw=2.4, extra='stroke-dasharray="4 4"') + \
        path("M18 42 H56 M18 52 H48 M18 60 H52", stroke=ORANGE, sw=3) + star(78, 50, 7, RED, sw=2)


@art("avion")
def _():
    return group("rotate(-30 50 50)",
                 path("M8 50 Q8 44 18 44 H82 Q94 46 94 50 Q94 54 82 56 H18 Q8 56 8 50Z", WHITE),
                 path("M44 44 L30 14 H40 L62 44Z", BLUE), path("M44 56 L30 86 H40 L62 56Z", BLUE),
                 path("M14 44 L8 30 H14 L24 44Z", BLUE), circle(84, 50, 3, LBLUE, sw=1.8),
                 dot(70, 50, 2.2, LBLUE), dot(60, 50, 2.2, LBLUE), dot(50, 50, 2.2, LBLUE)) + \
        path("M10 84 q8 -6 16 0 M2 72 q8 -6 16 0", stroke=LBLUE, sw=3)


@art("pasaporte")
def _():
    return rect(22, 10, 56, 80, "#1E5A43", rx=6) + rect(22, 10, 8, 80, DGREEN, rx=3) + \
        circle(54, 42, 13, "none", stroke=GOLD, sw=2.6) + path("M41 42 H67 M54 29 Q46 42 54 55 Q62 42 54 29", stroke=GOLD, sw=2) + \
        rect(40, 66, 28, 4, GOLD, rx=2, stroke=False) + rect(44, 74, 20, 3, GOLD, rx=1.5, stroke=False)


@art("piramide")
def _():
    steps = "".join(rect(14 + i * 9, 80 - i * 14, 72 - i * 18, 14, "#D9B26F" if i % 2 else "#C99A55") for i in range(4))
    return rect(0, 92, 100, 8, LGREEN, stroke=False) + steps + rect(43, 10, 14, 14, "#B5844A") + \
        path("M50 24 V92", stroke="#8A5E2E", sw=6) + path("M50 24 V92", stroke="#E8C88A", sw=2.4) + circle(84, 16, 8, YELLOW)


@art("cenote")
def _():
    vines = "".join(path(f"M{x} 6 q-3 12 2 22 q4 10 -2 20", stroke=GREEN, sw=3) for x in (24, 50, 74))
    return rect(6, 6, 88, 88, "#6B5B4B", rx=20) + ellipse(50, 66, 38, 22, TEAL) + ellipse(50, 66, 28, 14, "#7FE0D4", stroke=False) + \
        path("M30 66 q10 -4 20 0 t20 0", stroke=WHITE, sw=2.6) + vines + \
        path("M38 6 L28 54 M62 6 L72 54", stroke=LYELLOW, sw=5, extra='opacity="0.55"') + \
        circle(24, 34, 4, GREEN, sw=2) + circle(76, 50, 4, GREEN, sw=2)


# ── La rutina diaria ──

@art("despertarse")
def _():
    return circle(50, 54, 32, RED) + circle(50, 54, 25, WHITE) + path("M50 54 V38 M50 54 L60 60", sw=4) + \
        circle(26, 22, 10, YELLOW) + circle(74, 22, 10, YELLOW) + path("M30 82 L24 92 M70 82 L76 92", sw=4.5) + \
        path("M12 40 l-6 -2 M10 54 h-7 M88 40 l6 -2 M90 54 h7", sw=3) + rect(46, 14, 8, 8, DGREY, rx=2)


@art("banarse")
def _():
    drops = "".join(path(f"M{x} {y} q-3 6 0 8 q3 -2 0 -8z", BLUE, sw=1.8) for x, y in [(34, 52), (46, 58), (58, 52), (70, 60), (40, 72), (54, 76), (66, 82), (28, 78)])
    return path("M20 10 H52 Q64 10 64 22 V26", sw=5) + path("M46 26 H82 L74 42 H54Z", LGREY) + \
        "".join(dot(x, 38, 1.8) for x in (60, 66, 72)) + drops + rect(10, 6, 12, 10, LGREY, rx=3)


@art("desayunar")
def _():
    return ellipse(50, 80, 42, 10, WHITE) + ellipse(50, 70, 30, 8, TAN) + rect(20, 62, 60, 8, TAN, stroke=False) + ellipse(50, 62, 30, 8, TAN) + \
        rect(20, 54, 60, 8, TAN, stroke=False) + path("M20 54 V70 M80 54 V70", sw=3.2) + ellipse(50, 54, 30, 8, "#F2CB8C") + \
        path("M34 52 Q42 46 50 52 Q60 58 66 52 Q70 46 64 44 H38 Q30 46 34 52Z", GOLD, sw=2.4) + rect(42, 38, 14, 8, LYELLOW, rx=2, sw=2.2) + \
        path("M30 66 h40", stroke="#C9965A", sw=2)


@art("trabajar")
def _():
    return rect(12, 34, 76, 54, BROWN, rx=8) + rect(36, 22, 28, 14, "none", rx=5, sw=5) + rect(12, 52, 76, 8, DBROWN, rx=2) + \
        rect(44, 50, 12, 14, GOLD, rx=3)


@art("comer")
def _():
    return bowl(50, 52, 72, ORANGE, "#E07A3A", 32) + circle(38, 50, 4, GREEN, stroke=False) + circle(56, 48, 4, LGREEN, stroke=False) + \
        circle(48, 54, 3.5, YELLOW, stroke=False) + rect(66, 20, 7, 40, LGREY, rx=3.5, rot=25) + ellipse(76, 16, 8, 6, LGREY, rot=25) + steam(36, 36, 3, 12)


@art("cenar")
def _():
    return plate(50, 64, 36, 16) + path("M36 60 Q50 48 64 60 Q50 68 36 60Z", "#C75A3A", sw=2.4) + circle(42, 62, 3, GREEN, stroke=False) + \
        rect(6, 38, 5, 46, GREY, rx=2.5) + path("M4 26 V40 M8.5 26 V40 M13 26 V40 M4 40 Q8.5 46 13 40", sw=2.4) + \
        path("M92 26 Q84 40 92 56 V84", fill=LGREY) + rect(89, 56, 5, 28, GREY, rx=2.5) + \
        path("M70 16 A10 10 0 1 0 82 28 A8 8 0 1 1 70 16Z", LYELLOW, sw=2.4)


@art("dormir")
def _():
    return rect(6, 54, 88, 30, BLUE, rx=10) + rect(6, 46, 30, 18, WHITE, rx=8) + \
        circle(26, 46, 13, SKIN) + path("M18 46 q3 3 6 0 M28 46 q3 3 6 0", sw=2.2) + path("M14 40 C14 28 38 28 38 40 C32 36 20 36 14 40Z", DBROWN, sw=2.4) + \
        text(60, 36, "Z", 18, NAVY) + text(76, 24, "Z", 13, NAVY) + text(88, 14, "z", 10, NAVY)


@art("cafe")
def _():
    return path("M22 40 H70 V72 Q70 88 54 88 H38 Q22 88 22 72Z", RED) + path("M70 48 Q86 48 86 60 Q86 72 70 70", sw=5) + \
        ellipse(46, 40, 24, 6, DBROWN) + path("M30 58 H62", stroke=WHITE, sw=3) + steam(36, 30, 3, 10) + ellipse(46, 92, 34, 5, LGREY, sw=2.4)


# ── La salud ──

@art("cabeza")
def _():
    return face(50, 54, 34, mood="tired") + path("M18 36 Q50 18 82 36 L80 46 Q50 30 20 46Z", WHITE) + \
        path("M74 40 l10 -8 M76 44 l12 0", sw=3) + rect(46, 26, 8, 12, RED, rx=1, stroke=False) + rect(44, 29, 12, 6, RED, rx=1, stroke=False)


@art("estomago")
def _():
    return path("M34 10 V26 C34 34 20 36 20 54 C20 78 40 90 60 86 C80 82 86 62 76 50 C68 40 56 46 52 34 C50 26 52 18 52 10", "#FF9DB0", sw=3.4) + \
        path("M34 10 V26 C34 34 20 36 20 54 C20 78 40 90 60 86 C80 82 86 62 76 50 C68 40 56 46 52 34 C50 26 52 18 52 10Z", "#FF9DB0") + \
        path("M32 56 Q40 72 58 72", stroke="#FFD0DA", sw=4) + path("M60 86 Q70 92 72 100", sw=4)


@art("diente")
def _():
    return path("M28 22 C18 30 20 50 28 60 C32 66 32 90 40 90 C46 90 44 70 50 70 C56 70 54 90 60 90 C68 90 68 66 72 60 C80 50 82 30 72 22 C64 16 58 22 50 22 C42 22 36 16 28 22Z", WHITE) + \
        path("M32 34 Q34 28 40 28", stroke=LBLUE, sw=3.5) + sparkle(84, 20, 7, LBLUE)


@art("mano")
def _():
    return hand(48, 78, 1.25, rot=0) + rect(30, 86, 36, 14, BLUE, rx=4)


@art("pie")
def _():
    toes = "".join(circle(x, y, r, SKIN) for x, y, r in [(30, 22, 8), (44, 18, 6), (55, 18, 5.2), (64, 21, 4.6), (72, 26, 4)])
    return path("M22 34 C20 54 26 70 30 82 C34 94 56 96 60 86 C64 76 56 66 62 52 C66 42 78 38 76 30 C70 26 30 26 22 34Z", SKIN) + toes + \
        path("M36 70 Q42 76 48 72", stroke=SKIN2, sw=2.4)


@art("doctor")
def _():
    coat = path("M22 104 C22 80 34 66 50 66 C66 66 78 80 78 104 Z", WHITE) + path("M42 68 L50 86 L58 68", fill=LBLUE, sw=2.4) + \
        path("M38 70 Q32 88 42 92 M42 92 a3 3 0 1 0 0.1 0", sw=2.4) + circle(42, 94, 3.5, GREY, sw=2)
    return person(shirt=WHITE, hair_style="short", hair_color=BLACK, skin=SKIN2, glasses=True, extra_front=coat) + \
        rect(66, 78, 6, 6, RED, stroke=False) + rect(64, 80, 10, 2, RED, stroke=False)


@art("pastilla")
def _():
    return group("rotate(-40 50 50)", path("M20 50 A16 16 0 0 1 36 34 H50 V66 H36 A16 16 0 0 1 20 50Z", RED),
                 path("M50 34 H64 A16 16 0 0 1 64 66 H50Z", WHITE), path("M28 46 Q30 40 36 40", stroke="#FF9A8F", sw=3)) + \
        circle(78, 78, 8, LBLUE) + line(72, 78, 84, 78, sw=2.2)


@art("fiebre")
def _():
    return rect(42, 8, 16, 60, WHITE, rx=8) + circle(50, 76, 14, RED) + rect(47, 30, 6, 40, RED, stroke=False) + \
        path("M58 20 h6 M58 30 h6 M58 40 h6 M58 50 h6", sw=2.4) + \
        path("M24 18 q-4 7 0 10 q4 -3 0 -10z", LBLUE, sw=2) + path("M78 52 l8 -4 M80 62 h10 M78 72 l8 4", stroke=RED, sw=3)


# ── Fiestas y tradiciones ──

@art("pinata")
def _():
    cone = lambda a, c: group(f"rotate({a} 50 52)", poly([(42, 34), (50, 4), (58, 34)], c))
    tassels = "".join(path(f"M{x} 82 q-2 8 2 14", stroke=c, sw=3) for x, c in [(40, RED), (46, BLUE), (52, YELLOW), (58, GREEN)])
    return "".join(cone(a, c) for a, c in zip(range(0, 360, 72), [PINK, YELLOW, BLUE, GREEN, ORANGE])) + \
        circle(50, 52, 20, PINK) + path("M30 48 H70 M31 58 H69", stroke=YELLOW, sw=4) + tassels


@art("mariachi")
def _():
    hat = ellipse(50, 26, 40, 9, BLACK) + path("M36 24 C36 6 42 2 50 2 C58 2 64 6 64 24Z", BLACK) + \
        path("M14 26 Q50 40 86 26", stroke=GOLD, sw=2.6) + path("M37 18 Q50 22 63 18", stroke=GOLD, sw=2.4)
    suit = path("M22 104 C22 80 34 66 50 66 C66 66 78 80 78 104 Z", BLACK) + path("M44 66 L50 80 L56 66Z", WHITE, sw=2) + \
        "".join(dot(x, y, 2, GOLD) for x, y in [(32, 80), (68, 80), (30, 92), (70, 92)])
    return person(shirt=BLACK, hair_style="short", hair_color=BLACK, skin=SKIN2, mustache=True, bow=RED,
                  extra_back="", extra_front=suit + path("M43 70 L50 74 L57 70 L57 78 L50 74 L43 78Z", RED, sw=2)) + hat


@art("calavera")
def _():
    return path("M50 10 C26 10 16 28 18 48 C19 60 26 64 30 70 V82 Q30 88 36 88 H64 Q70 88 70 82 V70 C74 64 81 60 82 48 C84 28 74 10 50 10Z", WHITE) + \
        circle(36, 48, 10, PINK) + circle(64, 48, 10, BLUE) + circle(36, 48, 4, WHITE, sw=2) + circle(64, 48, 4, WHITE, sw=2) + \
        path("M47 62 L50 56 L53 62Z", BLACK) + path("M38 74 H62 M42 70 V78 M50 70 V78 M58 70 V78", sw=2.2) + \
        "".join(circle(x, 22, 3.5, c, sw=1.8) for x, c in [(40, ORANGE), (50, GREEN), (60, ORANGE)]) + \
        path("M24 36 q4 -6 8 0 M68 36 q4 -6 8 0", stroke=PURPLE, sw=2.4)


@art("vela")
def _():
    return path("M50 6 C40 18 42 28 50 32 C58 28 60 18 50 6Z", ORANGE) + path("M50 16 C46 22 47 27 50 28 C53 27 54 22 50 16Z", YELLOW, sw=2) + \
        line(50, 32, 50, 38, sw=2.6) + rect(36, 38, 28, 50, CREAM, rx=4) + path("M40 38 Q42 50 46 46 Q48 40 52 38", WHITE, sw=2.4) + \
        ellipse(50, 90, 26, 6, GOLD)


@art("cempasuchil")
def _():
    petals = "".join(group(f"rotate({a} 50 46)", ellipse(50, 26, 9, 14, ORANGE, sw=2.6)) for a in range(0, 360, 30))
    inner = "".join(group(f"rotate({a + 15} 50 46)", ellipse(50, 34, 6, 9, "#FFB833", sw=2.2)) for a in range(0, 360, 45))
    return path("M50 66 Q46 84 50 98", stroke=DGREEN, sw=5) + path("M50 84 Q36 76 30 84 Q38 92 50 86", GREEN, sw=2.4) + \
        petals + inner + circle(50, 46, 8, "#E07A1A")


@art("fuegos-artificiales")
def _():
    def burst(cx, cy, r, c):
        return "".join(group(f"rotate({a} {cx} {cy})", line(cx, cy - r * 0.35, cx, cy - r, sw=3.4, color=c)) for a in range(0, 360, 30)) + \
            circle(cx, cy, r * 0.18, c, sw=2)
    return rect(4, 4, 92, 92, NAVY, rx=18) + burst(36, 38, 26, PINK) + burst(70, 30, 18, YELLOW) + burst(66, 70, 16, LGREEN) + \
        sparkle(20, 76, 5, WHITE) + sparkle(84, 54, 4, WHITE)


@art("pan-de-muerto")
def _():
    return path("M10 70 C10 40 30 28 50 28 C70 28 90 40 90 70 Q90 80 80 80 H20 Q10 80 10 70Z", "#D99A4E") + \
        path("M18 54 Q34 44 50 52 Q66 60 82 52", stroke="#A8692E", sw=7) + path("M18 54 Q34 44 50 52 Q66 60 82 52", stroke="#E9B46E", sw=3) + \
        path("M50 30 Q42 44 50 62", stroke="#A8692E", sw=7) + path("M50 30 Q42 44 50 62", stroke="#E9B46E", sw=3) + \
        circle(50, 30, 7, "#C9853F") + "".join(dot(x, y, 1.4, WHITE) for x, y in [(26, 66), (36, 72), (64, 70), (74, 64), (30, 40), (70, 42)])


@art("ofrenda")
def _():
    return rect(10, 70, 80, 22, PURPLE) + rect(20, 50, 60, 22, PINK) + rect(30, 30, 40, 22, ORANGE) + \
        rect(40, 10, 20, 24, WHITE, rx=2) + circle(50, 19, 4, SKIN, sw=1.8) + path("M44 30 Q50 22 56 30", BLUE, sw=1.8) + \
        "".join(rect(x, 36, 5, 14, CREAM, rx=1.5, sw=2) + circle(x + 2.5, 33, 2.6, YELLOW, sw=1.6) for x in (33, 62)) + \
        "".join(circle(x, 62, 5.5, ORANGE, sw=2) for x in (28, 72)) + circle(50, 60, 7, "#D99A4E", sw=2) + \
        path("M10 70 l10 -4 l10 4 l10 -4 l10 4 l10 -4 l10 4 l10 -4 l10 4", stroke=YELLOW, sw=2.6)


# ── Tiempo libre ──

@art("futbol")
def _():
    return circle(50, 50, 38, WHITE) + poly([(50, 36), (62, 45), (58, 59), (42, 59), (38, 45)], BLACK, sw=2) + \
        path("M50 36 V14 M62 45 L82 38 M58 59 L70 76 M42 59 L30 76 M38 45 L18 38", sw=2.4) + \
        path("M40 14 L50 13 L60 15 L56 22 H44Z", BLACK, sw=2) + path("M86 46 L80 38 L84 30", BLACK, sw=2) + \
        path("M14 46 L20 38 L16 30", BLACK, sw=2) + path("M62 84 L70 76 L78 80", BLACK, sw=2) + path("M38 84 L30 76 L22 80", BLACK, sw=2)


@art("lucha-libre")
def _():
    return path("M50 8 C24 8 14 30 16 54 C18 76 32 92 50 92 C68 92 82 76 84 54 C86 30 76 8 50 8Z", RED) + \
        path("M50 8 C44 24 44 34 50 40 C56 34 56 24 50 8Z", YELLOW, sw=2.4) + \
        path("M22 44 Q34 32 46 46 Q36 60 22 52Z", WHITE, sw=2.6) + path("M78 44 Q66 32 54 46 Q64 60 78 52Z", WHITE, sw=2.6) + \
        dot(36, 48, 3.4) + dot(64, 48, 3.4) + path("M38 70 Q50 80 62 70 Q50 74 38 70Z", SKIN, sw=2.4) + \
        path("M24 40 L14 30 M76 40 L86 30", stroke=YELLOW, sw=4) + path("M40 60 L50 66 L60 60", stroke=YELLOW, sw=3)


@art("musica")
def _():
    return path("M34 74 V24 L80 14 V64", sw=5) + path("M34 34 L80 24", sw=6) + \
        ellipse(26, 76, 11, 8, PURPLE, rot=-20) + ellipse(72, 66, 11, 8, PINK, rot=-20) + \
        sparkle(14, 30, 6) + sparkle(90, 84, 5, LBLUE)


@art("cine")
def _():
    stripes = "".join(poly([(20 + i * 12, 40), (26 + i * 12, 40), (24 + i * 11.4, 92), (18 + i * 11.4, 92)], RED if i % 2 == 0 else WHITE, stroke=False) for i in range(6))
    kernels = "".join(circle(x, y, 9, LYELLOW, sw=2.4) for x, y in [(26, 34), (40, 26), (54, 30), (68, 26), (78, 36), (34, 18), (60, 16), (48, 14)])
    return kernels + poly([(16, 38), (84, 38), (74, 92), (26, 92)], WHITE) + stripes + poly([(16, 38), (84, 38), (74, 92), (26, 92)], "none")


@art("libro")
def _():
    return path("M50 26 Q32 16 10 20 V80 Q32 76 50 86Z", BLUE) + path("M50 26 Q68 16 90 20 V80 Q68 76 50 86Z", LBLUE) + \
        path("M50 30 Q34 22 16 25 V74 Q34 71 50 80Z", WHITE, sw=2.2) + path("M50 30 Q66 22 84 25 V74 Q66 71 50 80Z", WHITE, sw=2.2) + \
        path("M22 36 Q34 34 44 38 M22 46 Q34 44 44 48 M22 56 Q34 54 44 58 M56 38 Q66 34 78 36 M56 48 Q66 44 78 46", stroke=GREY, sw=2.2)


@art("guitarra")
def _():
    return group("rotate(35 50 50)",
                 rect(45, 2, 10, 46, BROWN, rx=2), rect(42, -6, 16, 12, DBROWN, rx=3),
                 path("M50 44 C36 44 30 52 34 60 C26 64 24 80 34 88 C42 94 58 94 66 88 C76 80 74 64 66 60 C70 52 64 44 50 44Z", ORANGE),
                 circle(50, 66, 7, DBROWN), rect(42, 78, 16, 5, DBROWN, rx=2),
                 path("M48 4 V80 M52 4 V80", stroke=WHITE, sw=1))


@art("baile")
def _():
    return circle(54, 16, 9, SKIN2) + path("M46 12 Q50 4 60 8 Q64 12 62 18", BLACK, sw=2.4) + circle(64, 10, 4, RED, sw=2) + \
        path("M54 26 L50 50", stroke=SKIN2, sw=6) + \
        path("M52 30 L30 22 M54 32 L80 42", stroke=SKIN2, sw=5) + \
        path("M50 28 C44 30 44 44 48 50 C30 60 14 76 18 86 C34 80 40 92 52 86 C64 92 70 80 86 84 C88 70 70 58 56 50 C60 42 58 30 50 28Z", RED) + \
        path("M24 82 C34 76 40 86 52 82 C62 86 68 76 80 80", stroke=YELLOW, sw=3) + path("M44 88 L42 98 M58 88 L62 98", stroke=SKIN2, sw=4)


@art("fiesta")
def _():
    balloon = lambda x, y, c: ellipse(x, y, 13, 16, c) + path(f"M{x} {y + 16} l-3 4 h6z", c, sw=2) + path(f"M{x} {y + 20} q-6 14 2 30", sw=2.2)
    confetti = "".join(rect(x, y, 5, 3, c, rx=1, rot=r, stroke=False) for x, y, c, r in [(14, 80, YELLOW, 30), (84, 76, PINK, -20), (20, 18, BLUE, 10), (86, 18, GREEN, 40), (50, 90, ORANGE, 0)])
    return balloon(32, 30, RED) + balloon(66, 26, BLUE) + balloon(50, 44, YELLOW) + confetti + sparkle(84, 50, 5)


# ── Cocina mexicana ──

@art("mole")
def _():
    seeds = "".join(ellipse(x, y, 2.2, 1.2, CREAM, stroke=False, rot=r) for x, y, r in [(40, 54, 20), (52, 50, -10), (60, 58, 30), (46, 62, 0), (66, 52, -30), (34, 60, 10)])
    return plate(50, 62, 42, 18) + path("M20 60 Q24 44 50 46 Q78 44 80 60 Q76 72 50 72 Q24 72 20 60Z", "#5A2E1A") + \
        path("M40 54 Q50 48 60 54", stroke="#8A4A2A", sw=3) + seeds + steam(38, 38, 3, 12)


@art("pozole")
def _():
    kernels = "".join(circle(x, y, 3.4, WHITE, sw=1.6) for x, y in [(34, 48), (44, 46), (56, 47), (66, 49), (40, 54), (60, 53)])
    return bowl(50, 48, 76, "#2F6DB5", "#C9402E", 36) + kernels + path("M70 40 l8 -10 l4 6z", GREEN, sw=2) + \
        circle(30, 44, 4, "#FF6B8A", sw=1.8) + steam(38, 30, 3, 12) + \
        path("M24 66 q8 6 16 0 q8 6 16 0 q8 6 16 0", stroke=WHITE, sw=2.4)


@art("tamal")
def _():
    return path("M50 6 C34 20 26 50 30 80 L50 96 L70 80 C74 50 66 20 50 6Z", "#C9B26A") + \
        path("M50 20 C40 32 36 52 38 76 L50 86 L62 76 C64 52 60 32 50 20Z", LYELLOW, sw=2.4) + \
        path("M50 30 C46 44 46 60 48 74", stroke="#C9402E", sw=4) + \
        path("M30 80 C36 70 34 40 50 6 M70 80 C64 70 66 40 50 6", stroke="#A08A44", sw=2) + \
        path("M28 58 H72", stroke=DBROWN, sw=3)


@art("chilaquiles")
def _():
    chips = "".join(poly([(x, y), (x + 14, y - 6), (x + 6, y + 10)], GOLD, sw=2.2) for x, y in [(26, 54), (40, 48), (56, 50), (34, 60), (52, 60), (64, 56)])
    return plate(50, 66, 42, 18) + path("M18 64 Q22 52 50 52 Q78 52 82 64 Q76 74 50 74 Q24 74 18 64Z", "#4E9A3E") + chips + \
        path("M30 56 Q40 52 50 58 Q60 52 70 58", stroke=WHITE, sw=4) + circle(66, 50, 5, WHITE, sw=2) + circle(66, 50, 2.4, YELLOW, stroke=False) + \
        "".join(rect(x, y, 4, 3, WHITE, rx=1, stroke=False) for x, y in [(38, 62), (56, 64), (46, 54)])


@art("frijoles")
def _():
    beans = "".join(ellipse(x, y, 5, 3.4, "#5A2E2A", sw=1.8, rot=r) for x, y, r in [(34, 40, 20), (46, 37, -10), (58, 38, 30), (68, 42, -20), (40, 46, 0), (54, 45, 15), (28, 46, -30), (64, 48, 10)])
    return path("M14 44 Q14 86 50 86 Q86 86 86 44 Z", "#C9653A") + ellipse(50, 44, 36, 10, "#7A3B2E") + beans + \
        path("M8 46 H18 M82 46 H92", sw=5) + path("M26 66 q8 4 16 0 M58 66 q8 4 16 0", stroke="#E99A6A", sw=3)


@art("quesadilla")
def _():
    return path("M12 72 A38 38 0 0 1 88 72 Z", "#F2D48A") + \
        path("M22 72 Q24 80 30 76 Q34 84 40 78 Q46 86 52 78 Q58 84 62 76 Q70 82 74 72Z", LYELLOW, sw=2.4) + \
        "".join(circle(x, y, r, "#C98A3A", stroke=False) for x, y, r in [(34, 50, 3), (50, 42, 3.4), (66, 52, 3), (44, 60, 2.4), (58, 62, 2.6)]) + \
        path("M12 72 H88", sw=3.2)


@art("horchata")
def _():
    return poly([(26, 20), (74, 20), (68, 92), (32, 92)], "#F4EEDF") + poly([(29, 34), (71, 34), (67, 88), (33, 88)], WHITE, sw=2) + \
        ellipse(50, 20, 24, 5, WHITE) + rect(58, 4, 7, 40, "#B5703A", rx=3, rot=15) + \
        "".join(dot(x, y, 1.4, "#C9965A") for x, y in [(40, 50), (52, 58), (46, 70), (58, 76), (42, 80)])


@art("concha")
def _():
    return path("M10 66 C10 38 28 24 50 24 C72 24 90 38 90 66 Z", "#E8B06A") + \
        path("M16 60 C16 40 30 30 50 30 C70 30 84 40 84 60 Z", PINK, sw=2.4) + \
        path("M50 30 V60 M34 34 Q30 46 30 60 M66 34 Q70 46 70 60 M20 46 Q50 38 80 46", stroke="#FFDCE8", sw=2.6) + \
        rect(10, 64, 80, 10, "#D99A4E", rx=5)


# ── Los animales ──

@art("perro")
def _():
    return ellipse(26, 40, 10, 20, BROWN, rot=20) + ellipse(74, 40, 10, 20, BROWN, rot=-20) + \
        circle(50, 52, 30, TAN) + ellipse(50, 66, 16, 12, CREAM) + ellipse(50, 60, 6, 4.5, BLACK) + \
        dot(39, 46, 3.4) + dot(61, 46, 3.4) + path("M44 70 Q50 75 56 70", sw=2.6) + \
        path("M47 76 Q50 86 53 76", PINK, sw=2.2) + circle(62, 30, 6, BROWN, stroke=False)


@art("gato")
def _():
    return poly([(24, 40), (28, 10), (46, 28)], ORANGE) + poly([(76, 40), (72, 10), (54, 28)], ORANGE) + \
        poly([(29, 32), (31, 18), (40, 28)], PINK, stroke=False) + poly([(71, 32), (69, 18), (60, 28)], PINK, stroke=False) + \
        ellipse(50, 56, 32, 28, ORANGE) + path("M40 32 l4 8 M50 30 v9 M60 32 l-4 8", stroke="#D9761A", sw=3) + \
        ellipse(38, 52, 4, 5.5, LGREEN, sw=2) + ellipse(62, 52, 4, 5.5, LGREEN, sw=2) + dot(38, 52, 1.8) + dot(62, 52, 1.8) + \
        path("M47 62 h6 l-3 3z", PINK, sw=1.8) + path("M44 70 Q47 72 50 66 Q53 72 56 70", sw=2.2) + \
        path("M30 62 H12 M30 66 L14 72 M70 62 H88 M70 66 L86 72", sw=1.8)


@art("burro")
def _():
    return ellipse(34, 20, 7, 20, GREY, rot=-15) + ellipse(66, 20, 7, 20, GREY, rot=15) + ellipse(34, 22, 3, 13, LPINK, rot=-15, stroke=False) + \
        ellipse(66, 22, 3, 13, LPINK, rot=15, stroke=False) + path("M28 42 C28 30 72 30 72 42 L68 76 C66 92 34 92 32 76Z", GREY) + \
        ellipse(50, 78, 18, 13, LGREY) + dot(44, 76, 2.2) + dot(56, 76, 2.2) + dot(40, 52, 3.2) + dot(60, 52, 3.2) + \
        path("M40 30 q6 6 10 -2 q4 8 10 2", DGREY, sw=2.2)


@art("aguila")
def _():
    return path("M50 40 C34 30 16 36 4 30 C10 44 18 50 30 52 C20 56 14 62 10 70 C26 68 38 62 46 56Z", BROWN) + \
        path("M50 40 C66 30 84 36 96 30 C90 44 82 50 70 52 C80 56 86 62 90 70 C74 68 62 62 54 56Z", BROWN) + \
        ellipse(50, 56, 12, 20, DBROWN) + circle(50, 32, 11, WHITE) + path("M58 32 L68 36 L58 40Z", GOLD, sw=2.2) + dot(52, 30, 2.2) + \
        path("M44 74 L42 86 M56 74 L58 86", stroke=GOLD, sw=4) + path("M38 88 h8 M54 88 h8", stroke=GOLD, sw=3)


@art("serpiente")
def _():
    return path("M14 82 C30 92 52 88 54 74 C56 60 34 62 34 48 C34 34 56 30 66 36", stroke=INK, sw=17) + \
        path("M14 82 C30 92 52 88 54 74 C56 60 34 62 34 48 C34 34 56 30 66 36", stroke=GREEN, sw=11) + \
        path("M20 84 l4 -4 M36 86 l2 -6 M48 78 l5 -2 M44 64 l-4 -4 M36 50 l-6 0 M46 38 l-2 -5", stroke=YELLOW, sw=3) + \
        ellipse(72, 34, 13, 10, GREEN) + dot(74, 30, 2.4) + path("M84 36 l8 2 l-4 2 l4 2 l-8 -1", stroke=RED, sw=2)


@art("ajolote")
def _():
    gills = lambda side: "".join(path(f"M{50 + side * 20} {y} q{side * 12} {-4 + i * 2} {side * 16} {-10 + i * 6}", stroke="#FF5C8A", sw=4.5) for i, y in enumerate((34, 42, 50)))
    return gills(-1) + gills(1) + ellipse(50, 74, 26, 14, "#FFB3C8") + path("M72 76 Q90 70 96 82 Q86 86 72 82Z", "#FFB3C8") + \
        ellipse(50, 46, 26, 20, "#FFB3C8") + dot(38, 42, 3.4) + dot(62, 42, 3.4) + path("M40 54 Q50 60 60 54", sw=2.6) + \
        circle(32, 52, 3.5, "#FF7FA6", stroke=False) + circle(68, 52, 3.5, "#FF7FA6", stroke=False) + \
        path("M34 84 l-4 8 M64 84 l4 8", sw=3)


@art("mariposa")
def _():
    wing = lambda s: path(f"M50 48 C{50 + s * 10} 20 {50 + s * 40} 8 {50 + s * 44} 24 C{50 + s * 46} 38 {50 + s * 30} 48 50 50 C{50 + s * 30} 52 {50 + s * 42} 70 {50 + s * 30} 82 C{50 + s * 18} 90 {50 + s * 8} 70 50 52Z", ORANGE)
    veins = lambda s: path(f"M50 48 L{50 + s * 30} 22 M50 50 L{50 + s * 34} 42 M50 52 L{50 + s * 26} 76", stroke=INK, sw=2.4)
    spots = "".join(dot(x, y, 2, WHITE) for x, y in [(12, 26), (88, 26), (16, 38), (84, 38), (28, 82), (72, 82)])
    return wing(-1) + wing(1) + veins(-1) + veins(1) + spots + ellipse(50, 52, 4, 20, BLACK) + \
        path("M48 34 Q42 22 38 18 M52 34 Q58 22 62 18", sw=2.2)


@art("jaguar")
def _():
    spots = "".join(circle(x, y, r, "none", stroke=DBROWN, sw=2.6) for x, y, r in [(32, 40, 4), (68, 40, 4), (24, 58, 3.5), (76, 58, 3.5), (50, 30, 3.6), (40, 26, 2.6), (60, 26, 2.6)])
    return circle(24, 24, 10, GOLD) + circle(76, 24, 10, GOLD) + circle(24, 24, 5, TAN, stroke=False) + circle(76, 24, 5, TAN, stroke=False) + \
        circle(50, 52, 34, GOLD) + spots + ellipse(50, 68, 16, 12, CREAM) + poly([(44, 60), (56, 60), (50, 66)], DBROWN, sw=2) + \
        ellipse(38, 48, 4.5, 5.5, "#9BE36B", sw=2) + ellipse(62, 48, 4.5, 5.5, "#9BE36B", sw=2) + ellipse(38, 48, 1.4, 4, BLACK, stroke=False) + \
        ellipse(62, 48, 1.4, 4, BLACK, stroke=False) + path("M44 72 Q50 76 56 72", sw=2.2) + path("M50 66 V72", sw=2)
