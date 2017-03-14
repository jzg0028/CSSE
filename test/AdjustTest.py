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

    def test_temperatureValueError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'temperature' : '12.5'}))

    def test_pressureHighBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'pressure' : '1101'}))

    def test_pressureLowBoundError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'pressure' : '99'}))

    def test_pressureValueError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'pressure' : '12.5'}))

    def test_horizonArtificialLowCaseNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'artificial'}))

    def test_horizonArtificialUpCaseNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'ARTIFICIAL'}))

    def test_horizonArtificialMixCaseNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'ArTiFiCiAl'}))

    def test_horizonNaturalLowCaseNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'natural'}))

    def test_horizonNaturalUpCaseNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'NATURAL'}))

    def test_horizonNaturalMixCaseNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'nAtUrAl'}))

    def test_horizonValueError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'horizon' : 'foobar'}))

    def test_extraKeyNoError(self):
        self.assertTrue(not 'error' in adjust.adjust(
            {'observation' : '0d0.1', 'foo' : 'bar'}))
        self.assertTrue('foo' in adjust.adjust(
            {'observation' : '0d0.1', 'foo' : 'bar'}))

    def test_altitudePresentError(self):
        self.assertTrue('error' in adjust.adjust(
            {'observation' : '0d0.1', 'altitude' : '0d0.0'}))

    def test_defaultResultPresent(self):
        self.assertTrue('altitude' in adjust.adjust(
            {'observation' : '42d0.0'}))

    def test_defaultResultValue(self):
        self.assertEqual('41d59.0',
            adjust.adjust({'observation' : '42d0.0'})['altitude'])

    def test_nominalArtificialValue(self):
        self.assertEqual('29d59.9', adjust.adjust (
                {'observation' : '30d1.5',
                'height' : '19',
                'pressure' : '1000',
                'temperature' : '85',
                'horizon' : 'artificial' })['altitude'])
