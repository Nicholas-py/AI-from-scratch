import cProfile as profile
from AIinterface import trainer,net 
from train import runbackprop
from ActivationFunctions import HypTan, HypTanFast
from timeit import Timer
import numpy as np

def timeacfunction(activationfunction):
    f1 = lambda x:(lambda : x(np.array([1.3,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,-1.1])))

    c = Timer(f1(activationfunction))
    print('Time:      ',c.timeit(number=10000))


timeacfunction(HypTan)
timeacfunction(HypTanFast)

def backpropspeedtest():
    inp = np.array([0.56, 0.23])
    op = np.array([1])
    for i in range(100000):
        runbackprop(net, inp, op)

profile.run('backpropspeedtest()')
input()
profile.run('trainer.train()')


