#! /bin/env python
import thinkdsp as dsp
import numpy as np
import sys
import bode

def write(wavFiles, frameRate):
    wavIn = thinkdsp.read_wave(wavFile[1])
    wavOut = thinkdsp.read_wave(wavFile[2])
    trasferFunc = len(wavIn) * np.correlate(wavIn.ys,wavOut.ys)
    dsp.Wave(trasferFunc, frameRate).write('wnTransferFunc.wav')
    bode.plot(np.fft.fft(trasferFunc), 'White noise')
    return


if __name__ == "__main__":
    write(sys.argv[1:2], sys.argv[3])
