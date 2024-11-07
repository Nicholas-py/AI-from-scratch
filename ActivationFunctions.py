from math import tanh, atanh, exp, log
import numpy as np

class MultiCallArgFunction:
    def __init__(self, function):
        self.function = function
    
    def __call__(self, inp):
        lst = []
        for i in range(len(inp)):
            lst.append(self.function(inp[i]))
        return np.array(lst)
    
class SingleCallArgFunction:
    def __init__(self,function):
        self.function = function
    def __call__(self,inp):
        return self.function(inp)

class ActivationFunction:
    def __init__(self, function, derivative, inverse):
        self.function = ActivationFunction.savefunction(function)
        self.derivative = ActivationFunction.savefunction(derivative)
        self.inverse = ActivationFunction.savefunction(inverse)
    
    def savefunction(func):
        try:
            func(np.array([0.1,0.2]))
            return SingleCallArgFunction(func)
        except (TypeError, ValueError):
            return MultiCallArgFunction(func)


    def __call__(self, inp):
        return self.function(inp)

def relu(n):
    return max(0,n)
def drelu(n):
    return int(n>0)
def invrelu(n):
    return [-1,n][float(n)>0]
ReLU = ActivationFunction(relu, drelu, invrelu)

def dtanh(n):
    return 1-tanh(n)**2
def invtanh(n):
    if n == 1:
        return 10**10
    elif n == -1:
        return 10**-10
    else:
        return atanh(n)
HypTan = ActivationFunction(tanh, dtanh, invtanh)


def dtanh2(n):
    return 1-np.tanh(n)**2
def invtanh2(n):
    return np.atanh(n)
HypTanFast = ActivationFunction(np.tanh, dtanh2, invtanh2)

def leakyrelu(n):
    return max(n/20,n)
def dleakyrelu(n):
    return [1/20,1][float(n)>0]
def invleakyrelu(n):
    return min(20*n, n)
LeakyReLU = ActivationFunction(leakyrelu, dleakyrelu, invleakyrelu)

def sigmoid(n):
    return 1/(1+exp(-n))
def invsigmoid(n):
    return log(n/(1-n))
def dsigmoid(n):
    return sigmoid(n)*(1-sigmoid(n))
Sigmoid = ActivationFunction(sigmoid, dsigmoid, invsigmoid)

diction = {'relu':ReLU, 'leakyrelu':LeakyReLU, 'sigmoid':Sigmoid, 'tanh':HypTanFast}

def getfunction(string):
    try:
        return diction[string.lower()]
    except KeyError:
        print("Warning - invalid function. Defaulting to ReLU")
        return ReLU