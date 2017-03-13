import unittest
import softwareprocess.adjust as adjust

class AngleTest(unittest.TestCase):

    def test_observationMissingError(self):
        self.assertTrue('error' in adjust.adjust({}))

    def test_observationPresentNotError(self):
        self.assertTrue(not 'error' in adjust.adjust({'observation' : '5d0.0'}))

    def test_observationLowBoundError(self):
        self.assertTrue('error' in adjust.adjust({'observation' : '0d0.0'}))

    def test_observationHighBoundError(self):
        self.assertTrue('error' in adjust.adjust({'observation' : '90d0.1'}))

    def test_observationFormatError(self):
        self.assertTrue('error' in adjust.adjust({'observation' : '0d0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '0d.0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '0d0.'}))
        self.assertTrue('error' in adjust.adjust({'observation' : 'd0.0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '0y0.0'}))
        self.assertTrue('error' in adjust.adjust({'observation' : '00.0'}))

    def test_heightLowBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'height' : '-1'}))

    def test_heightValueError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'height' : '12.5'}))

    def test_temperatureHighBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'temperature' : '121'}))

    def test_temperatureLowBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'temperature' : '-21'}))

    def test_heightValueError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'temperature' : '12.5'}))

    def test_pressureHighBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'pressure' : '1101'}))

    def test_pressureLowBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'pressure' : '99'}))

    def test_heightValueError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'pressure' : '12.5'}))
