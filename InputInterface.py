import matplotlib.pyplot as plt
from Imagedecoder import getimage
import numpy as np
from AI import save
import random
from tictactoe import playagainst, networkplayagainst, networkplayagainst2, midai

class EndTraining(Exception):
    pass


def interact(network):
    if network.neuroncounts[0] == 2 and network.neuroncounts[-1] == 1:
        getimage(network)
    if network.neuroncounts[0] == 9 and network.neuroncounts[-1] == 9:
        print(playagainst(networkplayagainst(network), -1))

    if network.neuroncounts[0] == 9 and network.neuroncounts[-1] == 2:
        print(playagainst(networkplayagainst2(network), -1))
    
    if network.neuroncounts[0] == 10 and network.neuroncounts[-1] == 1:
        print(playagainst(midai,1,stepfunc = lambda x,y: printwinner(x,y,network)))


def printwinner(board, player, network):
    result = network.fire(board+[player])[0][0]
    confidence = abs(abs(result)-0.5)*200
    print("Predicted winner:",{-1:"O",0:"tie",1:"X"}[round(result)],f"(confidence {confidence}%)")


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
    dual = lambda x : pickone(x, trainer, trainer2)
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
            raise EndTraining("Exiting program")
        
        elif ip[0] == 's':
            dual(savenet)

        elif ip[0] == 'w':
            print("WEIGHTS:")
            dual(lambda x:[print(i) for i in x.network.weights])

        elif ip[0] == 'b':
            dual(lambda x:[print(i) for i in x.network.biases])

        elif ip[0] == 'i':
            try:
                dual(lambda x:interact(x.network))
            except Exception as e:
                print('An error occurred.')
        
        elif ip[0] == 'm':
            dual(modify)

        else:
            return


def modify(trainer):
    print('''Options for modification:
          W: Weight learning rate
          B: Bias learning rate
          D: Learning rate descent factor
          S: Batchsize
          R: Rounds per print
          U: Update time
          ''')
    inp = input('Pick a letter: ').lower().strip()
    if inp[0] not in 'wbdsru':
        print('Invalid')
        return
    
    val = float(input("What value would you like to set it to? ").strip())

    if inp[0] == 'w':
        trainer.network.weightlearnrate = val
    elif inp[0] == 'b':
        trainer.network.biaslearnrate = val
    elif inp[0] == 'd':
        trainer.network.descentfactor = val
    elif inp[0] == 's':
        trainer.batchsize = int(val)
    elif inp[0] == 'r':
        trainer.roundsperprint  = int(val)
    elif inp[0] == 'u':
        trainer.updatetime = int(val)

def savenet(trainer):
    save(trainer.network)

def pickone(func, one, two):
    if two is None:
        func(one)
        return
    
    while True:
        inp = input("Which network? ").lower().strip()
        if inp[0] == '1' or 'one' in inp or  'first' in inp:
            func(one)
            return
        elif inp[0] == '2' or 'two' in inp or  'second' in inp:
            func(two)
            return
        elif 'x' in inp:
            print("Canceling... ")
            return

    