#import RPi.GPIO as GPIO
import os

class TaskSystemStatus:

    def __init__(self, controller=None, path=None):
        print "TaskSystemStatus: initalizing, path:", path
        self.path = path
        self.loaded = False
        self.controller = controller

    def run(self, time):
        if self.path != None:
            if self.loaded == False:
                led = self.controller.getTask("led")
                led.setStatus(3)
                if os.path.exists(self.path) == True:
                    print "TaskSystemStatus: system loaded!"
                    self.loaded = True
                    led.setStatus(4)
                    try:
                        os.remove(self.path)
                    except OSError, e:
                        print "TaskSystemStatus: error while removing status file"

    def cleanup(self):
        print "TaskSystemStatus: cleanup"

