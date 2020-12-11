import numpy as np
import pandas as pd


def run_simulation(s0: float, mu: float, sigma: float, t: int, n: int):
    """ Simulate geometric brownian motion

    :param s0: initial value
    :param mu: mean
    :param sigma: standard deviation
    :param t: time
    :param n: number of simulations
    :return: dataframe with simulated values
    """
    values = s0 * np.exp((mu-sigma**2/2) * t + np.random.normal(0, sigma, n))
    return pd.DataFrame(values, columns=['value'])
