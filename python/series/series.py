def slices(series, length):
    if length <= 0:
        raise ValueError("length must be positive")
    if length > len(series):
        raise ValueError("length may not be longer than the input string")
    return [series[i : i + length] for i in range(0, len(series) - length + 1)]
