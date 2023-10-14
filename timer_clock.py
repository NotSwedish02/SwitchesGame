import utils

class Timer():
    def __init__(self, limit):
        self.time = 0
        self.limit = limit
        self.ringing = False

    def update(self):

        self.time += utils.DELTA
        if self.time > self.limit:
            self.time = 0
            return True
    
        return False
