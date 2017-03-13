import unittest
import softwareprocess.angle as angle

class AngleTest(unittest.TestCase):

    def test_valid_toString(self):
        self.assertEqual('0d0.0', angle.toString(0))
        self.assertEqual('0d30.0', angle.toString(0.5))
        self.assertEqual('30d30.0', angle.toString(30.5))
        self.assertEqual('90d0.0', angle.toString(90.0))

    def test_valid_parse(self):
        self.assertAlmostEqual(0.0, angle.parse('0d0.0'))
        self.assertAlmostEqual(0.5, angle.parse('0d30.0'))
        self.assertAlmostEqual(30.5, angle.parse('30d30.0'))
        self.assertAlmostEqual(90.0, angle.parse('90d0.0'))
