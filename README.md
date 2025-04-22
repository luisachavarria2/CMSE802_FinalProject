# CMSE 802 - Final Project

# Modeling of volume change with iron in ferropericlase (Mg,Fe)O 

Solid solutions can have different styles of mixing. In the ideal mixing, the volume of the solution changes as the concentration of one of the elements fluctuates. As part of my PhD, I’m studying the solid solution of ferropericlase (Mg,Fe)O. This mineral is the second most abundant mineral in the Earth’s lower mantle and has a simple cubic crystallographic structure. My project looks to study the incorporation of sodium inside the structure as a substitution for iron and I’ve been using three powder samples of (Mg,Fe)O with different concentrations of iron. The samples were provided from a collaborator in Northwestern University. They also supplied an XRD spectra that was used to calculate the atomic volume of the sample.

Initially, the collaborators provided an estimated composition, however, as part of the characterization, the samples require a verification to double-check that the concentration of iron is correct for the future analysis. Then, this project looks to use techniques of modeling to characterize the concentration of iron in the samples using as starting point the atomic volume calculated from XRD data. To do this, we are going to compare the Vegard’s law volume prediction with the linear regression using least squares fit. 

The main question of this project is: can a least squares fit model have a better prediction than the Vegard’s law? This comparison will allow to determine which approach is better, understand how the unit cell changes as iron is incorporated, and then calculate the concentration of iron of the samples received from Northwestern University based on the XRD volume. Vegard’s law is going to be used as a null hypothesis to verify how ideal is the mixing of the samples we received. 

Additionally, by studying the substitution of magnesium by iron, it is a first approximation to understand how substitution affects the dimensions of the unit cell of ferropericlase. This approach could be useful in the future for understanding how atoms like Na could be incorporated in the structure. In this case, iron is smaller than sodium, but it can be used as an example of how large atoms change the dimensions of the unit cell. Linear algebra is going to be implemented to calculate an equation that allows the evaluation of the relation between volume and iron concentration. 

Objectives: 

1.	Compare the least squares fit (LSF) vs Vegard’s law. 
2.	Characterize the change in the unit cell as the iron concentration increase
3.	Calculate the concentration of the ferropericlase samples from Northwestern University. 

This repository has the following structure:

* /scr/ - All source code modules and scripts
* /notebooks/ - Jupyter notebooks for analysis and visualization
* /data/ - Data files or constants 
* /tests/ - Unit tests for implementation
* /results/ - Generated outputs (figures, model checkpoints, etc.)

* .gitignore 
* README.md

Installation:
* The data is contained in the file Fe_volume_fp.csv
* The modules required for installation are in the file requirements.txt as well as the dependencies and versions
* Download all the modules contained in the folder src and run them using the notebook FinalProject_analysis_visualization.ipynb
