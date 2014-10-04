import numpy as np
import scipy.io.wavfile
import math
from numpy.fft import *

rate, data = scipy.io.wavfile.read('Clear Speech No Noise.wav')

print data
print len(data)

f = fft(data)
print f

fft.freq
