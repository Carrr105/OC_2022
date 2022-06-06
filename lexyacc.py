# Proyecto Final Compiladores gpo 2
# Carlos Gerardo Herrera Cortina - A00821946
# Omar Alejandro Balboa Lara - A00825034
import sys
import ply.lex as lex
import ply.yacc as yacc
import SemanticCube
from DirFunc import DirFunc as df
from CodigoIntermedio import CI as ci
import re
from six.moves import reduce

df = df()
ci = ci()

reserved = {
    'program' : 'PROGRAM',
    'float' : 'FLOAT',
    'int' : 'INT',
    'char' : 'CHAR',
    'bool' : 'BOOL',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'class' : 'CLASS',
    'vars' : 'VARS',
    'function' : 'FUNCTION',
    'main' : 'MAIN',
    'read' : 'READ',
    'write' : 'WRITE',
    'then' : 'THEN',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'to' : 'TO',
    'and' : 'AND',
    'or' : 'OR',    
    'not' : 'NOT',
    'return' : 'RETURN',
    'call' : 'CALL',
    'void' : 'VOID'
    
}

tokens = [
    'OPENPARENTHESES', 'CLOSEPARENTHESES','ID', 'CTEF', 'CTEI', 'CTEB', 'CTEC',
    'HASHTAG', 'CTE_COMMENT',
    'DOT', 'TWODOTS', 'SEMICOLON',
    'OPENBRACE', 'CLOSEBRACE',
    'GREATER', 'LESS', 'DIFFERENT', 'CTESTRING',
    'EQUALS_BOOLEAN', 'DIVIDE', 'MULTIPLY',
    'PLUS', 'MINUS', 'OPENBRACKET', 'CLOSEBRACKET', 'COMMA', 'QUOTATIONMARK',
    'LESSEQUAL', 'GREATEREQUAL', 'EQUALS'
] + list(reserved.values())

precedence = (
     ('nonassoc', 'LESS', 'GREATER', 'LESSEQUAL', 'GREATEREQUAL', 'EQUALS_BOOLEAN'),  # Nonassociative operators
     ('left', 'PLUS', 'MINUS'),
     ('left', 'MULTIPLY', 'DIVIDE'),
     ('right', 'EQUALS')
)

t_HASHTAG = r'\#'
t_OPENPARENTHESES = r'\('
t_CLOSEPARENTHESES = r'\)'
t_SEMICOLON = r'\;'
t_TWODOTS = r'\:'
t_OPENBRACE = r'\{'
t_CLOSEBRACE = r'\}'
t_EQUALS = r'\='
t_EQUALS_BOOLEAN = r'\=='
t_DOT = r'\.'
t_GREATER = r'\>'
t_LESS = r'\<'
t_DIFFERENT = r'\<>'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ignore = r' '
t_OPENBRACKET = r'\['
t_CLOSEBRACKET = r'\]'
t_COMMA = r'\,'
t_QUOTATIONMARK = r'\''
t_LESSEQUAL = r'\<='
t_GREATEREQUAL = r'\>='
t_CTE_COMMENT = r'(\#(.|\n)*?)\#'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_CTEF(t):
    r'-?([0-9])+\.([0-9])*'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_CTEB(t):
    r'^(?i)(TRUE|FALSE)$'
    t.value = bool(t.value)
    print("hi1")
    return t

def t_CTEC(t):
    r'"(.?)"'
    t.value = str(t.value)
    return t

def t_CTESTRING(t):
    r'"(.*)"'
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

'#parser'

varstack = []
type_var = '' # cambiar a stack
scopestack = []
resultstack = []
paramstack = [] 
dimstack = [] # guarda tamaños de dimensiones de arreglos matrices etc
paramcount = 0
isParamFunc = False
recorridodimensiones = [] # guarda dimensiones para calcular cuanto hay que recorrer
R = 1
functype=""
currdimlist = [] #contiene las dimensiones de la variable en cuestion
isClass = False
myvars = {}

start = 'programa'
globalname = ''

def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON establishglobalscope programaP
    '''
    p[0] = "PROGRAM COMPILED"
    ci.gen_end_quad()

# este tipo de reglas vacias servirán para poder hacer acciones intermedias,
# ya que PLY no cuenta con un soporte natural para ellas.
# es una "mexicanada" pero sirve
def p_establishglobalscope(p):
    "establishglobalscope :"
    global scopestack
    scopestack.append("global")
    df.insert_function("global", "global")
    df.print_functions()
    globalname ="global"
    print("global scope name is ")
    print(globalname)
    ci.gen_main_goto() # generacion del goto al main
    print("just started bro")

def p_programaP(p):
    '''
    programaP : vars programaP
    | clase programaP
    | funcion programaP
    | CTE_COMMENT programaP
    | bloque
    '''

def p_clase(p):
    '''
    clase : CLASS ID insert_class OPENBRACE claseP CLOSEBRACE
    '''
    global isClass
    isClass=False

def p_insert_class(p):
    '''
    insert_class : 
    '''
    global scopestack
    scopestack.append(p[-1])
    print("heyboyy1")
    print (p[-1])
    df.insert_class(p[-1])
    global isClass
    isClass=True
    ci.reset_counters()

## cero o más declaraciones de vars. 
def p_claseP(p):
    '''
    claseP : vars claseP
         | CTE_COMMENT claseP
         | clasePP
    '''
# cero o más funcion
def p_clasePP(p):
    '''
    clasePP : funcion clasePP
            | CTE_COMMENT claseP
            | empty
    '''

def p_funcion(p):
    '''
    funcion : FUNCTION tipo_f TWODOTS ID savefuncscope OPENPARENTHESES paramsfunction savesequence CLOSEPARENTHESES OPENBRACE turnoff estatuto CLOSEBRACE
    '''
    ci.gen_endfunc()

def p_turnoff(p):
    '''
    turnoff : 
    '''
    global paramcount
    paramcount = 1
    global isParamFunc
    isParamFunc = False

def p_tipo_f(p):
    '''
    tipo_f : INT
            | FLOAT
            | BOOL
            | CHAR
            | VOID
    '''
    #p[0]=p[1]
    #p[0]=p[1]
    global paramcount
    paramcount = 1
    global isParamFunc
    isParamFunc = True
    global functype 
    functype = p[1]

def p_savefuncscope(p):
    '''
    savefuncscope : 
    '''
    global isClass
    global scopestack
    global functype
    if not isClass:
        print("entre2")
        scopestack.append(p[-1])
        print("heyboyy1")
        print (p[-1])
        print (functype)
        ci.reset_counters()
        df.insert_function(p[-1], functype, function="True", ip=ci.counter)
        if functype == 'int' or functype== 'float' or functype== 'bool' or functype== 'char':
            addr=ci.get_address(functype, "global")
            df.insert_var("global",p[-1],functype,addr,isFunction=True)
        functype = ""
    else:
        print("p1is")
        print(p[-1])
        df.insert_function(p[-1], functype, function="True", ip=ci.counter, isClass = isClass)
        if functype == 'int' or functype== 'float' or functype== 'bool' or functype== 'char':
            addr=ci.get_address(functype, "local")
            df.insert_var("local",p[-1],functype,addr,isFunction=True, isClass=isClass)
        functype = ""



def p_paramsfunction(p):
    '''
    paramsfunction : tipo savetipo param COMMA paramsfunction
                    | tipo savetipo param
                    | empty
    '''

def p_savetipo(p):
    '''
    savetipo : 
    '''
    global type_var
    type_var = p[-1]
    global paramstack
    print("appending")
    print(p[-1])
    paramstack.append(p[-1])
    print("n0w")
    print(paramstack)

def p_savesequence(p):
    '''
    savesequence : 
    '''
    global paramstack
    global isClass
    print("insertin3 sequence...")
    print(paramstack)
    print (scopestack[-1])
    df.insert_param_types(scopestack[-1], paramstack, isClass=isClass)
    paramstack.clear()
    print("func state")
    print(df.function_dictionary)

def p_return(p):
    '''
    return : RETURN exp SEMICOLON
            | RETURN SEMICOLON
    '''
    if (df.current_name=="main"):
        raise TypeError("can't return inside main!")
    print("l00king")
    print(df.current_name)
    var = df.search(df.current_name, function=True)
    print("wefound")
    print(var)
    if var=="void":
        print("hi")
        ci.gen_empty_return(df.current_name)
    else:
        ci.gen_return(var["type"], var["address"])

def p_vars(p):
    '''
    vars : VARS tipo savetype TWODOTS varsP
    '''

def p_varsP(p):
    '''
    varsP : param COMMA varsP
            | param SEMICOLON
    '''

def p_savetype(p):
    '''
    savetype : 
    '''
    global type_var
    type_var = p[-1]
    print("type_var is ")
    print(type_var)
    print("verifying...")
    print (type_var)
    print(type(type_var))
    if type_var != "int" and type_var != "char" and type_var != "bool" and type_var != "float":
        verify = df.search_class(type_var)
        print("verified")
        print(verify)

def p_param(p):
    '''
    param : ID
        | ID declare_dims
    '''
    global type_var
    global isParamFunc
    global paramcount
    global isClass
    global myvars
    print("....currentscope")
    print(df.current_scope)
    print("....xd")
    print(df.function_dictionary['global'])
    if (len(p)==2):
        if df.current_scope is df.function_dictionary['global']:
            address = ci.get_address(type_var, "global")
            df.insert_var(scopestack[-1], p[1], type_var, address, [], 0, isFunction=False, isClass=isClass)
        elif type_var != "int" and type_var != "char" and type_var != "bool" and type_var != "float" and isClass == False:
            address = -1
            print("l00k1")
            print(type_var)
            myvarfromclass = df.search_class(type_var)
            myvars = myvarfromclass["vars"]
            print("beforecycle")
            print(ci.counter_local)
            print("letstry1")
            print(df.current_name)
            mylist = []
            for k,v in myvars.items():
                mylist.append((k,v["type"],v["value"],ci.get_address(v["type"], "local")))
                print(v)
                print("info2")
                print(k)
                print(v["address"])
            print("aftercycle")
            print(ci.counter_local)
            print("newmyvars")
            print(myvars)
            if not isParamFunc:
                df.insert_var(scopestack[-1], p[1], type_var, address, [], 0, isFunction=False, isClass=isClass, myvarss=mylist)
        elif isClass:
            address = ci.get_address(type_var, "local")
            df.insert_var(scopestack[-1], p[1], type_var, address, [], 0, isFunction=False, isClass=isClass)
        else:
            address = ci.get_address(type_var, "local")
            if isParamFunc:
                df.insert_var(scopestack[-1], p[1], type_var, address, [], paramcount, isFunction=False, isClass=isClass)
                paramcount+=1
            df.insert_var(scopestack[-1], p[1], type_var, address, [], 0, isFunction=False, isClass=isClass)
            
            
        myvars = {}
    else:
        # guardar variable con direccion base y con el numero de dimensiones
        print("hola")
        print("saving as normal id for now")
        print("dimstack1 received is")
        global dimstack
        print(dimstack)
        # dimaux almacena los valores de las direcciones para calcular el size
        dimaux = []
        dct = dict(ci.ctes_table)
        for i in dimstack:
            val = dct.get(i)
            if val != None:
                if isinstance(val, int) and val > 1:
                    dimaux.append(val)
                else:
                    raise TypeError("really...")
        #print(ci.ctes_table.values())
        print("dimauxx")
        print(dimaux)
        # la dirección calculada es la base
        if df.current_scope is df.function_dictionary['global'] and not isClass:
            address = ci.get_address(type_var, "global", value=None, size = reduce(lambda x, y: x*y, dimaux))
        else:
            if not isClass:
                address = ci.get_address(type_var, "local", value=None, size = reduce(lambda x, y: x*y, dimaux))
            else:
                address = None
        if isParamFunc:
            df.insert_var(scopestack[-1], p[1], type_var, address, [], paramcount, isFunction=False, isClass=isClass)
            paramcount+=1
        else:
            print("dimztack")
            print(dimstack)
            # se almacenan dimensiones directamente como valores por cuestion de tiempo
            df.insert_var(scopestack[-1], p[1], type_var, address, dimaux, 0, isFunction=False, isClass=isClass)
        dimstack.clear()
        dimaux.clear()

def p_declare_dims(p):
    '''
    declare_dims : OPENBRACKET exp CLOSEBRACKET declare_dims
                | OPENBRACKET exp CLOSEBRACKET
    '''
    global dimstack
    if (ci.stTypes.pop()=="int"):
        dimstack.append(ci.stOperands.pop())
    else:
        raise TypeError("dimension should be an int!")


        

def p_paramsP(p):
    '''
    paramsP : exp COMMA paramsP
            | exp
    '''

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
         | BOOL
         | ID
    '''
    p[0] = p[1]


def p_class(p):
    '''
    class : 
    '''
    


def p_bloque(p):
    '''
    bloque : MAIN OPENPARENTHESES CLOSEPARENTHESES OPENBRACE establishmainscope estatuto CLOSEBRACE
            | MAIN OPENPARENTHESES CLOSEPARENTHESES OPENBRACE CLOSEBRACE
    '''

# no olvidar dejar el espacio antes de los dos puntos
def p_establishmainscope(p):
    '''
    establishmainscope : 
    '''
    global scopestack
    scopestack.append("main")
    df.insert_function("main", "void", function="False", ip=ci.counter)
    df.print_functions()
    print("main has been found")
    ci.reset_counters()
    ci.fill_main_goto()

def p_estatuto(p):
    '''
    estatuto : asignacion estatuto
        | llamada estatuto
        | lectura estatuto
        | escritura estatuto
        | repeticion estatuto
        | declaracion estatuto
        | condicion estatuto
        | return estatuto
        | CTE_COMMENT estatuto
        | empty
    '''

def p_declaracion(p):
    '''
    declaracion : vars
    '''
def p_llamada(p):
    '''
    llamada : ID gen_era OPENPARENTHESES param_call CLOSEPARENTHESES
    '''
    ci.gen_gosub(p[1])
    var = df.search(p[1])
    print(var)
    ci.stOperands.append(var["address"])
    ci.stTypes.append(var["type"]) #mexicanada, repetir el append para que no este vacio el stack
    print("mystackuwu")
    ci.stOperators.append("=")
    #ci.parche_guadalupano()



def p_gen_era(p):
    '''
    gen_era : 
    '''
    print("p1ok")
    print(p[-1])
    #var = df.search(p[-1])
    ci.gen_era(p[-1])

def p_param_call(p):
    '''
    param_call : exp gen_param printt
                | exp gen_param COMMA param_call
    '''

def p_printt(p):
    '''
    printt : 
    '''
    print("finished..")

def p_gen_param(p):
    '''
    gen_param : 
    '''
    ci.gen_param()

def p_lectura(p):
    '''
    lectura : READ OPENPARENTHESES ID CLOSEPARENTHESES SEMICOLON
            | READ OPENPARENTHESES ID dims CLOSEPARENTHESES SEMICOLON
    '''
    if (len(p)==6):
        print("var to look for")
        print(p[3])
        var = df.search(p[3]) 
        print(var)
        if (var["function"]=="True"):
            raise TypeError("XD, no se puede asignar valor a una función")
        ci.stOperators.append(p[1])
        ci.stOperands.append(var["address"])
        ci.stTypes.append(var["type"])
        ci.gen_read()
    if (len(p)==7):
        var = df.search(p[3]) 
        print(var)
        if (var["function"]=="True"):
            raise TypeError("XD, no se puede leer una funcion")
        ci.stOperators.append(p[1])
        global recorridodimensiones
        global R
        print("R -1 =")
        print(R - 1)
        # dir base + recorrido
        ci.stOperands.append(var["address"] + (R - 1))
        ci.stTypes.append(var["type"])
        ci.gen_read()
        recorridodimensiones.clear()
        R = 1


def p_param_read(p):
    '''
    param_read : 
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUALS exp SEMICOLON
        | ID retrieve_var_dims dims EQUALS exp SEMICOLON
    '''
    print ("asignación encontrada")

    if len(p) == 5:
        print("var to look for")
        print(p[1])
        var = df.search(p[1]) 
        print(var)
        if (var["function"]=="True"):
            raise TypeError("no te pases de listo XD, se intentó asignar un valor a una función")
        ci.stOperators.append(p[2])
        ci.stOperands.append(var["address"])
        ci.stTypes.append(var["type"])
        ci.new_quadruple()
    elif len(p) == 6:
        print("var with dimensions to look for")
        print(p[1])
        var = df.search(p[1]) 
        print("unuchan")
        print(var)
        if (var["function"]=="True"):
            raise TypeError("no te pases de listo XD, se intentó asignar un valor a una función")
        ci.stOperators.append(p[3])
        global recorridodimensiones
        global R
        print("R - 1 =")
        print(R - 1)
        # dir base + recorrido
        ci.stOperands.append(var["address"] + (R - 1))
        ci.stTypes.append(var["type"])
        ci.new_quadruple()
        recorridodimensiones.clear()
        R = 1
    
def p_retrieve_var_dims(p):
    '''
    retrieve_var_dims : 
    '''
    global currdimlist
    var = df.search(p[-1]) 
    currdimlist = var["dimensions"]


def p_dims(p):
    '''
    dims : OPENBRACKET exp calculate CLOSEBRACKET dims
        | OPENBRACKET exp calculate CLOSEBRACKET
    '''

def p_calculate(p):
    '''
    calculate : 
    '''
    global recorridodimensiones
    global R
    global currdimlist
    if (ci.stTypes.pop()=="int"):
        #recorridodimensiones.append(ci.stOperands.pop())
        dim = ci.stOperands.pop()
        print("dimiss")
        print(dim)
        dct = dict(ci.ctes_table)
        val = dct.get(dim)
        print("dimbasado")
        print(val)
        if len(currdimlist) != 0:
            currdimfromvar = currdimlist.pop()
            print("now comparing2")
            print(currdimfromvar)
            print(val)
        else:
            raise TypeError("se introdujeron mas dimensiones de las que tiene la variable")
        if val >= 0 and val < currdimfromvar:
            R = R * (val+1)
        else:
            raise TypeError("indice no valido")
    else:
        raise TypeError("dimension should be inttttt")


def p_escritura(p):
    '''
    escritura : WRITE OPENPARENTHESES escrituraP CLOSEPARENTHESES SEMICOLON
    '''
    ci.stOperators.append(p[1])
    ci.gen_write()
    

def p_escrituraP(p):
    '''
    escrituraP : exp
                | writestring
    '''

def p_writestring(p):
    '''
    writestring : CTESTRING
    '''
    print ("CTE string found!")
    address = ci.get_address("char", "constants", p[1])
    ci.stTypes.append("char")
    ci.stOperands.append(address)

def p_condicion(p):
    '''
    condicion : IF OPENPARENTHESES exp CLOSEPARENTHESES OPENBRACE gen_gotof condicionp fill_goto
    '''

def p_gen_gotof(p):
    '''
    gen_gotof : 
    '''
    ci.gen_gotoF()
    

def p_fill_gotof(p):
    '''
    fill_gotof : 
    '''
    ci.fill_gotof()

def p_gen_goto(p):
    '''
    gen_goto : 
    '''
    ci.gen_goto()

def p_fill_goto(p):
    '''
    fill_goto : 
    '''
    ci.fill_goto()

def p_fill_gotof_if(p):
    '''
    fill_gotof_if : 
    '''
    ci.fill_gotoF_if()

def p_condicionp(p):
    # soporta if, if else, if else if, if else if else
    '''
    condicionp : estatuto fill_gotof_if gen_goto CLOSEBRACE ELSE OPENBRACE estatuto CLOSEBRACE
          | estatuto fill_gotof_if gen_goto CLOSEBRACE ELSE condicion
          | estatuto fill_gotof_if gen_goto CLOSEBRACE
    '''

def p_repeticion(p):
    '''
    repeticion : condicional
        | no_condicional
    '''

def p_condicional(p):
    '''
    condicional : WHILE OPENPARENTHESES migaja exp gen_gotof CLOSEPARENTHESES OPENBRACE estatuto fill_gotof_while gen_goto_migaja CLOSEBRACE 
    '''

def p_migaja(p):
    '''
    migaja : 
    '''
    ci.migaja()

def p_gen_goto_migaja(p):
    '''
    gen_goto_migaja : 
    '''
    ci.gen_goto_migaja()

def p_gen_goto_while(p):
    '''
    gen_goto_while : 
    '''
    ci.gen_goto_while()

def p_gen_fill_goto(p):
    '''
    gen_fill_goto : 
    '''
    ci.gen_fill_goto()

def p_fill_goto_while(p):
    '''
    fill_goto_while : 
    '''
    ci.fill_goto_while()

def p_fill_gotof_while(p):
    '''
    fill_gotof_while : 
    '''
    ci.fill_gotof_while()


def p_nocondicional(p):
    '''
    no_condicional : FOR ID EQUALS exp TO exp OPENBRACE estatuto CLOSEBRACE
    '''


def p_exp(p):
    '''
    exp : iexp
        | NOT iexp
    '''
    if (len(p)==3):
        ci.stOperators.append(p[1])
        ci.gen_not_quadruple()



def p_iexp(p):
    '''
    iexp : nexp
        | iexp AND nexp
        | iexp OR nexp
    '''
    if (len(p)==4):
        #ci.stOperands.append(p[1])
        #print("p[1]")
        #print(p[1])
        ci.stOperators.append(p[2])
        print("p[2]")
        print(p[2])
        #ci.stOperands.append(p[3])
        #print("p[3]")
        #print(p[3])
        #ci.stTypes.append("int")
        print("_____stacks___")
        print(ci.stTypes)
        print(ci.stOperands)
        print(ci.stOperators)
        ci.new_quadruple()

def p_nexp(p):
    '''
    nexp : pexp
        | nexp GREATER pexp
        | nexp LESS pexp
        | nexp DIFFERENT pexp
        | nexp EQUALS_BOOLEAN pexp
        | nexp LESSEQUAL pexp
        | nexp GREATEREQUAL pexp
    '''
    if (len(p)==4):
        #ci.stOperands.append(p[1])
        #print("p[1]")
        #print(p[1])
        ci.stOperators.append(p[2])
        print("p[2]")
        print(p[2])
        #ci.stOperands.append(p[3])
        #print("p[3]")
        #print(p[3])
        #ci.stTypes.append("int")
        print("_____stacks___")
        print(ci.stTypes)
        print(ci.stOperands)
        print(ci.stOperators)
        ci.new_quadruple()


def p_pexp(p):
    '''
    pexp : termino
        | pexp PLUS termino
        | pexp MINUS termino
    '''
    if (len(p)==4):
        #ci.stOperands.append(p[1])
        #print("p[1]")
        #print(p[1])
        ci.stOperators.append(p[2])
        print("p[2]")
        print(p[2])
        #ci.stOperands.append(p[3])
        #print("p[3]")
        #print(p[3])
        #ci.stTypes.append("int")
        print("_____stacks___")
        print(ci.stTypes)
        print(ci.stOperands)
        print(ci.stOperators)
        ci.new_quadruple()
        # en este momento se genera un temporal que se agrega al stack de 
        # operandos dentro del archivo de codigo intermedio
        # p[0] = p[1] * p[3]

def p_termino(p):
    '''
    termino : factor
    | termino MULTIPLY factor
    | termino DIVIDE factor
    '''
    if (len(p)==4):
        #ci.stOperands.append(p[1])
        #print("p[1]")
        #print(p[1])
        ci.stOperators.append(p[2])
        print("p[2]")
        print(p[2])
        #ci.stOperands.append(p[3])
        #print("p[3]")
        #print(p[3])
        #ci.stTypes.append("int")
        print("_____stacks___")
        print(ci.stTypes)
        print(ci.stOperands)
        print(ci.stOperators)
        ci.new_quadruple()
        # en este momento se genera un temporal que se agrega al stack de 
        # operandos dentro del archivo de codigo intermedio
        # p[0] = p[1] * p[3]


def p_factor(p):
    # falta meter ids con dimensiones
    '''
    factor :
        | CTEF
        | CTEI
        | CTEC
        | ID
        | CTEB
        | llamada printt printt
        | OPENPARENTHESES exp CLOSEPARENTHESES
        | ID retrieve_var_dims dims 
    '''
    if (len(p)==3):
        print("var with dimensions to look for")
        print(p[1])
        var = df.search(p[1]) 
        print(var)
        global R
        print("R - 1 =")
        print(R - 1)
        # dir base + recorrido
        ci.stOperands.append(var["address"] + (R - 1))
        ci.stTypes.append(var["type"])
        R = 1
    if (len(p) == 2):
        print("trying...")
        print(p[1])
        if bool(re.match("-?([0-9])+\.([0-9])*", str(p[1]))):
            print("CTEFf found!")
            #print(parser.token().type)
            address = ci.get_address("float", "constants", p[1])
            ci.stTypes.append("float")
            ci.stOperands.append(address)
        elif bool(re.match("-?\d+", str(p[1]))):
            print("CTEI found!")
            address = ci.get_address("int", "constants", p[1])
            ci.stTypes.append("int")
            ci.stOperands.append(address)
        elif bool(re.match("^(?i)(TRUE|FALSE)$", str(p[1]))):
            print("CTE BOOL found!")
            print(str(p[1]))
            address = ci.get_address("bool", "constants", p[1])
            ci.stTypes.append("bool")
            ci.stOperands.append(address)
        elif bool(re.match("[a-zA-Z][a-zA-Z_0-9]*", str(p[1]))):
            print("ID found!")
            #print(parser.token().type)
            var = df.search(p[1])
            ci.stTypes.append(var["type"])
            ci.stOperands.append(var["address"])
        elif bool(re.match('"(.?)"', str(p[1]))):
            print ("CTE CHAR found!")
            address = ci.get_address("char", "constants", p[1])
            ci.stTypes.append("char")
            ci.stOperands.append(address)
        else:
            raise TypeError("XD")
        
def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
   print("Syntax error in input!")


parser = yacc.yacc()

if __name__ == '__main__':
    try:
        archivo = open('./tests/test_recursivosimple.txt','r')
        info = archivo.read()
        lexer.input(info)
        #tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok)
        archivo.close()
        if(yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("success")
            df.print_var()
            ci.new_obj_file(str(df.function_dictionary))
        else:
            print("syntax error")
    except EOFError:
        print(EOFError)