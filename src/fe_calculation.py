"""
fe_calculation.py

Author: Luisa Chavarria, AI (ChatGPT)
Date: April 2025
"""


def estimate_fe(volume):
    """
    Estimate the Fe concentration (x) from the unit cell volume
    using the linear equation derived from a least-squares fit:
        V = 4.816 * x + 75.074

    Parameters:
    ----------
    volume : float
        The unit cell volume in Å³ for which the Fe concentration (x)
        is to be estimated.

    Returns:
    -------
    float
        The estimated Fe mole fraction (x), which ranges from 0.0
        (pure MgO) to 1.0 (pure FeO).

    Raises:
    ------
    ValueError: If the volume is less than or equal to 0.
    Warning: If the estimated Fe fraction falls outside the
    valid range (0.0 to 1.0).

    Notes:
    ------
    This function assumes that the input volume corresponds to the
    linear equation derived from experimental data. If the volume is outside the
    expected range, the result may not be accurate.

    Example:
    --------
    For a unit cell volume of 160.1 Å³, the estimated Fe concentration will be:
    `estimate_fe(160.1)` will output approximately 0.20.
    """
    # Check for non-physical volumes
    if volume <= 0:
        raise ValueError("Volume must be greater than zero.")

    # Check for large volumes
    if volume > 81:
        print("Warning: Volume is unusually large. Please verify the input.")

    # Calculate the Fe mole fraction from the volume using
    # the linear fit formula
    x = (volume - 75.074) / 4.816

    # Ensure the mole fraction is within the valid range [0.0, 1.0]
    if x < 0 or x > 1:
        print(
            f"Warning: The calculated Fe fraction {x:.4f} is out of bounds. "
            "It may not be physically meaningful."
        )

    # Convert the mole fraction to a percentage for easier interpretation
    percent = x * 100

    # Print the result
    print(
        f"For the volume = {volume:.2f} Å³, the estimated Fe concentration is "
        f"{percent:.2f}%"
    )

    return x
