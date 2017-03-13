def adjust(values):
    if not 'observation' in values:
        values['error'] = 'mandatory information is missing'
    return values
