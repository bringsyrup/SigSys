#! /bin/env python

import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavIn, wavOut):
    freqRespIn = np.fft.fft(dsp.read_wave(wavIn).ys)
    freqRespOut = np.fft.fft(dsp.read_wave(wavOut).ys)
    f = open('chirpFFT.csv', 'w')
    freqResp = freqRespOut/freqRespIn
    for i in range(len(freqRespIn)):
        f.write('{!s}\n'.format(freqResp[i]))
    bode.plot(freqResp[0:len(freqResp)/2], "Chirp Signal")
    return

if __name__=="__main__":
    write(sys.argv[1], sys.argv[2])

    
