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

weightlearningrate = 0.6
biaslearningrate = 0

inputs = []#aiinputs#[]#[[0,0],[0,1],[1,0],[1,1],[1,1], [0.5,0.5]]*100
targets = []#aioutputs# [[-1],[1],[1],[-1],[-1]]*100

for i in range(10003):
    x, y = random(), random()
    boolean = (x-0.5)**2+(y-0.5)**2 < 0.2
    currenttarget = int(boolean)*2-1
    inputs.append([x,y])
    targets.append([currenttarget])

def plotinputs(inputs, targets):
    if len(inputs[0]) == 2 and len(targets[0]) == 1:
        toplot = []
        for i in range(len(inputs)):
            if targets[i][0] > 0:
                toplot.append(inputs[i])
        plt.scatter([i[0] for i in toplot], [i[1] for i in toplot])
        plt.show(block=False)

assertcorrectinput()
plotinputs(inputs,targets)
tally = 0
error = 0

if __name__ == '__main__' and 'y' in input("Load last result?"):
    net = load()
else:  
    net = NeuralNetwork(neuroncounts, weightlearningrate, biaslearningrate, acfunction)

if __name__ == '__main__':
    trainer = Trainer(net, inputs, targets)
    trainer.train()



