import serial

def makeIntFunc(port):
	s = serial.Serial(port)
	s.timeout = 1
	def readInt():
		bytes = [ord(x) for x in s.read(2)]
		return (bytes[0] << 8)+bytes[1]
	def openPort():
		s.open()
	def closePort():
		s.close()
	return (readInt, openPort, closePort)
