def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    k = len(digits)
    return number == sum(d ** k for d in digits)
