from angle import Angle
import math

class AdjustedAltitude(object):

    def __init__(self, observation, height = 0.0, pressure = 1010,
        temperature = 72, horizon = 'natural'):
        self.setObservation(observation)
        self.setHeight(height)
        self.setPressure(pressure)
        self.setTemperature(temperature)
        self.setHorizon(horizon)

    def __float__(self):
        return float(Angle(float(self.observation)
            + self.dip() + self.refraction()).normalize(-90.0, 90.0))

    def __str__(self):
        return str(Angle(float(self)))

    @classmethod
    def dispatch(AdjustedAltitude, values):
        try:
            if 'altitude' in values:
                raise ValueError('key "altitude" can\'t be present')
            values['altitude'] = str(
                AdjustedAltitude (
                    Angle.parse(values['observation']),
                    float(0.0 if not 'height' in values
                        else values['height']),
                    int(1010 if not 'pressure' in values
                        else values['pressure']),
                    int(72 if not 'temperature' in values
                        else values['temperature']),
                    ('natural' if not 'horizon' in values
                        else values['horizon'])
                )
            )
        except Exception as e:
            values['error'] = str(e)
        return values

    def setObservation(self, observation):
        if float(observation) > 90.0 or float(observation) < 0.001666666667 \
            or observation.getMinutes() > 60.0 \
            or observation.getMinutes() < 0:
            raise ValueError('observation out of bounds: %s'
                % str(observation))
        self.observation = observation

    def setHeight(self, height):
        if height < 0.0:
            raise ValueError('height is negative: %f' % height)
        self.height = height

    def setPressure(self, pressure):
        if pressure > 1100 or pressure < 100:
            raise ValueError('pressure out of bounds: %d' % pressure)
        self.pressure = pressure

    def setTemperature(self, temperature):
        if temperature > 120 or temperature < -20:
            raise ValueError('temperature out of bounds: %d' % temperature)
        self.temperature = temperature

    def setHorizon(self, horizon):
        horizon = horizon.lower()
        if horizon == 'natural':
            self.horizon = False
        elif horizon == 'artificial':
            self.horizon = True
        else:
            raise ValueError('invalid horizon: %s' % horizon)

    def dip(self):
        return 0.0 if self.horizon \
            else (-0.97 * math.sqrt(self.height)) / 60.0

    def refraction(self):
        return ((-0.00452 * self.pressure)
            / (273 + ((self.temperature - 32) * 5 / 9))
            / math.tan(math.radians(float(self.observation))))
