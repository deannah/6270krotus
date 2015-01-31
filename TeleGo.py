from TeleopController import *

bot = RobotController()
tele = TeleopController(bot)

try:
	while(1):
		tele.receive()

except KeyboardInterrupt:
	tele.stopAll()
