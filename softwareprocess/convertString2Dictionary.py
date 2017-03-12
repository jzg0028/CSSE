"""
    Jesse 2/2/17
    Jesse 2/5/17
"""

import urllib
import re
from collections import Counter

def convertString2Dictionary(inputString = ''):
    inputString = urllib.unquote(inputString)
    # if the string is valid
    if re.compile(r'\s*[a-zA-Z]\w*\s*=\s*\w+\s*'
        r'(?:,\s*[a-zA-Z]\w*\s*=\s*\w+\s*)*$').match(inputString):
        # find all key/value pairs
        o = re.compile(r'([a-zA-Z]\w*)\s*=\s*(\w+)').findall(inputString)
        # if there are no duplicates
        if all(count == 1 for _, count
            in Counter(key for key, _ in o).iteritems()):
            # return a dictionary
            return dict(o)
    # return the error
    return {'error' : 'true'}
