"""
Module for fitting experimental data to Vegard's Law, which describes the linear
relationship between the unit cell volume of a solid solution and its composition.

This is typically applied to binary systems like (Mg,Fe)O to estimate the
end-member volumes (e.g., MgO and FeO) based on intermediate compositions.

Author: Luisa Chavarria, Ai (ChatGPT)
Date: April 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def fit_vegards_law(x, V):
    """
    Fit a linear model to volume-composition data using Vegard's Law.

    Parameters:
    ----------
    x : np.ndarray
        1D array of Fe mole fractions (from 0 to 1).
    V : np.ndarray
        1D array of corresponding unit cell volumes in Å³.

    Returns:
    -------
    model : sklearn.linear_model.LinearRegression
        Fitted linear regression model.
    V_FeO : float
        Extrapolated volume for pure FeO (x = 1).
    V_MgO : float
        Extrapolated volume for pure MgO (x = 0).

    Output:
    ------
    Prints the fitted equation and extrapolated end-member values.
    """
    x_reshaped = x.reshape(-1, 1)
    model = LinearRegression().fit(x_reshaped, V)
    V_FeO = model.predict([[1]])[0]
    V_MgO = model.predict([[0]])[0]

    print(f"\nVegard's Law Fit:")
    print(f"   V(x) = {model.coef_[0]:.4f} * x + {model.intercept_:.4f}")
    print(f"   Extrapolated V_FeO (x=1): {V_FeO:.4f} Å³")
    print(f"   Extrapolated V_MgO (x=0): {V_MgO:.4f} Å³")

    return model, V_FeO, V_MgO


def plot_fit(x, V, model):
    """
    Plot the input data and the fitted Vegard's Law linear model.

    Parameters:
    ----------
    x : np.ndarray
        Fe mole fractions.
    V : np.ndarray
        Corresponding unit cell volumes in Å³.
    model : sklearn.linear_model.LinearRegression
        Fitted regression model.
    """
    x_reshaped = x.reshape(-1, 1)
    plt.scatter(x, V, label='Data', color='blue')
    plt.plot(x, model.predict(x_reshaped), label="Vegard's Law Fit", color='red')
    plt.xlabel("Fe Fraction (x)")
    plt.ylabel("Unit Cell Volume (Å³)")
    plt.title("(Mg,Fe)O — Vegard's Law")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def run_analysis(x, V, plot=False):
    """
    Perform Vegard's Law fitting and optionally plot the results.

    Parameters:
    ----------
    x : np.ndarray
        1D array of Fe mole fractions.
    V : np.ndarray
        1D array of unit cell volumes.
    plot : bool, optional (default=False)
        Whether to generate a plot of the fitted model.

    Returns:
    -------
    model : sklearn.linear_model.LinearRegression
        Fitted model object.
    V_FeO : float
        Predicted volume for pure FeO (x=1).
    V_MgO : float
        Predicted volume for pure MgO (x=0).
    """
    model, V_FeO, V_MgO = fit_vegards_law(x, V)
    if plot:
        plot_fit(x, V, model)
    return model, V_FeO, V_MgO
