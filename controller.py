import time

class PiController:

    def __init__(self):
        print "PiController: initializing"
        self.tasks = {}
        self.loopInterval = 0.2

    def addTask(self, name, task):
        print "PiController: adding task", name
        self.tasks[name] = task

    def removeTask(self, name):
        print "PiController: removing task", name
        del self.tasks[name]

    def getTask(self, name):
        return self.tasks[name]

    def runTasks(self):
        keys = self.tasks.keys()
        ct = time.time()
        for key in keys:
            self.tasks[key].run(ct)

    def loop(self):
        while True:
            self.runTasks()
            time.sleep(self.loopInterval)

    def cleanup(self):
        print "cleaning up"
        keys = self.tasks.keys()
        for key in keys:
            self.tasks[key].cleanup()

    def start(self):
        try:
            self.loop()
        except (RuntimeError, KeyboardInterrupt):
            print "finishing"
            self.cleanup()
