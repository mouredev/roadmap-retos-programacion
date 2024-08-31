# Tipos de datos por valor 

variable_a = 20

variable_b = variable_a

variable_b = 40

print(variable_a)
print(variable_b)

# Tipos de datos por referencia

my_lista_1 = [1,2,3]

my_lista_2 = my_lista_1

my_lista_3 = my_lista_2

my_lista_2.append(4)

print(my_lista_1)
print(my_lista_2)
print(my_lista_3)

# Funciones con datos por valor

def función_valor(value:int):
    value = value + 10
    print(value)

# Funciones con datos por referencia
    
def funcion_referencia(lista:list):
    lista_2 = lista
    lista_2.append(50)
    print(lista)
    print(lista_2)
    
     
función_valor(10)
funcion_referencia([10,20,30,40])
print()

""" Extra """

variable_1:int = 10
variable_2:int = 20

def variables(var_1, var_2):
    var_1, var_2 = var_2, var_1    
    
    return var_1, var_2

new_var_1, new_var_2 = variables(variable_1,variable_2)

print(f"Parametros: {variable_1} - {variable_2} \nRetorno: {new_var_1} - {new_var_2}")

lista_1:list = [10,20,30]
lista_2:list = [40,50,60]

new_lista_1, new_lista_2 = variables(lista_1,lista_2) 
print(f"Parametros: {lista_1} - {lista_2} \nRetorno: {new_lista_1} - {new_lista_2}")