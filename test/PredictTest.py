import unittest
import prod.predict as predict

class PredictTest(unittest.TestCase):

    def test_bodyMissing(self):
        self.assertTrue('error' in predict.predict({}))

    def test_invalidBodyName(self):
        self.assertTrue('error' in predict.predict({'body' : 'foobar'}))

    def test_invalidBodyName(self):
        self.assertTrue('error' not in predict.predict({'body' : 'Polaris'}))
