# NICS-2D

**Python scripts for generating, extracting, and plotting NICS-2D (Nucleus-Independent Chemical Shifts) grids.**

NICS is a powerful computational tool for assessing aromaticity and antiaromaticity in molecules. Visualizing NICS values as a 2-dimensional grid can be helpful in various applications, such as evaluating "hotspots" of (anti)aromaticity in extended π-conjugated compounds and visualizing changes in aromaticity in different charge or electronic states.

## Overview

NICS-2D is a collection of Python scripts designed to facilitate the generation, extraction, and visualization of NICS-2D grids. It is specifically designed to work with Gaussian 16.

## Key Features

- `NICS-2D_input.py`: Generate NICS-2D grids for your molecular systems. This is an interactive Python script that creates an input file (name.com) and let the used input the level of theory, charge and multiplicity, xyz coordinates, and the specifications of the grid (size and distance to the ring). The input file is then used to run the Gaussian 16 calculation.
- `NICS-2D_extractor.py`: Extract NICS data from the output file generated using Gaussian 16.
- `NICS-2D_plot.ipynb`: Jupyter notebook for visualizing the NICS-2D plots.

## Instructions: 

### `NICS-2D_input.py`

1. Find the XYZ coordinates of the molecule of interest and ensure it is centered in the XY plane.
2. Run the following command in your terminal:


    ```shell
    python NICS-2D_input.py
    ```
    
This command will open an interactive Python script. Follow the instructions provided by the script to input the following parameters:

For example, here is a command for generating NICS-2D grid input file for benzene in the ground state with a grid size of 6x6 Å² (ranging from -3 Å to +3 Å):

```shell
...............................................................................
.                                                                             .
.                Input file generator for NICS-2D calculations                .
.                         Aug. 31 2022 (Lucas Karas)                          .
.                                                                             .
...............................................................................

Name your NICS-2D input file (e.g., benzene.com): 
benzene.com
Enter the DFT method: B3LYP
Do you want to add dispersion [y/n]? n
Enther the basis set: def2TZVP
Enter molecule charge: 0
Enter molecule spin: 1

Input keywords successfully entered!

...............................................................................
Enter xyz geometry and then press ctrl+dd: 
C       0.00000      1.39700      0.00000
C       1.20980      0.69850      0.00000
C       1.20980     -0.69850      0.00000
C       0.00000     -1.39700      0.00000
C      -1.20980     -0.69850      0.00000
C      -1.20980      0.69850      0.00000
H       0.00000      2.48100      0.00000
H       2.14860      1.24050      0.00000
H       2.14860     -1.24050      0.00000
H       0.00000     -2.48100      0.00000
H      -2.14860     -1.24050      0.00000
H      -2.14860      1.24050      0.00000
^D
Input geometry successfully entered!

...............................................................................
Enter the grid range in x in Å (e.g., -1 1): -3 3
Enter the grid range in y in Å (e.g., -1 1): -3 3
Enter the spacing between the Bq atoms in Å (e.g., 0.25): 0.2
Enter the Bq atom distance to the ring plane in Å: 1

2D grid successfully generated!
...............................................................................

Writing connectivity.

Connectivity done!
...............................................................................

Input Saved. Normal Termination.
...............................................................................
```

3. Your input file is created and can now be submit to a Gaussian 16 calculation. Once the job is done, go to `NICS-2D_extractor.py` instructions. 


### `NICS-2D_extractor.py`

1. Ensure you have the output file in your working folder.
2. Run the following command in your terminal:

    ```shell
    python NICS-2D_extractor.py
    ```
   This command will open an interactive Python script that simplifies the extraction process. The script will guide you through the extraction of the desired NICS values. The available extraction options are as follows:
    1. **IMS**: Extract the absolute value of the isotropic magnetic shielding.
    2. **MSzz**: Extract the ZZ component of the absolute value of the decomposed magnetic shielding.
    3. **NICSiso**: Extract isotropic NICS values.
    4. **NICSzz**: Extract the ZZ component of the decomposed NICS values.

   Choose the option that best suits your analysis.

For example, here is a command for extracting NICSzz from the benzene output file:

```shell
...............................................................................
.                                                                             .
.                              NICS-2D extractor                              .
.                         Sept. 01 2022 (Lucas Karas)                         .
.                                                                             .
...............................................................................

Reading the Gaussian output file:

Enter the output name: 
benzene.out

Checking the output file...
NMR keyword found in the output. Proceed.
Bq atom found in the output. Proceed.

Bq coordinates successfully archived.

Magnetic shieldings successfully archived.

Gaussian output closed! :D

...............................................................................
Choose between (1) IMS; (2) MSzz; (3) NICSiso; or (4) NICSzz: 
4

Name your NICS-2D file (e.g., benzene): benzene

Preparing the NICSzz data.

Normal Termination!
```


