#Team Hail Krotus 6.270 2015
=====

This repository contains code run on an Intel Edison to operate a robot contructed from Legos. The robot is capable of (hopefully) both autonomously operating and tele-operation using an Xbox controller. Its goal is to collect ping pong balls and deposit them in a goal.

### Code Structure

##### Setup

This is used for setting up the robot's autonomous operation. It initializes the RobotModel and the GlobalController and then waits for VPS data to become valid to start the robot. Will GlobalController be in charge of stopping the robot?

##### RobotModel

Uses data from sensors and VPS to estimates robot's position and theta.

##### FieldModel

Essentially keeps track of which points are passable and which are not. It probably also needs to know the shape of the field as well as the locations of the inner hexagon, dispensers, and goal. Ideally this wouldn't all be hard-coded but it may need to be.

##### GlobalController

Keeps track of list of tasks, sets LocalController into motion to complete individual tasks, uses RRT for navigational choices.

##### RRT

Using Rapidly Exploring Random Tree to make paths to points and navigate the robot. In theory, Global Controller will tell RRT a final destination and RRT will provide a list of points to get there. Uses FieldModel to determine if points are passable or not.

##### LocalController

Executes current task, whether that be navigate to a point (drive and turn), activate IR, open/close door and raise/lower arm (operate servos)

Controlled by GlobalController, makes use of RobotModel for estimates. Theoretically uses PID to drive to a point. Uses RobotController to actually manipulate robot.

##### PID

Use PID to actually move the robot to a point. Uses position and theta data to correct course so that the robot drives straight, hopefully.

##### RobotController

This is the lowest-level controller and is used by LocalController. This code actually operates motors, servos, and IR.

#### Teleop Control

##### TeleGo

Initializes TeleopController and RobotController and then makes TeleopController begin receiving commands. Essentially the Setup for teleoperation.

##### TeleopController

Uses a socket to receive commands from an Xbox controller. Uses RobotController to operate the robot.

##### Various Tests

The remaining files are all various tests that were important for figuring out how to make the robot work but are not necessary for operation. Many of these files may wind up getting deleted.

### Controlled Parts

TODO: fill in info about motors, servos, and IR, in a similar manner to the sensors section.

### Sensors

#####Gyro

Pin: Analog A2

gyro.read() returns 500 normally, goes to 0 when turning left and goes to 1000 when turning right.

#####Bump Sensors

Pin (Left): 2

Pin (Right): 4

Can do bump.read() to get 0/1 whether it is being pressed.
Can also set bump.isr to call a function on an edge. Originally, these triggered once when the sensors were pressed but then triggered several times once the trigger was no longer pressed. This was a workable state, though the left sensor occasionally triggered for no reason, but now it seems that both sensors trigger semi-regularly for no reason. At this point the bump sensors seem to be useless.


### Misc

#####Pin Swizzle

Since there seems to be no way to account for pin swizzling using code, we manually swapped out pins 9 and 11 between the Edison breakout board and the Arduino motor shield so now we can actually use both motors.

