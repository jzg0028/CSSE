import softwareprocess.angle as angle
import math

def dip(height):
    return (-0.97 * math.sqrt(height)) / 60

def refraction(pressure, temperature, observation):
    return ((-0.00452 * pressure)
        / (273 + ((temperature - 32) * 5 / 9))
        / math.tan(math.radians(observation)))

def adjust(values):

    if 'altitude' in values:
        values['error'] = 'key "values" can\'t be present'
        return values

    if not 'observation' in values:
        values['error'] = 'mandatory information is missing'
        return values

    observation = angle.parse(values['observation'])
    if not observation or observation < angle.parse('0d0.1') \
        or observation > angle.parse('90d0.0'):

        values['error'] = 'invalid observation'
        return values

    try:
        height = 0.0 if not 'height' in values else float(values['height'])
    except:
        values['error'] = 'height value error'
        return values
    if height < 0:
        values['error'] = 'height out of range'
        return values

    try:
        temperature = 72 if not 'temperature' in values \
            else int(values['temperature'])
    except:
        values['error'] = 'temperature value error'
        return values
    if temperature > 120 or temperature < -20:
        values['error'] = 'temperature out of range'
        return values

    try:
        pressure = 1010 if not 'pressure' in values \
            else int(values['pressure'])
    except:
        values['error'] = 'pressure value error'
        return values
    if pressure > 1100 or pressure < 100:
        values['error'] = 'pressure out of range'
        return values

    horizon = 'natural' if not 'horizon' in values \
        else values['horizon'].lower()
    if horizon != 'natural' and horizon != 'artificial':
        values['error'] = 'invalid horizon'
        return values

    values['altitude'] = angle.toString(observation
        + (dip(height) if horizon == 'natural' else 0)
        + refraction(pressure, temperature, observation))

    return values
