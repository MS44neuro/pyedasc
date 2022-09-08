""" """
# Importing modules for file synchronization
import os
import sys
import glob

# Creating paths to the module and abf files
data_path = "/../data/abfs/drg_neurons/getting_started/rfi/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the rfi module
sys.path.insert(0, pathToModule)
from pyedasc import rfi

# Looping through all .abf files sorted in the data path folder
for abf_file in sorted(glob.glob(pathToData + "/*.abf")):
    
    test = rfi.RFI(abf_file=abf_file, 
                   current_channel_number=0,
                   reference_int=[400, 800], 
                   recovery_int=[20500, 22500], 
                   baseline_interval=[16000, 19000],
                   t0_recovery=20511) 
    
    # Printing the time values from t0_recovery to each peak
    print(test.time_values())
    
    # Printing the time values from t0_recovery to each peak
    print(f"Decay time constant: {round(test.tau_value(), 2)} ms.")
    
    # Plotting the recovery peaks normalized at reference peak for each sweep 
    # against time values from t0_recovery to each recovery peak
    test.plotting()
    
    # Plotting the raw recording
    test.raw_plotting()
    
