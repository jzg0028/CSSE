import unittest
import prod.angle as angle

class AngleTest(unittest.TestCase):

    def testToString(self):
        self.assertEqual('0d0.0', angle.toString(0))
        self.assertEqual('0d30.0', angle.toString(0.5))
        self.assertEqual('30d30.0', angle.toString(30.5))
        self.assertEqual('90d0.0', angle.toString(90.0))

    def testParse(self):
        self.assertAlmostEqual(0.0, angle.parse('0d0.0'))
        self.assertAlmostEqual(0.5, angle.parse('0d30.0'))
        self.assertAlmostEqual(30.5, angle.parse('30d30.0'))
        self.assertAlmostEqual(90.0, angle.parse('90d0.0'))

    def testNegative(self):
        self.assertAlmostEqual(-30.5, angle.parse('-30d30.0'))
        self.assertAlmostEqual(-0.5, angle.parse('-0d30.0'))

    def testNormalize360(self):
        self.assertAlmostEqual(360.0, angle.normalize(360.0, 0, 360))
        self.assertAlmostEqual(1.0, angle.normalize(361.0, 0, 360))
        self.assertAlmostEqual(1.0, angle.normalize(721.0, 0, 360))
        self.assertAlmostEqual(359.0, angle.normalize(-1.0, 0, 360))

    def testNormalize90(self):
        self.assertAlmostEqual(0.0, angle.normalize(0.0, -90, 90))
        self.assertAlmostEqual(90.0, angle.normalize(90.0, -90, 90))
        self.assertAlmostEqual(90.0, angle.normalize(-90.0, -90, 90))
        self.assertAlmostEqual(-89.0, angle.normalize(91.0, -90, 90))

    def testParseDegrees(self):
        self.assertEqual(360, angle.parseDegrees('360d0.0'))
        self.assertEqual(360, angle.parseDegrees('360d1.0'))
        self.assertEqual(720, angle.parseDegrees('720d0.0'))

    def testParseMinutes(self):
        self.assertAlmostEqual(0.0, angle.parseMinutes('360d0.0'))
        self.assertAlmostEqual(0.5, angle.parseMinutes('360d30.0'))
        self.assertAlmostEqual(1.0, angle.parseMinutes('360d60.0'))
        self.assertAlmostEqual(1.5, angle.parseMinutes('360d90.0'))
