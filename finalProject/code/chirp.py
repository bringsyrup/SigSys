#! /bin/env python

import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavIn, wavOut):
    wavIn = dsp.read_wave(wavIn)
    wavOut = dsp.read_wave(wavOut)
    wavIn.ys = wavIn.ys.astype(float)
    wavOut.ys = wavOut.ys.astype(float)
    if wavOut.framerate != wavIn.framerate or len(wavOut.ys) != len(wavIn.ys):
        print "wav files must have same length and framerate"
    else:
        f = open('chirpFFT.csv', 'w')
        fout = np.fft.fft(wavOut.ys)
        fin = np.fft.fft(wavIn.ys)
        freqResp = fout/fin 
        ys = np.fft.ifft(freqResp)
        for i in xrange(len(ys)):
            f.write('{!s}\n'.format(ys[i]))
        bode.plot(freqResp[:20000], "Chirp Signal")
    return

if __name__=="__main__":
    write(sys.argv[1], sys.argv[2])

    
