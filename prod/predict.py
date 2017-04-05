from stars import Star
from datetime import datetime
from angle import Angle

class Prediction(object):

    def __init__(self, body, date = '2001-01-01', time = '00:00:00'):
        self.setBody(body)
        self.setReferenceDateTime('2001-01-01', '00:00:00')
        self.setObservationDateTime(date, time)
        self.refGHA = Angle.parse('100d42.6')

    def setBody(self, body):
       self.star = Star(body) 

    def setObservationDateTime(self, date, time):
        obsDate = datetime.strptime(date + ' ' + time,
            '%Y-%m-%d %H:%M:%S')
        if hasattr(self, 'refDate') and obsDate < self.refDate:
            raise ValueError('observation date > reference date')
        self.obsDate = obsDate

    def setReferenceDateTime(self, date, time):
        refDate = datetime.strptime(date + ' ' + time,
            '%Y-%m-%d %H:%M:%S')
        if hasattr(self, 'obsDate') and self.obsDate < refDate:
            raise ValueError('observation date > reference date')
        self.refDate = refDate

    def cumulativeProgression(self):
        return (self.obsDate.year - self.refDate.year) \
            * float(Angle.parse('-0d14.31667'))

    def leapProgression(self):
        leap = 0
        for i in xrange(self.refDate.year, self.obsDate.year):
            leap += 1 if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) else 0
        return 0.9829167 * leap

    def predictedGHA(self):
        return float(self.refGHA) + self.cumulativeProgression() \
            + self.leapProgression()

    def secondDifference(self):
        return (self.obsDate - datetime(self.obsDate.year,
            self.obsDate.month, 1)).total_seconds()
