import unittest
import softwareprocess.adjust as adjust

class AngleTest(unittest.TestCase):

    def test_observationMissingError(self):
        self.assertTrue('error' in adjust.adjust({}))

    def test_observationPresentNotError(self):
        self.assertTrue(not 'error' in adjust.adjust({'observation' : '5d0.0'}))

    def test_observationLowBoundError(self):
        self.assertTrue('error' in adjust.adjust({'observation' : '0d0.0'}))

    def test_observationFormatError(self):
        self.assertTrue('error' in adjust.adjust({'observation' : '0d0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '0d.0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '0d0.'}))
        self.assertTrue('error' in adjust.adjust({'observation' : 'd0.0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '0y0.0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '00.0'}))
