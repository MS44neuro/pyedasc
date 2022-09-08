"""This file is meant to help the user to get used to the ca module.
In this script, a single .abf file containing 29 sweeps is analyzed 
for Sodium currents. `imemb_region` region is set at the beginning 
of the voltage steps to capture the inward currents. Sets 1, 2 and 3 
use different ca module parameters to perform different portions 
of the analysis."""
# Importing modules for file synchronization
import os
import sys
import glob

# Creating paths to the module and abf files
data_path = "/../data/abfs/drg_neurons/getting_started/ca/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the ca module
sys.path.insert(0, pathToModule)
from pyedasc import ca

# Looping through all .abf files sorted in the data path folder
for abf_file in sorted(glob.glob(pathToData + "/*.abf")):
    
    # Creating multiple sets of parameters for the same abf file
    
    # Set1: Minimum input for generating an IV plot
    set1 = ca.Parameters(abf_file=abf_file, 
                         current_channel_number=0, 
                         voltage_channel_number=1, 
                         imemb_region=[1400, 1500], 
                         vcom_region=[1400, 1500], 
                         peak_polarity='negative')
    
    # Plotting IV curve
    set1.plotting(parameter='current', action='plot')
    
    # Printing current values
    print("Set1: Current values")
    print(set1.current_detection())
    
    # Printing the voltage steps from waveform and measured
    print("Set1: Voltage steps measured")
    print(set1.voltage_steps_measured())
    print("Set1: Voltage steps waveform")
    print(set1.voltage_steps_waveform())


    # Set2: Voltage step correction & plotting the chord conductance
            # Based on IV plot, an fitting region for reversal potential 
            # can be chosen or a fixed reversal potential value can be provided
    set2 = ca.Parameters(abf_file=abf_file, 
                         current_channel_number=0, 
                         voltage_channel_number=1, 
                         imemb_region=[1400, 1455], 
                         vcom_region=[1405, 1455], 
                         peak_polarity='negative',
                         liquid_junction_potential=2,
                         erev_fit_region=[-5,-3])
    
    # Plotting chord conductance
    set2.plotting(parameter='chord-conductance', action='plot')
    
    # Printing chord conductance
    print("Set2: Chord conductance")
    print(set2.chord_conductance())
    
    # Printing driving forces
    print("Set2: Driving forces")
    print(set2.driving_force())

    
    # Set3: Calculate current and conductance densities 
    set3 = ca.Parameters(abf_file=abf_file, 
                         current_channel_number=0, 
                         voltage_channel_number=1, 
                         imemb_region=[1400, 1500], 
                         vcom_region=[1400, 1500], 
                         peak_polarity='negative', 
                         erev_fit_region=[-5,-3], 
                         membrane_capacitance=13.34)
    
    # Plotting current density given in units of pA / um2
    set3.plotting(parameter='current-density-area', action='plot')
    
    # Plotting current density given in units of pA / pF
    set3.plotting(parameter='current-density-cm', action='plot')
    
    # Plotting conductance density
    set3.plotting(parameter='conductance-density', action='plot')
    
    set3.fitted_parameter(set3.voltage_steps_measured(),
                          set3.chord_conductance())
