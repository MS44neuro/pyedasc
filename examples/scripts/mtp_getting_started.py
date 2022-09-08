"""This file is meant to help the user to get used to the mtp module. 
This module extracts and averages the column values from .sta files
representing the Membrane Parameters saved in the experiment. 
In this script, a single .sta file containing around 500 rows (values)
is analyzed. """
# Importing modules for file synchronization
import os
import sys
import glob

# Creating paths to the module and abf files
data_path = "/../data/abfs/drg_neurons/getting_started/mtp/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the mtp module
sys.path.insert(0, pathToModule)
from pyedasc import mtp

# Looping through all .sta files sorted in the data path folder
for sta_file in sorted(glob.glob(pathToData + '/*.sta')):

    # Setting up the Extractor class with optional parameter reading_range
    extract = mtp.Extractor(reading_range=[30, 100])
    print(f"Data reading range from file columns: from " 
          + f"{extract.reading_range[0]} to {extract.reading_range[1]}.")

    # Printing the membrane parameters as means of column values
    print(f"Membrane capacitance: {extract.cm(sta_file)} pF.")
    print(f"Membrane resistance: {extract.rm(sta_file)} MOhms.")
    print(f"Access resistance: {extract.ra(sta_file)} MOhms.")
    print(f"Membrane time constant: {extract.tau(sta_file)} us.")
    print(f"Steady state current (holding): {extract.hold(sta_file)} pA.")
    print(f"Cell diameter: {extract.diameter(sta_file)} um.")
    