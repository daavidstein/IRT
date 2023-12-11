import numpy as np
def exp_part(diff: float, disc: float, ability: float) -> float:
    return np.exp(-disc*(ability-diff))


def irf(diff: float, disc: float, ability: float):
    """Item Response (Characteristic) Function

    Compute the probability that a subject with given ability will answer an item
    with difficulty `diff` and discrimination `disc` correctly

    """
    return 1 / (1 + exp_part(diff, disc, ability))
