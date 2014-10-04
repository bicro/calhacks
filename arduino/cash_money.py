from combine import makeIntFunc
from wavutils import poll_wav

def read_wav(filename, port, rate=44100, duration=1, bits=12):
    readInt, openPort, closePort = makeIntFunc(port)
    poll_wav(filename, rate, int(rate*duration), readInt, closePort, bits)
