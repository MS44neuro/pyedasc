
[![logo.png](https://i.postimg.cc/wTPvMWPb/logo.png)](https://postimg.cc/rK1cY9qS) 
# pyedasc
## Electrophysiology data analysis script colection

At this point, this python package is a collection of modules for analyzing electrophysiology data from patch-clamp recordings, including both current-clamp and voltage clamp acquisitions. Work here was inspired and made possible by the [pyabf project](https://pypi.org/project/pyabf/), which allowed an easily use of raw data recordings in Python.

## Features
- Detection and analysis of action potentials
-  Big data analysis
- Membrane current analysis: IV curves, voltage corrections, chord / slope conductances, current / conductance densities, 
- Plotting options
- Analysis for recovery from inactivation protocols
- Membrane test parameters extraction from _.sta_ files

## Installation - not yet published

```sh
pip install pyedasc # Not yet uploaded on PyPI
```



# How to use
# I. Action potential parameters analysis - ap module
Import the module:
```python
from pyedasc import ap
```
 _Minimum input_
 
The minimum input consists of the following parameters: ```abf_file```, which is either directly the name of the .abf file in the source folder or complete path to the file. Next, the ```current_channel_number``` and ```voltage_channel_number``` must be specified, as integers, from 0 to n-1, according to Digitizers Channels. ```sweep_number```is also used to specify the trace sweep where the detection will be made. All integer input so far will be given using the numbering from 0 to n-1. The last parameter needed is ```absolute_rp_interval```. This should be passed as a list of 2 integers representing the indexes of the interval edges on the voltage signal, where the absolute value of the resting potential will be calculated, later used to fix RP points.

The 2 classes in the module are Parameters and Plotting which accepts the same attributes: 
```python
parameters = ap.Parameters(abf_file='abf_file.abf', current_channel_number=0, voltage_channel_number=1, 
                           sweep_number=4,  absolute_rp_interval=[100, 500])

plotting = ap.Plotting(abf_file='abf_file.abf', current_channel_number=0, voltage_channel_number=1, 
                       sweep_number=4, absolute_rp_interval=[100, 500])
```


As a first example let's print the voltage peaks detected in the provided .abf file. Here, the first list, ```parameters.peaks()[0]``` contains the action potential peak values (in mV) and ```parameters.peaks()[1]``` contains their indices. 
```python
print(parameters.peaks())

OUTPUT
([59.08], [602]) # If only one AP peak detected
```

Next, let's print the RP points. These 3 points set the limits of the action potential and their correct detection is essential for the analysis. Each of these methods returns a tuple with (value, index) of the RP point.
```python
print(parameters.rp_1(), parameters.rp_2(), parameters.rp_3())

OUTPUT
(-73.24, 562) (-74.37, 620) (-74.4, 3101)
```
Below are 2 different recordings, with only one AP per trace or multiple APs per trace, where the red markers represents the  RP1, RP2 and RP3 points. In the case of _10kHz_ap_train_file_1.abf_, the ```ap_number``` parameter was passed, which allows the selection of the AP to be analyzed, from those detected.

[![RPs.png](https://i.postimg.cc/HkDr3Z28/RPs.png)](https://postimg.cc/9rbXQBsc)

If ```ap_number``` parameter is 1.

[![RPs-2-trains-ap2.png](https://i.postimg.cc/KcTLD0zg/RPs-2-trains-ap2.png)](https://postimg.cc/K4ZRZrtZ)

If ```ap_number``` parameter is 3.

[![RPs-2-trains-ap4.png](https://i.postimg.cc/YS7Nj9W0/RPs-2-trains-ap4.png)](https://postimg.cc/zydHcqpY)

## Other optional parameters that can be passed in ```Parameters()``` class:
Attribute | Description
-- | ----
```ap_number``` | which of the detected action potentials will be analyzed, by default 0 (first one)
```peak_detection_threshold```| voltage threshold for peak detection, by default None
| RP points: second level of detection
```rp_1_det```| list of 2 integers representing interval edges for rp1 detection, by default None
```rp_2_det```| list of 2 integers representing interval edges for rp1 detection, by default None
```rp_3_det```| list of 2 integers representing interval edges for rp1 detection, by default None
| RP points: third level of detection
```rp_1_fixedP```| fixed point for rp1, by default None
```rp_2_fixedP```| fixed point for rp2, by default None
```rp_3_fixedP```| fixed point for rp3, by default None
## Some of the methods in the ```Parameters()``` class:
Method | Description
-- | ----
AMPLITUDE PARAMETERS|
```threshold(method) ``` |  Calculate the action potential threshold by several methods. Returns (value, index) according to the specified method
```overshoot()```| Returns the positive voltage value at the AP peak (mV).
```total_amplitude()```|  Returns AP total amplitude or AP size by adding positive resting potential value to overshoot value.
```afterhyperpolarization()```| Returns the minimum voltage value in interval from rp2 to rp3, i.e. minimum voltage after falling phase.
```ahp_substracted_value()```| The value of ahp baselined at resting potential.
```afterhyperpolarization_at(percentage)```| Returns the point where the ahp amplitude was recovered to resting potential value, at a certain percentage.
DURATION PARAMETERS|
```ahp_recovery_time_at(percentage)```| Returns duration (ms) from ahp point to ahp recovery point at given procentage.
```duration_at(level)```| Returns durations for different parameters of AP.
```phase_time(region)```|  Returns durations for ascending (rising), descending (falling) phases and also ahp.
```latencies(between, th_method)```| Returns the latency of some parameters relative to the starting point of the stimulation.
RATE PARAMETERS |
```amplitude_over_time(region)```| Returns the voltage change over time, for rising & falling phases, ahp 80% recovery and total recovery.
AREA |
```area(region)```| Returns the area of the selected region ('base', 'overshoot', 'rise', 'fall', 'upper-rise', 'upper-fall', 'lower-rise', 'lower-fall').
```shoulder_area()```| Returns the AP repolarization shoulder area.
SLOPES |
```maximal_slope(phase)```| Returns the maximal slopes of rising and falling phases.


##### ```Plotting()``` class:
* Use abf file voltage signal and action potential parameters to generate figures and plots
*  Inherits all the methods and properties from Parameters class.

### Additional methods for plotting
Method | Description
-- | ----
```raw_recording(action, extension) ``` | Generates a plot with the raw content of the abf file.
```graph_3D(action:str, extension, text_box, rotation)```| Generates a 3D plot with the raw content of the abf file, only the voltage channel data for all sweeps in recording.
```gifs(action)```| Returns a gif animation with the action potential analyzed.  [![ap-file-1-abf.gif](https://i.postimg.cc/5yGyGF2N/ap-file-1-abf.gif)](https://postimg.cc/tn39nJ6L)
```gif_3D(action)```| Returns a gif animation with current action potential analyzed. [![3d-raw-sweeps.gif](https://i.postimg.cc/TY6452jB/3d-raw-sweeps.gif)](https://postimg.cc/SjgrwhvG)
```ap_plot(action, extension)``` | Returns a figure with current sweep voltage signal, reprezenting the action potential analyzed with some parameters highlighted. [![ap-plot-final.png](https://i.postimg.cc/DwRd9BzL/ap-plot-final.png)](https://postimg.cc/nXYD7KBh) [![ap-plot-final-trains-1.png](https://i.postimg.cc/gjv20cyG/ap-plot-final-trains-1.png)](https://postimg.cc/rRwknkYH)

 ```ap_plot``` it is a very useful method to directly check if the action potential has been analyzed correctly.
 
 
 
 
# II. Current analysis - ca module

The ca.py module aims to detect and analyze current traces in the abf files provided by the user. The required input is similar to that in the ap.py. The only class in this file is ```Parameters()```.

Import the module:
```python
from pyedasc import ca
```

 _Minimum input_
 
The minimum input consists of the following parameters: ```abf_file```, which is either directly the name of the .abf file in the source folder or complete path to the file. Next, the ```current_channel_number``` and ```voltage_channel_number``` must be specified, as integers, ```imemb_region``` , a list of 2 integers used to specify the region on the current trace  where the analysis will be performed, ```vcom_region```a list of 2 integers used to specify the region on the voltage trace where the analysis will be performed and ```peak_polarity``` specifies which type of current is detected in the range ```imemb_region``` ('negative' - minimum current, 'positive' - maximum current, 'mean' - mean current).

```python
# Minimum input for generating an IV plot
par = ca.Parameters(abf_file='abf_file.abf', current_channel_number=0, voltage_channel_number=1, 
                    imemb_region=[170, 1200], vcom_region=[170, 1200], peak_polarity='negative')
```

### Other optional parameters that can be passed in ```Parameters()``` class:
Attribute | Description
-- | ----
```liquid_junction_potential``` | Liquid junction potential value calculated elsewhere.
```erev_calculated``` | Fix reversal potential value calculated elsewhere.
```erev_fit_region``` | A list of 2 integers, representing the region in IV (current-voltage steps plot) on which to extrapolate to calculate the reversal potential.
```access_resistance``` | Membrane test parameter, expected in M??.
```membrane_capacitance``` | Membrane test parameter, expected in pF.
```membrane_resistance``` | Membrane test parameter, expected in M??.
```memb_time_constant``` | Membrane test parameter, expected in ??s.
```holding_current``` | Membrane test parameter, expected in pA.
```diameter``` | Given in ??m, obtained from membrane capacitance.



### Methods in ```Parameters()``` class:
Attribute | Description
-- | ----
```current_detection()``` |  Returns the detected current in the range specified as input in ```imemb_region``` parameter.  Depending on ```peak_polarity``` the method returns maximum current (```'positive'```), minimum current (```'negative'```) or average current (```'mean'```).
```voltage_steps_measured()``` | Returns the average voltage detected in the range specified as the input in ```vcom_region``` parameter.
```voltage_steps_waveform() ``` | Returns the voltage step values at ```vcom_region[0]``` in waveform channel.
```voltage_steps_corrected()``` | Returns voltage values corrected for liquid_junction_potential and access resistance, i.e series resistance, if parameters are provided.
```reversal_potential()``` | Returns the reversal potential value, calculated or provided.
```driving_force()``` |  Returns driving force as voltage - reversal potential for every voltage step in trace.
```chord_conductance()``` | Returns the chord conductance values for all voltage steps.
```slope_conductance()``` |  Returns the slope conductance values for all voltage steps and new x axis
```current_density(given_in)``` |  Returns current density values for all voltage steps, using 2 methods, depending on the unit of measurement reported in ```given_in parameter```. 
```conductance_density(method, conductance_type)``` | Returns conductance density for all voltage steps by 2 different methods. 
```plotting(parameter, action, extension)``` | Returns a plot with x-axis the voltage steps corrected and different y-axis depending on the selected parameter.


[![na-act-1.png](https://i.postimg.cc/8zJ7W6Vp/na-act-1.png)](https://postimg.cc/sMzfC1Xq)


# III. Recovery from inactivation current analysis - rfi module
Import the module:
```python
from pyedasc import rfi

set1 = rfi.RFI(abf_file=abf_file, current_channel_number=0, t0_recovery=20511, reference_int=[400, 800],
               recovery_int=[20000, 24000], baseline_interval=[16000, 19000]) 
```
[![rfi.png](https://i.postimg.cc/sfqR0sPY/rfi.png)](https://postimg.cc/7b3c5vWh)

[![rfi-4.png](https://i.postimg.cc/tJSdDBnk/rfi-4.png)](https://postimg.cc/4Hchxb5H)

# IV. Tools - tools and mtp modules

## tools module
Import the module:
```python
from pyedasc import tools
```



## mtp module
The mtp module extracts the membrane parameters from the _.sta_ files. The only class, ```Extractor()```, processes the files and prepares the columns for extraction. The only attribute of the class is ```reading_range```, a list of 2 integers representing the indices of the interval on the column, where the values averaging is extracteed. By default None and reading range is from the 20th to 100th value in column.
            
Using the module:
```python
from pyedasc import mtp

extract = mtp.Extractor()

print(extract.cm('sta_file.sta')) # Membrane capacitance (pF)
print(extract.rm('sta_file.sta')) # Membrane resistance (MOhms)
print(extract.ra('sta_file.sta')) # Access resistance (MOhms)
print(extract.tau('sta_file.sta')) # Time constant (??s)
print(extract.hold('sta_file.sta')) # Holding current (pA)
print(extract.diameter('sta_file.sta')) # Cell diameter (??m)

OUTPUT
50.73
1233.1
3.5
245.26
-20.9
40.18
```



