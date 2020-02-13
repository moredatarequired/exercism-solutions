def convert(n) -> str:
    sound = "" if n % 3 else "Pling"
    sound += "" if n % 5 else "Plang"
    sound += "" if n % 7 else "Plong"
    return sound or str(n)
