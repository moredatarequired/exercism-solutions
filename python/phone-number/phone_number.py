import re


class PhoneNumber:
    def __init__(self, number):
        number = re.sub(r"\D", "", number)
        if len(number) == 11 and number[0] == "1":
            number = number[1:]
        if len(number) != 10:
            raise ValueError("Phone number must be 10 digits")
        if number[0] in ("0", "1") or number[3] in ("0", "1"):
            raise ValueError("Exchange codes and area codes cannot start with 0 or 1")
        self.number = number

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]}) {self.number[3:-4]}-{self.number[-4:]}"
