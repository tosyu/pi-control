import RPi.GPIO as GPIO
from subprocess import Popen

class TaskButton:

    def __init__(self, controller=None, gpio_id=24):
        print "TaskButton: initalizing, gpio_id:", gpio_id
        self.pressed = False
        self.controller = controller
        self.buttonGPIO = gpio_id
        GPIO.setup(self.buttonGPIO, GPIO.IN)

    def run(self, time):
        if self.pressed == False and GPIO.input(self.buttonGPIO) == False:
            self.pressed = True
            print "TaskButton: button pressed!"
            led = self.controller.getTask('led')
            led.setStatus(3)
            self.closeSystem()

    def closeSystem(self):
        p = Popen(['/sbin/shutdown', '-h', 'now'])

    def cleanup(self):
        print "TaskButton: cleanup"

