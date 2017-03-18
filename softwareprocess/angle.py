import re

def toString(angle):
    return '%dd%.1f' % (int(angle), (angle % 1) * 60)

def parse(angle):
    match = re.match('^(\d{1,3})d(\d{1,2}\.\d)$', angle)
    if not match:
        raise ValueError('invalid angle string format: ' + angle)
    return int(match.group(1)) + float(match.group(2)) / 60

def normalize(angle, low, high):
    total = abs(low) + abs(high)
    while(angle <= low):
        angle += total
    while(angle > high):
        angle -= total
    return angle
