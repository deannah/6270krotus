
"""
Using Wiring-x86 to power motor A which turns the left wheel forward.

Hitting Ctrl-C stops motor.
"""

#!usr/bin/python


from wiringx86 import GPIOEdison as GPIO
import time

gpio = GPIO(debug=False)
pin = 9
pin2 = 13
fastness = 100
delta = 5

gpio.pinMode(pin, gpio.PWM)
gpio.pinMode(pin2, gpio.OUTPUT)
gpio.digitalWrite(pin2, gpio.HIGH)

try:
	while(True):
		gpio.analogWrite(pin, fastness)
		fastness = fastness + delta
		if fastness == 0 or fastness == 255:
			delta = -delta
		time.sleep(0.03)

except KeyboardInterrupt:
	gpio.analogWrite(pin, 0)
	gpio.cleanup()
