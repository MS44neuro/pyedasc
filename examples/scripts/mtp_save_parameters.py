"""Saving average values of Membrane Test parameters 
for all .sta files in a folder. The values are stored 
in an Excel file that is generated in the data folder."""
# Importing modules for file synchronization
import os
import sys
import glob

# Importing modules for excel file writing
import string
from openpyxl import Workbook
from openpyxl.styles import Font

# Creating paths to the module and .sta files
pathToHere = os.path.abspath(os.path.dirname(__file__))
pathToData = os.path.abspath(pathToHere + "/../data/sta/")
pathToModule = os.path.abspath(pathToHere + "/../../")

# Setting the path to the mtp module
sys.path.insert(0, pathToModule)
from pyedasc import mtp

# Set workbook
wb = Workbook()
ws = wb.active

# Configure the worksheet
rows = list(range(2, 6))
columns = string.ascii_uppercase
ws.row_dimensions[1].height = 25
for row in rows: ws.row_dimensions[row].height = 23
ws.freeze_panes = 'A2'
for col in columns: ws.column_dimensions[col].width = 25

column_list = ['File name', 
               'Membrane capacitance (pF)', 
               'Access resistance (M\u03A9)', 
               'Membrane resistance (M\u03A9)', 
               'Time constant \u03C4 (\u03BCs)', 
               'Holding current (pA)', 
               'Diameter (\u03BCm)']
            
row_list = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
for l, c in zip(row_list, column_list): ws[l] = c

# Looping trough through all .sta files in data source folder
for sta_file in sorted(glob.glob(pathToData + '/*.sta')):

    # Setting up Extractor with a minimum reading range
    extract = mtp.Extractor(reading_range=[20,50])

    ws.append([os.path.basename(os.path.normpath(sta_file)), 
               extract.cm(sta_file), 
               extract.ra(sta_file), 
               extract.rm(sta_file),
               extract.tau(sta_file),
               extract.hold(sta_file), 
               extract.diameter(sta_file)])
    
    wb.save(filename=pathToData + '/mtp_raw_data.xlsx')