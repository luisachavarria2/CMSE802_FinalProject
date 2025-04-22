# vegards_volume.py

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


def vegards_volume(V_MgO, V_FeO, x_values=None):
    """
    Apply Vegard's Law to interpolate molar volume for the (Mg,Fe)O solid solution.

    Parameters:
        V_MgO (float): Molar volume of pure MgO.
        V_FeO (float): Molar volume of pure FeO.
        x_values (np.ndarray, optional): Array of Fe mole fractions (0 to 1). 
                                         If None, uses 100 points from 0 to 1.

    Returns:
        x_Fe (np.ndarray): Fe mole fractions.
        V_interp (np.ndarray): Interpolated volume values.
    """
    if x_values is None:
        x_values = np.linspace(0, 1, 100)
    else:
        x_values = np.asarray(x_values)  # ensure it's a NumPy array

        # Raise error
        if np.any(x_values < 0) or np.any(x_values > 1):
            raise ValueError("All fraction values in 'x_values' must be between 0 and 1.")

    V_interp = (1 - x_values) * V_MgO + x_values * V_FeO
    return x_values, V_interp


def plot_vegards_volume(V_MgO, V_FeO, x_values=None):
    """
    Plot Vegard's Law interpolation for atomic volume in the (Mg,Fe)O system.

    Parameters:
        V_MgO (float): Volume of pure MgO.
        V_FeO (float): Volume of pure FeO.
        x_values (np.ndarray, optional): Fe mole fractions.
    """
    x_Fe, V_interp = vegards_volume(V_MgO, V_FeO, x_values)

    plt.figure(figsize=(8, 5))
    plt.plot(x_Fe, V_interp, label="Vegard's Law", color='darkgreen')
    plt.scatter([0, 1], [V_MgO, V_FeO], color='red', label='Endmembers')
    plt.xlabel('FeO Mole Fraction (x)')
    plt.ylabel('Volume (Å³/atom)')
    plt.title("Vegard's Law for Volume in (Mg,Fe)O")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
