#! /bin/env python

import numpy as np

def generate(bits, rate=10000, bitWidth=250, freq=1000, padding=15.0):
    """
    bits --> an array of bits       
    rate --> transmission rate
    bitWidth --> number of samples per symbol
    freq --> cosine multiplier frequency
    padding --> the signal way expand during transmission so I account for that
    """
    
    end = (len(bits) + padding)*bitWidth/rate
    t = np.arange(0, end, 1./rate)
    signal = np.concatenate(
            (
                np.zeros(bitWidth), 
                np.ones(bitWidth), 
                np.cos(2*np.pi + np.pi*(1-np.repeat(bits, bitWidth)))
                )
            )
    try:
        signal = np.append(signal, np.zeros(len(t) - len(signal)))
    except ValueError:
        print "Try making the rate larger or bitWidth smaller"
        return 

    transmission = 1e4*signal*np.cos(2*np.pi*freq*t)
    return transmission


def findEnds(trans, threshold):
    start = 0
    end = len(trans)
    for i in xrange(0, len(trans)):
        if np.abs(trans[i]) > threshold:
            start = i
            break
    for i in xrange(0, len(trans)):
        if np.abs(trans[len(trans) - i - 1]) > threshold:
            end = len(trans) - i - 1
            break
    return start, end


def decode(transmission, freq=1000, rate=10000., bitWidth=250, TF=0.5, LPFcutoff=700):
    """
    transmission --> the raw recieved transmission
    freq --> cosine multiplier frequency
    rate --> transmission data rate
    bitWidth --> know sample width of one bit
    TF --> threshold factor. threshold = TF*max(transmission) 
    LPFcutoff --> low pass filter cutoff frequency
    """
    
    start, end = findEnds(transmission, TF*np.max(transmission))
    signal = transmission[start:end]
    t = np.arange(0, len(signal)/float(rate), 1./rate)[0:len(signal)]

    # search for best theta...
    Tc = np.arange(-bitWidth/rate, bitWidth/rate, 1./rate)
    sincFilter = 2*LPFcutoff*np.sinc(Tc*LPFcutoff/np.pi)
    bestVar = 0
    for theta in np.linspace(-np.pi, np.pi, 20):
        goodSignal = np.convolve(signal*np.cos(2*np.pi*freq*t + theta), sincFilter)
        variance = np.var(goodSignal[0:len(goodSignal)/2])
        if  variance > bestVar:
            bestVar = variance
            bestTheta = theta
    filtSignal = np.convolve(signal*np.cos(2*np.pi*t*freq + bestTheta), sincFilter)

    # some final filtering is necessary, as the filtered signal is shifted in time
    start, end = findEnds(filtSignal,  TF*np.max(filtSignal))
    
    signs = np.sign(filtSignal[start:end])
    zeroBiased = np.array([signs[i] for i in np.arange(0, len(signs), bitWidth)])
    bits = (zeroBiased[1:]*zeroBiased[0] + 1)/2 
    return bits 
