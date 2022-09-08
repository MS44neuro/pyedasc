"""

"""
import os
import sys
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))
from pyedasc.tools import Fitting

# Create fake perfect data
x = [3.65, 6.5, 9.5, 12.45, 15.45, 18.45, 21.45, 24.45, 27.45, 30.4, 33.4, 
     36.4, 39.4, 42.4, 45.4, 48.4, 51.4, 54.4, 57.4, 60.4, 63.4, 66.4, 69.4, 
     72.4, 75.4]
y = [0.23537354, 0.53641695, 0.6974953, 0.77202374, 0.81588846, 0.8479286, 
     0.8605062, 0.88016427, 0.8894128, 0.898398, 0.90049815, 0.9071902, 
     0.91407007, 0.9220623, 0.92449445, 0.92127657, 0.9244174, 0.9324494, 
     0.93014866, 0.9375539, 0.9359525, 0.93972915, 0.94234294, 0.9395922, 
     0.9452315]

fit_mono = Fitting.mono_exponential(x, y)
fit_bi = Fitting.bi_exponential(x, y)

plt.plot(x, y, 'o', markersize=10, markeredgewidth=2)
plt.plot(x, fit_mono[0], color='orange')
plt.plot(x, fit_bi[0], color='red')
plt.show()



print(fit_bi[1])