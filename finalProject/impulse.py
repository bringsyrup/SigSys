#! /bin/env python

import numpy as np
import thinkdsp as dsp
import sys
import bode

def write(wavFile):
    freqResp = np.fft.fft(dsp.read_wave(wavFile).ys)
    f = open('impulseFFT.csv', 'w')
    f.write('impulseFFT\n')
    for freq in freqResp:
        f.write('{!s}\n'.format(freq))
    bode.plot(freqResp, 'an impulse response')
    return

if __name__=="__main__":
    write(sys.argv[1])

