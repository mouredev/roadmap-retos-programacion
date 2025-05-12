# datos por valor
my_int_a = 10
my_int_b = my_int_a
my_int_a = 20
print(my_int_a)
print(my_int_b)

# datos por referencia
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_a.append(30)
print(my_list_a)
print(my_list_b)

# funcion con datos por valor
def my_int_func(my_int: int):
    my_int = 40
    print(my_int)

my_int_c = 30
my_int_func(my_int_c)
print(my_int_c)

# funcion con datos por referencia
def my_list_func(my_list: list):
    my_list.append(60)
    print(my_list)

my_list_c = [40, 50]
my_list_func(my_list_c)
print(my_list_c)

# EXTRA

# por valor
def cross_value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 100
my_int_e = 200
my_int_f, my_int_g = cross_value(my_int_d, my_int_e)
print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# por referencia
def cross_ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_d = [100, 200]
my_list_e = [300, 400]
my_list_f, my_list_g = cross_ref(my_list_d, my_list_e)
print(f"{my_list_d}, {my_list_e}")
print(f"{my_list_f}, {my_list_g}")