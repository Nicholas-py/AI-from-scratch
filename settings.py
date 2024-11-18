
settings = {
'inputcount': 2,
'outputcount': 1,
'neuroncounts': [30,30,30,30,30],
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 1001,
'updatetime': 100,
'testpercent': 5,
'batchsize': 200,

'weightlearningrate': 0.5,
'biaslearningrate': 0.001,
}

settings['neuroncounts'].append(settings['outputcount'])
settings['neuroncounts'] = [settings['inputcount']]+settings['neuroncounts']



settings2 = {
'inputcount': 2,
'outputcount': 1,
'neuroncounts': [30,30,30,30,30],
'acfunction': 'tanh',
'lowerval': -1,

'roundsperprint': 1000,
'updatetime': 100,
'testpercent': 5,
'batchsize': 200,

'weightlearningrate': 1,
'biaslearningrate': 0.001,
}

settings2['neuroncounts'].append(settings2['outputcount'])
settings2['neuroncounts'] = [settings2['inputcount']]+settings2['neuroncounts']