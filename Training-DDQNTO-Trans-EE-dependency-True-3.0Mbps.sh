#!/bin/bash

# Activate the conda environment
source /home/tzz789/anaconda3/etc/profile.d/conda.sh
conda activate RLTaskOffloading

# Run the Python script
python train.py --algo DDQNTO --scenario Trans --goal EE --dependency True
