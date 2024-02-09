import numpy as np
import pandas as pd
from girth import twopl_jml, ability_map
def exp_part(diff: float, disc: float, ability: float) -> float:
    return np.exp(-disc*(ability-diff))


def irf(diff: float, disc: float, ability: float):
    """Item Response (Characteristic) Function

    Compute the probability that a subject with given ability will answer an item
    with difficulty `diff` and discrimination `disc` correctly

    """
    return 1 / (1 + exp_part(diff, disc, ability))


def iic(ability, diff, disc, scale=True):
    """Item Information Function"""

    #D  is a normalization scaling fator
    D = 1.70

    prob = irf(ability=ability, diff=diff, disc=disc)
    info = (disc ** 2) * prob * (1 - prob)
    if scale:
        info = (D ** 2) * info
    return info

def se_est(ability,disc,diff):
    prob = irf(ability=ability, disc=disc, diff=diff)
    return 1/np.sqrt((disc**2)*prob*(1-prob))

def construct_lsat7_dataset(path_to_csv: str = "/home/daavid/lsat7.csv") -> pd.DataFrame:
    lsat7 = pd.read_csv(path_to_csv)
    lsat7 = lsat7.drop(columns="Unnamed: 0")
    lsat7 = lsat7.rename(columns={col: col.replace(".", "_") for col in lsat7.columns})
    lsat7.index.repeat(lsat7.freq)
    expanded = pd.DataFrame(np.repeat(lsat7.values, lsat7.freq, axis=0), columns=lsat7.columns).drop(columns="freq")
    return expanded


def fit_2pl(dataset: pd.DataFrame,transpose=True):
    """twopl_jml expects the array of responses to be in the form of items x subjects.
    Args:
        dataset: an array of responses in the form of items x subjects
        transpose: transpose an array in the form of subject x items into one of items x subjects
        """
    if transpose:
        dataset = dataset.transpose()
    item_params = twopl_jml(dataset)
    abilities = ability_map(dataset=dataset.to_numpy(), difficulty = item_params["Difficulty"], discrimination=item_params["Discrimination"])
    return item_params, abilities