   
   
   
def filters_test(self):
    self.abf.setSweep(self.sweep_number, self.voltage_channel_number)
    x = self.abf.sweepX
    y = self.abf.sweepY
    y1 = tools.Filters(array=y, cutoff_freq=1250, sampling_freq=self.abf.sampleRate, 
                                             order=8, type='lowpass').bessel()
    y2 = tools.Filters(array=y, cutoff_freq=1250, sampling_freq=self.abf.sampleRate, 
                                             order=8, type='lowpass').butterworth()
        
        
        
    plt.plot(x, y, 'k')
    plt.plot(x, y1, 'red')
    plt.plot(x, y2, 'blue')
        
    return plt.show()