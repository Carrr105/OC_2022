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

        self.global_base = 0
        self.local_base = 10000
        self.temporal_base = 20000
        self.ctes_base = 30000
        self.pointer_base = 40000

        self.char_start = 0
        self.int_start = 2500
        self.float_start = 5000
        self.bool_start = 7500
        # termina en 37501

        self.main_goto_pos = None
        self.counter = 1
        self.counter_global = [0,0,0,0]
        self.counter_pointer = [0,0,0,0]
        self.counter_local = [0,0,0,0]
        self.counter_ctes = [0,0,0,0]
        self.counter_temporal = [0,0,0,0]

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
            end = 2500 - 1
            count = 3
        else:
            print("type not valid")
            return -1
        
        if mem_type == "global" :
            address = self.global_base + start + self.counter_global[count]
            if address + size > self.global_base + start+ end :
                    print(address)
                    print(size)
                    print(start)
                    print(end)
                    print(self.global_base+start+ end)
                    raise TypeError("stack overflow global !")
            self.counter_global[count] += size
        elif mem_type == "pointer" :
            address = self.pointer_base + start + self.counter_pointer[count]
            if address + size > self.pointer_base + start+ end :
                    print(address)
                    print(size)
                    print(start)
                    print(end)
                    print(self.pointer_base+start+ end)
                    raise TypeError("stack overflow pointer !")
            self.counter_pointer[count] += size
        elif mem_type == "local" :
            address = self.local_base + start + self.counter_local[count]
            self.counter_local[count] += size
            if address + size > self.local_base + start + end :
                    print(self.local_base+start+ end)
                    raise TypeError("stack overflow local !")
        elif mem_type == "temporal" :
            address = self.temporal_base + start + self.counter_temporal[count]
            if address + size > self.temporal_base + start + end :
                    raise TypeError("stack overflow temporal !")
            self.counter_temporal[count] += size
        elif mem_type == "constants":
            inv_map = {v: k for k, v in self.ctes_table.items()}
            print("inverted1")
            print(inv_map)
            val = inv_map.get(value)
            print("value_received")
            print(value)
            print("val4")
            print(val)
            print("now invmap")
            print (inv_map)
            if val != None:
                address = val
            else:
                address = self.ctes_base + start + self.counter_ctes[count]
                if address + size > self.ctes_base + start + end :
                    raise TypeError("stack overflow constants !")
                if result_type=="bool" and address + size > 37502:
                    print(address)
                    raise TypeError("stack overflow, too many ctes bool !")
                self.ctes_table[address] = value
                self.counter_ctes[count] += size
        
        return address
    
    def reset_counters(self):
        #self.counter_global =  [0,0,0,0]
        self.counter_local =  [0,0,0,0]
        # las constantes no se reinician porque son globales
        #self.counter_ctes =  [0,0,0,0]
        self.counter_temporal = [0,0,0,0]
        #self.counter_pointer =  [0,0,0,0] por tiempo no se reinicia
    
    def new_quadruple(self, isPointer=False):
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
                if isPointer:
                    result = self.get_address(restype, "pointer")
                else:
                    result = self.get_address(restype, "temporal")
                quadruple = Quadruple(self.counter, operator, rightop, leftop, result)
                self.stOperands.append(result) # generacion del temporal 
                self.stTypes.append(restype)
            self.counter = self.counter + 1
            self.listQuadruples.append(quadruple)
        else:
            #print("type mismatch!")
            raise TypeError("Type mismatch!")
    
    def parche_guadalupano(self):
        print("stack of operators ")
        print (self.stOperators)
        print("stack of operands ")
        print (self.stOperands)
        print("stack of types ")
        print (self.stTypes)
        operator = self.stOperators.pop()
        rightop = self.stOperands.pop()
        righttype = self.stTypes.pop()

        result = self.get_address(righttype, "temporal")
        quadruple = Quadruple(self.counter, operator, None, rightop, result)
        self.stOperands.append(result) # generacion del temporal 
        self.stTypes.append(righttype)
        self.counter = self.counter + 1
        self.listQuadruples.append(quadruple)
    
    def gen_write(self):
        operator = self.stOperators.pop()
        rightop = self.stOperands.pop()
        righttype = self.stTypes.pop()

        quadruple = Quadruple(self.counter, operator, None, None, rightop)
        self.counter = self.counter + 1
        self.listQuadruples.append(quadruple)
    
    def gen_read(self):
        operator = self.stOperators.pop()
        rightop = self.stOperands.pop()
        righttype = self.stTypes.pop()

        quadruple = Quadruple(self.counter, operator, None, None, rightop)
        self.counter = self.counter + 1
        self.listQuadruples.append(quadruple)
    
    def gen_gosub(self, function_name):
        quad = Quadruple(self.counter, None, None, "GOSUB", function_name)
        self.listQuadruples.append(quad)
        self.counter += 1

    def print_quadruples(self):
        print("...................")
        print("printing quadruples")
        for quad in self.listQuadruples:
            print((quad.counter, quad.op, quad.op1, quad.op2, quad.res) )
        print("...................")
    
    def get_quadruples(self):
        return self.listQuadruples
    
    def gen_main_goto(self):
        quadruple = Quadruple(self.counter, None, None, "GOTO", None )
        self.listQuadruples.append(quadruple)
        self.main_goto_pos = self.counter - 1
        self.counter += 1
    
    def fill_goto(self):
        print("self counter is")
        print(self.counter)
        self.listQuadruples[self.stJumps.pop()].updateresult(self.counter)
    
    def fill_goto_while(self):
        print("self counter is")
        print(self.counter)
        self.listQuadruples[len(self.listQuadruples)-1].updateresult(self.stJumps.pop())
    
    def fill_gotof(self):
        print("self counter is")
        print(self.counter)
        self.listQuadruples[self.stJumps.pop()-1].updateresult(self.counter)
    
    def fill_gotof_while(self):
        print("self counter1 is")
        print(self.counter)
        print(self.stJumps)
        self.listQuadruples[self.stJumps.pop()-1].updateresult(self.counter+1)
    
    def fill_gotoF_if(self):
        print("self counter1 is")
        print(self.counter)
        print(self.stJumps)
        self.listQuadruples[self.stJumps.pop()-1].updateresult(self.counter+1)
    
    def fill_main_goto(self):
        self.listQuadruples[self.main_goto_pos].updateresult(self.counter)
    
    def gen_not_quadruple(self):
        operand = self.stOperands.pop()
        operator = self.stOperators.pop()
        type_ = self.stTypes.pop()

        if type_ != "bool":
            raise TypeError("not needs a boolean operand")
        else:
            res = self.get_address("bool", "temporal")
            quad = Quadruple(self.counter, operator, None, operand, res)
            self.listQuadruples.append(quad)
            self.stOperands.append(res)
            self.stTypes.append("bool")
            self.counter += 1
    
    def gen_gotoF(self):
        type_ = self.stTypes.pop()

        if type_ != "bool":
            raise TypeError("exp needs a boolean operand")
        else:
            res = self.stOperands.pop()
            quad = Quadruple(self.counter, res, None, "GOTOF", None)
            self.listQuadruples.append(quad)
            self.stJumps.append(self.counter)
            self.counter += 1
    
    def gen_goto(self):
        quad = Quadruple(self.counter, None, None, "GOTO", None)
        self.listQuadruples.append(quad)
        self.stJumps.append(self.counter-1)
        self.counter += 1
    
    def gen_fill_goto(self):
        quad = Quadruple(self.counter, None, None, "GOTO", self.stJumps[-1]+1)
        self.listQuadruples.append(quad)
        self.counter += 1
    
    def gen_goto_while(self):
        quad = Quadruple(self.counter, None, None, "GOTO", None)
        self.listQuadruples.append(quad)
        self.stJumps.append(self.counter-1)
        self.counter += 1
    
    def gen_end_quad(self):
        quad = Quadruple(self.counter, None, None, "ENDPROGRAM", None)
        self.listQuadruples.append(quad)
        #self.counter += 1
    
    def migaja(self):
        self.stJumps.append(self.counter)
    
    def gen_goto_migaja(self):
        quad = Quadruple(self.counter, None, None, "GOTO", self.stJumps.pop())
        self.listQuadruples.append(quad)
        self.counter+=1
    
    def gen_era(self, name):
        quad = Quadruple(self.counter, None, None, 'ERA', name)
        self.listQuadruples.append(quad)
        self.counter+=1
    
    def gen_param(self):
        quad = Quadruple(self.counter, 'PARAM', None, self.stOperands.pop(), None)
        self.listQuadruples.append(quad)
        self.counter+=1
    
    def gen_endfunc(self):
        quad = Quadruple(self.counter, 'ENDFUNC', None, None, None)
        self.listQuadruples.append(quad)
        self.counter+=1
    
    def gen_return(self, func_type, address):
        restype = self.semanticcube.get_type(func_type, self.stTypes.pop(), "=")
        quad = Quadruple(self.counter, None, self.stOperands.pop(), 'RETURN', address)
        self.listQuadruples.append(quad)
        self.counter += 1
    
    def gen_empty_return(self,name):
        quad = Quadruple(self.counter, None, None, 'RETURN', name)
        self.listQuadruples.append(quad)
        self.counter += 1
    
    def gen_ver(self,limit):
        quad = Quadruple(self.counter, self.stOperands.pop(), limit, 'VERIFY', None)
        self.listQuadruples.append(quad)
        self.counter += 1   

    def new_obj_file(self, df):
        newfile = {
            "Quadruples": [(quad.counter, quad.op, quad.op1, quad.op2, quad.res) for quad in self.listQuadruples],
            "Func_dir": df,
            "ctes_table": [(x, y) for x, y in self.ctes_table.items()]
        }

        with open ("obj.json", 'w') as f:
            json.dump(newfile, f, separators=(',', ':'))