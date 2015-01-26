#!/usr/bin/python
import mraa
import time

x = mraa.Pwm(5)
x.period_ms(20)
x.enable(True)


while True:
	for i in range(800,2300,100):
		x.pulsewidth_us(i)
		time.sleep(0.05)
	for j in range(2100,700,-100):
		x.pulsewidth_us(j)
		time.sleep(0.05)
