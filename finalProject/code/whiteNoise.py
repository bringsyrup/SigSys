#! /bin/env python
from scipy.io import wavfile
import numpy as np
import sys
import bode
import matplotlib.pyplot as plt

def write(wavIn, wavOut):
    frin, yin = wavfile.read(wavIn)
    frout, yout = wavfile.read(wavOut)
    if frin != frout:
        print "WARNING: wav files do not have equal framerates"
    transferFunc = np.correlate(yin.flatten().astype(float), yout.flatten().astype(float), 'full')
    transferFunc = transferFunc/np.max(transferFunc)
    freqResp = np.fft.fft(transferFunc)
    wavfile.write('wnTransferFunc.wav', frout, transferFunc[len(transferFunc)/2:])
    plt.plot(transferFunc[len(transferFunc)/2:])
    plt.show()
    #bode.plot(freqResp[:20000], 'White noise')
    return

if __name__ == "__main__":
    write(sys.argv[1], sys.argv[2])
