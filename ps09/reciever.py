#! /bin/env python

import numpy as np
import BPSK
import pyaudio as pido
import matplotlib.pyplot as plt
from array import array

def b2a(bits):
    string = ''
    for byte in np.arange(0, int(np.ceil(len(bits)/7))):
        tmp = 0
        for bit in np.arange(0, 7):
            b = bits[byte*7+bit]
            tmp += (2**(6-bit))*b
        string += chr(int(tmp))
    return string

def recieve(sampleRate=8000, threshold=1000, chunkSize=1000):
    stream = pido.PyAudio().open(
            format=pido.paInt16,
            channels=1,
            rate=sampleRate,
            input=True,
            output=False
            )

    chunks = array('h')

    while True:
        firstChunk = array('h', stream.read(chunkSize))
        if max(firstChunk) > threshold:
            break
    chunks.extend(firstChunk)
    
    while True:
        chunk = array('h', stream.read(chunkSize))
        chunks.extend(chunk)
        if max(chunk) < threshold:
            break

    sig = np.frombuffer(chunks, dtype=np.dtype('int16'))
    stream.stop_stream()
    stream.close()
    pido.PyAudio().terminate()
    return sig

if __name__=="__main__":
    sampleRate = 10000
    signal = recieve(sampleRate=sampleRate, threshold=16000, chunkSize=1000)
    bits = BPSK.decode(signal)
    print b2a(bits)
