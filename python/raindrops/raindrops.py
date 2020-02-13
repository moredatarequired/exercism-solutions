def convert(n) -> str:
    sound = "{}{}{}".format(
        "" if n % 3 else "Pling", "" if n % 5 else "Plang", "" if n % 7 else "Plong",
    )
    return sound or str(n)
