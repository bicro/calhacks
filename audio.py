import scipy.io.wavfile
import matplotlib.pyplot as plt
from numpy.fft import *

from matplotlib import pyplot as plt


rate, data = scipy.io.wavfile.read('Clear Speech No Noise.wav')

print (data)
print (rate)
print (len(data))

f = fft(data)


#fft.freq


plt.plot(f)
plt.show()


# fs, frames = scipy.io.wavfile.read('Clear Speech No Noise.wav')

# channels = [
#     np.array(frames[:, 0]),
#     np.array(frames[:, 1])
# ]

# # generate specgram
# Pxx, freqs, t, plot = pylab.specgram(
#     channels[0],
#     NFFT=4096, 
#     Fs=44100, 
#     detrend=pylab.detrend_none,
#     window=pylab.window_hanning,
#     noverlap=int(4096 * 0.5))
