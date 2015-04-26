#! /bin/env python

import numpy as np
import thinkdsp as dsp

def csvParser(csv):
    with open(csv) as f:
        data = np.asarray(f.readlines()).astype(np.complex)
    return data

def theoretical(wav):
    print "this function doesn't work yet"
    return

def chirp(x, csv="chirpFFT.csv"):
    H = csvParser(csv)
    X = np.fft.fft(x.ys)
    Y = H*X
    y = np.fft.ifft(Y)
    dsp.Wave(y, framerate=x.framerate).write("filtered_chirp.wav")
    return

def impulse(x, csv="impulseFFT.csv"):
    H = csvParser(csv)
    X = np.fft.fft(x.ys)
    Y = H*X
    y = np.fft.ifft(Y)
    dsp.Wave(y, framerate=x.framerate).write("filtered_impulse.wav")
    return

def whiteNoise(x, wav="wnTransferFunc.wav"):
    h = dsp.read_wave(wav)
    y = np.convolve(x.ys, h.ys)
    dsp.Wave(y, framerate=x.framerate).write("filtered_whiteNoise.wav")
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
    
    signal = dsp.read_wave(args.wav)

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
        whiteNoise(args.wav)
