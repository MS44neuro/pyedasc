"""In this file, the analysis of 3 .abf files with multiple APs each, 
10 kHz sample rate is performed. All files come from the same waveform 
protocol and have an equal number of sweeps. In all files, the 3rd AP 
in trace is analyzed."""
# Importing modules for file synchronization
import os
import sys
import glob

# Creating paths to the module and .abf files
data_path = "/../data/abfs/drg_neurons/action_potentials/trains/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the ap module
sys.path.insert(0, pathToModule)
from pyedasc import ap

# Looping through all .abf files sorted in the data path folder
for file in sorted(glob.glob(pathToData + "/*.abf")):

    par = ap.Parameters(abf_file=file, 
                        current_channel_number=0, 
                        voltage_channel_number=1, 
                        sweep_number=4, 
                        absolute_rp_interval=[50, 400], 
                        ap_number=2) 
    plot = ap.Plotting(abf_file=file, 
                       current_channel_number=0, 
                       voltage_channel_number=1, 
                       sweep_number=4, 
                       absolute_rp_interval=[50, 400], 
                       ap_number=2) 
    
    # Some plotting options
    plot.ap_plot(action='plot')
    plot.thresholds(action='plot')
    
    plot.raw_recording(action='plot')
    plot.graph_3D(action='plot', rotation=False, text_box=True)

