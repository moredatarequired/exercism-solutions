import random


def modifier(stat):
    return (stat - 10) // 2


class Character:
    def __init__(self):
        self.strength = Character.ability()
        self.dexterity = Character.ability()
        self.constitution = Character.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability(n=4, d=6, drop=1):
        dice = sorted(random.randint(1, d) for _ in range(n))
        return sum(dice[drop:])
