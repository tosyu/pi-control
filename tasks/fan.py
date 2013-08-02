import time
import RPi.GPIO as GPIO
import os
import subprocess

class TaskFan:

    def __init__(self, controller=None, gpio_id=25):
        print "TaskFan: initializing, gpip_id", gpio_id
        self.status = 0
        self.cooldownstarttime = time.time()
        self.lasttime = time.time()
        self.cooldownduration = 60 * 3
        self.cooldowntemp = 67
        self.pollinterval = 10
        self.fanGPIO = gpio_id
        self.tempcmd = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "bin" + os.sep + "temperature"
        GPIO.setup(gpio_id, GPIO.OUT);

    def run(self, time):
        if self.status == 0:
           # poll
           diff = time - self.lasttime
           if diff >= self.pollinterval:
               self.lasttime = time
               temps = self.getTemps()
               if temps[0] >= self.cooldowntemp or temps[1] >= self.cooldowntemp:
                   self.status = 1
                   self.cooldownstarttime = time
                   self.updateFan()
        elif self.status == 1:
            diff = time - self.cooldownstarttime
            if diff >= self.cooldownduration:
                self.status = 0
                self.cooldownstarttime = time
                self.updateFan()

    def getTemps(self):
        p = subprocess.Popen(self.tempcmd, shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        temps = p.communicate()[0].strip().split("/")
        return [float(temps[0]), float(temps[1])]

    def cleanup(self):
        print "TaskFAN: cleanup"

    def updateFan(self):
        if self.status == 0:
            print "TaskFan: RPI cooled, fan is off"
            GPIO.output(self.fanGPIO, False);
        else:
            print "TaskFan: Cooldown, fan is on"
            GPIO.output(self.fanGPIO, True);

