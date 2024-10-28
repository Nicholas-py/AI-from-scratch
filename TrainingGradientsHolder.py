import numpy as np

class NpArrayList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, index):
        return self.data[index]

    def __add__(self, other):
        datas = []
        for i in range(len(self)):
            datas.append(self.data[i] + other[i])
        return NpArrayList(datas)
    
    def __mul__(self, number):
        datas = []
        for i in range(len(self)):
            datas.append(self.data[i]*number)
        return NpArrayList(datas)
    
    def __truediv__(self, number):
        datas = []
        for i in range(len(self)):
            datas.append(self.data[i]/number)
        return NpArrayList(datas)
    



class TrainingGradientsHolder:
    def __init__(self,parent):
        self.parent = parent
        self.network = parent.network
        self.addnumber = 0

        self.weights = self.generatebaseweights()
        self.biases = self.generatebasebiases()
    

    def generatebaseweights(self):
        weights = []
        for i in range(len(self.network.neuroncounts)-1):
            weights.append(np.zeros([self.network.neuroncounts[i], self.network.neuroncounts[i+1]]))
        return NpArrayList(weights)
    

    def generatebasebiases(self):
        biases = []
        for i in range(len(self.network.neuroncounts)-1):
            biases.append(self.network.neuroncounts[i+1])
        return NpArrayList(biases)
    

    def addtrainresults(self, results):
        self.weights = self.weights + results[0]
        self.biases = self.biases + results[1]
        self.parent.errorrecords.append(results[2])
        self.addnumber += 1


    def returntotals(self):
        return(self.weights/self.addnumber,self.biases/self.addnumber)

