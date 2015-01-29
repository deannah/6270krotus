"""
For testing out printing from Edison
"""

#!/usr/bin/python

import mraa
import time

print "Hello from Mrao"
print "Meow."

x = mraa.Pwm(3)

try:
	print "turning motor on"
	x.period_us(700)
	x.enable(True)
	value = 0.0

	while True:
		x.write(value)
		time.sleep(.05)
		value += .01
		if value >= .7:
			value = 0
except KeyboardInterrupt:
	x.write(0)
	x.enable(False)
	print "motor off"
