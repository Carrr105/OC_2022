import json
  
# Opening JSON file
f = open('obj.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
dict_ctes = dict(data['ctes_table'])
dict_func = eval(data['Func_dir'])
#dict_quad = dict(data['Quadruples'])
dict_temp = {}
dict_copy = {}
dict_aux = {}
dict_point = {}
list_aux = []
cont = 0
contador_guadalupano = 0
function_name = ''
era_jump = 0
int_aux = 0
main_quad = 0

function_stack = []
auxiliar_pair = (1, 2)

dict_test = {9999: 2, 2222: 9}
# Iterating through the json
# list


while True:
    #Si llegamos al ultimo quadruplo, se termina
    if cont == len(data['Quadruples']):
        break 
    
    ##Print para el quadruplo que se esta ejecutando
    print(data['Quadruples'][cont])
    
    #SI EL CUADRUPLO ES UN "GOSUB"
    if data['Quadruples'][cont][3] == 'GOSUB':
        contador_guadalupano = 0
        dict_copy = dict(dict_temp)
        auxiliar_pair = (dict_copy, cont+1)
        function_stack.append(auxiliar_pair)
        dict_temp = dict(dict_aux)
        dict_aux.clear()
        cont = era_jump
        for function, value in dict_temp.items():
            list_aux.append(value)
        for function, value in dict_func[function_name]['vars'].items():
            if (len(list_aux) != 0 ):
                value['value'] = list_aux[contador_guadalupano]
                contador_guadalupano = contador_guadalupano + 1
            if contador_guadalupano == len(dict_func[function_name]['params']):
                break
        list_aux.clear()
    
    #SI EL CUADRUPLO ES UN "*"
    elif data['Quadruples'][cont][1] == '*':
        #print("SI LO ESTOY ENCONTRANDO")
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) * dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) * dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        elif data['Quadruples'][cont][2] in dict_temp:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] * dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] * dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "*", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        else:
            #print("SI ESTOY ENTRANDO")
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][2]:
                    dict_temp[data['Quadruples'][cont][4]] = value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][3]:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][4]] * value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
                        
    #SI EL CUADRUPLO ES UN "/"
    elif data['Quadruples'][cont][1] == '/':
        #print("SI LO ESTOY ENCONTRANDO")
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) / dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) / dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        elif data['Quadruples'][cont][2] in dict_temp:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] / dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] / dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "/", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        else:
            #print("SI ESTOY ENTRANDO")
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][2]:
                    dict_temp[data['Quadruples'][cont][4]] = value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][3]:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][4]] / value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
                        
    #SI EL CUADRUPLO ES UN "+"
    elif data['Quadruples'][cont][1] == '+':
        #print("SI LO ESTOY ENCONTRANDO")
        if data['Quadruples'][cont][4] >= 40000:
            if data['Quadruples'][cont][2] >= 30000:
                dict_point[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) + data['Quadruples'][cont][3]
                print(dict_point)
            else:
                dict_point[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] + data['Quadruples'][cont][3]
                print(dict_point[data['Quadruples'][cont][4]], "=" ,dict_temp[data['Quadruples'][cont][2]], "+" ,data['Quadruples'][cont][3])
                print(dict_point)
        elif data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) + dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) + dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        elif data['Quadruples'][cont][2] in dict_temp:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] + dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] + dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "+", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        else:
            #print("SI ESTOY ENTRANDO")
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][2]:
                    dict_temp[data['Quadruples'][cont][4]] = value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][3]:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][4]] + value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
        print("-->", "dict_temp =", dict_temp)
                        
    #SI EL CUADRUPLO ES UN "-"
    elif data['Quadruples'][cont][1] == '-':
        #print("SI LO ESTOY ENCONTRANDO")
        if data['Quadruples'][cont][2] >= 30000:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) - dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][2]) - dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        elif data['Quadruples'][cont][2] in dict_temp:
            if data['Quadruples'][cont][3] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] - dict_ctes.get(data['Quadruples'][cont][3])
                #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                #print("-->", "dict_temp =", dict_temp)
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][2]] - dict_temp[data['Quadruples'][cont][3]]
                    #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][2], "-", data['Quadruples'][cont][3])
                    #print("-->", "dict_temp =", dict_temp)
        else:
            #print("SI ESTOY ENTRANDO")
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][2]:
                    dict_temp[data['Quadruples'][cont][4]] = value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][3]:
                    dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][4]] - value['value']
                    #print(value['address'], '=', value['value'])
                    #print("-->", "dict_temp =", dict_temp)
    
    #SI EL CUADRUPLO ES "NOT"
    elif data['Quadruples'][cont][1] == 'not':
        if data['Quadruples'][cont][3] >= 30000:
            if data['Quadruples'][cont][1] == 37500:
                dict_temp[data['Quadruples'][cont][4]] = 'false'
                #print("-->", "not true = false")
                #print("-->", "dict_temp =", dict_temp)
            else:
                dict_temp[data['Quadruples'][cont][4]] = 'true'
                #print("-->", "not false = true")
                #print("-->", "dict_temp =", dict_temp)
        else:
            if data['Quadruples'][cont][3] in dict_temp:
                if dict_temp[data['Quadruples'][cont][3]] == 'true':
                    dict_temp[data['Quadruples'][cont][4]] = 'false'
                    #print("-->", "not true = false")
                    #print("-->", "dict_temp =", dict_temp)
                else:
                    dict_temp[data['Quadruples'][cont][4]] = 'true'
                    #print("-->", "not false = true")
                    #print("-->", "dict_temp =", dict_temp)
            
    
    #SI EL CUADRUPLO ES "ERA"
    elif data['Quadruples'][cont][3] == 'ERA':
        #print("--> ERA =", dict_func[data['Quadruples'][cont][4]]['ip'])
        function_name = data['Quadruples'][cont][4]
        #print("-->", function_name)
        era_jump = dict_func[data['Quadruples'][cont][4]]['ip'] - 2
        """
        auxiliar_pair = (dict_temp, cont)
        function_stack.append(auxiliar_pair)
        #print("DSDIDI")
        #print("-->", function_stack)
        dict_temp.clear()
        #print("-->", "dict_temp =", dict_temp)
        """
        
    #SI EL CUADRUPLO ES "PARAM"
    elif data['Quadruples'][cont][1] == 'PARAM':
        if data['Quadruples'][cont][3] >= 30000:
            dict_aux[data['Quadruples'][cont][3]] = dict_ctes[data['Quadruples'][cont][3]]
            #print("-->", dict_aux)
        else:
            if data['Quadruples'][cont][3] in dict_temp:
                dict_aux[data['Quadruples'][cont][3]] = dict_temp[data['Quadruples'][cont][3]]
                #print("-->", dict_aux)
    
    # #SI EL CUADRUPLO ES UN "GOSUB"
    # if data['Quadruples'][cont][3] == 'GOSUB':
    #     dict_copy = dict(dict_temp)
    #     auxiliar_pair = (dict_copy, cont+1)
    #     function_stack.append(auxiliar_pair)
    #     """
    #     dict_copy = dict_test
    #     auxiliar_pair = (dict_copy, cont)
    #     function_stack.append(auxiliar_pair)
    #     """
    #     #print("--> GUARDADO = ", function_stack)
    #     dict_temp = dict(dict_aux)
    #     #print("--> dict_temp = ", dict_temp)
    #     """
    #     #print("--> dict_temp = ", dict_temp)
    #     #print("--> dict_aux = ", dict_aux)
    #     #print("Este es el tipo: ", type(dict_temp))
    #     """
    #     dict_aux.clear()
    #     #print("--> dict_aux = ", dict_aux)
    #     #print("--> CLEAN = ", dict_temp)
    #     cont = era_jump + 1
    #     #print(dict_func[function_name]['vars']['uno']['address'])
    #     for function, value in dict_temp.items():
    #         #print(value)
    #         list_aux.append(value)
    #     # #print("THIS IS THE LIST =", list_aux)
    #     # #print("THE N ELEMENT IS THE =", list_aux[1])
    #     for function, value in dict_func[function_name]['vars'].items():
    #         #value['value'] = dict_temp[contador_guadalupano]
    #         # list_aux = list(dict_temp)[0][contador_guadalupano]
    #         # value['value'] = list_aux
    #         ##print("------------>", value['value'], "=" ,dict_temp[contador_guadalupano])
    #         ##print(list(dict_func))
    #         value['value'] = list_aux[contador_guadalupano]
    #         #print("THE NEW VALUE IS: ", value['value'])
    #         #print('contador guadalupano =', contador_guadalupano)
    #         contador_guadalupano = contador_guadalupano + 1
    #     list_aux.clear()
    #     #print(data['Quadruples'][cont])
    #     """
    #     #print("--> function_stack = ", function_stack)
    #     #print("--> dict_temp = ", dict_temp)
    #     #print("--> dict_aux = ", dict_aux)
    #     """
    
    #SI EL CUADRUPLO ES UN "RETURN"
    elif data['Quadruples'][cont][3] == 'RETURN':
        #print("-->", "dict_tempppp =", dict_temp)
        if data['Quadruples'][cont][2] is not None:
            if data['Quadruples'][cont][2] >= 30000 and function_name != '':
                dict_func[function_name]['value'] = dict_ctes[data['Quadruples'][cont][2]]
                #print(dict_func['global']['vars'][function_name]['address'], "=" ,dict_ctes[data['Quadruples'][cont][2]])
                #print(dict_func[function_name]['value'])
            elif data['Quadruples'][cont][2] in dict_temp and function_name != '':
                # # dict_func[function_name]['value'] = dict_temp[data['Quadruples'][cont][2]]
                # dict_func['global']['vars'][function_name]['value'] = dict_temp[data['Quadruples'][cont][2]]
                # #print(dict_func['global']['vars'][function_name]['address'], "=" , dict_temp[data['Quadruples'][cont][2]])
                # #print(dict_func[function_name]['vars']['value'])
                # #print("-->", "dict_temp =", dict_temp)
                # #print("do we are going to finish")
                for function, value in dict_func['global']['vars'].items():
                    if value['address'] == data['Quadruples'][cont][4]:
                        value['value'] = dict_temp[data['Quadruples'][cont][2]]
                        #print(value['address'], '=', value['value'])
                        #print("-->", "dict_temp =", dict_temp)
            #else:
                #print("UNA FUNCION SE ASIGNO A OTRA FUNCION")
        if function_stack:
            auxiliar_pair = function_stack.pop()
            #print("--> ENDFUNCTION")
            #print("--> auxiliar_pairHFIEHFGIEUHFEWUIHEFWUIHEFWIUHEFWUIHFEWUIHFEWUIHFEWIUHEFWUIHFEWUIHWFE = ", auxiliar_pair)
            dict_temp = auxiliar_pair[0]
            cont = auxiliar_pair[1] - 1
            #print(data['Quadruples'][cont])

    #SI EL CUADRUPLO ES UN "ENDFUNCTION"
    elif data['Quadruples'][cont][1] == 'ENDFUNC':
        if function_stack:
            auxiliar_pair = function_stack.pop()
            #print("--> ENDFUNCTION")
            #print("--> auxiliar_pair = ", auxiliar_pair)
            dict_temp = auxiliar_pair[0]
            cont = auxiliar_pair[1] - 1
            #print(data['Quadruples'][cont])
        
    
    #SI EL CUADRUPLO ES "="
    elif data['Quadruples'][cont][1] == '=':
        if data['Quadruples'][cont][4] >= 40000:
            print("Aqui se asigna la direccion del array")
            
            #dict_point[data['Quadruples'][cont][4]] = data['Quadruples'][cont][3]
            if data['Quadruples'][cont][3] >= 30000:
                #dict_temp[dict_point[data['Quadruples'][cont][4]]] = data['Quadruples'][cont][3]
                dict_temp[dict_point[data['Quadruples'][cont][4]]] = dict_ctes.get(data['Quadruples'][cont][3])
                print("-->", "dict_temp =", dict_point) 
                print("-->", "dict_temp =", dict_temp)
            else:
                dict_temp[dict_point[data['Quadruples'][cont][4]]] = dict_temp[data['Quadruples'][cont][3]]
        elif data['Quadruples'][cont][3] >= 40000:
            if dict_point[data['Quadruples'][cont][3]] >= 30000:
                dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(dict_point[data['Quadruples'][cont][3]])
            else:
                dict_temp[data['Quadruples'][cont][4]] = dict_temp[dict_point[data['Quadruples'][cont][3]]]
        elif data['Quadruples'][cont][3] >= 30000:
            #print("-->", data['Quadruples'][cont][4], '=', data['Quadruples'][cont][3])
            dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][3])
            #print("-->", "dict_temp =", dict_temp)
        elif data['Quadruples'][cont][3] in dict_temp:
            #print("-->", data['Quadruples'][cont][4], "=", data['Quadruples'][cont][3])
            dict_temp[data['Quadruples'][cont][4]] = dict_temp[data['Quadruples'][cont][3]]
            #print("-->", "dict_temp =", dict_temp)
        # if dict_func['global']['vars'][function_name]['value'] is not None:
        # """
        # for k,v in dict_func.items():
        #     #print(k, v)
        # #print()
        # #print(dict_func['global']['vars'][function_name])
        # """
        # elif data['Quadruples'][cont][3] in dict_func['global']['vars'][function_name]:
        #     dict_temp[data['Quadruples'][cont][4]] = dict_func['global']['vars'][function_name]['value']
        #     #print(dict_func['global']['vars'][function_name]['value'])
        #     #print("-->", dict_aux)
        elif data['Quadruples'][cont][0] > main_quad:
            #print("SI ESTOY ENTRANDO A MAYOR QUE MAIN")
            for function, value in dict_func['global']['vars'].items():
                if value['address'] == data['Quadruples'][cont][3]:
                    int_aux = value['value']
                    #print("-->", "dict_temp =", dict_temp)
            for function, value in dict_func['main']['vars'].items():
                if value['address'] == data['Quadruples'][cont][4]:
                    value['value'] = int_aux
                    #print("-->", "dict_temp =", dict_temp)
        else:
            #print("SI ESTOY ENTRANDO A menor QUE MAIN")
            for function, value in dict_func['global']['vars'].items():
                if value['address'] == data['Quadruples'][cont][3]:
                    int_aux = value['value']
                    #print("-->", "dict_temp =", dict_temp)
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][4]:
                    value['value'] = int_aux
                    #print("-->", "dict_temp =", dict_temp)    
                    
    #SI EL CUADRUPLO ES "or"         
    elif data['Quadruples'][cont][1] == 'or':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Si el primer valor es true
            if dict_ctes.get(data['Quadruples'][cont][2]) == "true":
                dict_temp[data['Quadruples'][cont][4]] = "true"
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][3]) == "true":
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_temp[data['Quadruples'][cont][3]] == "true":
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
            if data['Quadruples'][cont][2] in dict_temp:
                if dict_temp[data['Quadruples'][cont][2]] == "true":
                    dict_temp[data['Quadruples'][cont][4]] = "true"
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_ctes.get(data['Quadruples'][cont][3]) == "true":
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][3]] == "true":
                            dict_temp[data['Quadruples'][cont][4]] = "true" 
        
#SI EL CUADRUPLO ES "and"         
    elif data['Quadruples'][cont][1] == 'and':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) == "true" and dict_ctes.get(data['Quadruples'][cont][3]) == "true":
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) == "true" and dict_temp[data['Quadruples'][cont][3]] == "true":
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
            if data['Quadruples'][cont][2] in dict_temp:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] == "true" and dict_ctes.get(data['Quadruples'][cont][3]) == "true":
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] == "true" and dict_temp[data['Quadruples'][cont][3]] == "true":
                            dict_temp[data['Quadruples'][cont][4]] = "true" 

    #SI EL CUADRUPLO ES GOTO
    elif data['Quadruples'][cont][3] == 'GOTO':
        if data['Quadruples'][cont][0] == 1:
            main_quad = data['Quadruples'][cont][4] - 2
        #print(data['Quadruples'][cont][4])
        cont = data['Quadruples'][cont][4] - 2 #Brinca uno antes del cuadruplo por cont + 1
        
    #SI EL CUADRUPLO ES GOTOF
    elif data['Quadruples'][cont][3] == 'GOTOF':
        if data['Quadruples'][cont][1] in dict_ctes:
            if dict_ctes.get(data['Quadruples'][cont][1]) == "false":
                #print(data['Quadruples'][cont][4])
                cont = data['Quadruples'][cont][4] - 2 #Brinca uno antes del cuadruplo por cont + 1
        else:
            if data['Quadruples'][cont][1] in dict_temp:
                if dict_temp[data['Quadruples'][cont][1]] == "false":
                    #print(data['Quadruples'][cont][4])
                    cont = data['Quadruples'][cont][4] - 2 #Brinca uno antes del cuadruplo por cont + 1
                    
    #SI EL CUADRUPLO ES "write"
    elif data['Quadruples'][cont][1] == 'write':
        if data['Quadruples'][cont][4] >= 40000:
            if dict_point[data['Quadruples'][cont][4]] >= 30000:
                print(dict_ctes.get(dict_point[data['Quadruples'][cont][4]]))
            else:
                print(dict_temp[dict_point[data['Quadruples'][cont][4]]])
        elif data['Quadruples'][cont][4] >= 30000:
            print(dict_ctes[data['Quadruples'][cont][4]])
        elif data['Quadruples'][cont][4] in dict_temp:
            print(dict_temp[data['Quadruples'][cont][4]])
            print("entro aqui")
        elif data['Quadruples'][cont][0] > main_quad:
            #print("SI ESTOY ENTRANDO A MAYOR QUE MAIN")
            for function, value in dict_func['main']['vars'].items():
                if value['address'] == data['Quadruples'][cont][4]:
                    print(value['value'])
                    #print("-->", "dict_temp =", dict_temp)
        else:
            #print("SI ESTOY ENTRANDO A menor QUE MAIN")
            for function, value in dict_func[function_name]['vars'].items():
                if value['address'] == data['Quadruples'][cont][4]:
                    print(value['value'])
                    #print("-->", "dict_temp =", dict_temp)
            
    #SI EL CUADRUPLO ES "read"
    elif data['Quadruples'][cont][1] == 'read':
        if data['Quadruples'][cont][4] >= 30000:
            dict_temp[data['Quadruples'][cont][4]] = input()
            #print("input =", dict_temp[data['Quadruples'][cont][4]])
        elif data['Quadruples'][cont][4] in dict_temp:
            dict_temp[data['Quadruples'][cont][4]] = input()
        else:
            print("found a read")
            print(dict_func)

            #print("input =", dict_temp[data['Quadruples'][cont][4]])

    #AQUI COMIENZAN TODOS LOS OPERADORES RELACIONALES

    #SI EL CUADRUPLO ES '<'
    elif data['Quadruples'][cont][1] == '<':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) < dict_ctes.get(data['Quadruples'][cont][3]):
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) < dict_temp[data['Quadruples'][cont][3]]:
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] < dict_ctes.get(data['Quadruples'][cont][3]):
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] < dict_temp[data['Quadruples'][cont][3]]:
                            dict_temp[data['Quadruples'][cont][4]] = "true"
                            
    #SI EL CUADRUPLO ES '<='
    elif data['Quadruples'][cont][1] == '<=':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) <= dict_ctes.get(data['Quadruples'][cont][3]):
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) <= dict_temp[data['Quadruples'][cont][3]]:
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] <= dict_ctes.get(data['Quadruples'][cont][3]):
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] <= dict_temp[data['Quadruples'][cont][3]]:
                            dict_temp[data['Quadruples'][cont][4]] = "true"
                            
    #SI EL CUADRUPLO ES '>'
    elif data['Quadruples'][cont][1] == '>':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) > dict_ctes.get(data['Quadruples'][cont][3]):
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) > dict_temp[data['Quadruples'][cont][3]]:
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] > dict_ctes.get(data['Quadruples'][cont][3]):
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] > dict_temp[data['Quadruples'][cont][3]]:
                            dict_temp[data['Quadruples'][cont][4]] = "true"
                            
    #SI EL CUADRUPLO ES '>='
    elif data['Quadruples'][cont][1] == '>=':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) >= dict_ctes.get(data['Quadruples'][cont][3]):
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) >= dict_temp[data['Quadruples'][cont][3]]:
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] >= dict_ctes.get(data['Quadruples'][cont][3]):
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] >= dict_temp[data['Quadruples'][cont][3]]:
                            dict_temp[data['Quadruples'][cont][4]] = "true"
                            
    #SI EL CUADRUPLO ES '=='
    elif data['Quadruples'][cont][1] == '==':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) == dict_ctes.get(data['Quadruples'][cont][3]):
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) == dict_temp[data['Quadruples'][cont][3]]:
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] == dict_ctes.get(data['Quadruples'][cont][3]):
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] == dict_temp[data['Quadruples'][cont][3]]:
                            dict_temp[data['Quadruples'][cont][4]] = "true"
                            
    #SI EL CUADRUPLO ES '!='
    elif data['Quadruples'][cont][1] == '!=':
        dict_temp[data['Quadruples'][cont][4]] = "false"
        #Si el primer valor esta en la tabla de constantes 30000
        if data['Quadruples'][cont][2] >= 30000:
            #Verificamos el segundo valor en todas sus formas
            if data['Quadruples'][cont][3] >= 30000:
                if dict_ctes.get(data['Quadruples'][cont][2]) != dict_ctes.get(data['Quadruples'][cont][3]):
                    dict_temp[data['Quadruples'][cont][4]] = "true"
            else:
                if data['Quadruples'][cont][3] in dict_temp:
                    if dict_ctes.get(data['Quadruples'][cont][2]) != dict_temp[data['Quadruples'][cont][3]]:
                        dict_temp[data['Quadruples'][cont][4]] = "true"
        else:
                if data['Quadruples'][cont][3] >= 30000:
                    if dict_temp[data['Quadruples'][cont][2]] != dict_ctes.get(data['Quadruples'][cont][3]):
                        dict_temp[data['Quadruples'][cont][4]] = "true"
                else:
                    if data['Quadruples'][cont][3] in dict_temp:
                        if dict_temp[data['Quadruples'][cont][2]] != dict_temp[data['Quadruples'][cont][3]]:
                            dict_temp[data['Quadruples'][cont][4]] = "true"

    elif data['Quadruples'][cont][3] == 'VERIFY':
        if data['Quadruples'][cont][1] >= 30000:
            if dict_ctes[data['Quadruples'][cont][1]] >= data['Quadruples'][cont][2]:
                print("Limite de arreglo excedido")
                exit()

    cont = cont + 1

#print("JHDCOJUDJD")
# #print(dict_func['myotherfunction']['ip'])

#print("AQUI VA EL DICCIONARIO DE FUNCIONES")
#print(dict_func)

for i in data['ctes_table']:
   print(i)

auxiliar_pair = (dict_temp, cont)
function_stack.append(auxiliar_pair)
#print(function_stack)
function_stack.pop()
#print(function_stack)
# Closing file
f.close()