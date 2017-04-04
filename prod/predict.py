def predict(values):
    if not 'body' in values:
        values['error'] = 'body not present'
    return values
