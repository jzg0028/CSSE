from adjust import AdjustedAltitude
from predict import Prediction
from correct import Correction

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        return AdjustedAltitude.dispatch(values)
    elif(values['op'] == 'predict'):
        return Prediction.dispatch(values)
    elif(values['op'] == 'correct'):
        return Correction.dispatch(values)
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
