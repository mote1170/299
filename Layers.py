import numpy as np
class Layer:
    def __init__(self,nb_neurons,activation_function):
        self.nb_neurons = nb_neurons
        self.activation_function = activation_function
        self.weights = np.random.randn(inputs , number_of_neurons)  # Random matrix of weights
        self.biases = np.zeros((1,number_of_neurons)) # Initially, no biases ie 0 





