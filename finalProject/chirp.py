#! /bin/env python

import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavIn, wavOut):
    freqRespIn = np.fft.fft(dsp.read_wave(wavIn).ys)
    freqRespOut = np.fft.fft(dsp.read_wave(wavOut).ys)
    f = open('chirpFFT.csv', 'w')
    f.write('chirpFFT\n')
    freqResp = freqRespOut/freqRespIn
    for i in range(len(freRespIn)):
        f.write('{!s}\n'.format(freqResp[i]))
    bode.plot(freqResp)
    return

if __name__=="__main__":
    write(sys.argv[1], sys.argv[2])

    
