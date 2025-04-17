"""
generator.py

Author: Luisa Chavarria, AI (ChatGPT)
Date: April 2025
"""

import numpy as np


def generate_atoms(scaled_a, fe_fraction, grid_size):
    """
    Generates a 2D grid of atoms for a given Fe fraction, scaled by 'scaled_a'.
    The atoms are placed on a square grid, and the Fe fraction determines how
    many Fe atoms are randomly placed in the grid. The remaining atoms are
    either Mg or O.

    Parameters:
    ----------
    scaled_a : float
        Scaling factor for atomic distances (unit cell size in Å).

    fe_fraction : float
        Fraction of Fe atoms in the grid. Must be between 0 and 1.

    grid_size : int
        Number of unit cells along one side. Total atoms = grid_size².

    Returns:
    -------
    list of tuples
        Each tuple contains (x, y, species), where species is 'Fe', 'Mg', or 'O'.
    """
    atoms = []

    for i in range(grid_size):
        for j in range(grid_size):
            if (i + j) % 2 == 0:
                symbol = 'Fe' if np.random.rand() < fe_fraction else 'Mg'
            else:
                symbol = 'O'

            x, y = i * scaled_a, j * scaled_a
            atoms.append((x, y, symbol))

    return atoms
