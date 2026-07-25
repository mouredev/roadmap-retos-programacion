"""
Valor y Referencia
"""

# Tipos de datos por valor (primitivos)
print("Tipos de datos por valor:")
my_int_a = 10
my_int_b = my_int_a
print(my_int_a)
print(my_int_b)

my_int_b = 20
print(my_int_a)
print(my_int_b)

# Tipos de datos por referencia (no primitivos)
print("-----------------------------")
print("Tipos de datos por referencia:")
my_list_a = [10, 20]
my_list_b = my_list_a
print(my_list_a)
print(my_list_b)

my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor 
print("--------------------------------")
print("Funciones con datos por valor:")
my_int_c = 10
def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia

print("--------------------------------")
print("Funciones con datos por referencia:")
my_list_c = [10, 20]
def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)

my_list_func(my_list_c)
print(my_list_c)

# DIFICULTAD EXTRA (opcional):

# Por valor
print("--------------------------------")
print("Por valor:") # 10, 20

my_int_d = 10
my_int_e = 20
def my_int_func_extra(my_int_d: int, my_int_e: int):
    temp = my_int_d
    my_int_d = my_int_e
    my_int_e = temp
    return my_int_d, my_int_e

new_int_d, new_int_e = my_int_func_extra(my_int_d, my_int_e)
print(f"Originales: {my_int_d}, {my_int_e}")
print(f"Nuevas: {new_int_d}, {new_int_e}")

# Por referencia
print("--------------------------------")
print("Por referencia:") # 10, 20

my_list_d = [10, 20]
my_list_e = [30, 40]
def my_list_func_extra(my_list_d: list, my_list_e: list):
    temp = my_list_d.copy()
    my_list_d.clear()
    my_list_d.extend(my_list_e)
    my_list_e.clear()
    my_list_e.extend(temp)

print(f"Originales: {my_list_d}, {my_list_e}")
my_list_func_extra(my_list_d, my_list_e)
print(f"Modificadas: {my_list_d}, {my_list_e}")
