import matplotlib.pyplot as plt
import pickle
from AI import NeuralNetwork
from random import randint, shuffle, random
from Imagedecoder import genbear
from train import Trainer

def assertcorrectinput():
    for i in targets:
        assert len(i) == outputcount
    for i in inputs:
        assert len(i) == inputcount
        
def load(name="AI.txt"):
    return pickle.load(open(name,"rb"))



#################
####SETTINGS#####
#################

inputcount = 2
outputcount = 1
neuroncounts = [inputcount,10,10,10,10,10,outputcount]
acfunction = 'tanh'
lowerval = -1

roundsperprint = 1000
updatetime = 100
testpercent = 95
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

args = [roundsperprint, updatetime, testpercent, batchsize]

if __name__ == '__main__' and 'y' in input("Load last result?"):
    print('loading... (probably broken)')
    net = load()
else:  
    net = NeuralNetwork(neuroncounts, weightlearningrate, biaslearningrate, acfunction)

trainer = Trainer(net, inputs, targets, args)

if __name__ == '__main__':
    plotinputs(inputs,targets)
    print('Length:', len(targets))
    suum = 0
    for i in targets:
        if i[0] == lowerval:
            suum += 1
    print('Zeroes:',suum)


    try:
        trainer.train()
    except KeyboardInterrupt:
        trainer.save()
        quit()



