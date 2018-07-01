hidden_layer_amount = 16

class ann():
    def __init__(self):
        self.neural = neural()
        self.hidden_layer = self.init_hidden()
        print(self.hidden_layer[0].weights)
    def init_hidden(self):
        hidden_layer = []
        
        for i in range(hidden_layer_amount):
            hidden_layer.append(self.neural)
        return hidden_layer
        
    def input_layer(self, mat):
        X = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                X.append(mat[i][j])
        return (X,len(mat)*len(mat))

class neural():
    def __init__(self):
        self.weights = self.init_weights()
    def init_weights(self):
        weights = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return weights
            
