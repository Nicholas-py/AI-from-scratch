from PIL import Image
from random import shuffle

mcibear = Image.open("Waterbear.png")
pix = mcibear.load()
pix[50,50] = (0,0,0,255)

aiinputs = []
aioutputs = []

def genbear(datanumber, lowerval = -1):
    r1 = list(range(1,mcibear.size[0]))
    r2 = list(range(mcibear.size[1]))
    r3 = [[i,j] for i in r1 for j in r2]
    shuffle(r3)
    for i, j in r3:
            compressed = [i/mcibear.size[0],j/mcibear.size[1]]
            aiinputs.append(compressed)
            colour = int(pix[i,j][2] > 100)
            if lowerval == -1:
                colour = colour*2-1
            aioutputs.append([colour])
            #aioutputs.append([colour])
            pix[i,j] = (255*colour, 255*colour, 255*colour, 255)
    return aiinputs[0:min(len(aiinputs), datanumber)], aioutputs[0:min(len(aiinputs), datanumber)]



def getimage(net):
    bear = Image.open("Waterbear.png")
    pix = bear.load()
    for i in range(mcibear.size[0]):
        for j in range(mcibear.size[1]):
            compressed = [i/mcibear.size[0],j/mcibear.size[1]]
            colour = net.fire(compressed)[0]
            pix[i,j] = (int(colour*255), int(colour*255), int(colour*255), 255)
    bear.save("Newbear.png")
    Image.open("Newbear.png").show()

