
settings = {
'inputcount': 9,
'outputcount': 9,
'neuroncounts': [10]*4,
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 58,
'updatetime': 100,
'testpercent': 0,
'batchsize': 500,

'weightlearningrate': 1,
'biaslearningrate': 0.001,
'descentfactor':0.99996  #The closer to 1, the slower the descent (if greater than one learnrate increases)
}

settings['neuroncounts'].append(settings['outputcount'])
settings['neuroncounts'] = [settings['inputcount']]+settings['neuroncounts']


settings2 = {
'inputcount': 9,
'outputcount': 9,
'neuroncounts': [10]*4,
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 580,
'updatetime': 100,
'testpercent': 5,
'batchsize': 500,

'weightlearningrate': 1,
'biaslearningrate': 0.001,
'descentfactor':0.99996  #The closer to 1, the slower the descent (if greater than one learnrate increases)
}

settings2['neuroncounts'].append(settings2['outputcount'])
settings2['neuroncounts'] = [settings2['inputcount']]+settings2['neuroncounts']