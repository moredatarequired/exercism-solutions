from collections import Counter
from enum import auto, Enum


class Category(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    YACHT = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    LITTLE_STRAIGHT = auto()
    BIG_STRAIGHT = auto()
    CHOICE = auto()


def score(dice, category):
    die_counts = Counter(dice)

    if category.value in range(1, 7):
        return sum(d for d in dice if d == category.value)
    if category is Category.YACHT:
        return 50 if len(die_counts) == 1 else 0
    if category is Category.CHOICE:
        return sum(dice)
    if category is Category.BIG_STRAIGHT:
        return 30 if 1 not in die_counts and len(die_counts) == 5 else 0
    if category is Category.LITTLE_STRAIGHT:
        return 30 if 6 not in die_counts and len(die_counts) == 5 else 0
    if category is Category.FULL_HOUSE:
        return sum(dice) if len(die_counts) == 2 and 3 in die_counts.values() else 0
    if category is Category.FOUR_OF_A_KIND:
        four_die = [d for d, c in die_counts.items() if c >= 4]
        return four_die[0] * 4 if four_die else 0
