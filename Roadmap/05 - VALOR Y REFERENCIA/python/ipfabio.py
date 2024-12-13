"""
Valor y referencia
"""

# Tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
# my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tpos de datos por referencia
# No copian su valor, heredan la posición de memoria.

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30) # altera también la lista A
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c) # Vale 20
print(my_int_c) # Sigue valiendo 10

# Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c) # Agrega el 30
print(my_list_c) # Mantiene el cambio de append

"""
Extra
"""

# Por valor

def value(val_a: int, val_b: int) -> tuple:
    temp = val_a
    val_a = val_b
    val_b = temp
    return val_a, val_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Por referencia
"""
Preferentemente no utlizar con copias en caminos separados (que les ocurran cosas distintas a las copias)
porque se puede generar un error alterando la version original de la lista
"""
def ref(val_a: list, val_b: list) -> tuple:
    temp = val_a
    temp.append(50) # Agrega en ambos/
    val_a = val_b
    val_b = temp
    return val_a, val_b

my_list_e = [10,20]
my_list_f = [30,40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")