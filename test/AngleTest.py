import unittest
from prod.angle import Angle
import sys

class AngleTest(unittest.TestCase):

    def testDefaultValues(self):
        try:
            Angle()
        except ValueError as e:
            self.fail('threw: ' + e)

    def testDegreesEqualBoundsPositive(self):
        for i in xrange(1, 720):
            try:
                Angle(degHi = i, degLo = i)
                self.fail('no exception with hi %d and lo %d', (i, i))
            except ValueError:
                sys.exc_clear()

    def testDegreesEqualBoundsNegative(self):
        for i in xrange(-720, 0):
            try:
                Angle(degHi = i, degLo = i)
                self.fail('no exception with hi %d and lo %d', (i, i))
            except ValueError:
                sys.exc_clear()

    def testDegreesEqualBoundsZero(self):
        try:
            Angle(degHi = 0, degLo = 0)
            self.fail('no exception with hi 0 and lo 0')
        except ValueError:
            sys.exc_clear()

    def testMinutesEqualBoundsPositive(self):
        i = 0.01
        while i < 160.0:
            try:
                Angle(minHi = i, minLo = i)
                self.fail('no exception with hi %d and lo %d', (i, i))
            except ValueError:
                sys.exc_clear()
            i += 1

    def testMinutesEqualBoundsNegative(self):
        i = -0.01
        while i < 0.0:
            try:
                Angle(minHi = i, minLo = i)
                self.fail('no exception with hi %d and lo %d', (i, i))
            except ValueError:
                sys.exc_clear()
            i += 1

    def testMinutesEqualBoundsZero(self):
        try:
            Angle(minHi = 0, minLo = 0)
            self.fail('no exception with hi 0 and lo 0')
        except ValueError:
            sys.exc_clear()

    def testParse(self):
        self.assertEquals('359d0.0', str(Angle.parse('359d0.0')))

    def testDegreesCommutativePositive(self):
        i = 0
        while i < 360:
            self.assertEquals(i, Angle.parse(str(Angle(i))))
            i += 1
