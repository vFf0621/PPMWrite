# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:44:49 2021

@author: Fei Guan
"""

import serial, time
arduino = serial.Serial('COM7', 1500000)
while True:
    print(time.time())
    for i in range(1000, 2000):
        s = str(i) + ' ' + str(i) + ' ' + str(i) + ' ' + str(i) + ' '
        print(time.time())
        arduino.write(s.encode())
        print(arduino.readline())

