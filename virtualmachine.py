import json
  
# Opening JSON file
f = open('obj.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
dict_ctes = dict(data['ctes_table'])
#dict_quad = dict(data['Quadruples'])
dict_temp = {}
dict_aux = {}
cont = 0

function_stack = []
auxiliar_pair = (1, 2)

  
# Iterating through the json
# list


while True:
    #Si llegamos al ultimo quadruplo, se termina
    if cont == len(data['Quadruples']):
        break 
    
    #Print para el quadruplo que se esta ejecutando
    print(data['Quadruples'][cont])
    
    #SI EL CUADRUPLO ES UN "*"
    if data['Quadruples'][cont][1] == '*':
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) * dict_ctes.get(data['Quadruples'][cont][3])
                print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) * dict_temp[data['Quadruples'][cont][3]]
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
        else:
            if data['Quadruples'][cont][2] in dict_temp:
                if data['Quadruples'][cont][3] >= 30000:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] * dict_ctes.get(data['Quadruples'][cont][3])
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] * dict_temp[data['Quadruples'][cont][3]]
                        print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                        print("-->", "dict_temp =", dict_temp)
                        
    #SI EL CUADRUPLO ES UN "/"
    if data['Quadruples'][cont][1] == '/':
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) / dict_ctes.get(data['Quadruples'][cont][3])
                print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) / dict_temp[data['Quadruples'][cont][3]]
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
        else:
            if data['Quadruples'][cont][2] in dict_temp:
                if data['Quadruples'][cont][3] >= 30000:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] / dict_ctes.get(data['Quadruples'][cont][3])
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] / dict_temp[data['Quadruples'][cont][3]]
                        print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                        print("-->", "dict_temp =", dict_temp)
                        
    #SI EL CUADRUPLO ES UN "+"
    if data['Quadruples'][cont][1] == '+':
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) + dict_ctes.get(data['Quadruples'][cont][3])
                print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) + dict_temp[data['Quadruples'][cont][3]]
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
        else:
            if data['Quadruples'][cont][2] in dict_temp:
                if data['Quadruples'][cont][3] >= 30000:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] + dict_ctes.get(data['Quadruples'][cont][3])
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] + dict_temp[data['Quadruples'][cont][3]]
                        print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                        print("-->", "dict_temp =", dict_temp)
                        
    #SI EL CUADRUPLO ES UN "-"
    if data['Quadruples'][cont][1] == '-':
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) - dict_ctes.get(data['Quadruples'][cont][3])
                print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) - dict_temp[data['Quadruples'][cont][3]]
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
        else:
            if data['Quadruples'][cont][2] in dict_temp:
                if data['Quadruples'][cont][3] >= 30000:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] - dict_ctes.get(data['Quadruples'][cont][3])
                    print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                    print("-->", "dict_temp =", dict_temp)
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] - dict_temp[data['Quadruples'][cont][3]]
                        print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                        print("-->", "dict_temp =", dict_temp)
    
    #SI EL CUADRUPLO ES "NOT"
    if data['Quadruples'][cont][1] == 'not':
        if data['Quadruples'][cont][3] >= 30000:
            if data['Quadruples'][cont][1] == 37500:
                dict_temp[data['Quadruples'][cont][4]] = 'false'
                print("-->", "not true = false")
                print("-->", "dict_temp =", dict_temp)
            else:
                dict_temp[data['Quadruples'][cont][4]] = 'true'
                print("-->", "not false = true")
                print("-->", "dict_temp =", dict_temp)
        else:
            if data['Quadruples'][cont][3] in dict_temp:
                if dict_temp[data['Quadruples'][cont][3]] == 'true':
                    dict_temp[data['Quadruples'][cont][4]] = 'false'
                    print("-->", "not true = false")
                    print("-->", "dict_temp =", dict_temp)
                else:
                    dict_temp[data['Quadruples'][cont][4]] = 'true'
                    print("-->", "not false = true")
                    print("-->", "dict_temp =", dict_temp)
            
    
    #SI EL CUADRUPLO ES "ERA"
    if data['Quadruples'][cont][3] == 'ERA':
        auxiliar_pair = (dict_temp, cont)
        function_stack.append(auxiliar_pair)
        print("DSDIDI")
        print("-->", function_stack)
        dict_temp.clear()
        print("-->", "dict_temp =", dict_temp)
    
    #SI EL CUADRUPLO ES "="
    if data['Quadruples'][cont][1] == '=':
        if data['Quadruples'][cont][3] >= 30000:
            print("-->", data['Quadruples'][cont][4], '=', data['Quadruples'][cont][3])
            dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][3])
            print("-->", dict_temp)
        else:
            if data['Quadruples'][cont][3] in dict_temp:
                print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][3])
                dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][3]]
                print("-->", dict_temp)
            
    #SI EL CUADRUPLO ES "or"
    if data['Quadruples'][cont][1] == 'or':
        if data['Quadruples'][cont][3] >= 30000:
            print("-->", dict_ctes.get(data['Quadruples'][cont][2]), "or", dict_ctes.get(data['Quadruples'][cont][3]))
            if dict_ctes.get(data['Quadruples'][cont][2]) == "true" or dict_ctes.get(data['Quadruples'][cont][3]) == "true":
                dict_temp[data['Quadruples'][cont][4]] = "true"
                print("-->", dict_temp)

    """
    #SI EL CUADRUPLO ES GOTO
    if data['Quadruples'][cont][3] == 'GOTO':
        print(data['Quadruples'][cont][4])
        cont = data['Quadruples'][cont][4] - 2 #Brinca uno antes del cuadruplo por cont + 1
        
    #SI EL CUADRUPLO ES GOTOF
    if data['Quadruples'][cont][3] == 'GOTOF':
        print(dict_ctes.get(data['Quadruples'][cont][1]))
        if dict_ctes.get(data['Quadruples'][cont][1]) == "false":
            print(data['Quadruples'][cont][4])
            cont = data['Quadruples'][cont][4] - 2 #Brinca uno antes del cuadruplo por cont + 1
    """
    
    cont = cont + 1

print(data['Func_dir'])
    
for i in data['ctes_table']:
    print(i)

auxiliar_pair = (dict_temp, cont)
function_stack.append(auxiliar_pair)
print(function_stack)
function_stack.pop()
print(function_stack)
# Closing file
f.close()