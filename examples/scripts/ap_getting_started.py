"""This file is meant to help the user to get used to the ap module.
In this script, a single abf file containing a single AP is analyzed. 
Sets 1, 2 and 3 differ by the parameters of the ap module used."""

# Importing modules for file synchronization
import os
import sys
import glob

# Creating paths to the module and abf files
data_path = "/../data/abfs/drg_neurons/getting_started/ap/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the ap module
sys.path.insert(0, pathToModule)
from pyedasc import ap

# Looping through all .abf files sorted in the data path folder
for abf_file in sorted(glob.glob(pathToData + "/*.abf")):
    
    # Creating multiple sets of parameters for the same abf file
    
    ### Set 1 ###
    # Only the functional attributes passed
    parameters_set_1 = ap.Parameters(abf_file=abf_file, 
                                     current_channel_number=0,
                                     voltage_channel_number=1)
    plotting_set_1 = ap.Plotting(abf_file=abf_file, 
                                 current_channel_number=0, 
                                 voltage_channel_number=1)    
    
    ### Set 2 ###
    # Absolute RP interval and sweep number added as attributes
    parameters_set_2 = ap.Parameters(abf_file=abf_file, 
                                     current_channel_number=0,
                                     voltage_channel_number=1,
                                     absolute_rp_interval=[10, 500],
                                     sweep_number=4)
    plotting_set_2 = ap.Plotting(abf_file=abf_file, 
                                 current_channel_number=0, 
                                 voltage_channel_number=1,
                                 absolute_rp_interval=[10, 500],
                                 sweep_number=4)
    
    ### Set 3 ###
    # Fixed points for RP1, RP2 and RP3 added as attributes
    parameters_set_3 = ap.Parameters(abf_file=abf_file, 
                                     current_channel_number=0,
                                     voltage_channel_number=1,
                                     absolute_rp_interval=[10, 500],
                                     sweep_number=4,
                                     rp_1_fixedP =562,
                                     rp_2_fixedP=620,
                                     rp_3_fixedP=3101)
    plotting_set_3 = ap.Plotting(abf_file=abf_file, 
                                 current_channel_number=0, 
                                 voltage_channel_number=1,
                                 absolute_rp_interval=[10, 500],
                                 sweep_number=4,
                                 rp_1_det=[560,563],
                                 rp_2_fixedP=620,
                                 rp_3_fixedP=3101)
    
    # Plotting the abf file voltage signal with ap_plot()
    plotting_set_1.ap_plot(action='plot')
    plotting_set_2.ap_plot(action='plot')
    plotting_set_3.ap_plot(action='plot')
 
    
    # Plotting the thresholds
    plotting_set_1.thresholds(action='plot')
    plotting_set_2.thresholds(action='plot')
    plotting_set_3.thresholds(action='plot')
    
    # Printing and comparing some of the important AP parameters 
    print("Resting potential")
    print(f"SET 1: {parameters_set_1.resting_potential()} mV.")
    print(f"SET 2: {parameters_set_2.resting_potential()} mV.")
    print(f"SET 3: {parameters_set_3.resting_potential()} mV.")
    
    print("RP1, RP2, RP3")
    print(f"SET 1: {parameters_set_1.rp_1()}, {parameters_set_1.rp_2()}, "
          + f"{parameters_set_1.rp_3()}.")
    print(f"SET 2: {parameters_set_2.rp_1()}, {parameters_set_2.rp_2()}, " 
          + f"{parameters_set_2.rp_3()}.")
    print(f"SET 3: {parameters_set_3.rp_1()}, {parameters_set_3.rp_2()}, " 
          + f"{parameters_set_3.rp_3()}.")
    
    print("Duration at the base")
    print(f"SET 1: {parameters_set_1.duration_at(level='base')[0]} ms.")
    print(f"SET 2: {parameters_set_2.duration_at(level='base')[0]} ms.")
    print(f"SET 3: {parameters_set_3.duration_at(level='base')[0]} ms.")
    
    print("Threshold method VII")
    print(f"SET 1: {parameters_set_1.threshold(method='VII')[0]} mV.")
    print(f"SET 2: {parameters_set_2.threshold(method='VII')[0]} mV.")
    print(f"SET 3: {parameters_set_3.threshold(method='VII')[0]} mV.")

