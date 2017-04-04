from stars import stars
from datetime import datetime
import angle

def predict(values):
    error = None
    if 'body' not in values:
        error = 'body not present'
    elif values['body'] not in (i[0] for i in stars):
        error = 'invalid body'

    date = '2001-01-01' if 'date' not in values else values['date']
    time = '00:00:00' if 'time' not in values else values['time']

    try:
        datetime.strptime(date + time, '%Y-%m-%d%H:%M:%S')
    except Exception as e:
        error = str(e)
        

    if error:
        values['error'] = error
    return values

def countLeapYears(fromYear, toYear):
    out = 0
    for year in xrange(fromYear, toYear):
        out += 1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) \
            else 0
    return out

def angularDifference(fromYear, toYear):
    return (toYear - fromYear) * angle.parse('0d14.31667') * -1
