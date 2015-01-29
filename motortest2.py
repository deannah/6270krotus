"""
Using mraa to power both motors, theoretically getting robot
to drive forward.

Hitting Ctrl-C stops both motors.
"""

import mraa
import time

x = mraa.Pwm(3)
y = mraa.Pwm(9)
z = mraa.Gpio(8)
z.dir(mraa.DIR_OUT)
a = mraa.Gpio(11)
a.dir(mraa.DIR_OUT)
b = mraa.Gpio(12)
b.dir(mraa.DIR_OUT)
c = mraa.Gpio(13)
c.dir(mraa.DIR_OUT)

x.period_us(700)
y.period_us(700)

x.enable(True)
y.enable(True)

value = .6

z.write(0)
a.write(0)
b.write(0)
c.write(0)

try:
	while(True):
		x.write(value)
		y.write(value)
		time.sleep(0.05)
except KeyboardInterrupt:
	x.write(0)
	y.write(0)
	x.enable(False)
	y.enable(False)
