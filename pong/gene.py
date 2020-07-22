
import numpy as np


input_size = 4
hidden_size = 4

class gene(object):

    def __init__(self, inputNum, hiddenNum, outputNum, info_bit = 8):
        
        self.info_bit = info_bit
        self.inputNum = inputNum
        self.hiddenNum = hiddenNum
        self.outputNum = outputNum
        
        