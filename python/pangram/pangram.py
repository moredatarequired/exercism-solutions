from string import ascii_lowercase


def is_pangram(sentence):
    return ascii_lowercase in "".join(sorted(set(sentence.lower())))
