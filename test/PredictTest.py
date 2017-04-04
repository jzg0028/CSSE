import unittest
import prod.predict as predict

class PredictTest(unittest.TestCase):

    def test_bodyMissing(self):
        self.assertTrue('error' in predict.predict({}))
