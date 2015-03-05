#! /bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Fourier series: sum C_k * j*sin(2*pi*k*t/T)
# for a square wave: C_k =  0.5             for k = 0
#                           0               for k is even
#                           T/(j*2*pi*k)    for k is odd

def squareWave(k_range=[0, 100], t_res=100, T=1):
    T = int(T)
    if len(k_range) == 1:
        kmin = 0
        kmax = k_range[0]
    else:
        kmin = int(min(k_range))
        kmax = int(max(k_range))
    K = xrange(kmin, kmax)
    ts = np.linspace(-T, T, t_res)
    terms = []

    for k in K:
        if k == 0:
            terms.append([0 for t in ts])
        elif k % 2 == 1:
            terms.append([t * np.sinc(2*k*t/T) for t in ts])
        else:
            pass
    return ts, np.sum(terms, axis=0)

if __name__=="__main__":
    ts1, x1 = squareWave(k_range=[5], T=4)
    ts2, x2 = squareWave(k_range=[17], T=4)
    ts3, x3 = squareWave(k_range=[257], T=4)
    plt.subplot(311)
    plt.plot(ts1, x1, linewidth=2)
    plt.title("Fourier Square Waves with T = 4 and k = 5, 17, and 257", fontsize=24)
    plt.subplot(312)
    plt.plot(ts2, x2, linewidth=2)
    plt.subplot(313)
    plt.plot(ts3, x3, linewidth=2)
    plt.show()
