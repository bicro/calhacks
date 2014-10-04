import numpy
import pylab
import scipy.io.wavfile
from numpy.fft import *
from matplotlib import pyplot as plt


rate, data = scipy.io.wavfile.read('Clear Speech No Noise.wav')

print data
print rate
print len(data)

f = fft(data)

pylab.specgram(f)
print f

#fft.freq

plt.plot(f)
plt.show()

