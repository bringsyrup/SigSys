#! /bin/env python
import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavIn, wavOut):
    wavIn = dsp.read_wave(wavIn)
    wavOut = dsp.read_wave(wavOut)
    if wavIn.framerate != wavOut.framerate or len(wavIn.ys) != len(wavOut.ys):
        print "wav files must have same framerate and length"
    else:
        transferFunc = np.correlate(wavIn.ys, wavOut.ys, 'same')
        freqResp = np.fft.fft(transferFunc)
        dsp.Wave(transferFunc, wavIn.framerate).write('wnTransferFunc.wav')
        bode.plot(freqResp[0:len(freqResp)/2], 'White noise')
    return


if __name__ == "__main__":
    write(sys.argv[1], sys.argv[2])
