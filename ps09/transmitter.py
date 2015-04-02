#! /bin/env python

import pyaudio as pido
import numpy as np
import BPSK
import time
import sys

def a2b(string):
    bits = np.asarray([float((byte>>(7-bit-1))&1) for byte in bytearray(string, 'ascii') for bit in xrange(0, 7)])
    return bits

def transmit(sig, rate):
    stream = pido.PyAudio().open(
            format=pido.paInt16, 
            channels=1, 
            rate=rate, 
            input=False, 
            output=True,
            frames_per_buffer=len(sig)
            )
    time.sleep(5)
    stream.write(sig.astype(np.int16).tostring())
    stream.stop_stream()
    stream.close()
    pido.PyAudio().terminate()
    return

if __name__=="__main__":
    string = sys.argv[1]
    wordbits = a2b(string)
    signal = BPSK.generate(wordbits)
    transmit(signal, rate=10000)



