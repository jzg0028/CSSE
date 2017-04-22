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

    def testLongitudeOutOfLowBound(self):
        try:
            Correction(Angle.parse('0d0.0'), Angle.parse('-0d0.1'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
            self.fail('longitude out of bounds didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testLongitudeWithinLowBound(self):
        try:
            Correction(Angle.parse('0d0.0'), Angle.parse('0d0.0'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
        except ValueError:
            self.fail('longitude within bounds raised exception')

    def testLongitudeOutOfHighBound(self):
        try:
            Correction(Angle.parse('0d0.0'), Angle.parse('360d0.0'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
            self.fail('longitude out of bounds didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def testLongitudeWithinHighBound(self):
        try:
            Correction(Angle.parse('0d0.0'), Angle.parse('359d59.9'),
                Angle.parse('1d0.0'), Angle.parse('0d0.0'),
                Angle.parse('0d0.0'))
        except ValueError:
            self.fail('longitude within bounds raised exception')

    def testCorrectedDistance(self):
        self.assertEquals (
            '65d50.1',
            str(Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')) \
                .correctedDistance())
        )
