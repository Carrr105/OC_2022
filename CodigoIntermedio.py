from SemanticCube import SemanticCube
from Quadruple import Quadruple
import json

class CI:
    
    def __init__(self):
        self.ctes_table = {}
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
        self.temporal_base = 25000

        self.char_start = 1
        self.int_start = 3000
        self.float_start = 6000
        self.bool_start = 9000

        self.main_goto_pos = None
        self.counter = 1
        self.counter_global = self.counter_local = self.counter_ctes = self.counter_temporal = [0,0,0,0]

    def get_address(self, result_type, mem_type, value=None, size = 1):
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
            return -1
        
        if mem_type == "global" :
            address = self.global_base + start + self.counter_global[count]
            self.counter_global[count] += size
        elif mem_type == "local" :
            address = self.local_base + start + self.counter_local[count]
            self.counter_local[count] += size
        elif mem_type == "temporal" :
            address = self.temporal_base + start + self.counter_temporal[count]
            self.counter_temporal[count] += size
        elif mem_type == "constants":
            address = self.ctes_base + start + self.counter_ctes[count]
            self.ctes_table[address] = value
            self.counter_ctes[count] += size
        
        return address
    
    def reset_counters(self):
        self.counter_global =  [0,0,0,0]
        self.counter_local =  [0,0,0,0]
        self.counter_ctes =  [0,0,0,0]
        self.counter_temporal = [0,0,0,0]
    
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
            if operator == "=":
                print("igualandoo...")
                # no se deberia permitir asignar un valor float a una variable int
                result = leftop
                quadruple = Quadruple(self.counter, operator, None, rightop, result)
            else:
                result = self.get_address(restype, "temporal")
                quadruple = Quadruple(self.counter, operator, rightop, leftop, result)
                self.stOperands.append(result) # generacion del temporal 
                self.stTypes.append(restype)
            self.counter = self.counter + 1
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
    
    def gen_main_goto(self):
        quadruple = Quadruple(self.counter, None, None, "GOTO", None )
        self.listQuadruples.append(quadruple)
        self.main_goto_pos = self.counter - 1
        self.counter += 1
    
    def fill_main_goto(self):
        self.listQuadruples[self.main_goto_pos].updateresult(self.counter)
    
    def new_obj_file(self, df):
        newfile = {
            "Quadruples": [(quad.counter, quad.op, quad.op1, quad.op2, quad.res) for quad in self.listQuadruples],
            "Func_dir": df,
            "ctes_table": [(x, y) for x, y in self.ctes_table.items()]
        }

        with open ("obj.json", 'w') as f:
            json.dump(newfile, f, separators=(',', ':'))