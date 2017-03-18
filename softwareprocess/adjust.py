import angle
import math

def dip(height, horizon):
    error = 'height' if height < 0.0 \
        else 'horizon' if horizon != 'natural' and horizon != 'artificial' \
        else None
    if error:
        raise ValueError('values out of range: ' + error)
    return 0.0 if horizon == 'artificial' \
        else (-0.97 * math.sqrt(height)) / 60

def refraction(pressure, temperature, observation):
    error = 'pressure' if pressure > 1100 or pressure < 100 \
        else 'temperature' if temperature > 120 or temperature < -20 \
        else 'observation' if observation < angle.parse('0d0.1') \
        or observation > angle.parse('90d0.0') else None
    if error:
        raise ValueError('values out of range: ' + error)
    return ((-0.00452 * pressure)
        / (273 + ((temperature - 32) * 5 / 9))
        / math.tan(math.radians(observation)))

def adjustedAltitude(observation, height, pressure, temperature, horizon):
    return observation \
        + dip(height, horizon) \
        + refraction(pressure, temperature, observation)

def adjust(values):
    try:
        if 'altitude' in values:
            raise ValueError('key "values" can\'t be resent')
        values['altitude'] = angle.toString (
            angle.normalize (
                adjustedAltitude (
                    angle.parse(values['observation']),
                    float(0.0 if not 'height' in values
                        else values['height']),
                    int(1010 if not 'pressure' in values
                        else values['pressure']),
                    int(72 if not 'temperature' in values
                        else values['temperature']),
                    ('natural' if not 'horizon' in values
                        else values['horizon'].lower())
                ), -90, 90
            )
        )
    except Exception as e:
        values['error'] = str(e)
    return values
