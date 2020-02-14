from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = Rational.reduced(numer, denom)

    @staticmethod
    def gcd(a, b):
        return a if b == 0 else Rational.gcd(b, a % b)

    @staticmethod
    def reduced(a, b):
        d = Rational.gcd(a, b)
        return a // d, b // d

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __neg__(self):
        return Rational(-self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom,
        )

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
