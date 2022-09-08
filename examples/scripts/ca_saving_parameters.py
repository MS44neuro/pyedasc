""" """
# Importing modules for file synchronization
import os
import sys
import glob

# Importing modules for excel file writing
import string
from openpyxl import Workbook

# Creating paths to the module and abf files
data_path = "/../data/abfs/drg_neurons/current_analysis/inward_activation/"
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + data_path)
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the ca and mtp modules
sys.path.insert(0, pathToModule)
from pyedasc import ca
from pyedasc import mtp

# Set workbook
wb = Workbook()
ws = wb.active

# Create empty lists for data
parameter = []
voltage_steps = []

for abf_file, sta_file in zip(sorted(glob.glob(pathToData + "/*.abf")), 
                              sorted(glob.glob(pathToData + "/*.sta"))):
    
    # Extract membrane test parameters from the .sta file
    extract = mtp.Extractor(reading_range=[20,30])
    # Set 
    set1 = ca.Parameters(abf_file=abf_file, 
                         current_channel_number=0, 
                         voltage_channel_number=1, 
                         imemb_region=[1400, 1500], 
                         vcom_region=[1400, 1500], 
                         peak_polarity='negative', 
                         erev_fit_region=[-5, -2], 
                         liquid_junction_potential=2,
                         membrane_capacitance=extract.cm(file=sta_file))
    
    voltage_steps.append(set1.voltage_steps_waveform())
    parameter.append([set1.abf_file_name, set1.conductance_density()])
    
    # Plotting the conductance density to verify the analysis
    # set1.plotting(parameter='conductance-density', action='plot')
    

    
vs = voltage_steps[0]
vs.insert(0, "Files / Voltage steps (mV)") 

# Configure the Excel file  
columns = string.ascii_uppercase
all_columns = [c for c in columns] + [('A' + c) for c in columns]
columns_for_vs = all_columns[0:len(vs)+1]

for index, column in zip(columns_for_vs, vs):
        ws[index + '1'] = column


    
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 30
ws.freeze_panes = 'A2'

row_appender = []
for n in range(len(parameter)):
    parameter[n][1].insert(0, parameter[n][0])
    row_appender.append(parameter[n][1])

for n in row_appender:  
    ws.append(n)
        
wb.save(pathToData + '/ca_saved_parameter.xlsx')
