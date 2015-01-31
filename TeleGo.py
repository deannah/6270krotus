from TeleopController import *

bot = RobotController.init()
tele = TeleopController.init(bot)
quit = False

while !quit:
	tele.receive()

except KeyboardInterrupt:
	quit = True
	tele.stopAll()

