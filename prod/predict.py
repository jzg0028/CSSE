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
