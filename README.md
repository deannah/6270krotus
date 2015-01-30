#Team Hail Krotus 6.270 2015
=====

This repository contains code run on an Intel Edison to 
(hopefully) achieve an autonomous robot capable of 
movement, particularly collecting and depositing ping pong balls.

### Misc


#####Pin Swizzle

Since there seems to be no way to account for pin swizzling, we manually swapped out pins 9 and 11.


##### Drive

Currently using mraa library, robot successfully drives (which at this point means the motors turn on and the wheels turn) backwards. From here we need to turn this into an actual autonomously moving robot. I probably want to draw out a state machine, from there plan out a code structure which'll give us a pretty decent to do list.

##### VPS

We'll have some function to call that will get VPS data. This will be team #, x, y, theta, and time. It'll be a thread running in the background. Not entirely sure how to utilize it at this point.

### Sensors

#####Gyro

Pin: Analog A2

gyro.read() returns 500 normally, goes to 0 when turning left and goes to 1000 when turning right.

#####Bump Sensors

Pin (Left): 2

Pin (Right): 4

Can do bump.read() to get 0/1 whether it is being pressed.
Can also set bump.isr to call a function on an edge. This triggers nicely when the sensor is pressed but when you stop pressing the sensor it triggers several times, so that'll be something to watch out for.

Also the left bump sensor seems to be a little derpy and occasionally decides it is being pressed when it is not.

#####Future IR something?

### Code Structure

##### Setup

Initialize the RobotModel, create the GlobalController, this will probably control starting the robot (waiting for VPS data to be accurate, maybe by having the model do something?) and stopping the robot (timer), though stopping might be up to GlobalController...

Depending on GlobalController implementation, may have to do some work to set it up.

##### RobotModel

Estimates robot's position, theta, and velocity.

##### FieldModel

Essentially keeps track of which points are passable and which are not. Need to figure out how to deal with hexagons and whether or not to hardcode inner hexagon. Ideally this would know where dispensers are which I'm guessing has to be hard coded? Maybe it'll also know where the goal is. It probably has to...

##### GlobalController

Keeps track of list of tasks, sets LocalController into motion, uses RRT for navigational choices.

##### RRT

Using Rapidly Exploring Random Tree to make paths to points and navigate the robot or something. I don't actually know exactly how this will be utilized by GlobalController yet.

##### LocalController

Executes current task, whether that be navigate to a point (drive and turn), operate servo, activate IR...

Controlled by GlobalController, makes use of RobotModel for estimates. Uses RobotController to actually manipulate robot.

##### PID

Use PID to actually move the robot to a point. Cool.

##### RobotController

Lowest level controller. This code actually controls motors, servos, and IR. Used by LocalController.
