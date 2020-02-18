def factors(n):
    """Return all the factors > 1 of the number (not just prime factors)."""
    return [f for f in range(1, n // 2 + 1) if n % f == 0]


def classify(number):
    if number < 1:
        raise ValueError("Classify only accepts positive integers.")
    sum_fact = sum(factors(number))
    if sum_fact == number:
        return "perfect"
    if sum_fact > number:
        return "abundant"
    return "deficient"
