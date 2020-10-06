import numpy as np
class Cost_Function:
    def __init__(self):
        self.cost_function=None
    
# Can add cost functions as needed similar to the quadratic cost function implemented below

class Quadratic_Cost(Cost_Function):
    def get_total(self,pected,actual):
        diff=pected-actual
        return np.dot(diff,diff)
    def get_derivative(self,pected,actual):
        return np.multiply((pected-actual),2)

#q = Quadratic_Cost()
#print(q.get_derivative(np.array([3,5,6]),np.array([1,6,7])))

