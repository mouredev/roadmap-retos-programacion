"""
Valor y referencia
"""
# Los tipos de datos primitivos
# Asignación de variables por valor
my_int_1 = 1
my_int_2 = my_int_1
my_int_2 = 3

print(my_int_1)
print(my_int_2)

# Los tipos de datos que no son primitivos
# Asignación por  referencia
my_list_1 = [1, 2]
my_list_2 = my_list_1
my_list_2.append(3)

print(my_list_1)
print(my_list_2)


# Función por valor

def valor(my_int):
    my_int = 12
    print(my_int)


my_int_3 = 4
valor(my_int_3)
print(my_int_3)


# Función por referencia

def referencia(my_list):
    my_list.append(11)
    print(my_list)


my_list_3 = [22, 23]
referencia(my_list_3)
print(my_list_3)

"""
Extra
"""


def por_valor(value_1: int, value_2: int) -> tuple:
    temp = value_1
    value_1 = value_2
    value_2 = temp
    return value_1, value_2


my_int_4 = 4
my_int_5 = 5
my_int_6, my_int_7 = por_valor(my_int_4, my_int_5)

print(my_int_4)
print(my_int_5)
print(my_int_6)
print(my_int_7)


def por_referencia(value_1: list, value_2: list) -> tuple:
    temp = value_1
    value_1 = value_2
    value_2 = temp
    return value_1, value_2


my_list_4 = [4, 5]
my_list_5 = [6, 7]
my_list_6, my_list_7 = por_referencia(my_list_4, my_list_5)

print(my_list_4)
print(my_list_5)
print(my_list_6)
print(my_list_7)
