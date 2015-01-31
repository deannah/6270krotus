from TeleopController import *

bot = RobotController.init()
tele = TeleopController.init(bot)

try:
	tele.receive()

except KeyboardInterrupt:
	tele.stopAll()

