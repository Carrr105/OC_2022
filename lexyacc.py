# Proyecto Final Compiladores gpo 2
# Carlos Gerardo Herrera Cortina - A00821946
# Omar Alejandro Balboa Lara - A00825034
import sys
import ply.lex as lex
import ply.yacc as yacc
import SemanticCube
from DirFunc import DirFunc as df
from CodigoIntermedio import CI as ci

df = df()
ci = ci()

reserved = {
    'program' : 'PROGRAM',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'class' : 'CLASS',
    'vars' : 'VARS',
    'function' : 'FUNCTION',
    'main' : 'MAIN',
    'read' : 'READ',
    'return' : 'RETURN',
    'write' : 'WRITE',
    'then' : 'THEN',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'to' : 'TO',
    'and' : 'AND',
    'or' : 'OR', 
    'return' : 'RETURN'
    
}

tokens = [
    'ID', 'CTEI', 'CTEF',
    'OPENPARENTHESES', 'CLOSEPARENTHESES',
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTESTRING(t):
    r'%([^.]+?)%'
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

start = 'programa'
globalname = ''

def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON establishglobalscope programaP
    '''
    p[0] = "PROGRAM COMPILED"

# este tipo de reglas vacias servirán para poder hacer acciones intermedias,
# ya que PLY no cuenta con un soporte natural para ellas.
# es una "mexicanada" pero sirve
def p_establishglobalscope(p):
    "establishglobalscope :"
    global scopestack
    scopestack.append(p[-2])
    df.insert_function(p[-2], "void")
    df.print_functions()
    globalname = p[-2]
    print("global scope name is ")
    print(globalname)

def p_programaP(p):
    '''
    programaP : vars programaP
    | clase programaP
    | funcion programaP
    | bloque
    | empty
    '''

def p_clase(p):
    '''
    clase : CLASS ID OPENBRACE claseP CLOSEBRACE
    '''

## cero o más declaraciones de vars. 
def p_claseP(p):
    '''
    claseP : vars clasePP
         | clasePP
    '''
# cero o más funcion
def p_clasePP(p):
    '''
    clasePP : funcion clasePP
            | empty
    '''

def p_funcion(p):
    '''
    funcion : FUNCTION tipo TWODOTS ID savefuncscope OPENPARENTHESES paramsfunction CLOSEPARENTHESES OPENBRACE CLOSEBRACE
    '''

def p_savefuncscope(p):
    '''
    savefuncscope : 
    '''
    global scopestack
    scopestack.append(p[-1])
    df.insert_function(p[-1], p[-3])

def p_paramsfunction(p):
    '''
    paramsfunction : tipo param COMMA paramsfunction
                    | tipo param
    '''


def p_return(p):
    '''
    return : RETURN exp
            | RETURN
    '''

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

def p_param(p):
    '''
    param : ID
        | ID OPENBRACKET paramsP CLOSEBRACKET
    '''
    df.insert_var(scopestack[-1], p[1], type_var)

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
    '''
    p[0] = p[1]

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
    df.insert_function("main", "void")
    df.print_functions()
    print("main has been found")

def p_estatuto(p):
    '''
    estatuto : asignacion estatuto
        | llamada estatuto
        | retorno estatuto
        | lectura estatuto
        | escritura estatuto
        | repeticion estatuto
        | estatuto estatuto
        | declaracion estatuto
        | empty
    '''

def p_declaracion(p):
    '''
    declaracion : vars
    '''

def p_llamada(p):
    '''
    llamada : ID OPENPARENTHESES param CLOSEPARENTHESES SEMICOLON
        | ID OPENPARENTHESES CLOSEPARENTHESES SEMICOLON
    '''

def p_retorno(p):
    '''
    retorno : RETURN OPENPARENTHESES exp CLOSEPARENTHESES SEMICOLON
    '''

def p_lectura(p):
    '''
    lectura : READ OPENPARENTHESES param CLOSEPARENTHESES SEMICOLON
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUALS exp SEMICOLON
        | ID OPENBRACKET paramsP CLOSEBRACKET EQUALS exp SEMICOLON
    '''
    print ("asignación encontrada")
    if len(p) == 5:
        ci.stOperators.append(p[2])
        ci.stOperands.append(p[1])
        ci.stTypes.append("int")
        ci.new_quadruple()

def p_escritura(p):
    '''
    escritura : WRITE OPENPARENTHESES escrituraP CLOSEPARENTHESES SEMICOLON
    '''

def p_escrituraP(p):
    '''
    escrituraP : QUOTATIONMARK CTESTRING QUOTATIONMARK COMMA escrituraP
        | exp COMMA escrituraP
        | ID COMMA escrituraP
        | QUOTATIONMARK CTESTRING QUOTATIONMARK
        | exp
        | ID
    '''

def p_condicion(p):
    '''
    condicion : IF OPENPARENTHESES exp CLOSEPARENTHESES THEN OPENBRACE estatuto CLOSEBRACE ELSE OPENBRACE estatuto CLOSEBRACE
          | IF OPENPARENTHESES exp CLOSEPARENTHESES THEN OPENBRACE CLOSEBRACE ELSE OPENBRACE estatuto CLOSEBRACE
          | IF OPENPARENTHESES exp CLOSEPARENTHESES THEN OPENBRACE estatuto CLOSEBRACE ELSE OPENBRACE CLOSEBRACE
          | IF OPENPARENTHESES exp CLOSEPARENTHESES THEN OPENBRACE estatuto CLOSEBRACE
          | IF OPENPARENTHESES exp CLOSEPARENTHESES THEN OPENBRACE CLOSEBRACE
    '''

def p_repeticion(p):
    '''
    repeticion : condicional
        | no_condicional
    '''

def p_condicional(p):
    '''
    condicional : WHILE OPENPARENTHESES exp CLOSEPARENTHESES DO OPENBRACE estatuto CLOSEBRACE
        | WHILE OPENPARENTHESES exp CLOSEPARENTHESES DO OPENBRACE CLOSEBRACE
    '''

def p_nocondicional(p):
    '''
    no_condicional : FOR ID EQUALS exp TO exp OPENBRACE estatuto CLOSEBRACE
        | FOR ID EQUALS exp TO exp DO OPENBRACE CLOSEBRACE
    '''



def p_exp(p):
    '''
    exp : termino
    | exp PLUS termino
    | exp MINUS termino
    '''
    if (len(p)==4):
        if p[2] == '+':
            p[0] = p[1] + p[3]
            print ("suma encontrada")
        elif p[2] == '-':
            p[0] = p[1] - p[3]

def p_termino(p):
    '''
    termino : factor
    | termino MULTIPLY factor
    | termino DIVIDE factor
    '''
    if (len(p)==4):
        if p[2] == '*':
            #ci.stOperands.append(p[1])
            #print("p[1]")
            #print(p[1])
            ci.stOperators.append(p[2])
            print("p[2]")
            print(p[2])
            #ci.stOperands.append(p[3])
            #print("p[3]")
            #print(p[3])
            ci.stTypes.append("int")
            ci.new_quadruple()
            # en este momento se genera un temporal que se agrega al stack de 
            # operandos dentro del archivo de codigo intermedio
            # p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]


def p_factor(p):
    '''
    factor : ID OPENPARENTHESES exp CLOSEPARENTHESES
    | ID
    | CTEF
    | CTEI
    | OPENPARENTHESES h_exp CLOSEPARENTHESES
    '''
    if (len(p) == 2):
        address = ci.get_address("int", "constants", 1, p[1])
        ci.stTypes.append("int")
        ci.stOperands.append(address)
        resultstack.append(p[1])
        print("p[1]")
        print(p[1])

def p_hexp(p):
    '''
    h_exp : s_exp
    | s_exp AND h_exp
    | s_exp OR h_exp
    '''
    if p[2] == 'AND':
         p[0] = p[1] and p[3]
    elif p[2] == 'OR':
         p[0] = p[1] or p[3]

def p_sexp(p):
    '''
    s_exp : exp
    | exp GREATER exp
    | exp LESS exp
    | exp DIFFERENT exp
    | exp EQUALS_BOOLEAN exp
    | exp LESSEQUAL exp
    | exp GREATEREQUAL exp
    '''
    if p[2] == '>':
         p[0] = p[1] > p[3]
    elif p[2] == '<':
         p[0] = p[1] < p[3]
    elif p[2] == '!=':
         p[0] = p[1] != p[3]
    elif p[2] == '==':
         p[0] = p[1] == p[3]
    elif p[2] == '<=':
         p[0] = p[1] >= p[3]
    elif p[2] == '>=':
         p[0] = p[1] <= p[3]

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
        archivo = open('test.txt','r')
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
            ci.new_obj_file()
        else:
            print("syntax error")
    except EOFError:
        print(EOFError)