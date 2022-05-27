class Quadruple:
    
    def __init__(self, op, op1, op2, res):
        self.op  = op
        self.op1 = op1
        self.op2 = op2
        self.res = res
    
    def updateresult(self, newr):
        self.res = newr
