#! /bin/env python

import matplotlib.pyplot as plt
import numpy as np

def LRC(L, R, C, omega):
    H = 1/np.sqrt((R*C*omega)**2 + (L*C*omega**2 -1)**2)
    PR = -np.arctan(omega*R*C/(L*C*omega**2 -1))
    return H, PR

if __name__=="__main__":
    omega = np.logspace(-2, 6, 5000)
    L = 1e-2
    R1 = 400
    C = 1e-7

    R2 = 50

    H1, PR1 = LRC(L, R1, C, omega)
    H2, PR2 = LRC(L, R2, C, omega)

    plt.subplot(2, 1, 1)
    plt.loglog(omega, H1)
    plt.title('Bode plot for L = 10^-2, R = 400, C = 10^-7')
    plt.ylabel('Magnitude of freq. response')

    plt.subplot(2, 1, 2)
    plt.semilogx(omega, PR1)
    plt.ylabel('phase (theta)')
    plt.xlabel('frequency (rad/s)')
    plt.show()
