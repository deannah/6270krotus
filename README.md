#Team Hail Krotus 6.270 2015
=====

This repository contains code run on an Intel Edison to 
(hopefully) achieve an autonomous robot capable of 
movement, particularly collecting and depositing ping pong balls.

###Pin Swizzle

Since there seems to be no way to account for pin swizzling, we manually swapped out pins 9 and 11.


### Drive

Currently using mraa library, robot successfully drives (which at this point means the motors turn on and the wheels turn) backwards. From here we need to turn this into an actual autonomously moving robot. I probably want to draw out a state machine, from there plan out a code structure which'll give us a pretty decent to do list.

### Sensors

#####Gyro

Pin: Analog A0

#####Bump Sensor Left

Pin: 2

#####Bump Sensor Right

Pin: 4

#####Future IR something
