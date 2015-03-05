#! /bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Fourier series: sum C_k * j*sin(2*pi*k*t/T)
# for a triangle wave: C_k =    0.5             for k = 0
#                               0               for k is even
#                               2/(pi^2*k^2)    for k is odd

def triangleWave(k_range=[0, 100], t_res=100, T=1, shift=0.0):
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
            terms.append([0.5 for t in ts])
        elif k % 2 == 1:
            terms.append([4/((np.pi**2)*(k**2))*np.cos(2*np.pi*k*t/T) for t in ts])
        else:
            pass
    return ts, np.sum(terms, axis=0)

if __name__=="__main__":
    T=3
    ts, x = triangleWave(k_range=[50], T=T)
    plt.plot(ts, x, linewidth=2)
    plt.title("Fourier Triangle Waves with T = 1, k = 50", fontsize=24)
    plt.xlabel("t", fontsize=20)
    plt.show()
