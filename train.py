from AI import NeuralNetwork, save
from InputInterface import getinputabouttraining
from TrainingGradientsHolder import TrainingGradientsHolder
from random import randint


def runbackprop(net, networkinput, networktarget):
    result, savedputs = net.fire(networkinput)
    error = NeuralNetwork.error(networktarget, result)
    weightgradients, biasgradients = net.backprop(result, savedputs, networktarget)
    return weightgradients, biasgradients, error


class Trainer:
    roundsperprint = 340
    updatetime = 100
    testpercent = 10
    batchsize = 200
    


    def __init__(self, net, inputs, targets):
        self.network = net
        
        package = self.splittraintest(inputs, targets)
        self.traininputs = package[0]
        self.traintargets = package[1]
        self.testinputs = package[2]
        self.testtargets = package[3]

        self.errorrecords = []
        self.lasterror = 100
        self.cleanerrorrecords = []
        self.randtodisplay = randint(0, len(self.testinputs)-1)

        self.learnratefunction = self.descendinglearnrate

    def errortiedlearnrate(self,lr):
        factor = 10
        min(lr*factor,factor,self.lasterror)/factor

    def descendinglearnrate(self,lr):
        return max(0.001, lr*0.99995)
    
    def splittraintest(self, inputs, targets):
        tally = 0
        trainputs, traingets, testputs, testgets = [],[],[],[]
        for i in range(len(inputs)):
            tally += Trainer.testpercent

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

    def trainstep(self):
        tally = 0
        for i in range(Trainer.roundsperprint):
            if (i+1)%Trainer.updatetime == 0:
                print(str(int(100*i/Trainer.roundsperprint))+"% done")

            tally += 1
            trainholder = TrainingGradientsHolder(self)
            for i in range(Trainer.batchsize):

                dataindex = randint(0, len(self.traininputs)-1)
                results = runbackprop(self.network, self.traininputs[dataindex], self.traintargets[dataindex])
                trainholder.addtrainresults(results)
            
            weightgrads, biasgrads = trainholder.returntotals()
            self.network.gradientdescent(weightgrads, biasgrads)

            self.updatelearnrate()
        self.calclasterror()
        


    def train(self):
        while True:

            try:
                getinputabouttraining(self)
            except ZeroDivisionError:
                break
            
            self.trainstep()
            self.log()

        save(self.network)
    

    def updatelearnrate(self):
        self.network.weightlearnrate = self.learnratefunction(self.network.weightlearnrate)
        #self.network.biaslearnrate = Trainer.learnratefunction(self.network.biaslearnrate)



    def test(self):
        error = 0
        for i in range(len(self.testinputs)):
            result = self.network.fire(self.testinputs[i])[0]
            error += NeuralNetwork.error(self.testtargets[i], result)
        return error/len(self.testinputs)
    

    def calclasterror(self):
        self.lasterror = sum(self.errorrecords[-Trainer.roundsperprint*Trainer.batchsize:])/Trainer.roundsperprint/Trainer.batchsize

    def save(self):
        save(self.network)








    


        
