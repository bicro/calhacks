import wave
from math import sin, pi

def compose(pitches, rate, bpm):
	beat = 60/bpm
	retval = bytes()
	for p in pitches:
		retval += tone(pitch[p], beat, rate)
	return retval
def tone(freq, duration, rate):
	return bytes(int(127.5*sin(x*freq*2*pi/rate)+127.5) for x in range(0, int(44100*duration)))

pitch={"C":261.63,"D":293.66, "E":329.63,"F":349.23,"G":392,"A":440,"B":493.88,".":0}

def wav(filename, data, rate=44100, width=1):
	if(type(data) != bytes):
		data = bytes(max(0, min(255, int(x))) for x in data)
	w = wave.open(filename, "wb")
	w.setnchannels(1)
	w.setsampwidth(width)
	w.setframerate(rate)
	w.writeframes(data)
	w.close()
