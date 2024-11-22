import matplotlib.pyplot as plt
import pickle
from AI import NeuralNetwork
from random import randint, shuffle, random
from Imagedecoder import genbear
from train import Trainer, multitrain
from InputInterface import EndTraining
from settings import settings as s1 # type: ignore
from settings import settings2 as s2 #type: ignore

def assertcorrectinput():
    for i in targets:
        assert len(i) == outputcount
    for i in inputs:
        assert len(i) == inputcount
        
def load(name="AI.txt"):
    return pickle.load(open(name,"rb"))

def printlengths(targets):
    print('Length:', len(targets))
    suum = 0
    for i in targets:
        if i[0] == lowerval:
            suum += 1
    print('Zeroes:',suum)

#################
####SETTINGS#####
#################

inputcount = 2
outputcount = 1
neuroncounts = [inputcount,30,30,30,30,30,outputcount]
acfunction = 'tanh'
lowerval = -1

roundsperprint = 100
updatetime = 100
testpercent = 5
batchsize = 200

weightlearningrate = 1
biaslearningrate = 0.001

def genring(datanumber, lowerval=lowerval):
    inputs = []
    targets = []
    for _ in range(datanumber):
        x, y = random(), random()
        boolean = (x-0.5)**2+(y-0.5)**2 < 0.2 and 2*(x-0.5)**2+(y-0.5)**2 > 0.05
        currenttarget = int(boolean)
        if lowerval == -1:
            currenttarget = currenttarget*2-1
        inputs.append([x,y])
        targets.append([currenttarget])
    return inputs, targets

def plotinputs(inputs, targets):
    if len(inputs[0]) == 2 and len(targets[0]) == 1:
        toplot1 = []
        toplot2 = []
        for i in range(len(inputs)):
            if targets[i][0] > 0:
                toplot1.append(inputs[i])
            else:
                toplot2.append(inputs[i])
        plt.scatter([i[0] for i in toplot1], [i[1] for i in toplot1])
        plt.scatter([i[0] for i in toplot2], [i[1] for i in toplot2])
        plt.show()

inputs, targets = genbear(100003, lowerval)#getbear(lowerval=lowerval)
assertcorrectinput()

args = [s1['roundsperprint'], s1['updatetime'], s1['testpercent'], s1['batchsize'], s1['descentfactor']]
arg2 = [s2['roundsperprint'], s2['updatetime'], s2['testpercent'], s2['batchsize'], s2['descentfactor']]


if __name__ == '__main__':
    plotinputs(inputs,targets)
    printlengths(targets)

    dual = 'n' not in input("Dual train? ")
    if not dual:
        if 'y' in input("Load last result?"):
            print('loading... (probably broken)')
            net = load()
        else:  
            net = NeuralNetwork(neuroncounts, weightlearningrate, biaslearningrate, acfunction)
        trainer = Trainer(net, inputs, targets, args)
        try:
            trainer.train()
        except (KeyboardInterrupt, EndTraining):
            print("Exiting")
            trainer.save()
            quit()


    if dual:
        net1 = NeuralNetwork(s1['neuroncounts'], s1['weightlearningrate'], s1['biaslearningrate'], s1['acfunction'])
        net2 = NeuralNetwork(s2['neuroncounts'], s2['weightlearningrate'], s2['biaslearningrate'], s2['acfunction'])
        trainer1 = Trainer(net1, inputs, targets, args)
        trainer2 = Trainer(net2, inputs, targets, arg2)

        while True:
            try:
                multitrain(trainer1, trainer2)
            except (KeyboardInterrupt, EndTraining):
                print("Exiting")
                trainer1.save()
                quit()









