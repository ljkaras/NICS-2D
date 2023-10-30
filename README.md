# NICS-2D

**Python scripts for generating, extracting, and plotting NICS-2D (Nucleus-Independent Chemical Shifts) grids.**

NICS is a powerful computational tool for assessing aromaticity and antiaromaticity in molecules. Visualizing NICS values as a 2-dimensional grid can be helpful in various applications, such as evaluating "hotspots" of (anti)aromaticity in extended π-conjugated compounds and visualizing changes in aromaticity in different charge or electronic states.

## Overview

NICS-2D is a collection of Python scripts designed to facilitate the generation, extraction, and visualization of NICS-2D grids. It is specifically designed to work with Gaussian 16.

## Key Features

- `NICS-2D_input.py`: Generate NICS-2D grids for your molecular systems. This is an interactive Python script that creates an input file (name.com) and let the used input the level of theory, charge and multiplicity, xyz coordinates, and the specifications of the grid (size and distance to the ring). The input file is then used to run the Gaussian 16 calculation.
  Run in the command line as:
    ```shell
    python NICS-2D_input.py
    ```
  Follow instructions to create the input file.
  
- `NICS-2D_extractor.py`: Extract NICS data from the output file generated using Gaussian 16.
- `NICS-2D_plot.ipynb`: Jupyter notebook for visualizing the NICS-2D plots.
