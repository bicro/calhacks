import wave
from array import array
from math import sin, pi

def compose(pitches, rate, bpm):
	beat = 60/bpm
	retval = bytes()
	for p in pitches:
		retval += tone(pitch[p], beat, rate)
	return retval
def tone(freq, duration, rate, scale=255):
	return bytes(int(scale/2*sin(x*freq*2*pi/rate)+scale/2) for x in range(0, int(rate*duration)))

pitch={"C":261.63,"D":293.66, "E":329.63,"F":349.23,"G":392,"A":440,"B":493.88,".":0}

def wav(filename, data, rate=44100, width=2, channels=1):
	datarray = array("h")
	max_val = (2**(width*8-1)) -1
	min_val = -(2**(width*8-1))
	for x in data:
		datarray.append(max(min_val, min(max_val, int(x))))

	with wave.open(filename, "wb") as w:
		w.setnchannels(channels)
		w.setsampwidth(width)
		w.setframerate(rate)
		w.writeframes(datarray)
		w.close()

def poll_wav(filename, rate, samples,val_func, finish_func=None, in_bits=12):
	width=2
	channels=1
	data = []
	scale = 2**(16-in_bits)
	bias = 2**(in_bits-1)
	for _ in range(samples):
		data.append(scale*(val_func()-bias))
	if finish_func: finish_func()
	wav(filename, data, rate, width, channels)

def print_hello():
	print("hello")

def tone_func(freq, rate, scale, offset):
	def tgen():
		n = 0
		while True:
			yield int(scale*sin(n*freq*2*pi/rate)+offset)
			n += 1
	g = tgen()
	return lambda: next(g) 
