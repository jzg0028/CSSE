import re

def toString(angle):
    return '%dd%.1f' % (int(angle), (angle % 1) * 60)

def parse(angle):
    return parseDegrees(angle) + parseMinutes(angle)

def parseDegrees(angle):
    return int(capture(angle)[0])

def parseMinutes(angle):
    return float(capture(angle)[1]) / 60

def capture(angle):
    match = re.match('^([-+]?)(\d+)d(\d+\.\d+)$', angle)
    if not match:
        raise ValueError('invalid angle string format: ' + angle)
    return (match.group(1) + match.group(2), match.group(1) + match.group(3));

def normalize(angle, low, high):
    total = abs(low) + abs(high)
    while(angle <= low):
        angle += total
    while(angle > high):
        angle -= total
    return angle
