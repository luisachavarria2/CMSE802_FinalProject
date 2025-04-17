# cmse802_project_hw3

# Modeling of volume change with iron in ferropericlase (Mg,Fe)O 

Description: Ferropericlase (Mg,Fe)O is the second most abundant mineral in the Earth's lower mantle. 
Sodium (Na1+) can incorporate inside the structure through different mechanisms at high pressures conditions (23-136 GPa) (Figure 1). 
This project looks to understand how substitution affects the dimensions of the unit cell of ferropericlase. 
Then, it is going to focused on how the volume changes when the concentration of iron changes in the mineral. 
Linear algebra is going to be implemented to calculate an equation that allows the evaluation of the relation between volume and iron concentration. 

Objectives:

1. Model the substitution of iron in (Mg,Fe)O
2. Use linear algebra to estimate the concentration of iron according to the volume
3. Compare the least squares fit model vs the Vegard's law

This repository has the following structure:

* /scr/ - All source code modules and scripts
* /notebooks/ - Jupyter notebooks for analysis and visualization
* /data/ - Data files or constants 
* /tests/ - Unit tests for implementation
* /docs/ - Documentation files
* /results/ - Generated outputs (figures, model checkpoints, etc.)

* .gitignore 
* README.md

Installation:
* The data is contained in the file Fe_volume_fp.csv
* The modules required for installation are in the file requirements.txt as well as the dependencies and versions
