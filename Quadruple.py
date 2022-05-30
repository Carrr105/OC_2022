class Quadruple:
    
    def __init__(self, counter, op, op1, op2, res):
        self.counter = counter
        self.op  = op
        self.op1 = op1
        self.op2 = op2
        self.res = res
    
    def updateresult(self, newr):
        self.res = newr
