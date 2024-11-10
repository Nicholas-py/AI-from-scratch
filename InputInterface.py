import matplotlib.pyplot as plt
from Imagedecoder import getimage
import numpy as np
from AI import save

class EndTraining(Exception):
    pass

def plotresults(errorrecords):
    ax = plt.subplot(2,1,1)
    ax.plot(errorrecords)
    ax.set_title("Error over time")
    ax2 = plt.subplot(2,1,2)
    ax2.set_yscale('log')
    ax2.set_title("Error over time (log)")
    ax2.plot(errorrecords)
    plt.show()



def getinputabouttraining(trainer):
    while True:
        ip = input("Input: ")
        if len(ip) == 0:
            return
        if ip[0] == 'p' or ip[0] == 'g':
            trainer.condenseerrorrecords(10000)
            plotresults(trainer.cleanerrorrecords)
        elif ip[0] == 'f':
            print("Input the test inputs: ")
            userinput = list(map(float, input().split(' ')))
            userresults = trainer.network.fire(np.array(userinput))
            print("Your results:", userresults[0])
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
            getimage(trainer.network)
        else:
            return

