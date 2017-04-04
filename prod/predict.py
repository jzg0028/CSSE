from stars import stars
from datetime import datetime

def predict(values):
    if 'body' not in values:
        error = 'body not present'
    elif values['body'] not in (i[0] for i in stars):
        error = 'invalid body'

    try:
        datetime.strptime(values['date'], '%Y-%m-%d')
    except Exception as e:
        error = str(e)
        

    if error:
        values['error'] = error
    return values
