import math
class Activation_Function():
    def __init__(self):
        self.activation_function=None

class ReLU(Activation_Function):
    def function(self,x):
        return 0 if x < 0 else x
    def derivative(self,x):
        return 0 if x < 0 else 1

class Sigmoid(Activation_Function):
    def function(self,x):
        return 1.0/(1.0 + math.exp(-x))
    def derivative(self,x):
        return x*(1.0-x)  

a=Sigmoid()
print(a.derivative(1))
a.derivative(45)
