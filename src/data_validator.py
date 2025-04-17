# data_validator.py

""""
Module for the validation of the data.
This module ensures that the input data meet the
required criteria for analysis.

Author: Luisa Chavarria, Ai (ChatGPT)
Date: April 2025

"""

import numpy as np

def check_data_validity(x, V):

    """
    Validates that x and V are suitable for analysis and prints statistics.

    Parameters:
    - x (np.ndarray): Array of Fe mole fractions
    - V (np.ndarray): Array of corresponding molar volumes

    Raises:
    - ValueError: If any validation check fails

    Output:

    - Prints:
        - Confirmation message if data is valid.
        - Minimum, maximum, mean, and standard deviation for both `x` and `V`.
    """

    if len(x) != len(V):
        raise ValueError("The length of x and V arrays must be the same.")
    if len(x) == 0 or len(V) == 0:
        raise ValueError("x and V arrays must not be empty.")
    if np.any(np.isnan(x)) or np.any(np.isnan(V)):
        raise ValueError("x and V arrays must not contain NaN values.")
    if np.any(np.isinf(x)) or np.any(np.isinf(V)):
        raise ValueError("x and V arrays must not contain infinite values.")

    # Print statistics
    print("Data is valid.\n")
    print("Statistics:")
    print(f"- x (Fe mole fractions): min = {np.min(x):.4f}, max = {np.max(x):.4f}, mean = {np.mean(x):.4f}, std = {np.std(x):.4f}")
    print(f"- V (volume - A^3): min = {np.min(V):.4f}, max = {np.max(V):.4f}, mean = {np.mean(V):.4f}, std = {np.std(V):.4f}")
