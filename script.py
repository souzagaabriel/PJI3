#!/usr/bin/env python
       
import time
import serial
import json
import requests

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
	x = ser.read(size=1)

	if x is not '' :
		valor = bin(int(x.encode("hex"), 16))[2:].zfill(8)
        print valor
        url = "http://nuvem.sj.ifsc.edu.br:5011/inserir"
        data = {'valorPico': valor}
        headers = {'Content-type': 'application/json'}
        data=json.dumps(data)
        r = requests.post(url, data=data, headers=headers)
