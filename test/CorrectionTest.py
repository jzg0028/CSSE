import unittest
from prod.correct import Correction
from prod.angle import Angle
import sys
import math

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

    def testIntermediateDistance(self):
        self.assertAlmostEquals (
            -0.789,
            Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).intermediateDistance(),
            3
        )

    def testCorrectedDistance(self):
        self.assertEquals (
            -3950,
            Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).correctedDistance()
        )

    def testCorrectedAzimuth(self):
        self.assertEquals (
            '164d43.1',
            str(Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).correctedAzimuth())
        )

    def testA(self):
        self.assertAlmostEquals (
            0.285,
            Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).a(),
            3
        )

    def testB(self):
        self.assertAlmostEquals (
            0.789,
            Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).b(),
            3
        )

    def testC(self):
        self.assertAlmostEquals (
            0.593,
            Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).c(),
            3
        )

    def testD(self):
        self.assertAlmostEquals (
            0.614,
            Correction(Angle.parse('16d32.3'), Angle.parse('95d41.6'),
                Angle.parse('13d42.3'), Angle.parse('-53d38.4'),
                Angle.parse('74d35.3')).d(),
            3
        )
