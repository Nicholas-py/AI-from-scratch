from math import tanh, atanh, exp, log
import numpy as np

class ArgFunction:
    def __init__(self, function):
        self.function = function
    
    def __call__(self, inp):
        try:
            return np.array([self.function(i) for i in inp])
        except TypeError:
            return self.function(inp)
        except ValueError:
            print(inp)

class ActivationFunction:
    def __init__(self, function, derivative, inverse):
        self.function = ArgFunction(function)
        self.derivative = ArgFunction(derivative)
        self.inverse = ArgFunction(inverse)
    
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

diction = {'relu':ReLU, 'leakyrelu':LeakyReLU, 'sigmoid':Sigmoid, 'tanh':HypTan}

def getfunction(string):
    try:
        return diction[string.lower()]
    except KeyError:
        print("Warning - invalid function. Defaulting to ReLU")
        return ReLU