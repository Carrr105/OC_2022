from SemanticCube import SemanticCube
from Quadruple import Quadruple
import json

class CI:
    
    def __init__(self):
        self.semanticcube = SemanticCube()
        self.listQuadruples = []
        self.stTypes = []
        self.stOperands = []
        self.stOperators = []
        self.stJumps = []
        self.tempCount = 0
        self.paramCount = 0

        self.global_base = 5000
        self.local_base = 10000
        self.ctes_base = 20000

        self.char_start = 1
        self.int_start = 3000
        self.float_start = 6000
        self.bool_start = 9000

        self.counter = 1
        self.counter_global = self.counter_local = self.counter_ctes = [0,0,0,0]

    def get_address(self, result_type, scope):
        # count seria la posicion de la lista que se va a modificar
        # char int float bool
        #  0  1  2  3
        # [0, 0, 0, 0]
        if result_type == "char" :
            start = self.char_start
            end = self.int_start - 1
            count = 0 
        elif result_type == "int": 
            start = self.int_start
            end = self.float_start - 1
            count = 1
        elif result_type == "float":
            start = self.float_start
            end = self.bool_start - 1 
            count = 2
        elif result_type == "bool":
            start = self.bool_start
            end = 12000 - 1
            count = 3
        else:
            print("type not valid")
        
        if scope=="local":
            address = self.local_base + start + self.counter_local[count]
            size = 1 # por ahora size es 1 pero para arreglos y matrices debe ser diferente
            self.counter_local[count] += size
        
        return address
    
    def new_quadruple(self):
        print("stack of operators ")
        print (self.stOperators)
        print("stack of operands ")
        print (self.stOperands)
        print("stack of types ")
        print (self.stTypes)
        operator = self.stOperators.pop()
        leftop = self.stOperands.pop()
        rightop = self.stOperands.pop()
        lefttype = self.stTypes.pop()
        righttype = self.stTypes.pop()
        

        restype = self.semanticcube.get_type(lefttype, righttype, operator)

        if restype != "ERROR":
            result = self.get_address(restype, "local")
            if operator == "=":
                quadruple = Quadruple(self.counter, operator, None, rightop, result)
                self.counter = self.counter + 1
            else:
                quadruple = Quadruple(self.counter, operator, leftop, rightop, result)
                self.counter = self.counter + 1
                self.stOperands.append(result) # generacion del temporal 
            self.listQuadruples.append(quadruple)
        else:
            print("type mismatch!")
    
    def print_quadruples(self):
        print("...................")
        print("printing quadruples")
        for i in range(len(self.listQuadruples)):
            print (self.listQuadruples[i])
        print("...................")
    
    def get_quadruples(self):
        return self.listQuadruples
    
    def new_obj_file(self):
        newfile = {
            "Quadruples": [(quad.counter, quad.op, quad.op1, quad.op2, quad.res) for quad in self.listQuadruples]
        }

        with open ("obj.json", 'w') as f:
            json.dump(newfile, f)