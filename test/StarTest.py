import unittest
from prod.stars import Star

class StarTest(unittest.TestCase):

    def test(self):
        star = Star('Alnair')
        self.assertEquals('27d42.0', star.getSHA())
        self.assertEquals('-46d53.1', star.getDeclination())
