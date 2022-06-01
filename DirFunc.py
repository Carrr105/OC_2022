
# VarTable estructura
# nomre -> tipo -> 

#DIRFUNC
# nombre | tipo | | apuntador a tabla de variables correspondiente al scope

#TABLA VARS
# nombre | tipo |
import json

class DirFunc:
    function_dictionary = dict()
    var_dictionary = dict()
    current_type = ''
    stack_name = []
    scope = ''
    # antes {'test': 'void', 'main': 'void'}
    # ahora {'test': {'void'}, 'main': {'void'}}
    # mas antes {'test': 'void', 'main': 'void'}
    # antes {'test': {'void'}, 'main': {'void'}}
    # ahora
    # <class 'dict'>
    # {'test': {'void', 'vars'}, 'main': {'void', 'vars'}}
    # ahora de nuevo
    # {'test': {'void'}, 'main': {'void'}}

    def insert_function(self, name, type_):
        self.function_dictionary[name] = {
                                            "type" : type_,
                                            "vars" : {

                                                }
                                            }
        self.current_scope = self.function_dictionary[name]

    ######### VAR TABLE
    def insert_var(self, currentscope, name, type_, address):
        currsize = len(self.function_dictionary)
        #print("PROBANDO")
        #print(self.function_dictionary[currentscope])
        # regresa 
        # {'vars', 'void'}
        self.function_dictionary[currentscope]["vars"][name] = {
                                                                'type' : type_,
                                                                'address' : address
                                                                }
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
    
    def search(self, var_name):
        if var_name in self.current_scope["vars"]:
            return self.current_scope["vars"][var_name]
        elif var_name in self.function_dictionary["global"]["vars"]:
            return self.function_dictionary["global"]["vars"][var_name]
        else:
            raise NameError("{var_name} not defined")