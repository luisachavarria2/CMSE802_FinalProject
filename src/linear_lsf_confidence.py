# linear_lsf_confidence.py

"""
Linear Least Squares Fit with Confidence Intervals

This module fits a linear model to experimental data using the least squares method. 
It calculates the coefficient of determination (R²) and plots the regression line 
alongside a 95% confidence interval band.

Features:
---------
- Linear regression using SciPy's curve_fit
- R² (goodness of fit) computation
- 95% confidence interval estimation
- Visualization of the fitted model and confidence bands

Author: Luisa Chavarria, Ai (ChatGPT)
Date: April 2025
"""

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np


def linear_model(x, a, b):
    """
    Linear model function.

    Parameters:
    -----------
    x : array-like
        Independent variable.
    a : float
        Slope of the line.
    b : float
        Intercept of the line.
    """
    return a * x + b


def fit_and_plot_linear_model(x, V):
    """
    Fits a linear model to the data and plots the fit along with a 95% confidence band.

    Parameters:
    -----------
    x : array-like
        Independent variable (e.g., Fe fraction).
    V : array-like
        Dependent variable (e.g., atomic volume).

    Returns:
    --------
    tuple
        (a, b, r², conf_interval)
        - a : float
            Fitted slope of the linear model.
        - b : float
            Fitted intercept.
        - r² : float
            Coefficient of determination (R²).
        - conf_interval : ndarray
            95% confidence intervals for a and b: [±Δa, ±Δb].
    """
    try:
        # Initial parameter guess: slope = 1, intercept = 74
        params, covariance = curve_fit(linear_model, x, V, p0=[1, 74])
        a, b = params

        # Calculate residuals (difference between the actual and fitted values)
        V_pred = linear_model(x, a, b)
        residuals = V - V_pred

        # Calculate R^2 (coefficient of determination)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((V - np.mean(V))**2)
        r2 = 1 - (ss_res / ss_tot)

        # Calculate the standard errors of the parameters (diagonal elements of the covariance matrix)
        perr = np.sqrt(np.diag(covariance))

        # Confidence intervals (95% confidence level)
        conf_interval = 1.96 * perr  # For 95% confidence, use 1.96 for a normal distribution

    except Exception as e:
        print(f"An error occurred during curve fitting: {e}")
        return None, None, None, None

    # Calculate the confidence bands (for plotting)
    V_upper = linear_model(x, a + conf_interval[0], b + conf_interval[1])
    V_lower = linear_model(x, a - conf_interval[0], b - conf_interval[1])

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(x, V, label='Experimental Data', color='blue', zorder=5)
    plt.plot(
        x, linear_model(x, a, b),
        label=f'Linear Fit: V = {a:.3f}x + {b:.3f}, R²: {r2:.3f}',
        color='red', linewidth=2)
    plt.fill_between(x, V_lower, V_upper, color='gray', alpha=0.3,
                     label='95% Confidence Band')

    plt.xlabel('Fe Fraction (x)', fontsize=12)
    plt.ylabel('Volume (Å³/atom)', fontsize=12)
    plt.title('Fe Fraction vs Volume', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Output results
    print(f"Fitted parameters: a = {a:.3f}, b = {b:.3f}")
    print(f"Linear Fit: V = {a:.3f}x + {b:.3f}")
    print(f"R²: {r2:.3f}")
    print(f"Confidence intervals (95%): a = ±{conf_interval[0]:.3f}, "
          f"b = ±{conf_interval[1]:.3f}")

    return a, b, r2, conf_interval
