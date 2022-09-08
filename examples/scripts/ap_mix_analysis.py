"""Code here tests the automatization potential of ap module 
by executing only with the mandatory parameters (path to .abf file 
and channels for voltage and current). The /mixed folder contains 40 .abf 
files with 1 or more sweeps, 1 or more APs, with 1 or more 
stimulation epochs in the waveform and with sample rates from 1 to 100 kHz.
"""
# Importing modules for file synchronization
import os
import sys
import glob

# Creating paths to the module and .abf files
data_path = "/../data/abfs/drg_neurons/action_potentials/mixed/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the ap module
sys.path.insert(0, pathToModule)
from pyedasc import ap

# Looping through all .abf files sorted in the data path folder
for file in sorted(glob.glob(pathToData + "/*.abf")):

    # Passing only the essential parameters
    par = ap.Parameters(abf_file=file, 
                        current_channel_number=0, 
                        voltage_channel_number=1)
    plot = ap.Plotting(abf_file=file, 
                       current_channel_number=0, 
                       voltage_channel_number=1) 

    # Plotting the abf file voltage signal with ap_plot()
    plot.ap_plot(action='plot')
    
    # Plotting the thresholds
    plot.thresholds(action='plot')
    

 
    
 
    
