from __future__ import division
from scipy import signal

#low pass filter
def lowpass(x):
    cutoff = int(x)
    fs = 48000
    Wn = cutoff/(fs/2)
    b, a = signal.butter(2, Wn, 'lowpass', analog=False)
    return b, a


#band pass filter
def bandpass(x, y):
    cutoff1 = int(x)
    cutoff2 = int(y)
    fs = 48000
    Wn = [cutoff1/(fs/2), cutoff2/(fs/2)]
    b, a = signal.cheby1(2, 1, Wn, 'bandpass', analog=False)
    return b, a

#high pass filter
def highpass(x):
    cutoff = int(x)
    fs = 48000
    Wn = cutoff/(fs/2)
    b, a = signal.butter(2, Wn, 'highpass', analog=False)
    return b, a

#convert to hex
def convert(x):
    a = str(x)
    if float(a) < 0:
        b = str(2 + float(a))
        c = int(round(float("0." + b.split(".")[1])*2**30))
        d = str(bin(c)).split("b")[1]
        if not len(d) == 30:
            d = "0"*(30-len(d)) + d
        if int(a.split(".")[0]) == -1:
            e = "10"
        else:
            e = "11"
        f = e + d
        g = str(hex(int(f, 2))).split('x')[1]
        return g
    else:
        b = a
        c = int(round(float("0." + b.split(".")[1])*2**30))
        d = str(bin(c)).split("b")[1]
        if not len(d) == 30:
            d = "0"*(30-len(d)) + d
        e = str(bin(int(b.split(".")[0]))).split("b")[1]
        if not len(e) == 2:
            e = "0"*(2-len(e)) + e
        f = e + d
        g = str(hex(int(f, 2))).split('x')[1]
        if not len(g) == 8:
            g = "0"*(8-len(g)) + g
        return g