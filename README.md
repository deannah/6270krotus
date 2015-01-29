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

### Code Structure

##### Setup

Initialize the RobotModel, create the GlobalController, this will probably control starting the robot (waiting for VPS data to be accurate, maybe by having the model do something?) and stopping the robot (timer), though stopping might be up to GlobalController...

Depending on GlobalController implementation, may have to do some work to set it up.

##### RobotModel

Estimates robot's position, theta, and velocity.

##### GlobalController

Keeps track of list of tasks, sets LocalController into motion

##### LocalController

Executes current task, whether that be navigate to a point (drive and turn), operate servo, activate IR sensor...

Controlled by GlobalController, makes use of RobotModel for estimates.
