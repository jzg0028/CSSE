import unittest
from prod.correct import Correction
from prod.angle import Angle
import sys

class CorrestionTest(unittest.TestCase):

    def testLatitudeOutOfLowBound(self):
        try:
            Correction(Angle.parse('-90d0.0'), Angle.parse('0d0.0'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
            self.fail('latitude out of bounds didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testLatitudeWithinLowBound(self):
        try:
            Correction(Angle.parse('-89d59.9'), Angle.parse('0d0.0'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
        except ValueError:
            self.fail('latitude within bounds raised exception')

    def testLatitudeOutOfHighBound(self):
        try:
            Correction(Angle.parse('90d0.0'), Angle.parse('0d0.0'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
            self.fail('latitude out of bounds didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testLatitudeWithinHighBound(self):
        try:
            Correction(Angle.parse('89d59.9'), Angle.parse('0d0.0'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
        except ValueError:
            self.fail('latitude within bounds raised exception')
