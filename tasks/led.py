import time
#import RPi.GPIO as GPIO

class TaskLEDIndicator:

    def __init__(self, controller=None, gpio_id=22):
        print "TaskLEDIndicator: initalizing, gpio_id:", gpio_id
        self.status = 0
        self.lasttime = time.time()
        self.constantBlinkInterval = 0.4
        self.shortBlinkInterval = 0.2
        self.led = False
        self.ledGPIO = gpio_id
        self.shortBlinkStep = 0
        # GPIO.setup(self.ledGPIO, GPIO.OUT)

    def run(self, time):
        if self.status == 3:
            diff = time - self.lasttime
            if diff >= self.constantBlinkInterval:
                self.lasttime = time
                self.led = not self.led
            self.updateLed()
        elif self.status == 4:
            diff = time - self.lasttime
            if diff >= self.shortBlinkInterval:
                self.lasttime = time
                self.led = not self.led
                if self.led == True:
                    self.shortBlinkStep += 1
                if self.shortBlinkStep > 3:
                    self.setStatus(1)
                    self.shortBlinkStep = 0
            self.updateLed()
        elif self.status == 1 and self.led == False:
            self.led = True
            self.updateLed()
        elif self.status == 0 and self.led == True:
            self.led = False
            self.updateLed()

    def cleanup(self):
        print "TaskLEDIndicator: cleanup"

    def updateLed(self):
        if self.led == True:
            print "TaskLEDIndicator: set led on!"
            # GPIO.outout(self.ledGPIO, True)
        else:
            print "TaskLEDIndicator: set led off!"
            # GPIO.outout(self.ledGPIO, False)

    def setStatus(self, status):
        if self.status != status:
            print "TaskLEDIndicator: setting status to", status
            self.status = status

