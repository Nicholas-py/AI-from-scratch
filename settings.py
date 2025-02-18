
settings =  {
'inputcount': 10,
'outputcount': 1,
'neuroncounts': [50]*8,
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 580,
'updatetime': 50,
'testpercent': 5,
'batchsize': 1600,

'weightlearningrate': 0.8,
'biaslearningrate': 0.0001,
'descentfactor':0.999999  #The closer to 1, the slower the descent (if greater than one learnrate increases)
}

settings['neuroncounts'].append(settings['outputcount'])
settings['neuroncounts'] = [settings['inputcount']]+settings['neuroncounts']


settings2 = {
'inputcount': 10,
'outputcount': 1,
'neuroncounts': [50]*8,
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 580,
'updatetime': 50,
'testpercent': 5,
'batchsize': 3200,

'weightlearningrate': 1.2,
'biaslearningrate': 0.0001,
'descentfactor':0.9999  #The closer to 1, the slower the descent (if greater than one learnrate increases)
}

settings2['neuroncounts'].append(settings2['outputcount'])
settings2['neuroncounts'] = [settings2['inputcount']]+settings2['neuroncounts']