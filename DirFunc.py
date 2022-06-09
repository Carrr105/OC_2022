
# VarTable estructura
# nomre -> tipo -> 

#DIRFUNC
# nombre | tipo | | apuntador a tabla de variables correspondiente al scope

#TABLA VARS
# nombre | tipo |
import json
from CodigoIntermedio import CI

class DirFunc:
    #currentscope=""
    # antes {'test': 'void', 'main': 'void'}
    # ahora {'test': {'void'}, 'main': {'void'}}
    # mas antes {'test': 'void', 'main': 'void'}
    # antes {'test': {'void'}, 'main': {'void'}}
    # ahora
    # <class 'dict'>
    # {'test': {'void', 'vars'}, 'main': {'void', 'vars'}}
    # ahora de nuevo
    # {'test': {'void'}, 'main': {'void'}}

    def __init__(self):
        self.function_dictionary = dict()
        self.var_dictionary = dict()
        self.current_type = ''
        self.stack_name = []
        self.scope = ''
        self.current_class = ''
        self.curr_var_class = {}



    def insert_function(self, name, type_, function="False", ip=1, isClass=False):
        if not isClass :
            self.function_dictionary[name] = {
                                                "type" : type_,
                                                "params" : [],
                                                "function" : function,
                                                "dimensions" : [],
                                                "ip": ip,
                                                "classes" : {},
                                                "vars" : {

                                                    }
                                                }
            self.current_name = name
            self.current_scope = self.function_dictionary[name]
        else:
            self.function_dictionary["global"]["classes"][self.current_class]["functions"][name] = {
                                                "type" : type_,
                                                "params" : [],
                                                "function" : function,
                                                "dimensions" : [],
                                                "ip": ip,
                                                "classes" : {},
                                                "vars" : {

                                                    }
                                                }
            self.current_name = name
            self.current_scope = self.function_dictionary["global"]["classes"][self.current_class]

    
    def insert_class(self, name):
        self.function_dictionary["global"]["classes"][name] = {
                                            "vars" : {

                                            },
                                            "functions" : {

                                            }
        }
        self.current_class = name
        self.current_name = name
        self.current_scope = self.function_dictionary["global"]["classes"][name]



    def insert_param_types(self, currentscope, paramstack, isClass=False, name=""):
        if not isClass:
            print("PARAMS ORDER1: ")
            print(paramstack)
            print("ordered too")
            print(self.function_dictionary[currentscope])
            for i in range(len(paramstack)):
                self.function_dictionary[currentscope]["params"].append(paramstack[i])
            print("nownow10")
            print(self.function_dictionary[currentscope])
        else:
            print("isclass true")
            print("PARAMS ORDER1: ")
            print(paramstack)
            print("ordered too")
            #print(self.function_dictionary["global"]["classes"][self.current_class]["functions"][self.current_scope])
            for i in range(len(paramstack)):
                self.function_dictionary["global"]["classes"][self.current_class]["functions"][self.current_scope]["params"].append(paramstack[i])
            print("nownow10")
            #print(self.function_dictionary["global"]["classes"][self.current_class]["functions"][self.current_scope])

    ######### VAR TABLE
    def insert_var(self, currentscope, name, type_, address, dim_stack = [],paramcount=0, isFunction=False, isClass=False, myvarss={}):
        currsize = len(self.function_dictionary)
        #print("PROBANDO")
        #print(self.function_dictionary[currentscope])
        # regresa 
        # {'vars', 'void'}
        #print("dimztackuwu")
        #print(dim_stack)
        print("valuess")
        print(currentscope)
        print(name)
        print("pritnb")
        print(isClass)
        print("pritnbvar")
        print(myvarss)
        self.curr_var_class = myvarss
        if not isClass:
            if type_ != "int" and type_ != "char" and type_ != "bool" and type_ != "float" and self.curr_var_class != {}:
                print("masdebug7")
                print(currentscope)
                print(name)
                print (isClass)
                print (self.function_dictionary[currentscope]["vars"])
                print(self.curr_var_class)
                self.function_dictionary[currentscope]["vars"][name] = {
                                                                        'type' : type_,
                                                                        'content' : []
                                                                        }
                self.function_dictionary[currentscope]["vars"][name]["content"].append(myvarss)                                                 
                print("adres1s")
                print(address)
            else:
                self.function_dictionary[currentscope]["vars"][name] = {
                                                                        'type' : type_,
                                                                        'address' : address,
                                                                        'value' : None,
                                                                        'function' : str(isFunction),
                                                                        'dimensions' : [],
                                                                        'paramcount' : paramcount
                                                                        }
                print("SSS")
                print (self.function_dictionary[currentscope]["vars"][name])
                for i in range(len(dim_stack)):
                    print("apanding")
                    print(dim_stack[i])
                    self.function_dictionary[currentscope]["vars"][name]["dimensions"].append(dim_stack[i])
                print("UWU")
                print (self.function_dictionary[currentscope]["vars"][name])
    
        else:
            self.function_dictionary["global"]["classes"][self.current_class]["vars"][name] = {
                                                                    'type' : type_,
                                                                    'address' : address,
                                                                    'value' : None,
                                                                    'function' : str(isFunction),
                                                                    'dimensions' : [],
                                                                    'paramcount' : paramcount
                                                                    }
            for i in range(len(dim_stack)):
                self.function_dictionary["global"]["classes"][self.current_class]["vars"][name]["dimensions"].append(dim_stack[i])
        
        #print("PROBANDO")
        #print(self.function_dictionary)
        #print(type(self.function_dictionary))
        #print ("regresando llaves")
        #print (self.function_dictionary["global"].keys())
        #print (type(self.function_dictionary["global"]["vars"]))
        ### ligar diccionario de variables a diccionario de funciones
        ### quizas hacerlo en el main ? hacer un metodo para al final de la compilacion
        ### llamarlo y agregar al directorio de funciones de las filas que correspondan
        ### al scope

    def insert_type(self, type_):
        self.current_type = type_
        #print("type received is ")
        #print(self.current_type)
        
    
    def insert_name(self, name):
        self.stack_name.append(name)
        #print("name received will be added to stack and is ")
        #print(self.stack_name)
    
    def insert_scope(self, scope):
        self.scope = scope
        #print("current scope received is ")
        #print(self.scope)
    
    def print_var(self):
        print(self.var_dictionary)
    
    def print_functions(self):
        print(self.function_dictionary)
    
    def join_functdirectory_vartables(self, currscope):
        print("helloo")
        print(self.function_dictionary[currscope])
    
    def search(self, var_name, function=False):
        print("wereceived")
        print(var_name)
        print (self.function_dictionary)
        if var_name in self.current_scope["vars"]:
            return self.current_scope["vars"][var_name]
        elif var_name in self.function_dictionary["global"]["vars"]:
            return self.function_dictionary["global"]["vars"][var_name]
        else:
            if not function:
                print(var_name)
                raise NameError("{var_name} not defined")
            elif var_name in self.function_dictionary:
                return "void"
            else:
                raise NameError("{var_name} not defined lol")
        
    
    def search_class(self, class_name):
        print("wereceived")
        print(class_name)
        print (self.function_dictionary)
        if class_name in self.function_dictionary["global"]["classes"]:
            return self.function_dictionary["global"]["classes"][class_name]
        else:
            raise NameError("Esta clase no ha sido declarada")