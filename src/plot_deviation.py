# plot_deviation.py

"""
This module provides a function to compare the predicted volumes from a 
Least Squares Fit (LSF) against those estimated by Vegard's Law for a binary 
solid solution between MgO and FeO.

Author: Luisa Chavarria, AI (ChatGPT)
Date: April 2025
"""

import matplotlib.pyplot as plt


def plot_deviation_vegard(x, V_lsf, V_MgO, V_FeO):
    """
    Plot the deviation of LSF from Vegard's Law across Fe fraction.
    
    Parameters:
    -----------
    x : np.ndarray
        Fe mole fraction.
    V_lsf : np.ndarray
        Molar volume predicted by the Least Squares Fit.
    V_MgO : float
        Molar volume of pure MgO.
    V_FeO : float
        Molar volume of pure FeO.

    Returns
    -------
    None
        Displays a matplotlib plot of the deviation curve.
    """
    
    # Calculate Vegard's Law values
    V_vegard = (V_FeO - V_MgO) * x + V_MgO
    
    # Calculate deviation
    deviation = V_lsf - V_vegard

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.axhline(0, color='gray', linestyle='--', linewidth=1.5,
                label="Vegard's Law (baseline)")

    plt.scatter(x, deviation, color='purple', s=60,
                label='Deviation from Vegard\'s Law')
    plt.plot(x, deviation, color='purple', alpha=0.6)

    plt.xlabel('Fe Fraction (x)', fontsize=12)
    plt.ylabel('Deviation from Vegard\'s Law (Å³)', fontsize=12)
    plt.title('Deviation of LSF from Vegard\'s Law', fontsize=14)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
