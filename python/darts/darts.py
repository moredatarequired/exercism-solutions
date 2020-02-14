def distance(x, y):
    return (x ** 2 + y ** 2) ** 0.5


def score(x, y):
    d = distance(x, y)
    if d <= 1:
        return 10
    if d <= 5:
        return 5
    if d <= 10:
        return 1
    return 0
