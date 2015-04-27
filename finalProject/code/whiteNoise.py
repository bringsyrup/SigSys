#! /bin/env python
import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavIn, wavOut):
    wavIn = dsp.read_wave(wavIn)
    wavOut = dsp.read_wave(wavOut)
    transferFunc = len(wavIn) * np.correlate(wavIn.ys, wavOut.ys)
    dsp.Wave(transferFunc, wavIn.framerate).write('wnTransferFunc.wav')
    freqResp = np.fft.fft(transferFunc)
    print transferFunc
    bode.plot(freqResp[0:len(freqResp/2)], 'White noise')
    return


if __name__ == "__main__":
    write(sys.argv[1], sys.argv[2])
