from AI import NeuralNetwork, save
from InputInterface import getinputabouttraining, EndTraining
from TrainingGradientsHolder import TrainingGradientsHolder
from random import random, randint


def runbackprop(net, networkinput, networktarget):
    result, savedputs = net.fire(networkinput)
    error = NeuralNetwork.error(networktarget, result)
    weightgradients, biasgradients = net.backprop(result, savedputs, networktarget)
    return weightgradients, biasgradients, error


class Trainer:
    roundsperprint = 1000
    updatetime = 100
    testpercent = 95
    batchsize = 200
    


    def __init__(self, net, inputs, targets, otherargs):
        self.network = net
        
        package = self.splittraintest(inputs, targets)
        self.traininputs, self.traintargets = package[0], package[1]
        self.testinputs, self.testtargets = package[2], package[3]

        self.errorrecords = []
        self.lasterror = 100
        self.cleanerrorrecords = []
        self.randtodisplay = randint(0, len(self.testinputs)-1)

        self.learnratefunction = self.descendinglearnrate

        self.roundsperprint = otherargs[0]
        self.updatetime = otherargs[1]
        self.testpercent = otherargs[2]
        self.batchsize = otherargs[3]


    def errortiedlearnrate(self,lr):
        factor = 10
        min(lr*factor,factor,self.lasterror)/factor

    def descendinglearnrate(self,lr):
        return max(0.000, lr*0.99999)
    
    def splittraintest(self, inputs, targets):
        tally = 0
        trainputs, traingets, testputs, testgets = [],[],[],[]
        for i in range(len(inputs)):
            tally += self.testpercent

            if tally > 100:
                tally = tally - 100
                testputs.append(inputs[i])
                testgets.append(targets[i])
            else:
                trainputs.append(inputs[i])
                traingets.append(targets[i])

        return trainputs, traingets, testputs, testgets


    def log(self):
        print("Training Error:", self.lasterror)
        print("Test Error: ", self.test())
        print("Learning rate: ", self.network.weightlearnrate)
        print("Sample Input:", self.testinputs[self.randtodisplay])
        print("Sample Target: ", self.testtargets[self.randtodisplay])
        print('Sample Result:', self.network.fire(self.testinputs[self.randtodisplay])[0])

    def condenseerrorrecords(self, amount = 1000):
        newputs = []
        for i in range(len(self.errorrecords)//amount):
            sublist = self.errorrecords[i*amount:(i+1)*amount+1]
            average = sum(sublist)/len(sublist)
            newputs.append(average)
        self.cleanerrorrecords = newputs

    def checktoprint(self,i):
        if (i+1)%self.updatetime == 0:
            print(str(int(100*i/self.roundsperprint))+"% done")

    def getresults(self):
        dataindex = int(random()* (len(self.traininputs)-1))
        results = runbackprop(self.network, self.traininputs[dataindex], self.traintargets[dataindex])
        return results


    def trainstep(self):
        for i in range(self.roundsperprint):
            self.checktoprint(i)

            trainholder = TrainingGradientsHolder(self)
            for i in range(self.batchsize):
                results = self.getresults()
                trainholder.addtrainresults(results)
            
            weightgrads, biasgrads = trainholder.returntotals()

            self.network.gradientdescent(weightgrads, biasgrads)

            self.updatelearnrate()
        self.calclasterror()

        


    def train(self):
        while True:

            getinputabouttraining(self)
            self.trainstep()
            self.log()

    

    def updatelearnrate(self):
        self.network.weightlearnrate = self.learnratefunction(self.network.weightlearnrate)
        self.network.biaslearnrate = self.learnratefunction(self.network.biaslearnrate)



    def test(self):
        error = 0
        for i in range(len(self.testinputs)):
            result = self.network.fire(self.testinputs[i])[0]
            error += NeuralNetwork.error(self.testtargets[i], result)
        return error/len(self.testinputs)
    

    def calclasterror(self):
        self.lasterror = sum(self.errorrecords[-self.roundsperprint*self.batchsize:])/self.roundsperprint/self.batchsize

    def save(self):
        save(self.network)




def multitrain(trainer1, trainer2):
    getinputabouttraining(trainer1, trainer2)
    print('\nNetwork 1\n')
    trainer1.trainstep()
    trainer1.log()
    print('\nNetwork 2\n')
    trainer2.trainstep()
    trainer2.log()




    


        
