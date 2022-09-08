"""In this file, the 6 parameters extracted from all .sta files 
in a folder are saved in separate lists and a statistical analysis 
is performed. This includes the mean, the values of the standard 
error of the mean, the standard deviation and the sample number. 
The values are stored in an Excel file that is generated in the 
data folder."""
# Importing modules for file synchronization
import os
import sys
import glob

# Importing modules for data statistics
import numpy as np
from scipy.stats import sem
import statistics as sts

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
# Headers
column_list = ['Parameter', 'Mean value', 'SEM', 'SD', 'N']  
row_list = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
for l, c in zip(row_list, column_list): ws[l] = c

# Create empty lists to append all parameters
cm = []
ra = [] 
rm = []
tau = []
hold = []
diameter = []

# Looping trough through all .sta files in data source folder
for sta_file in sorted(glob.glob(pathToData + '/*.sta')):
       
    # Setting up Extractor with a minimum reading range
    extract = mtp.Extractor(reading_range=[20, 50])
    
    # Appending each parameter from all the .sta files separately
    cm.append(extract.cm(sta_file))
    ra.append(extract.ra(sta_file))
    rm.append(extract.rm(sta_file))
    tau.append(extract.tau(sta_file))
    hold.append(extract.hold(sta_file))
    diameter.append(extract.diameter(sta_file))
    
# Perform minimal analysis on each parameter list
cm_ = ['Membrane capacitance (pF)', 
       round(np.mean(cm), 2),
       round(sem(cm), 2),
       round(sts.stdev(cm), 2),
       len(cm)] 

ra_ = ['Access resistance (M\u03A9)', 
       round(np.mean(ra), 2),
       round(sem(ra), 2),
       round(sts.stdev(ra), 2),
       len(ra)] 

rm_ = ['Membrane resistance (M\u03A9)', 
       round(np.mean(rm), 2),
       round(sem(rm), 2),
       round(sts.stdev(rm), 2),
       len(rm)] 

tau_ = ['Membrane time constant \u03C4 (\u03BCs)', 
       round(np.mean(tau), 2),
       round(sem(tau), 2),
       round(sts.stdev(tau), 2),
       len(tau)] 

hold_ = ['Holding current (pA)', 
       round(np.mean(hold), 2),
       round(sem(hold), 2),
       round(sts.stdev(hold), 2),
       len(hold)] 

diameter_ = ['Diameter (\u03BCm)', 
       round(np.mean(diameter), 2),
       round(sem(diameter), 2),
       round(sts.stdev(diameter), 2),
       len(diameter)] 

# Append to Excel file
ws.append(cm_)
ws.append(ra_)
ws.append(rm_)
ws.append(tau_)
ws.append(hold_)
ws.append(diameter_)

wb.save(filename=pathToData + '/mtp_data_analysis.xlsx')
    