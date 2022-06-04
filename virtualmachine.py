import json
  
# Opening JSON file
f = open('obj.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
dict_ctes = dict(data['ctes_table'])
#dict_quad = dict(data['Quadruples'])
dict_temp = {}
cont = 0
  
# Iterating through the json
# list

        
while True:
    #Si llegamos al ultimo quadruplo, se termina
    if cont == len(data['Quadruples']):
        break 
    #Print para el quadruplo que se esta ejecutando
    print(data['Quadruples'][cont])
    
    #SI EL CUADRUPLO ES "="
    if data['Quadruples'][cont][1] == '=':
        if data['Quadruples'][cont][3] >= 20000 and data['Quadruples'][cont][3] < 25000:
            print(data['Quadruples'][cont][4], '=', data['Quadruples'][cont][3])
            dict_temp[data['Quadruples'][cont][4]] = dict_ctes.get(data['Quadruples'][cont][3])
            print(dict_temp)
    
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
    
    cont = cont + 1

print(data['Func_dir'])
    
for i in data['ctes_table']:
    print(i)
    

# Closing file
f.close()