#! /bin/env python

import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavIn, wavOut):
    wavIn = dsp.read_wave(wavIn)
    wavOut = dsp.read_wave(wavOut)
    if wavOut.framerate != wavIn.framerate or len(wavOut.ys) != len(wavIn.ys):
        print "wav files must have same length and framerate"
    else:
        f = open('chirpFFT.csv', 'w')
        freqResp = np.fft.fft(wavOut.ys)/np.fft.fft(wavIn.ys)
        for i in range(len(freqResp)):
            f.write('{!s}\n'.format(freqResp[i]))
        bode.plot(freqResp, "Chirp Signal")
    return

if __name__=="__main__":
    write(sys.argv[1], sys.argv[2])

    
