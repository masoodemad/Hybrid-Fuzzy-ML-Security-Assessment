import numpy as np

def triangular_membership(x, a, b, c):

    if x <= a or x >= c:
        return 0

    elif a < x <= b:
        return (x - a) / (b - a)

    else:
        return (c - x) / (c - b)


def fuzzy_risk_score(confidentiality,
                     integrity,
                     availability,
                     access_control,
                     threat_exposure,
                     privacy):

    score = (
        confidentiality * 0.236 +
        integrity * 0.190 +
        availability * 0.145 +
        access_control * 0.171 +
        threat_exposure * 0.196 +
        privacy * 0.063
    )

    return round(score, 3)
