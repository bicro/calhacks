from numpy.fft import *
from pylab import *
from scipy.io import wavfile
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
import scipy
import pylab

def plotGraph(fftArray1, fftArray2):
	plt.figure(2)
	plt.subplot(211)
	plt.plot(fftArray1)
	plt.subplot(212)
	plt.plot(fftArray2)
	plt.show()


def plotSpecgram(fftArray):
	f = 10.
	w = 2. * np.pi * f
	time_interval = 100
	samples = 5000
	t = np.linspace(0, time_interval, samples)
	Pxx, freqs, t, plot = pylab.specgram(fftArray, NFFT=128, Fs=44100, detrend=pylab.detrend_none, window=pylab.window_hanning, noverlap=int(128 * 0.5))
	plt.show()


def avgFilter(fftArray):
	fftArray2 = fftArray[:]
	total = 0
	for i in range(len(fftArray)):
		total+=abs(fftArray[i])
	mean = total/len(fftArray)

	threshhold = mean * 1.5
	

	return fftArray2.clip(-threshhold,threshhold)

def main():
	rate1, data1 = scipy.io.wavfile.read('SineWave_Merged.wav')
	rate2, data2 = scipy.io.wavfile.read('SineWave_Low.wav')

	print ("rate 1: " + str(rate1))
	print ("rate 2: " + str(rate2))

	print ("data 1: " + str(data1))
	print ("data 2: " + str(data2))

	# f1 = fft(data1)
	# f2 = fft(data2)

	maxAmp = 0
	minAmp = 0

	newData3 = data2[:]
	for i in range(len(data2)):
		maxAmp = max(maxAmp,data2[i])
		minAmp = min(minAmp,data2[i])

	print (maxAmp)
	print (minAmp)

	newData2 = data1[:]
	for i in range(len(data1)):
		if data1[i] < maxAmp and data1[i] > 0:
			newData2[i] = 0
		else:
			newData2[i] = data1[i]
		if data1[i] > minAmp and data1[i] < 0:
			newData2[i] = 0
		else:
			newData2[i] = data1[i]	


	# for i in range(min(len(data1),len(data2))):
	# 	if data2[i]:
	# 		newData2[i] = data1[i]/data2[i]



	# f3 = avgFilter(f2)

	# plotGraph(data1[:1000], data2[:1000])
	# plotGraph(data2[:1000], newData2[:1000])

	#plotSpecgram(data1)

	#plotGraph(newData2, newData2)
	write('test.wav', 44100, newData2)





if __name__ == "__main__":
	main()



