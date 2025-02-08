
settings = {
'inputcount': 2,
'outputcount': 1,
'neuroncounts': [30]*4,
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 580,
'updatetime': 50,
'testpercent': 5,
'batchsize': 800,

'weightlearningrate': 0.2,
'biaslearningrate': 0.001,
'descentfactor':0.99999  #The closer to 1, the slower the descent (if greater than one learnrate increases)
}

settings['neuroncounts'].append(settings['outputcount'])
settings['neuroncounts'] = [settings['inputcount']]+settings['neuroncounts']


settings2 = {
'inputcount': 9,
'outputcount': 2,
'neuroncounts': [30]*4,
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 580,
'updatetime': 50,
'testpercent': 0.1,
'batchsize': 800,

'weightlearningrate': 0.2,
'biaslearningrate': 0.001,
'descentfactor':0.999999  #The closer to 1, the slower the descent (if greater than one learnrate increases)
}

settings2['neuroncounts'].append(settings2['outputcount'])
settings2['neuroncounts'] = [settings2['inputcount']]+settings2['neuroncounts']