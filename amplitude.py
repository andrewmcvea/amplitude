#Imported packages for histograms
from __future__ import division
import h5py
import numpy as np
from zmq_client import adc_to_voltage
import sys
from scipy.optimize import fmin

print "start program"

def get_window(v):
    ind = np.argmin(v[np.min(v,axis=1) < -10],axis=1)
    med = np.median(ind)
    # 20 ns window
    return med - 20, med + 20


#Finds the amplitude of each of the charge curves with barrier
def find_amp(v):
	amplitude = np.min(v,axis=1)
	win = get_window(v)
#	chargeamp = -adc_to_voltage(np.trapz(dset2[:,win[0]:win[1]]))*1e3/2/50.0
	return abs(amplitude)

#Takes the input from the terminal and reads it
if __name__ == '__main__':
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="input filename")
    args = parser.parse_args()

    f = h5py.File(args.filename)
    dset = f['c1'][:100000]
    histamp = find_amp(dset)
#    dset2 = f['c2'][:100000]
 #   histamp2 = find_amp(dset2)

    plt.hist(histamp, bins=range(min(histamp), max(histamp), 1))
  #  plt.hist(histamp2, bins=range(min(histamp2), max(histamp2), 1))
    plt.title("Histogram of Pulse Amplitude")
    plt.xlabel("Amplitude")

    plt.show()



