#!usr/bin/python

import mraa
import time

x = mraa.Gpio(7)
x.dir(mraa.DIR_OUT)

while True:
	x.write(1)
	time.sleep(0.2)
	x.write(0)
	time.sleep(0.2)