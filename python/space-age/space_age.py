from enum import Enum


class Planet(Enum):
    MERCURY = 1
    VENUS = 2
    EARTH = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8


# Age in earth years / AGE_FACTOR[x] = age in years on planet `x`.
AGE_FACTOR = {
    Planet.MERCURY: 0.2408467,
    Planet.VENUS: 0.61519726,
    Planet.EARTH: 1,  # By definition.
    Planet.MARS: 1.8808158,
    Planet.JUPITER: 11.862615,
    Planet.SATURN: 29.447498,
    Planet.URANUS: 84.016846,
    Planet.NEPTUNE: 164.79132,
}


class SpaceAge:
    def __init__(self, seconds):
        self.earth_age = seconds / 31557600

    def age_on(self, planet):
        return round(self.earth_age / AGE_FACTOR[planet], 2)

    def on_mercury(self):
        return self.age_on(Planet.MERCURY)

    def on_venus(self):
        return self.age_on(Planet.VENUS)

    def on_earth(self):
        return self.age_on(Planet.EARTH)  # Not strictly necessary.

    def on_mars(self):
        return self.age_on(Planet.MARS)

    def on_jupiter(self):
        return self.age_on(Planet.JUPITER)

    def on_saturn(self):
        return self.age_on(Planet.SATURN)

    def on_uranus(self):
        return self.age_on(Planet.URANUS)

    def on_neptune(self):
        return self.age_on(Planet.NEPTUNE)
