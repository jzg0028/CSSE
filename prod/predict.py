from stars import stars

def predict(values):
    if 'body' not in values:
        values['error'] = 'body not present'
    elif values['body'] not in (i[0] for i in stars):
        values['error'] = 'invalid body'
    return values
