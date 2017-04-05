from stars import Star
from datetime import datetime
from angle import Angle

class Prediction(object):

    def __init__(self, body, date = '2001-01-01', time = '00:00:00'):
        self.setBody(body)
        self.setObservationDateTime(date, time)
        self.setReferenceDateTime('2001-01-01', '00:00:00')

    def setBody(self, body):
       self.star = Star(body) 

    def setObservationDateTime(self, date, time):
        self.obsDate = datetime.strptime(date + ' ' + time,
            '%Y-%m-%d %H:%M:%S')

    def setReferenceDateTime(self, date, time):
        self.refDate = datetime.strptime(date + ' ' + time,
            '%Y-%m-%d %H:%M:%S')

    def cumulativeProgression(self):
        return (self.obsDate.year - self.refDate.year) \
            * float(Angle.parse('-0d14.31667'))

    def countLeapYears(self):
        out = 0
        for i in xrange(self.refDate.year, self.obsDate.year):
            out += 1 if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) else 0
        return out

    def leapProgression(self):
        return 0.9829167 * self.countLeapYears()
