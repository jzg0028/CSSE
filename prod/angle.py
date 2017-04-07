import re

class Angle(object):

    def __init__(self, angle = 0.0):
        self.setMinutes((angle - int(angle)) * 60.0)
        self.setDegrees(int(angle))
        self.setSign(angle)

    def getDegrees(self):
        return self.degrees * self.getSign()

    def getMinutes(self):
        return self.minutes * self.getSign()

    def getSign(self):
        return self.sign

    def setDegrees(self, degrees):
        self.degrees = abs(degrees)

    def setMinutes(self, minutes):
        self.minutes = abs(minutes)

    def setSign(self, sign):
        self.sign = -1 if sign < 0.0 else 1 if sign > 0.0 else 0

    def __str__(self):
        return '%s%dd%.1f' % ('-' if self.getSign() < 0 else '',
            abs(self.getDegrees()), abs(self.getMinutes()))

    def __float__(self):
        return self.getDegrees() + self.getMinutes() / 60.0

    @classmethod
    def parse(Angle, angle):
        match = re.match(r'^([-+]?)(\d+)d(\d+\.\d+)$', angle)
        if not match:
            raise ValueError('invalid angle string format: ' + angle)
        angle = Angle()
        angle.setDegrees(int(match.group(2)))
        angle.setMinutes(float(match.group(3)))
        angle.setSign(-1 if match.group(1) == '-' else 1)
        return angle

    def normalize(self, low, high):
        angle = float(self)
        total = abs(low) + abs(high)
        while(angle < low):
            angle.angle += total
        while(angle >= high):
            angle -= total
        return Angle(angle)
