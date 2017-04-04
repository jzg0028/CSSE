from stars import stars
from datetime import datetime

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

def aries(date, time):
    observation = None
    try:
        observation.strptime(date + ' ' + time, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise ValueError('bad date or time format: ' + e)
    reference = datetime(2001, 1, 1)

def countLeapYears(fromYear, toYear):
    out = 0
    for year in xrange(fromYear, toYear):
        out += 1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) \
            else 0
    return out
