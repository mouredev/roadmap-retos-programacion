""" Reto 05: Valor y Referencia """

# Tipos de datos por valor
my_int_a = 12
my_int_b = my_int_a
my_int_b = 2
# my_int_a = 21
print(my_int_a)
print(my_int_b)

# Tipos de datos por referencia
my_list_a = [12, 21]
my_list_b = my_list_a
my_list_b.append(24)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor
def my_int_func(my_int: int):
    my_int = 22
    print(my_int)

my_int_c = 24
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia
def my_list_func(my_list: list):
    my_list.append(22)
    my_list_d = my_list
    my_list_d.append(1)
    print(my_list)
    print(my_list_d)

my_list_c = [2, 16]
my_list_func(my_list_c)
print(my_list_c)



""" Reto extra """

# Por valor
def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)
print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Por referencia
def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")
