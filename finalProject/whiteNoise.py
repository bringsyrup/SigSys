#! /bin/env python
import thinkdsp as dsp
import numpy as np
import matplotlib.pyplot as plt
import sys
import bode

def write(wavFiles, frameRate):
    wavIn = thinkdsp.read_wave(wavFile[1])
    wavOut = thinkdsp.read_wave(wavFile[2])
    freqResp = len(wavIn) * np.correlate(wavIn.ys,wavOut.ys)
    dsp.Wave(freqResp, frameRate).write('whiteNoiseFFT.wav')
    bode.plot(freqResp, 'White noise')
    return


if __name__ == "__main__":
    write(sys.argv[1:2], sys.argv[3])
