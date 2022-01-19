import random
import string

class Robot:
    def __init__(self):
        self.name = Robot.name(self)

    def name(self):
        name = ''.join(random.choice(string.ascii_uppercase) for x in range(2))
        name += ''.join(random.choice(str(random.randint(0, 9))) for x in range(3))
        return name

    def reset(self):
         random.seed(random.randint(0, 1024))
         self.name = Robot.name(self)

print(Robot().name)
print(Robot().name)