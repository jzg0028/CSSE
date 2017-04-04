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
        self.asserTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'date' : '20XX-04-01'
            })
        )
        self.asserTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'date' : '2012/04/01'
            })
        )
        self.asserTrue (
            'error' in predict.predict ({
                'body' : 'Betelgeuse',
                'date' : 'foobar'
            })
        )
