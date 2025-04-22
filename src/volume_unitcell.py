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
from matplotlib.patches import Patch
from generator import generate_atoms  # Must return a list of (x, y, species) tuples


# Configuration
atomic_radii = {'Mg': 1.6, 'Fe': 1.26, 'O': 0.74}  # Angstroms
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


def create_plots_cell(fe_fractions, c1, c2, base_a=4.21, delta_a=0.1,
                      visual_exaggeration=10.0, grid_size=2):
    """
    Create 2D plots of (Mg,Fe)O unit cells with varying Fe content.

    Parameters
    ----------
    fe_fractions : list of float
        List of Fe mole fractions (values between 0 and 1) to visualize.

    c1 : float
        Linear coefficient for volume as a function of Fe fraction.

    c2 : float
        Constant term in the volume equation.

    base_a : float, optional
        Lattice parameter for pure MgO (in angstroms). Default is 4.21.

    delta_a : float, optional
        Change in lattice parameter per unit Fe mole fraction. Default is 0.1.

    visual_exaggeration : float, optional
        Factor to exaggerate lattice distortions for visualization purposes. Default is 10.0.

    grid_size : int, optional
        Number of unit cells along x and y directions. Default is 2.
    """
    fig, axes = plt.subplots(1, len(fe_fractions), figsize=(18, 5))
    axes = axes.flatten()

    max_scaled_a = base_a + delta_a * max(fe_fractions) * visual_exaggeration
    plot_limit = max_scaled_a * grid_size + 1

    for i, fe_fraction in enumerate(fe_fractions):

        # Compute actual and exaggerated lattice parameters
        actual_a = base_a + delta_a * fe_fraction
        scaled_a = base_a + delta_a * fe_fraction * visual_exaggeration

        # Generate atomic configuration
        atoms = generate_atoms(scaled_a, fe_fraction, grid_size)
        positions = np.array([[x, y] for x, y, _ in atoms])
        color_list = [colors[s] for _, _, s in atoms]
        size_list = [radius_to_size(atomic_radii[s]) for _, _, s in atoms]

        # Define bond drawing cutoff
        bond_cutoff = scaled_a * 1.5

        ax = axes[i]
        ax.scatter(
            positions[:, 0], positions[:, 1],
            c=color_list, s=size_list,
            edgecolor='black', linewidth=0.7
        )
        plot_bonds(ax, atoms, bond_cutoff)

        # Draw unit cell outline
        cell_size = scaled_a * grid_size
        ax.plot(
            [0, cell_size, cell_size, 0, 0],
            [0, 0, cell_size, cell_size, 0],
            'gray', linestyle='--', linewidth=1.5
        )

        # Calculate and display cell volume
        volume = c1 * fe_fraction + c2
        ax.set_title(f"Fe = {fe_fraction*100:.0f}%\nVolume = {volume:.2f} Å³")
        ax.set_xlim(-1, plot_limit)
        ax.set_ylim(-1, plot_limit)
        ax.set_aspect('equal')
        ax.axis('off')

    # Legend for the atoms
    legend_handles = [Patch(facecolor=colors[el], edgecolor='black', label=el)
                      for el in colors]
    axes[0].legend(handles=legend_handles, loc='upper right', frameon=True)

    plt.tight_layout()
    plt.show()
