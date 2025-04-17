"""
Module to generate 2D visualizations of atomic configurations
in (Mg,Fe)O solid solutions. Atom positions and bond networks
are plotted for different Fe mole fractions, with visual exaggeration
to highlight structural differences.

Author: Luisa Chavarria, AI (ChatGPT)
Date: April 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from generator import generate_atoms  # Must return a list of (x, y, species) tuples

# Configuration
atomic_radii = {'Mg': 1.60, 'Fe': 1.40, 'O': 0.60}  # Angstroms
colors = {'Mg': 'green', 'Fe': 'orange', 'O': 'red'}  # Color mapping for the atoms
radius_to_size = lambda r: (r ** 2) * 200  # Convert atomic radius to marker size


def plot_bonds(ax, atoms, cutoff):
    """
    Plot bonds between atoms based on a distance cutoff.

    Parameters:
    ----------
    ax : matplotlib.axes.Axes
        The axes on which to draw bonds.
    atoms : list of tuples
        Each atom is represented as (x, y, species).
    cutoff : float
        Maximum distance between atoms to draw a bond.
    """
    for i, (x1, y1, _) in enumerate(atoms):
        for j, (x2, y2, _) in enumerate(atoms):
            if i < j:
                dist = np.hypot(x2 - x1, y2 - y1)
                if dist < cutoff:
                    ax.plot([x1, x2], [y1, y2], color='black', lw=1)


def create_plots(fe_fractions, base_a=4.21, delta_a=0.1,
                 visual_exaggeration=10.0, grid_size=2):
    """
    Generate and display structural plots for a range of Fe concentrations.

    Parameters:
    ----------
    fe_fractions : list of float
        List of Fe mole fractions (values between 0 and 1).
    base_a : float, optional
        Base lattice parameter for pure MgO (default: 4.21 Å).
    delta_a : float, optional
        Lattice parameter increase per unit Fe fraction (default: 0.1 Å).
    visual_exaggeration : float, optional
        Factor to exaggerate visual differences in lattice parameter (default: 10.0).
    grid_size : int, optional
        Number of unit cells in x and y directions (default: 2).
    """
    fig, axes = plt.subplots(1, len(fe_fractions), figsize=(18, 5))
    axes = axes.flatten()

    # Determine plot limits based on largest scaled cell
    max_scaled_a = base_a + delta_a * max(fe_fractions) * visual_exaggeration
    plot_limit = max_scaled_a * grid_size + 1

    for i, fe_fraction in enumerate(fe_fractions):
        # Actual and exaggerated lattice parameters
        actual_a = base_a + delta_a * fe_fraction
        scaled_a = base_a + delta_a * fe_fraction * visual_exaggeration

        # Generate atoms for given composition
        atoms = generate_atoms(scaled_a, fe_fraction, grid_size)
        positions = np.array([[x, y] for x, y, _ in atoms])
        color_list = [colors[s] for _, _, s in atoms]
        size_list = [radius_to_size(atomic_radii[s]) for _, _, s in atoms]

        bond_cutoff = scaled_a * 1.5  # Reasonable threshold for bonding

        ax = axes[i]
        ax.scatter(
            positions[:, 0], positions[:, 1],
            c=color_list, s=size_list,
            edgecolor='black', linewidth=0.7
        )
        plot_bonds(ax, atoms, bond_cutoff)

        # Draw unit cell boundary
        cell_size = scaled_a * grid_size
        ax.plot(
            [0, cell_size, cell_size, 0, 0],
            [0, 0, cell_size, cell_size, 0],
            'gray', linestyle='--', linewidth=1.5
        )

        # Formatting
        volume = actual_a ** 3
        ax.set_title(f"Fe = {fe_fraction*100:.0f}%\nVolume = {volume:.2f} Å³")
        ax.set_xlim(-1, plot_limit)
        ax.set_ylim(-1, plot_limit)
        ax.set_aspect('equal')
        ax.axis('off')

    plt.tight_layout()
    plt.show()
