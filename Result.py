class Result:
    def __init__(self):
        output = None
        cost = None

    def __init__(self,output):
        self.output = output
        self.cost = None

    def __init__(self,output, cost):
        self.output = output
        self.cost = cost

    def getOutput(self):
        return self.output

    def getCost(self):
        return self.cost
    
    
