# linear_lsf.py

"""
Module for the modeling of the volume according to the iron concentration using 
Least squares fit (LSF)

This module provides functionality to fit a linear model to experimental data
(x: Fe mole fraction, V: molar volume) and visualize the result.

Author: Luisa Chavarria, Ai (ChatGPT)
Date: April 2025
"""

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def linear_model(x, a, b):
    """
    Defines a linear model: V = a * x + b

    Parameters:
    ----------
    x : float or np.ndarray
        Independent variable (Fe mole fraction).
    a : float
        Slope of the linear model.
    b : float
        Intercept of the linear model.

    Returns:
    -------
    float or np.ndarray
        Computed dependent variable (molar volume).
    """
    return a * x + b


def fit_and_plot_linear_model(x, V):
    """
    Fit a linear model to the data and plot it.

    Parameters:
    ----------
    x : np.ndarray
        Fe mole fraction
    V : np.ndarray
        Molar volume

    Returns:
    -------
    tuple
        (a, b) Fitted parameters of the linear model

    Raises:
    ------
    RuntimeError:
        If the curve fitting fails due to numerical issues.

    Output:
    ------
    - Displays a plot of the experimental data and the fitted line.
    - Prints the fitted equation and parameters.
    """
    try:
        # Initial parameter guess: slope = 1, intercept = 74
        params, covariance = curve_fit(linear_model, x, V, p0=[1, 74])
        a, b = params
    except Exception as e:
        print(f"An error occurred during curve fitting: {e}")
        return None, None

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(x, V, label='Experimental Data', color='blue', zorder=5)
    plt.plot(
        x, linear_model(x, a, b),
        label=f'Linear Fit: V = {a:.3f}x + {b:.3f}',
        color='red', linewidth=2)
        
    plt.xlabel('Fe Fraction (x)', fontsize=12)
    plt.ylabel('Volume (A^3)', fontsize=12)
    plt.title('Fe Mole Fraction vs Volume', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Output results
    print(f"Fitted parameters: a = {a:.3f}, b = {b:.3f}")
    print(f'Linear Fit: V = {a:.3f}x + {b:.3f}')
    return a, b
