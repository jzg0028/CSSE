import re

def normalize(val, low, high):
    total = abs(low) + abs(high)
    while(val <= low):
        val += total
    while(val > high):
        val -= total
    return val

class Angle(object):

    def __init__(self, angle = 0.0):
        self.angle = angle

    def getDegrees(self):
        return int(self.angle)

    def getMinutes(self):
        return (self.angle - int(self.angle)) * 60.0

    def __str__(self):
        return '%s%dd%.1f' % ('-' if self.angle < 0 else '',
            abs(self.getDegrees()), abs(self.getMinutes()))

    def __float__(self):
        return self.angle

    @classmethod
    def parse(Angle, angle):
        match = re.match(r'^([-+]?)(\d+)d(\d+\.\d+)$', angle)
        if not match:
            raise ValueError('invalid angle string format: ' + angle)
        return Angle(float(match.group(1) + match.group(2)) + \
            float(match.group(1) + match.group(3)) / 60.0)
