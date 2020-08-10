
import numpy as np
import random

input_size = 4
hidden_size = 4


#The gene class reprents the genetic informatio of each paddle. 
#8 bits of the 010101... gene sequence is mapped to the wegith and bias of the NN
#Through the process of fitness, selection, crossover and random mutation the bit string
# sequence will result in a solution for the NN. 
class gene(object):

    def __init__(self, inputNum, hiddenNum, outputNum, info_bit = 8, alleal = None):
        
        self.info_bit = info_bit

        #structure of the neural network. 
        self.inputNNnode = inputNum
        self.hiddenNNnode = hiddenNum
        self.outputNNnode = outputNum

        self.allele = allele

        #instantiate the DNA
        if (self.allele == None):
            #number of weights and biases
            weight1 = self.inputNNnode * self.hiddenNNnode 
            bias1 = self.hiddenNNnode

            weight2 = self.outputNNnode * self.outputNNnode
            bias2 = self.outputNNnode

            weightNbias = weight1 + bias1 + weight2 + bias2

            self.allele = []

            for i in range(info_bit * weightNbias):
                self.allele.append(random.randint(0,1))
            
    #default 5% chance to mutate
    def mutate(self, chance = 0.05):

        for i in len(self.allele):
            if (random.random() < chance):
                if (self.allele[i] == 0):
                    self.allele[i] = 1
                else:
                    self.allele[i] = 0


    #breeds two DNA's together
    def corssover(self, other):
        child = []
        
        for i in len(self.allele):
            if (random.random() < 0.5):
                child.append(self.allele[i])
            else:
                child.append(other[i])

        return child