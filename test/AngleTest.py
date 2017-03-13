import unittest
import softwareprocess.angle as angle

class AngleTest(unittest.TestCase):

    def test_valid_toString(self):
        self.assertEqual('0d0.0', angle.toString(0))
        self.assertEqual('0d30.0', angle.toString(0.5))
        self.assertEqual('30d30.0', angle.toString(30.5))
        self.assertEqual('90d0.0', angle.toString(90))
