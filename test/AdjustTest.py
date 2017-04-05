import unittest
from prod.adjust import AdjustedAltitude
import sys
from prod.angle import Angle

class AngleTest(unittest.TestCase):

    def testObservationLowBound(self):
        try:
            AdjustedAltitude(Angle.parse('0d0.0'))
            self.fail('observation low bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testObservationHighBound(self):
        try:
            AdjustedAltitude(Angle.parse('90d0.1'))
            self.fail('observation high bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testMinutesHighBound(self):
        try:
            AdjustedAltitude(Angle.parse('0d60.1'))
            self.fail('minute high bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testHeightLowBound(self):
        try:
            AdjustedAltitude(Angle.parse('30d30.0'), height = -0.1)
            self.fail('height low bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testPressureLowBound(self):
        try:
            AdjustedAltitude(Angle.parse('30d30.0'), pressure = 99)
            self.fail('pressure low bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testPressureHighBound(self):
        try:
            AdjustedAltitude(Angle.parse('30d30.0'), pressure = 1101)
            self.fail('pressure high bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testTemperatureLowBound(self):
        try:
            AdjustedAltitude(Angle.parse('30d30.0'), temperature = -21)
            self.fail('temperature low bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testTemperatureHighBound(self):
        try:
            AdjustedAltitude(Angle.parse('30d30.0'), temperature = 121)
            self.fail('temperature high bound didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testHorizonInvalid(self):
        for i in ('foobar', 'Foobar', 'natificial'):
            try:
                AdjustedAltitude(Angle.parse('30d30.0'), horizon = i)
                self.fail('invalid horizon %s didn\'t raise exception' % i)
            except ValueError:
                sys.exc_clear()

    def testHorizonValid(self):
        for i in ('artificial', 'natural', 'Artificial', 'NaTuRaL'):
            try:
                AdjustedAltitude(Angle.parse('30d30.0'), horizon = i)
            except ValueError as e:
                self.fail('valid horizon %s raised exception: %s'
                    % (i, str(e)))
