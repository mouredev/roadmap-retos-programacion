# DATOS POR VALOR Y REFERENCIA EN PYTHON 


# Datos por valor (primitivos)

var_a = 100
var_b = var_a
var_b = 150 
var_b = var_a
print(var_a)
print(var_b)

# Datos por referencia 

list_a = [100, 150]
list_b = [200, 250]
print(list_a)
print(list_b)

list_b = list_a # Desde esta declaración tienen la misma referencia de memoria
print(list_b)

list_b[0] = 300
print(list_b)
print(list_a)

# Funciones con datos por valor

dato_a = 100

def funcion_valor(dato: int):
    dato  = 10
    print(dato)

funcion_valor(dato_a)
print(dato_a)


# Funciones por referencia
lista_a = [500]

def funcion_ref(lista: list):
    lista[0] = 100
    print(lista)

funcion_ref(lista_a)
print(lista_a)

# EJERCICIO

num1 = 4
num2 = 5

def func_valor (num_1: int, num_2: int):
    temp = num_1
    num_1 = num_2
    num_2 = temp
    return num_1, num_2

variable_a, variable_b = func_valor(num1, num2)
print(variable_a, variable_b)


list1 = [100, 200]
list2 = [500]

def func_ref (list_1: list, list_2: list):
    temp = list_1
    list_1 = list_2
    list_2 = temp
    return list_1, list_2

lista_a, lista_b = func_ref(list1, list2)
print(lista_a, lista_b)