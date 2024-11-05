import numpy as np
import matplotlib.pyplot as plt
from ActivationFunctions import getfunction
import pickle

def save(network, name="AI.txt"):
    pickle.dump(network,open(name,"wb+"))


class NeuralNetwork:

    def __init__(self, neuroncounts, weightlearningrate = 0.05,biaslearningrate=0.05, activationfunction = "tanh"):
        self.neuroncounts = np.array(neuroncounts) #first row is inputs, last is outputs
        self.biases = self.generatebiases()
        self.weights = self.generateweights()
        self.activationfunction = getfunction(activationfunction)

        self.weightlearnrate = weightlearningrate
        self.biaslearnrate = biaslearningrate

    def generateweights(self):
        weights = []
        for i in range(len(self.neuroncounts)-1):
            nextweights = (np.random.random((self.neuroncounts[i],self.neuroncounts[i+1])))/self.neuroncounts[i]
            weights.append(nextweights)
        return weights
    
    def generatebiases(self):
        biases = []
        for i in range(1,len(self.neuroncounts)):
            biases.append(np.zeros(self.neuroncounts[i]))
        return biases

    def error(target, returned):
        return (1/2*(target-returned)**2).sum()

    def derivativeerror(target, returned):
        return returned-target

    def fire(self, inputs):
        savedputs = [np.array(inputs)]
        lastoutput = np.array(inputs)
        for layer in range(len(self.neuroncounts)-1):
            #print(self.weights[layer], lastoutput)
            lastoutput = np.matmul(lastoutput, self.weights[layer]) +self.biases[layer]
            lastoutput = self.activationfunction(lastoutput)
            savedputs.append(lastoutput)
        return lastoutput, savedputs

    def backprop(self,myoutput, savedputs, mytarget, loud=False):

        #Error function derivative calculation
        derror = NeuralNetwork.derivativeerror(mytarget, myoutput) 
        if loud:
            print("Input:", savedputs[0])
            print("Target: ", mytarget)
            print("Output:", myoutput)
            print("Derivative of error with respect to outputs:", derror)

        #Set things to the proper dimensions
        derror = derror[:, np.newaxis]
        neuronoutputs = []
        for i in savedputs:
            neuronoutputs.append(i[np.newaxis, :]) 

        dweights = []
        dbias = []

        #Calculate the error side of each layer
        for i in range(len(self.neuroncounts)-2,-1,-1):
            derror = derror[:,0]* self.activationfunction.derivative(self.activationfunction.inverse(neuronoutputs[i+1][0]))
            dbias.append(derror)

            derror = derror[:, np.newaxis]

            dweights.append(np.matmul(derror, neuronoutputs[i]))

            derror = np.matmul(self.weights[i], derror)

        dbias2 = dbias[::-1]
        dweights2 = []
        for i in range(len(dweights)-1,-1,-1):
            dweights2.append(np.transpose(dweights[i]))
        if loud:
            print("Gradients:")
            [print(i) for i in dweights2]
        return dweights2, dbias2
    
    def gradientdescent(self, gradients, biases):
        for i in range(len(self.weights)):
            self.weights[i] -= self.weightlearnrate * gradients[i]
            self.biases[i] -= self.biaslearnrate * biases[i]



NN = NeuralNetwork

    


