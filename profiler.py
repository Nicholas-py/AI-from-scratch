import cProfile as profile
from AIinterface import trainer
from ActivationFunctions import HypTan as th
from timeit import Timer
import numpy as np

def time(activationfunction):
    f1 = lambda x:(lambda : x(np.array([1.3,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,-1.1])))

    c = Timer(f1(activationfunction))
    print('Time:      ',c.timeit(number=10000))

time(th)
profile.run('trainer.train()')


