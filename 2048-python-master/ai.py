import math

hidden_layer_amount = 16

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class ann():
    def __init__(self):
        self.neural = neural()
        self.hidden_layer_weight = self.init_hidden_weight()
        #print(self.hidden_layer[0].weights)

    def input_layer(self, mat):
        X = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                X.append(mat[i][j])
        X = self.input_normalize(X)
        return (X,len(mat)*len(mat))

    def input_normalize(self, X):
        max_value = 0
        for i in X:
            if i > max_value:
                max_value = i
        Xn = []
        for i in X:
            Xn.append(i/max_value)
        return Xn
    
    def init_hidden_weight(self):
        hidden_layer = []
        
        for i in range(hidden_layer_amount):
            hidden_layer.append(self.neural)
        return hidden_layer
    

    #def output_layer(self):
        

class neural():
    def __init__(self):
        self.weights = self.init_weights()
    def init_weights(self):
        weights = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return weights
            
