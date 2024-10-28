from PIL import Image
mcibear = Image.open("Waterbear.png")
pix = mcibear.load()
pix[50,50] = (0,0,0,255)

aiinputs = []
aioutputs = []

for i in range(1,mcibear.size[0]):
    for j in range(mcibear.size[1]):
        compressed = [i/mcibear.size[0],j/mcibear.size[1]]
        aiinputs.append(compressed)
        #colour = int((compressed[0]**2+compressed[1]**2)<0.7)*2-1
        colour = int(pix[i,j][2] > 100)
        aioutputs.append([colour*2-1])
        #aioutputs.append([colour])
        pix[i,j] = (255*colour, 255*colour, 255*colour, 255)



def getimage(net):
    bear = Image.open("Waterbear.png")
    pix = bear.load()
    for i in range(mcibear.size[0]):
        for j in range(mcibear.size[1]):
            compressed = [i/mcibear.size[0],j/mcibear.size[1]]
            colour = net.fire(compressed)[0]/2+1/2
            pix[i,j] = (int(colour*255), int(colour*255), int(colour*255), 255)
    bear.save("Newbear.png")
    Image.open("Newbear.png").show()

