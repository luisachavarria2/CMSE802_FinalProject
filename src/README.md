## Source

This folder includes all source code modules and scripts

1. Data_validator: Module for the validation of the data. This module ensures that the input data meets the required criteria for analysis.

2. Vegards_volume: Module for fitting experimental data to Vegard's Law, which describes the linear relationship between the unit cell volume of a solid solution and its composition.

3. linear_lsf_confidence: This module fits a linear model to experimental data using the least squares method. It calculates the coefficient of determination (R²) and plots the regression line 
alongside a 95% confidence interval band.

4. lsf_vegard: Module to compare two linear fitting approaches for modeling the relationship between Fe mole fraction and unit cell volume: vegard's law and least squares fit

5. calculate_deviation: This module is designed for the calculation of the deviation of the LSF from the Vegard's Law.

6. plot_deviation: This module provides a function to compare the predicted volumes from a  Least Squares Fit (LSF) against those estimated by Vegard's Law for a binary  solid solution between MgO and FeO.

7. generator: generate atoms for the volume_unitcell.py module

8. volume_unitcell: Module to generate 2D visualizations of atomic configurations in (Mg,Fe)O solid solutions. Atom positions and bond networks are plotted for different Fe mole fractions, with visual exaggeration to highlight structural differences.

9. fe_calculation: Estimate the Fe concentration (x) from the unit cell volume using the linear equation derived from a least-squares fit. 

 


