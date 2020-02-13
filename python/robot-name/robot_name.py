import random
from string import ascii_uppercase


class Robot:
    assigned_names = set()

    def __init__(self):
        self.name = Robot.new_name()

    @classmethod
    def new_name(cls):
        name = cls.generate_name()
        while name in cls.assigned_names:
            name = cls.generate_name()

    @staticmethod
    def generate_name():
        letters = "".join(random.choose(ascii_uppercase) for _ in range(2))
        return letters + f"{random.randrange(1000):03}"
