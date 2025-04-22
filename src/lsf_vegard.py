# lsf_vegard.py

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

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def linear_model(x, a, b):
    """
    Defines a linear model: V = a * x + b.
    
    Parameters:
    -----------
    x : np.ndarray
        Fe mole fraction, which is the independent variable.
    
    a : float
        Slope of the linear fit (coefficient for x).
    
    b : float
        Intercept of the linear fit (constant term).
    
    Returns:
    --------
    np.ndarray
        The calculated volume values based on the linear model.
    """

    return a * x + b

def compare_models(x, V, V_MgO, V_FeO):
    """
    Fit a linear model to the data and plot it along with Vegard's Law line.
    
    Parameters:
    -----------
    x : np.ndarray
        Fe mole fraction
    V : np.ndarray
        Experimental molar volume data
    
    V_MgO : float
        Molar volume of MgO (pure MgO)
    
    V_FeO : float
        Molar volume of FeO (pure FeO)
    
    Returns:
    --------
    tuple
        (a, b) Fitted parameters of the linear model
    """
    try:
        # Fit the data using least squares
        params, covariance = curve_fit(linear_model, x, V, p0=[1, 74])
        a, b = params
    except Exception as e:
        print(f"An error occurred during curve fitting: {e}")
        return None, None

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(x, V, label='Experimental Data', color='blue', zorder=5)
    
    # Plot the least squares fit
    plt.plot(x, linear_model(x, a, b), label=f'Linear Fit: V = {a:.3f}x + {b:.3f}', color='red', linewidth=2)

    # Plot Vegard's Law line
    V_vegard = (V_FeO - V_MgO) * x + V_MgO
    plt.plot(x, V_vegard, label=f"Vegard's Law: V = ({V_FeO - V_MgO:.3f})x + {V_MgO:.3f}", color='green', linestyle='--', linewidth=2)
    
    # Labels and title
    plt.xlabel('Fe Fraction (x)', fontsize=12)
    plt.ylabel('Volume (A^3)', fontsize=12)
    plt.title('Fe Mole Fraction vs Volume', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Return fitted parameters for deviation calculation
    return a, b
