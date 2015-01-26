import mraa
import time

x = mraa.Pwm(3)
#y = mraa.Pwm(11)
z = mraa.Gpio(8)
z.dir(mraa.DIR_OUT)
a = mraa.Gpio(9)
a.dir(mraa.DIR_OUT)
b = mraa.Gpio(12)
b.dir(mraa.DIR_OUT)
c = mraa.Gpio(13)
c.dir(mraa.DIR_OUT)

x.period_us(700)
#y.period_us(700)

x.enable(True)
#y.enable(True)

value = 1.0

z.write(0)
a.write(0)
b.write(0)
c.write(0)

while(True):
	x.write(value)
#	y.write(value)
	time.sleep(0.05)
#	value = value + 0.01
#	if value >= 1:
#		value = 0.0
