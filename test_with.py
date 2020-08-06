import serial

ser = serial.Serial('/dev/tty1', 19200)
# ser.open()
ser.write(b'hello/n')
l=ser.read(100)
print(l)
# ser.close()