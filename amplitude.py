#Imported packages for histograms
from __future__ import division
import h5py
import numpy as np
from zmq_client import adc_to_voltage
import sys
from scipy.optimize import fmin

print "start program"

#Finds the amplitude of each of the charge curves with barrier
def find_amp(v):
        amplitude = np.min(v,axis=1)
        vamp = adc_to_voltage(amplitude)
        mask = vamp < -10e-3
        filteramp = vamp[mask]
        return abs(filteramp)

#Takes the input from the terminal and reads it
if __name__ == '__main__':
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="input filename")
    args = parser.parse_args()

    f = h5py.File(args.filename)
    #Trigger PMT
    dset = f['c1'][:100000]
    histamp = find_amp(dset)
    #Signal PMT
    dset2 = f['c2'][:100000]
    histamp2 = find_amp(dset2)
    
    l1 = len(histamp)
    l2 = len(histamp2)
    c_rate = l2/l1
    print c_rate

    plt.figure(1)
    plt.hist(histamp, bins=range(0, max(histamp), 10))
    plt.title("Trigger Pulse Amplitude")
    plt.xlabel("Amplitude")
    plt.figure(2)
    plt.hist(histamp2, bins=range(0, max(histamp2), 10))
    plt.title("Signal Pulse Amplitude")
    plt.xlabel("Amplitude")
    
    plt.show()




