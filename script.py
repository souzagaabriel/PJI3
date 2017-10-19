#!/usr/bin/env python
       
import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0
while 1:
	#x=binascii.hexlify(ser.read(8))
       #
	x = ser.read(size=1) 

	if x is not '' :
		print bin(int(x.encode("hex"), 16))[2:].zfill(8)
	
