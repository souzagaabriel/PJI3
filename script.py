#!/usr/bin/env python
       
import time
import serial
<<<<<<< HEAD
import json
import requests
=======
>>>>>>> ca2b0b6e4123442bbfb6bdd095a16d6a217e1e4f

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
<<<<<<< HEAD
	x = ser.read(size=1)

	if x is not '' :
		valor = bin(int(x.encode("hex"), 16))[2:].zfill(8)
        print valor
        url = "http://nuvem.sj.ifsc.edu.br:5011/inserir"
        data = {'valorPico': valor}
        headers = {'Content-type': 'application/json'}
        data=json.dumps(data)
        r = requests.post(url, data=data, headers=headers)
=======
	#x=binascii.hexlify(ser.read(8))
       #
	x = ser.read(size=1) 

	if x is not '' :
		print bin(int(x.encode("hex"), 16))[2:].zfill(8)
	
>>>>>>> ca2b0b6e4123442bbfb6bdd095a16d6a217e1e4f
