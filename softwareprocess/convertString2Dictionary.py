"""
    Jesse 2/2/17
"""

import urllib
import re

def convertString2Dictionary(inputString = ''):
    inputString = urllib.unquote(inputString)
    return (dict(re.compile('([a-zA-Z]\w*)\s*=\s*(\w+)').findall(inputString))
        if re.compile
        ('^\s*[a-zA-Z]\w*\s*=\s*\w+(?:\s*,\s*[a-zA-Z]\w*\s*=\s*\w+)+\s*$')
        .match(inputString)
        else {'error' : 'true'})
