import re

def toString(angle):
    return '%dd%.1f' % (int(angle), (angle % 1) * 60)

def parse(angle):
    match = re.match('^(\d{1,3})d(\d{1,2}\.\d)$', angle)

    return int(match.group(1)) + float(match.group(2)) / 60 if match else None
