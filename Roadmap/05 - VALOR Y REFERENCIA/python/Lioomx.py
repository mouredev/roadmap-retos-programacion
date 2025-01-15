
''' Asignación de variables'''

""" POR VALOR """

# Tipos inmutables - int, float, str, tuplas, bool

x = 10
y = x # Se copia el valor de 'x' a 'y'
y = 20 # Cambiar 'y' no afecta a 'x'

print(x)
print(y)

""" POR REFERENCIA """

# Tipos mutables - list, dict, set

a = [1, 2, 3]
b = a # Se asigna la referencia de 'a' a 'b'
b.append(4) # Modificamos la lista usando 'b'

print(a)
print(b)

''' Al ser mutables, tanto 'a' como 'b' apuntan al mismo objeto
y cualquier cambio afecta a ambos
'''

# Copiar por valor

a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a) 
print(b)

# Funciones con datos por valor

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia

def my_list_func(my_list: list):
    my_list_e = my_list
    my_list.append(30)

    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list_e)
    print(my_list_d)

my_list_c = [10, 20] 
my_list_func(my_list_c)
print(my_list_c)
