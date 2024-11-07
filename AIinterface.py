import matplotlib.pyplot as plt
import pickle
from AI import NeuralNetwork
from random import randint, shuffle, random
from Imagedecoder import aiinputs, aioutputs, getimage
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

weightlearningrate = 1
biaslearningrate = 0

inputs = []#aiinputs
targets = []#aioutputs
def genring(datanumber):
    for _ in range(datanumber):
        x, y = random(), random()
        boolean = (x-0.5)**2+(y-0.5)**2 < 0.2 and 2*(x-0.5)**2+(y-0.5)**2 > 0.05
        currenttarget = int(boolean)*2-1
        inputs.append([x,y])
        targets.append([currenttarget])

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
        plt.show(block=False)

genring(100003)
assertcorrectinput()
plotinputs(inputs,targets)

tally = 0
error = 0

if __name__ == '__main__' and 'y' in input("Load last result?"):
    print('loading... (probably broken)')
    net = load()
else:  
    net = NeuralNetwork(neuroncounts, weightlearningrate, biaslearningrate, acfunction)

trainer = Trainer(net, inputs, targets)

if __name__ == '__main__':
    try:
        trainer.train()
    except KeyboardInterrupt:
        trainer.save()
        quit()



