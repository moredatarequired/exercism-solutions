def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return list(sorted(scores, reverse=True))[:3]
