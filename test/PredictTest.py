import unittest
import prod.predict as predict

class PredictTest(unittest.TestCase):

    def test_bodyMissing(self):
        self.assertTrue('error' in predict.predict({}))

    def test_invalidBodyName(self):
        self.assertTrue('error' in predict.predict({'body' : 'foobar'}))

    def test_invalidBodyName(self):
        self.assertTrue('error' not in predict.predict({'body' : 'Polaris'}))

    def test_invalidDateFormat(self):
        self.assertTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'date' : '20XX-04-01'
            })
        )
        self.assertTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'date' : '2012/04/01'
            })
        )
        self.assertTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'date' : 'foobar'
            })
        )

    def test_invalidTimeFormat(self):
        self.assertTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'time' : 'XX:00:00'
            })
        )
        self.assertTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'time' : '12:30'
            })
        )
        self.assertTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'time' : 'foobar'
            })
        )

    def test_countLeapYears(self):
        self.assertEquals(3, predict.countLeapYears(2001, 2016))
