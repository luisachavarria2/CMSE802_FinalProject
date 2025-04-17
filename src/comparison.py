# compare_models.py

"""

Module to compare two linear fitting approaches for modeling the relationship
between Fe mole fraction and unit cell volume:

1. Vegard's Law: V(x) = V_MgO + (V_FeO - V_MgO) * x
2. Least Squares Fit (LSF): V(x) = a * x + b

The module fits both models to the data, prints the fitted parameters,
and displays a comparative plot.

Author: Luisa Chavarria, AI (ChatGPT)
Date: April 2025

"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Define Vegard's law model
def vegards_law(x, V_MgO, V_FeO):
    """
    Vegard's Law model: linear interpolation between end-member volumes.

    Parameters:
    ----------
    x : np.ndarray
        Mole fraction of Fe (0 ≤ x ≤ 1)
    V_MgO : float
        Volume of pure MgO (x = 0)
    V_FeO : float
        Volume of pure FeO (x = 1)

    Returns:
    -------
    np.ndarray
        Estimated volume at each x based on Vegard's law
    """

    return V_MgO + (V_FeO - V_MgO) * x


# Define a linear model for least squares fit
def linear_model(x, a, b):
    """
    Generic linear model for least squares fitting.

    Parameters:
    ----------
    x : np.ndarray
        Independent variable (Fe mole fraction)
    a : float
        Slope of the fitted line
    b : float
        Intercept of the fitted line

    Returns:
    -------
    np.ndarray
        Estimated volume at each x
    """

    return a * x + b


def compare_models(x, V):
    """
    Compare Vegard's law and least squares fit for given data.

    Parameters:
    x : numpy.ndarray
        Fe fraction data
    V : numpy.ndarray
        Unit cell volume data


    Returns:
    None - Prints fitted parameters and shows a comparative plot.
    """

    # Fit Vegard's law model to data
    popt_vegard, _ = curve_fit(vegards_law, x, V)

    # Extract fitted Vegard's law parameters
    V_MgO_fit, V_FeO_fit = popt_vegard
    print(f"Fitted Vegard's Law parameters: V_MgO = {V_MgO_fit:.4f}, V_FeO = {V_FeO_fit:.4f}")

    # Fit the linear model to data using least squares
    popt_linear, _ = curve_fit(linear_model, x, V)

    # Extract fitted linear model parameters
    a_fit, b_fit = popt_linear
    print(f"Fitted Least Squares parameters: a = {a_fit:.4f}, b = {b_fit:.4f}")

    # Plot data and both fitted models
    plt.figure(figsize=(8, 6))

    # Plot original data points
    plt.scatter(x, V, color='black', label='Data')

    # Plot Vegard's law fit
    x_fit = np.linspace(0, 1, 100)
    y_fit_vegard = vegards_law(x_fit, *popt_vegard)
    plt.plot(x_fit, y_fit_vegard, label="Vegard's Law Fit",
             color='blue', linestyle='--')

    # Plot Least Squares fit
    y_fit_linear = linear_model(x_fit, *popt_linear)
    plt.plot(x_fit, y_fit_linear, label="Least Squares Fit",
             color='red', linestyle='-.')

    # Labels and title
    plt.xlabel("Fe Fraction (x)")
    plt.ylabel("Unit Cell Volume (Å³)")
    plt.title("Comparison of Vegard's Law vs Least Squares Fit")
    plt.legend()

    # Show the plot
    plt.show()

# Example usage:

# x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])  # Example Fe fraction data

# Example volume data
# V = np.array([160.1, 162.3, 164.4, 166.5, 168.7, 170.8])

# compare_models(x, V)
