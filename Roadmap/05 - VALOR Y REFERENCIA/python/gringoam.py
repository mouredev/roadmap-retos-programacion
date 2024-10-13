"""
Valor y referencia
"""

# Tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor


def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

"""
Extra
"""
#Funcion de intercambio de valor con parametros por valor
my_int_d=10
my_int_e=20

def intercambioValor(my_int_d:int, my_int_e:int):
    aux=my_int_d
    my_int_d= my_int_e
    my_int_e= aux

    return my_int_d, my_int_e

print(f"Valores antes de intercambio\n{my_int_d}")
print(my_int_e)



my_int_f, my_int_g= intercambioValor(my_int_d, my_int_e)

print(f"Valores después de intercambio\n{my_int_f}")
print(my_int_g)

#Funcion de intercambio de valor con parametros por valor


my_list_d=[10, 20]
my_list_e=[30, 40]

def intercambioRef(my_int_d:list, my_int_e:list):
    aux=my_int_d
    my_int_d= my_int_e
    my_int_e= aux

    return my_int_d, my_int_e

print(f"Valores antes de intercambio\n{my_list_d}")
print(my_list_e)

my_list_f, my_list_g= intercambioRef(my_list_d, my_list_e)

print(f"Valores después de intercambio\n{my_list_f}")
print(my_list_g)
