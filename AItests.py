from AI import *
import numpy as np
from random import randint, random
from ActivationFunctions import *
from AIinterface import acfunction

def testall():
    testgenerateweights()
    testactivation()
    testderivativeactivation()
    testerror()
    testderivativeerror()
    testinverseactivation()
    testgradientdescent()
    testfire()
    testbackprop()
    print('All tests passed')

def testgenerateweights():
    net = NeuralNetwork([1,1,1])
    assert len(net.weights) == 2
    assert net.weights[0].shape == (1,1)
    assert net.weights[1].shape == (1,1)
    
    net = NeuralNetwork([3,16,16,2])
    assert len(net.weights) == 3
    assert np.matmul([1,2,3], net.weights[0]).shape == (16,)
    assert net.weights[2].shape == (16,2)

def testactivation():
    net = NN([2,3,4,5,6],activationfunction='tanh')
    assert type(net.activationfunction) == ActivationFunction
    assert net.activationfunction([2])[0]>net.activationfunction([1])[0]
    l1 = np.array(range(-10,10))/10
    l2 = net.activationfunction(np.array(range(-10,10))/10)
    assert  (l1 != l2).any()


def testderivativeactivation():
    net = NN([2,2], activationfunction=acfunction)
    num = random()*20-10
    val1, val2 = net.activationfunction([num])[0], net.activationfunction([num+0.000001])[0]
    assert round(net.activationfunction.derivative([num])[0],5) == round((val2-val1)/0.000001,5)

def testinverseactivation():
    net = NN([2,2], activationfunction=acfunction)
    for _ in range(100):
        r = random()
        assert round(net.activationfunction(net.activationfunction.inverse([r]))[0], 8) == round(r,8)
        assert round(net.activationfunction.inverse(net.activationfunction([r]))[0], 8) == round(r,8)


def testerror():
    arr = np.random.random(6)
    assert NN.error(arr,arr) == 0
    assert NN.error(arr, arr+1) > 0
    assert NN.error(arr, arr-1) > 0
    arr2 =arr.copy()
    arr2[0] += 1
    assert NN.error(arr, arr2) > 0
    assert NN.error(arr, 2*arr) < NN.error(arr, 4*arr)

def testderivativeerror():
    arr1, arr2 = np.random.random(6), np.random.random(6)
    val1, val2 = NN.error(arr1, arr2), NN.error(arr1, arr2+0.000001)
    assert (round(NN.derivativeerror(arr1, arr2).sum(),4) == round((val2-val1)/0.000001, 4))

def testgradientdescent():
    arr1 = np.array([[1.0,1.0],[1.0,1.0]])
    barray = [np.array([0.0,0.0])]
    net = NN([2,2])
    net.weights = [arr1]
    net2 = NN([2,2])
    net2.weights = [arr1]

    net.gradientdescent(arr1, barray)
    assert net.weights[0][0][0] < 1
    assert net.weights[0][0][0] == net.weights[0][1][0]
    assert net.weights[0][0][0] == net.weights[0][0][1]
    net.gradientdescent([-arr1],barray)
    assert (net.weights[0] == net2.weights[0]).all()

    net.gradientdescent(np.array([[0,1],[0,0]]),barray)
    assert net.weights[0][1][0] != net.weights[0][1][1]

def testfire():
    arr1 = np.array([[0.0],[0.0]])
    net = NN([2,1])
    net.weights = [arr1]
    assert net.fire([randint(-100,100), randint(-100,100)])[0] == [0]

    net2 = NN([1,13,23,99,2])
    assert all(net2.fire([67.32])[0] == net2.fire([67.32])[0])
    assert all(net2.fire([67.32])[1][2] == net2.fire([67.32])[1][2])
    x = [random()*200-100]
    
    assert net2.fire(x)[1][0] == x

def testbackprop():
    for i in range(100):
        net = NN([2,3,2])
        inp = np.random.random(2)*2-1
        manual = manualderivs(net,inp, d=0.0000001)
        backed = net.backprop(net.fire(inp)[0], net.fire(inp)[1], inp)[0][0]
        for i in [[0,0],[0,1],[1,0],[1,1]]:
            try:
                assert round(manual[i[0]][i[1]], 4) == round(backed[i[0]][i[1]],4)
            except AssertionError:
                print("ERROR!")
                print("weights:", net.weights)
                print("Input:", inp)
                print("Calculated derivs:", backed)
                print("Actual derivs:",manual)
                print('Fail on: ',i)
                raise AssertionError("I assert that you asserted assertions")


#Manual backprop for 2x2 networks
def manualderivs(net, inp, d= 0.001):
    res = net.fire(inp)[0]
    e0 = NN.error(inp, res)
    op = [[0,0],[0,0]]
    for i in [[0,0],[0,1],[1,0],[1,1]]:
        net.weights[0][i[0]][i[1]] += d
        res2 = net.fire(inp)[0]
        e2 = NN.error(inp, res2)
        op[i[0]][i[1]] = float(e2-e0)/d
        net.weights[0][i[0]][i[1]] -= d

    return op

NN = NeuralNetwork
testall()