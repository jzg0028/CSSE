import unittest
import softwareprocess.adjust as adjust

class AngleTest(unittest.TestCase):

    def test_invalid_observationMissing(self):
        self.assertTrue('error' in adjust.adjust({}))

    def test_valid_observationPresent(self):
        self.assertTrue(not 'error' in adjust.adjust({'observation' : '0d0.0'}))
