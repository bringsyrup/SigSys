#! /bin/env python

import numpy as np
import thinkdsp as dsp
import sys
import bode

def write(wavIn):
    wavIn = dsp.read_wave(wavIn)
    wavIn.ys = wavIn.ys.astype(float)
    freqResp = np.fft.fft(wavIn.ys, n=40000)
    f = open('impulseFFT.csv', 'w')
    for freq in freqResp:
        f.write('{!s}\n'.format(freq))
    bode.plot(freqResp[:20000], 'an impulse response')
    return

if __name__=="__main__":
    write(sys.argv[1])#, sys.argv[2])

