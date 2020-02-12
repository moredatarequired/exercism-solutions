import re


def convert(n) -> str:
    sound = f"{n % 3 or 'Pling'}{n % 5 or 'Plang'}{n % 7 or 'Plong'}"
    sound = re.sub(r"\d", "", sound)
    return sound if sound else str(n)
