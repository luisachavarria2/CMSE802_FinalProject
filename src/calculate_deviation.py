# calculate_deviation.py

"""
This module is designed for the calculation of the deviation of the LSF from the 
Vegard's Law.

Author: Luisa Chavarria, AI (ChatGPT)
Date: April 2025
"""

import numpy as np


def calculate_deviation_vegard(x, V, V_MgO, V_FeO, V_lsf):
    """
    Calculate the absolute and relative deviation between the Least Squares Fit (LSF) 
    and Vegard's Law.
    
    Parameters:
    -----------
    x : np.ndarray
        Fe mole fraction.
    V : np.ndarray
        Experimental molar volume data.
    V_MgO : float
        Molar volume of MgO (pure MgO).
    V_FeO : float
        Molar volume of FeO (pure FeO).
    V_lsf : np.ndarray
        Molar volume predicted by the Least Squares Fit.
    
    Returns:
    --------
    tuple
        (mean_deviation, mean_relative_deviation)
    """
    
    # Calculate volume predicted using Vegard's Law
    V_vegard = (V_FeO - V_MgO) * x + V_MgO
    
    # Calculate absolute and relative deviation
    deviation = np.abs(V_lsf - V_vegard)  # Absolute deviation
    relative_deviation = (deviation / np.abs(V_vegard)) * 100  # Relative deviation in percentage

    # Compute mean deviation
    mean_deviation = np.mean(deviation)
    mean_relative_deviation = np.mean(relative_deviation)

    return mean_deviation, mean_relative_deviation
