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

    def ariesGHA(self):
        return float(Angle(float(self.refGHA) + self.cumulativeProgression() \
            + self.leapProgression() + self.rotationAngle())
            .normalize(0.0, 360.0))

    def rotationAngle(self):
        return (self.obsDate - datetime(self.obsDate.year,
            self.obsDate.month, 1)).total_seconds() \
            / 86164.1 * 360.0

    def starGHA(self):
        return Angle(float(Angle(self.ariesGHA() + float(self.star.getSHA()))
            .normalize(0.0, 360.0)))

    def starDeclination(self):
        return self.star.getDeclination()

    @classmethod
    def dispatch(Prediction, values):
        try:
            if 'long' in values or 'lat' in values:
                raise ValueError('key "long" or "lat" can\'t be present')
            prediction = Prediction (
                values['body'],
                ('2001-01-01' if 'date' not in values
                    else values['date']),
                ('00:00:00' if 'time' not in values
                    else values['time'])
            )
            values['long'], values['lat'] = str(prediction.starGHA()), \
                str(prediction.starDeclination())
        except Exception as e:
            values['error'] = str(e)
        return values
