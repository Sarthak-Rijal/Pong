
"""
fitness = # num of times it bounces
A chromosome which expresses a possible solution to the problem as a string
A fitness function which takes a chromosome as input and returns a higher value for better solutions (much more likely to reproduce)
A population which is just a set of many chromosomes
A selection method which determines how parents are selected for breeding from the population
A crossover operation which determines how parents combine to produce offspring
A mutation operation which determines how random deviations manifest themselves
"""

#state = ( delta_y_ball/delta_x_ball                 range: (-1 to 1)
#           (y_ball-y_paddle)/height                 range: (-1 to 1)
#                   y_paddle/height                  range (0 to 1)    
#             x_ball/width                           range (0 to 1))

#output = # -1 0 1 scalar which way to go

#linear model 
# tanh(A*inputs) = output
# (1x4) * (4x1) = (1x1)
# A = (a1 a2 a3 a4) lets create a linear constraint where a has a possible value between (-1 to 1)

#inital population is randomly generated A's
#we then run through each one calculate fitness

import numpy as np


input_size = 4
hidden_size = 4

class NN(object):
    #        4x4 matrix        4x1 matrix           1x4 matrix          4x1 matrix
    # A = [[x, x, x, x]   input = [[x]      C = [[x, x, x, x]]  Bias1 & Bias2 = [[x]
    #      [x, x, x, x]            [x]                                           [x]
    #      [x, x, x, x]            [x]                                           [x]   
    #      [x, x, x, x]]           [x]]                                          [x]]

    # 4x1 matrix
    # hidden output =  tanh ((A * input) + Bias1)

    # 1x1 matrix
    # output = tanh ((C * hidden output) + Bias2)
    def __init__(self, input_size, hidden_size):
        
        self.input_size = input_size
        self.hidden_size = hidden_size        

    def neuralNetwork (self, A, Bias1, C, Bias2, input):

        #multiply input and hidden layer weights
        weightCalc = np.matmul(A, input).reshape((4,1))

        #Add the bias and take a tanh on matrix to output the values of the hidden layer
        hiddenLayerOutput = np.tanh( weightCalc + Bias1)

        #mulpiply the hiddenlayer * hidden-to-output wieghts, add bias and return the tanh of each. 
        result = np.tanh( np.dot(C, hiddenLayerOutput) + Bias2)

        return result