# Plaut_Model

## Dependencies
See requirements.txt

## General Information
There are several directories **required** for proper functionality:
 1. `checkpoints` This directory stores any created checkpoints for future use.
 2. `code` This directory contains the code and also the configuration file.
 3. `dataset` This directory contains the Plaut, anchor, and probe datasets in `.csv` format.
 4. `results` This directory stores the simulation results folders, which contain the plots and `.csv.gz` files created with each simulation.

## How to Use
1. The configuration file for simulations is located in `code/config.cfg`. This file contains all user-settable parameters, with descriptions of the usage of each parameter. This file must **not** be renamed nor moved in order for the simulation to run successfully. With each simulation, a copy of the `config.cfg` file will be placed in the simulation results folder.
2. After all desired parameter settings are made in the configuration file, the code in the Jupyter Notebook file `plaut_model.ipynb` can be executed. Information will be printed and plotted on intervals specified in the configuration file.
3. A folder containing simulation results will be created inside the `results` directory. This simulation folder will be named with the format `<label>-S<seed>D<dilution>O<order>-<date>`. Inside the simulation folder will be loss and accuracy plots, a copy of the configuration file, as well as `.csv.gz` file containing accuracy information for each word at specified intervals during the simulation.
