import numpy as np
import scipy.io.wavfile
import math
from numpy.fft import *
from matplotlib import pyplot as plt

rate, data = scipy.io.wavfile.read('Clear Speech No Noise.wav')

print data
print len(data)

f = fft(data)
print f

#fft.freq

plt.plot(f)
plt.show()