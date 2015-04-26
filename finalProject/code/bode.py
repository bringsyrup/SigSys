#! /bin/env python

import matplotlib.pyplot as plt
import cmath
import numpy as np

def polar(a):
    phases = np.array([])
    amps = np.array([])
    for item in a:
        phases = np.append(phases, cmath.polar(item)[1])
        amps = np.append(amps, cmath.polar(item)[0])
    return phases, amps

def plot(freqResp, transferType):
    phases, amps = polar(freqResp)
    plt.subplot(2, 1, 1)
    plt.plot(np.linspace(0, len(amps), len(amps)), amps)
    plt.title('Transfer function using' + transferType, fontsize=14)
    plt.ylabel('Amplitude', fontsize=12)
    plt.subplot(2, 1, 2)
    plt.plot(np.linspace(0, len(phases), len(phases)), phases)
    plt.ylabel('Phase', fontsize=12)
    plt.xlabel('Frequency (Hz)', fontsize=12)
    plt.show()
    return

if __name__=="__main__":
    s = np.linspace(np.complex(0 + 1j), np.complex(100 + 3j), 200)
    wc = np.complex(50+1j)
    h = wc/(wc + s)
    plot(h)

