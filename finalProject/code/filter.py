#! /bin/env python

import numpy as np
import thinkdsp as dsp
from scipy.io import wavfile

"""helper functions"""
def csvParser(csv):
    with open(csv) as f:
        data = np.asarray(f.readlines()).astype(np.complex)
    return data

def freqDomain(H, x):
    """H must be an fft, x must be a thinkdsp.Wave object"""
    X = np.fft.fft(x.ys)
    Y = H*X
    y = np.fft.ifft(Y)
    return y

"""filters"""
def theoretical(wav):
    print "this function doesn't work yet"
    return

def chirp(x, csv="chirpFFT.csv"):
    x = x[1]
    frx = x[0]
    H = csvParser(csv)
    y = freqDomain(H, x)
    wavfile.write("filtered_chirp.wav", frx, y)
    return

def impulse(x, csv="impulseFFT.csv"):
    x = x[1]
    frx = x[0]
    H = csvParser(csv)
    y = freqDomain(H, x)
    wavfile.write("filtered_impulse.wav", frx, y)
    return

def whiteNoise(x, wav="wnTransferFunc.wav"):
    x = x[1]
    frx = x[0]
    frh, h = wavfile.read(wav)
    y = np.convolve(x.astype(float), h.astype(float), 'full')
    wavfile.write("filtered_whiteNoise.wav", frx, y)
    return


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="This script filters .wav files through a capped PVC pipe with the transfer function for said PVC pipe.")
    parser.add_argument(
            "wav", 
            type=str,
            help="input .wav filename as string"
            )
    parser.add_argument(
            "-t", "--theoretical",
            action="store_true",
            help="filter wav with theoretical transfer function"
            )
    parser.add_argument(
            "-w", "--whiteNoise",
            action="store_true",
            help="filter wav file with whitenoise transfer function"
            )
    parser.add_argument(
            "-c", "--chirp",
            action="store_true",
            help="filter wav file with chirp transfer function"
            )
    parser.add_argument(
            "-i", "--impulse",
            action="store_true",
            help="filter wav file with impulse transfer function"
            )
    args = parser.parse_args()
    
    fr, signal = wavfile.read(args.wav)
    signal = [fr, signal]

    if args.theoretical:
        theoretical(signal)
    if args.whiteNoise:
        whiteNoise(signal)
    if args.chirp:
        chirp(signal)
    if args.impulse:
        impulse(signal)
    else:
        print "no filter type selected. The default is whitenoise"
        whiteNoise(signal)
