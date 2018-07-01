import math
from random import *

hidden_layer_amount = 16
goal = 1000
eta = 0.005

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class ann():
    def __init__(self):
        self.hidden_layer_weight = self.init_hidden_weight()
        self.output_layer_weight = self.init_output_weight()

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
            self.neural = neural(16)
            hidden_layer.append(self.neural)
        return hidden_layer

    def cal_U(self, X, weights):
        result = 0
        for i in range(len(X)):
            result+=X[i]*weights[i]
        result-=weights[len(X)]
        result = sigmoid(result)
        return result
    
    def init_output_weight(self):
        output_layer = []
        
        for i in range(4):
            self.neural = neural(hidden_layer_amount)
            output_layer.append(self.neural)
        return output_layer

    def predict(self, mat):
        X, amount = self.input_layer(mat)
        result1 = []
        for i in range(hidden_layer_amount):
            result1.append(self.cal_U(X, self.hidden_layer_weight[i].weights))
        result2 = []
        for i in range(4):
            result2.append(self.cal_U(result1, self.output_layer_weight[i].weights))
        print(repr(result2))

        prefer = 0
        for i in range(1,4):
            if result2[i] > result2[prefer]:
                prefer = i
        return (prefer, X, result1, result2)        

    def back_propagation_output(self, score, score_add, move, X, result1, result2):
        delta =self.cost(score)
        """
        for i in range(len(result2)):
            delta_result2_weight_one = []
            for j in range(len(result1)):
                delta_result2_weight_one.append(result1[j]*eta*delta)
                self.output_layer_weight[i].weights[j]+=result1[j]*eta*delta
                print(self.output_layer_weight[i].weights[j])
            delta_result2_weight_one.append((-1)*eta*delta)
            self.output_layer_weight[i].weights[len(result1)]+=(-1)*eta*delta
            print(self.output_layer_weight[i].weights[len(result1)])
            delta_result2_weight.append(delta_result2_weight_one)
        """
        

    def cost(self, score):
        return ((goal-score)/goal)
    
class neural():
    def __init__(self, d):
        self.weights = self.init_weights(d)
    def init_weights(self, d):
        weights = []
        for i in range(d+1):
            weights.append(uniform(-1*math.pow(d, (-1/2)),math.pow(d, (-1/2))))
        return weights
            
