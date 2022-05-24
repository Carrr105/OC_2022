from semanticcube import SemanticCube
from Quadruples import Quadruples

class CI:
    
    def __init__(self):
        self.semanticcube = SemanticCube()
        self.liQuadruples = []
        self.stTypes = []
        self.stOperands = []
        self.stOperators = []
        self.stJumps = []
        self.tempCount = 0
        self.paramCount = 0
