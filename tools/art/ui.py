"""Illustrations de l'interface (types de contenu, récompenses, recommandations…)."""
from .kit import *  # noqa: F401,F403

ART = {}


def art(key):
    def deco(fn):
        ART[key] = svg(fn())
        return fn
    return deco


@art("ui-flame")
def _():
    return path("M50 6 C56 22 74 30 76 54 C78 76 64 94 50 94 C36 94 22 80 24 60 C26 46 34 40 38 30 C42 40 44 44 48 46 C50 34 46 20 50 6Z", ORANGE) + \
        path("M50 50 C54 60 64 64 62 76 C60 86 54 90 50 90 C42 90 38 82 40 74 C42 66 48 62 50 50Z", YELLOW, sw=2.6)


@art("ui-star")
def _():
    return star(50, 52, 42, GOLD, inner=0.5) + path("M36 40 L42 34", stroke=WHITE, sw=4)


@art("ui-trophy")
def _():
    return path("M28 14 H72 V40 C72 56 62 64 50 64 C38 64 28 56 28 40Z", GOLD) + \
        path("M28 22 H14 Q12 40 30 46 M72 22 H86 Q88 40 70 46", sw=4.5) + rect(44, 64, 12, 12, GOLD) + \
        rect(30, 76, 40, 12, BROWN, rx=3) + path("M38 22 V40 Q38 50 46 54", stroke=LYELLOW, sw=4) + star(50, 32, 8, YELLOW, sw=2) + \
        sparkle(14, 66, 6) + sparkle(88, 64, 5, PINK)


@art("ui-sprout")
def _():
    return rect(26, 70, 48, 22, "#C9653A", rx=4) + rect(22, 64, 56, 10, "#E07A4A", rx=3) + \
        path("M50 64 V36", stroke=DGREEN, sw=5) + path("M50 44 C34 46 22 36 20 20 C36 20 48 28 50 44Z", GREEN) + \
        path("M50 38 C64 40 78 30 80 14 C64 14 52 22 50 38Z", LGREEN)


@art("ui-phrase")
def _():
    return path("M16 14 H84 Q92 14 92 22 V60 Q92 68 84 68 H44 L24 86 L28 68 H16 Q8 68 8 60 V22 Q8 14 16 14Z", WHITE) + \
        path("M22 32 H78 M22 46 H62", stroke=PINK, sw=5)


@art("ui-grammar")
def _():
    return rect(18, 10, 62, 80, BLUE, rx=6) + rect(18, 10, 12, 80, NAVY, rx=4) + rect(80, 16, 6, 70, WHITE, rx=2) + \
        rect(38, 24, 34, 24, WHITE, rx=4, sw=2.4) + text(55, 43, "Aa", 18, BLUE) + path("M40 62 H72 M40 72 H64", stroke=LBLUE, sw=3.4)


@art("ui-dialogue")
def _():
    return path("M8 14 H54 Q60 14 60 20 V44 Q60 50 54 50 H24 L12 62 L14 50 H8 Q2 50 2 44 V20 Q2 14 8 14Z", YELLOW) + \
        path("M46 40 H92 Q98 40 98 46 V70 Q98 76 92 76 H84 L86 88 L74 76 H46 Q40 76 40 70 V46 Q40 40 46 40Z", TEAL) + \
        path("M12 26 H48 M12 36 H36", stroke=WHITE, sw=3.4) + path("M50 52 H88 M50 62 H74", stroke=WHITE, sw=3.4)


@art("ui-film")
def _():
    return rect(10, 38, 80, 52, DGREY, rx=6) + group("rotate(-12 12 36)", rect(10, 22, 80, 16, WHITE, rx=3),
                                                    "".join(poly([(18 + i * 18, 22), (28 + i * 18, 22), (22 + i * 18, 38), (12 + i * 18, 38)], DGREY, stroke=False) for i in range(4))) + \
        rect(10, 38, 80, 14, WHITE, rx=3) + "".join(poly([(18 + i * 18, 38), (28 + i * 18, 38), (22 + i * 18, 52), (12 + i * 18, 52)], DGREY, stroke=False) for i in range(4)) + \
        rect(10, 38, 80, 14, "none", rx=3) + path("M22 66 H62 M22 76 H50", stroke=GREY, sw=3.4)


@art("ui-series")
def _():
    return path("M34 8 L50 22 L66 8", sw=3.4) + rect(8, 22, 84, 62, "#C9653A", rx=10) + rect(16, 30, 54, 46, LBLUE, rx=8) + \
        path("M24 38 q6 -4 12 0", stroke=WHITE, sw=3) + circle(81, 40, 5, GOLD, sw=2) + circle(81, 56, 5, GOLD, sw=2) + \
        path("M76 68 H86", sw=3) + rect(18, 84, 10, 8, DBROWN, rx=2) + rect(72, 84, 10, 8, DBROWN, rx=2)


@art("ui-book")
def _():
    return rect(16, 66, 70, 16, RED, rx=4) + rect(22, 50, 64, 16, GREEN, rx=4) + rect(12, 34, 70, 16, BLUE, rx=4) + \
        rect(20, 18, 60, 16, YELLOW, rx=4) + path("M74 66 V82 M78 50 V66 M24 34 V50 M70 18 V34", stroke=WHITE, sw=3)


@art("ui-podcast")
def _():
    return path("M16 62 V50 C16 26 32 12 50 12 C68 12 84 26 84 50 V62", sw=7) + path("M16 62 V50 C16 26 32 12 50 12 C68 12 84 26 84 50 V62", stroke=PURPLE, sw=3) + \
        rect(8, 52, 20, 34, PURPLE, rx=8) + rect(72, 52, 20, 34, PURPLE, rx=8) + \
        path("M40 50 q-6 10 0 20 M60 50 q6 10 0 20", stroke=PINK, sw=3) + circle(50, 60, 4, PINK)


@art("ui-bulb")
def _():
    return path("M50 10 C30 10 20 26 22 42 C24 54 34 60 36 70 H64 C66 60 76 54 78 42 C80 26 70 10 50 10Z", YELLOW) + \
        rect(36, 70, 28, 8, LGREY) + rect(38, 78, 24, 8, GREY, rx=2) + path("M44 86 h12", sw=4) + \
        path("M42 54 L46 40 L50 50 L54 40 L58 54", stroke=ORANGE, sw=2.6) + path("M34 28 q4 -8 12 -10", stroke=WHITE, sw=3.4)


@art("ui-review")
def _():
    return rect(30, 14, 52, 64, WHITE, rx=8, rot=10) + rect(18, 22, 52, 64, YELLOW, rx=8, rot=-6) + \
        path("M30 52 A14 14 0 1 1 46 66", stroke=PURPLE, sw=5) + poly([(40, 66), (50, 62), (46, 72)], PURPLE, sw=2)


@art("ui-brain")
def _():
    return path("M50 14 C40 6 24 10 22 24 C10 26 8 42 16 48 C8 56 14 72 26 72 C28 84 44 88 50 80 C56 88 72 84 74 72 C86 72 92 56 84 48 C92 42 90 26 78 24 C76 10 60 6 50 14Z", "#FF9DB0") + \
        path("M50 14 V80 M30 34 q8 4 8 12 M70 34 q-8 4 -8 12 M28 58 q10 -2 14 6 M72 58 q-10 -2 -14 6", sw=2.6)


@art("ui-speaker")
def _():
    return path("M14 38 H32 L54 18 V82 L32 62 H14Z", BLUE) + path("M66 36 q10 14 0 28 M76 26 q18 24 0 48", sw=4.5)


@art("ui-calendar")
def _():
    return calendar(header=GREEN) + cal_grid(highlight=(3, 4, 5, 6, 7, 8, 9), color=LGREEN)
