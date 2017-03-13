import softwareprocess.angle as angle

def adjust(values):
    if not 'observation' in values:
        values['error'] = 'mandatory information is missing'
        return values
    observation = angle.parse(values['observation'])
    # FIX this is inefficient, but easy for now
    if observation < angle.parse('0d0.1'):
        values['error'] = 'observation is below 0d0.1'
        return values
    return values
