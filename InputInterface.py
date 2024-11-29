import matplotlib.pyplot as plt
from Imagedecoder import getimage
import numpy as np
from AI import save
import random
from tictactoe import playagainst, networkplayagainst

class EndTraining(Exception):
    pass


def interact(network):
    if network.neuroncounts[0] == 2 and network.neuroncounts[-1] == 1:
        getimage(network)
    if network.neuroncounts[0] == 9 and network.neuroncounts[-1] == 9:
        print(playagainst(networkplayagainst(network), -1))



def plotresults(errorrecords, ax2 = 1, max2 = 1):
    ax = plt.subplot(2,1,1)
    ax.plot(errorrecords)
    ax.set_title("Error over time")
    ax2 = plt.subplot(2,1,2)
    ax2.set_yscale('log')
    ax2.set_title("Error over time (log)")
    ax2.plot(errorrecords)



def getinputabouttraining(trainer, trainer2 = None):
    multi = bool(trainer2 is not None)
    while True:
        ip = input("Input: ")
        if len(ip) == 0:
            return
        if ip[0] == 'p' or ip[0] == 'g':
            if not multi:
                trainer.condenseerrorrecords(25)
                plotresults(trainer.cleanerrorrecords)
            if multi:
                trainer.condenseerrorrecords(25)
                trainer2.condenseerrorrecords(25)
                plotresults(trainer.cleanerrorrecords, 1, 2)
                plotresults(trainer2.cleanerrorrecords, 2, 2)
            plt.show()
   
        elif ip[0] == 'f':
            while True:
                try:
                    n = trainer.network
                    if multi and 'y' in input("Switch to network 2? "):
                        n = trainer2.network
                    print("Input the test inputs: ")
                    userinput = list(map(float, input().split(' ')))
                    userresults = n.fire(np.array(userinput))
                    print("Your results:", userresults[0])
                except:
                    break

        elif ip[0] == 't':
            r = random.randint(0, len(trainer.traininputs)-20)
            [print(trainer.traininputs[i], trainer.traintargets[i]) for i in range(r, r+20)]
        elif ip[0] == 'q' or ip[0] == 'x' or ip[0:3] == 'cd ' or ip == "c:":
            save(trainer.network)
            raise EndTraining("Exiting program")
        elif ip[0] == 's':
            save(trainer.network)
        elif ip[0] == 'w':
            print("WEIGHTS:")
            for i in trainer.network.weights:
                print(i)
        elif ip[0] == 'b':
            for i in trainer.network.biases:
                print(i)
        elif ip[0] == 'i':
            interact(trainer.network)
            if multi:
                interact(trainer2.network)
        else:
            return

