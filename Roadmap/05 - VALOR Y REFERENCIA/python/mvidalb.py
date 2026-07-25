'''
Valor y referencia
'''
# Tipos de dato por valor (ÚNICO): etneros, flotantes, cadenas, booleanos, ...
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
my_int_a = 30
print(my_int_a)
print(my_int_b)


# Tipos de dato por referencia: listas, diccionarios, conjuntos, ...
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)    # [10, 20, 30]
print(my_list_b)    # [10, 20, 30]


# Funciones con datos por valor
my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)


# Funciones con datos por referencia

def my_list_func(my_list: list):
    my_list.append(30)
    my_list_d = my_list   # my_list_c = my_list = my_list_d (PUNTERO)
    my_list_d.append(40)
    print(my_list)
    print(my_list_d)      # [10, 20, 30, 40]


my_list_c = [10, 20]
my_list_func(my_list_c)   # [10, 20, 30]
print(my_list_c)          # [10, 20, 30]



'''
Ejercicio extra
'''
def valor(var1 : int, var2 : int):
    temp = var1
    var1 = var2
    var2 = temp
    return [var1, var2]

var1 = 1
var2 = 2
print(var1)
print(var2)
varmod_1, varmod_2 = valor(var1, var2)
print(varmod_1)
print(varmod_2)


def referencia(list1 : int, list2 : int):
    temp = list1
    list1 = list2
    list2 = temp
    return [list1, list2]

list1 = [10, 20]
list2 = [40, 50]
print(list1)
print(list2)
listmod_1, listmod_2 = referencia(list1, list2)
print(listmod_1)
print(listmod_2)
