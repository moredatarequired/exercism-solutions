from enum import Enum


class ResistorColor(Enum):
    BLACK = 0
    BROWN = 1
    RED = 2
    ORANGE = 3
    YELLOW = 4
    GREEN = 5
    BLUE = 6
    VIOLET = 7
    GREY = 8
    WHITE = 9


def color_code(color):
    return ResistorColor[color.upper()].value


# Ignores colors after the first two!
def value(colors):
    return 10 * color_code(colors[0]) + color_code(colors[1])
