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


def colors():
    return [color.name.lower() for color in ResistorColor]
