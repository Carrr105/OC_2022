
# VarTable estructura
# nomre -> tipo -> 

#DIRFUNC
# nombre | tipo | | apuntador a tabla de variables correspondiente al scope

#TABLA VARS
# nombre | tipo |

class DirFunc:
    function_dictionary = dict()
    var_dictionary = dict()
    current_type = ''
    stack_name = []
    scope = ''

    def insert_function(self, name, type_):
        self.function_dictionary[name] = type_

    ######### VAR TABLE
    def insert_var(self):
        while not len(self.stack_name) == 0:
            self.var_dictionary[self.stack_name.pop()] = {self.current_type : self.scope}

    def insert_type(self, type_):
        self.current_type = type_
        print("type received is ")
        print(self.current_type)
    
    def insert_name(self, name):
        self.stack_name.append(name)
        print("name received will be added to stack and is ")
        print(self.stack_name)
    
    def insert_scope(self, scope):
        self.scope = scope
        print("current scope received is ")
        print(self.scope)
    
    def print_var(self):
        print(self.var_dictionary)
    
    def print_functions(self):
        print(self.function_dictionary)