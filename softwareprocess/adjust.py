import softwareprocess.angle as angle

def adjust(values):
    if not 'observation' in values:
        values['error'] = 'mandatory information is missing'
        return values
    observation = angle.parse(values['observation'])
    if not observation or observation < 0.00168:
        values['error'] = 'invalid observation'
        return values
    return values
