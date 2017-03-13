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

    height = 0 if not 'height' in values else int(values['height'])
    if height < 0:
        values['error'] = 'height out of range'
        return values

    temperature = 72 if not 'temperature' in values \
        else int(values['temperature'])
    if temperature > 120:
        values['error'] = 'temperature out of range'
        return values

    return values
