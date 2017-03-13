import softwareprocess.angle as angle

def adjust(values):
    if not 'observation' in values:
        values['error'] = 'mandatory information is missing'
        return values
    observation = angle.parse(values['observation'])
    if not observation or observation < angle.parse('0d0.1') \
        or observation > angle.parse('90d0.0'):

        values['error'] = 'invalid observation'
        return values
    return values