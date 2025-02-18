from TrainingGradientsHolder import TrainingGradientsHolder
from AI import NeuralNetwork, save
from train import Trainer
from InputInterface import getinputabouttraining

from abc import ABC, abstractmethod

@ABC
class Game:
    
    def __init__(self):
        self.board = self.getstartboard()

    @abstractmethod
    def getstartboard(self):
        pass

    @abstractmethod
    def getboardstate(self):
        return self.board
    
    @abstractmethod
    def iswon(self):
        pass

    @abstractmethod
    def aioutputtomove(self, aioutput):
        pass

    @abstractmethod
    def movetoaioutput(self, move):
        pass

    @abstractmethod
    def updategamestate(self, move):
        pass


def playgameagainst(game, func1, func2):
    pass


class GameTrainer (Trainer):
    def __init__(self, net, game, otherargs):
        self.network = net
        
        self.errorrecords = []
        self.lasterror = 100
        self.cleanerrorrecords = []

        self.roundsperprint = otherargs[0]
        self.updatetime = otherargs[1]
        self.testpercent = otherargs[2]
        self.batchsize = otherargs[3]
        self.descentfactor = otherargs[4]
        
        self.game = game


    def trainstep(self, multi=False):
            if not multi:
                getinputabouttraining(self)
            for i in range(self.roundsperprint):
                self.checktoprint(i)


                trainholder = TrainingGradientsHolder()
                for j in range(self.batchsize):
                    inputs, outputs, targets = self.playagainstself()
                    for r in range(len(inputs)):
                        weightgrads, biasgrads = self.network.backprop(outputs[r][0],outputs[r][1],targets[r])
                        trainholder.addtrainresults((weightgrads, biasgrads))
                    
                totalw, totalb = trainholder.returntotals()
                self.network.gradientdescent(totalw, totalb)
            self.log()

    def playagainstself(self):
        currentgame = self.game()
        moves = [[],[]]
        states = []
        currentturn = 1
        tally = 0
        while True:
            tally += 1
            currentturn = (currentturn + 1)%2

            states.append(currentgame.getboardstate())

            aioutput = self.network.fire(states[-1])
            moves[currentturn] = aioutput
            currentgame.updategamestate(currentgame.aioutputtomove(aioutput[0]))

            if currentgame.iswon():
                break
        
        inputs = [states[i] for i in range(currentturn,tally, 2)]
        outputs = moves[currentturn]
        targets = []
        for i in inputs:
            move = currentgame.aioutputtomove(i[0])
            targets.append(currentgame.movetoaioutput(move))
        
        return inputs, outputs, targets


    def log(self):
        print("Training round complete!")

    def condenseerrorrecords(self, amount=5):
        return super().condenseerrorrecords(amount)
    
    def calclasterror(self):
        self.lasterror = sum(self.errorrecords[-self.roundsperprint*self.batchsize:])/self.roundsperprint/self.batchsize

    def save(self):
        save(self.network)

a = GameTrainer(1,2,3,[4,3,2,1,0])