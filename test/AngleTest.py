import unittest
from prod.angle import Angle
import sys

class AngleTest(unittest.TestCase):

    def testDefaultValues(self):
        try:
            Angle()
        except ValueError as e:
            self.fail('threw: ' + e)

    def testParse(self):
        self.assertEquals('359d0.0', str(Angle.parse('359d0.0')))

    def testDegreesCommutativePositive(self):
        i = 0.0
        while i < 360.0:
            self.assertEquals(i, float(Angle.parse(str(Angle(i)))))
            i += 1.0

    def testDegreesCommutativePositive(self):
        i = -360.0
        while i < 0.0:
            self.assertEquals(i, float(Angle.parse(str(Angle(i)))))
            i += 1.0
