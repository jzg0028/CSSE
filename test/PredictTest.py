import unittest
from prod.predict import Prediction
from prod.angle import Angle
import sys

class PredictTest(unittest.TestCase):

    def test_invalidBodyName(self):
        try:
            Prediction('foobar')
            self.fail('invalid body, but didn\'t raise exception')
        except ValueError:
            sys.exc_clear()

    def test_invalidBodyName(self):
        try:
            Prediction('Polaris')
        except ValueError:
            self.fail('valid body, but raised exception')
            sys.exc_clear()

    def test_invalidDateFormat(self):
        for i in ('20XX-30-30', 'foobar', '2013/03/04', '2000-01-01'):
            try:
                Prediction('Polaris', date = i)
                self.fail('invalid date %s, but didn\'t raise exception' % i)
            except ValueError:
                sys.exc_clear()

    def test_invalidTimeFormat(self):
        for i in ('XX:00:12', '25:00:00', 'foobar', '12:30'):
            try:
                Prediction('Polaris', time = i)
                self.fail('invalid time %s, but didn\'t raise exception' % i)
            except ValueError:
                sys.exc_clear()

    def test_cumulativeProgression(self):
        self.assertEquals('-3d34.8',
            str(Angle(Prediction('Betelgeuse',
            '2016-01-17', '03:15:42')
            .cumulativeProgression())))

    def test_leapProgression(self):
        self.assertEquals('2d56.9',
            str(Angle(Prediction('Betelgeuse',
            '2016-01-17', '03:15:42')
            .leapProgression())))

    def test_ariesGHA(self):
        self.assertEquals('164d54.5',
        str(Angle(Prediction('Betelgeuse',
        '2016-01-17', '03:15:42')
        .ariesGHA())))

    def test_starGHA(self):
        self.assertEquals('75d53.6',
        str(Prediction('Betelgeuse',
        '2016-01-17', '03:15:42')
        .starGHA()))

    def test_nominal0(self):
        self.assertEquals (
            '75d53.6',
            Prediction.dispatch ({
                'body' : 'betelgeuse',
                'date' : '2016-01-17',
                'time' : '03:15:42'
            })['long']
        )
