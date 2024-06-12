# Valor y Rferencia


# tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
my_int_a = 30
print(my_int_a)
print(my_int_b)

# tipos de datos por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones por datos por valor
my_int_c = 10

def my_int_func( my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# funciones de datos por referencia


def my_list_func(my_list: int):
    my_list_e = my_list
    my_list.append(30)
    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

#Buscar mecanismo de copiado

#EXTRA

def value (value_a: int, value_b: int):
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b
    

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# referencia

def ref (value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b
    

my_list_e = [10, 20]
my_int_f = [30, 40]
my_int_g, my_int_h = ref(my_list_e, my_int_f)

print(f"{my_list_e}, {my_int_f}")
print(f"{my_int_g}, {my_int_h}")


