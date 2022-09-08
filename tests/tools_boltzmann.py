""" 

"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../pyedasc/'))
from tools import Fitting

# Fake perfect data
x = np.array([-80, -75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20,
              -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
y = np.array([0.01818127777570314, 0.01762738247748779, 0.01870869677456871, 
              0.02246700550090525, 0.031359762959453294, 0.029188033793094658,
              0.022015120449188734, 0.023905750034648697, 0.08588750351635943, 
              0.5472923717303525, 1.2503545229439155, 2.099020857920147, 
              2.5081311185131088, 2.8002756139041276, 2.862605884466482, 
              2.9265128218582985, 2.9498861772031195, 2.970338576744269, 
              2.9771510314161396, 2.9888596773551908, 3.0008593085011963, 
              3.028293925155429, 3.015751049906451, 3.0301165157620904, 
              3.0169631113141935, 3.0414171259150877, 3.0120726566857123, 
              3.0155074044392656])

bz = Fitting.boltzmann(x, y)    


bz_R = Fitting.boltzmann_R(x, y)  
print(bz_R)

# plt.plot(x, y, 'o', linewidth=2, color='black', label='Raw data')
# plt.plot(x, bz[0], '-', color='orange', label='Boltzmann fit')

# plt.ylabel('[Unit of measurement]Y', fontweight='bold', fontsize=16)
# plt.xlabel('Voltage steps (mV)', fontweight='bold', fontsize=16)

#plt.yticks(fontsize=12)
# plt.xticks(fontsize=12)

plt.legend(fontsize=14)
# plt.show()

print(f'Fitting parameters: A1 = {bz[1][0]}, A2 = {bz[1][1]}, x0 = {bz[1][2]}, dx = {bz[1][3]}.')



plt.plot(x, y,'o', color='#515151', linewidth=4.5, alpha=1, mfc='red', mec='k',
         markersize=14, markeredgewidth=2, label='Conductance density')
textbox = [f'Fitting parameters: \n A1 = {round(bz[1][0], 3)}\n '
           + f'A2 = {round(bz[1][1], 3)}\n '
           + f'x0 = {round(bz[1][2], 3)}\n '
           + f'dx = {round(bz[1][3], 3)}\n '
           + f'R\u00b2 = {round(bz_R, 3)}']


        
props = dict(boxstyle='round', facecolor='#53868B', alpha=0.3)
plt.text(-83, 2.5, textbox[0], fontsize=23, verticalalignment='top', bbox=props)


plt.plot(x, bz[0], '-', color='orange', linewidth=3, label='Boltzmann fit')
plt.title("file.abf", fontsize=40, fontweight='bold')
plt.ylabel('Conductace density (nS/pF)', fontweight='bold', fontsize=35)
plt.xlabel('Voltage steps (mV)', fontweight='bold', fontsize=35)

plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

plt.legend(fontsize=25)

plt.show()