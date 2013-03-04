#import RPi.GPIO as GPIO

class TaskButton:

    def __init__(self, controller=None, gpio_id=24):
        print "TaskButton: initalizing, gpio_id:", gpio_id
        self.pressed = False
        self.controller = controller
        self.buttonGPIO = gpio_id

    def run(self, time):
        #if self.pressed == False and GPIO.event_detected(self.buttonGPIO):
        if self.pressed == False:
            self.pressed = True
            led = self.controller.getTask('led')
            # led.setStatus(3)


    def cleanup(self):
        print "TaskButton: cleanup"

