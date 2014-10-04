from numpy.fft import *
from pylab import *
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import scipy
import pylab


def plotGraph(fftArray1, fftArray2):
	#plt.figure(1)
	#plt.subplot(211)
	plt.plot(fftArray1)
	#plt.subplot(212)
	#plt.plot(fftArray2)
	plt.show()


def plotSpecgram(fftArray):
	f = 10.
	w = 2. * np.pi * f
	time_interval = 100
	samples = 5000
	t = np.linspace(0, time_interval, samples)
	Pxx, freqs, t, plot = pylab.specgram(fftArray, NFFT=128, Fs=44100, detrend=pylab.detrend_none, window=pylab.window_hanning, noverlap=int(128 * 0.5))
	show()

def main():
	rate1, data1 = scipy.io.wavfile.read('Clear Speech No Noise.wav')
	rate2, data2 = scipy.io.wavfile.read('Clear Speech With Noise.wav')

	print ("rate 1: " + str(rate1))
	print ("rate 2: " + str(rate2))

	print ("data 1: " + str(data1))
	print ("data 2: " + str(data2))

	f1 = fft(data1)
	f2 = fft(data2)

	#plotGraph(data2,f2)
	#plotGraph(data2,f2)
	# plotGraph(f2)
	plotSpecgram(data2)

if __name__ == "__main__":
	main()



