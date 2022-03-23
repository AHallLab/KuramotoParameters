import numpy as np
import pandas as pd
import math


def get_kuramoto_params(x):
    """
    Calculates the two Kuramoto parameters: r for measuring synchrony and ψ for the average phase.

    Arguments:
    x = 1D numpy array or pandas series, shape (n) where n is number of timepoints, expects unit of time to be hours

    Returns:
    mag = the magnitude of synchrony (r) between the set of oscillators, between [0-1]
    ang = the average phase (ψ) of the set of oscillators

    If you use this code, consider citing https://www.biorxiv.org/content/10.1101/2022.01.11.475783v1
    """
    if isinstance(x, (pd.Series, pd.DataFrame)):
        x = x.values
    if x.ndim > 1:
        print("Input data must be 1 dimensional")
        return np.nan, np.nan
    # Convert from hours to radians
    x = x * np.pi / 12
    scale_factor = 1/x.shape[0]
    cosine_term, sine_term = 0, 0
    for i in range(x.shape[0]):
        cosine_term += np.cos(x[i])
        sine_term += np.sin(x[i])
    # Get magnitude of combined vector through square root of sum of squares
    mag = scale_factor * np.sqrt(cosine_term**2 + sine_term**2)
    # Calculate angle of combined vector, set to be from positive real axis
    ang = math.atan2(cosine_term, sine_term)
    ang += 2*np.pi
    ang = ang % (2*np.pi)
    return mag, ang
