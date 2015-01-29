class PID:
    def _init_(self,ki,kd,kp):
        self.ki=ki
        self.kd=kd
        self.kp=kp
        self.lastDiff=None
        self.integral=0
        self.past=0
        self.lastTime

    def update(diff, currentTime):
        if (!self.past):
            derivative=0
            self.past=1
        else:
            dT=self.lastTime-curentTime
            derivative=(diff-self.lastDiff)/dT
            self.integral += diff*dT
        if self.integral >= 1:
            self.integral=1
        self.lastDiff=diff
        self.lastTime=currentTime
        PID=kp*diff+ki*self.integral+kd*derivative
        return PID