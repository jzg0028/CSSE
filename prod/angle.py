import re

def normalize(val, low, high):
    total = abs(low) + abs(high)
    while(val <= low):
        val += total
    while(val > high):
        val -= total
    return val

class Angle(object):

    def __init__(self, degrees = 0, minutes = 0.0, norm = False,
        degLo = 0, degHi = 360, minLo = 0.0,  minHi = 60.0):
        self.setBounds(degLo, degHi, minLo, minHi)
        self.setDegrees(degrees, norm, degLo, degHi)
        self.setMinutes(minutes, norm, minLo, minHi)

    def setBounds(self, degLo = 0, degHi = 360, minLo = 0.0, minHi = 60.0):
        if degLo >= degHi or minLo >= minHi:
            raise ValueError('low bound > high bound')
        self.degLo, self.degHi = degLo, degHi
        self.minLo, self.minHi = minLo, minHi

    def setDegrees(self, degrees, norm = False, lo = None, hi = None):
        lo, hi = lo or self.degLo, hi or self.degHi
        if not norm and (degrees < lo or degrees >= hi):
            raise ValueError('degrees out of bounds: %d' % degrees)
        self.degrees = normalize(degrees, lo, hi)

    def getDegrees(self):
        return self.degrees

    def setMinutes(self, minutes, norm = False, lo = None, hi = None):
        lo, hi = lo or self.minLo, hi or self.minHi
        if not norm and (minutes < lo or minutes >= hi):
            raise ValueError('minutes out of bounds: %d' % minutes)
        self.minutes = normalize(minutes, lo, hi)

    def getMinutes(self):
        return self.minutes

    def __str__(self):
        return '%dd%.1f' % (self.getDegrees(), self.getMinutes())

    @classmethod
    def parse(Angle, angle, norm = False, degLo = 0, degHi = 360,
        minLo = 0.0, minHi = 60.0):
        match = re.match(r'^([-+]?)(\d+)d(\d+\.\d+)$', angle)
        if not match:
            raise ValueError('invalid angle string format: ' + angle)
        return Angle(int(match.group(1) + match.group(2)),
            float(match.group(1) + match.group(3)), norm,
            degLo, degHi, minLo, minHi)
