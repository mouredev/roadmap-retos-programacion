'''
Valor y Referencia
'''
# Tipos de datos por valor
'''
en las variables primitives, el valor se almacena en la variable

'''

# Tipos de datos por referencia
''''     
en las variables por referencia, la variable almacena una referencia a la dirección de memoria donde se almacena el valor
son los tipos de datos no primitivos    
por ejemplo, las listas, los diccionarios, los conjuntos, las tuplas, los objetos, etc.
no cpian su valor, heredan su posición en la memoria        
'''

# ejemplo funciones param por valor


def my_func(x):
    x = 20
    print(x)    # 20


x = 10
my_func(x)  # 20
print(x)    # 10

# ejemplo funciones param por referencia


def my_func(x):
    x.append(20)
    print(x)    # [10, 20]


x = [10]
my_func(x)  # [10, 20]
print(x)    # [10, 20]

'''
EXTRA
'''
# intercambiar el valor de 2 variables pasadas por valor

print("intercambiar el valor de 2 variables pasadas por valor")


def value_swap(a: int, b: int) -> tuple:
    a, b = b, a  # intercambiar el valor de 2 variables sin usar variable auxiliar tipo temp
    print(f"a: {a} b: {b}")
    return a, b


my_int_a = 10
my_int_b = 20
print(f"my_int_a: {my_int_a} my_int_b: {my_int_b}")
my_int_a, my_int_b = value_swap(my_int_a, my_int_b)
print(f"my_int_a: {my_int_a} my_int_b: {my_int_b}")

# intercambiar el valor de 2 variables pasadas por referencia


def value_swap_ref(a: list, b: list) -> tuple:
    # intercambiar el valor de 2 variables sin usar variable auxiliar tipo temp x referencia
    a, b = b, a
    # print(f"a: {a} b: {b}")
    return a, b


print("intercambiar el valor de 2 variables pasadas por referencia")
my_list_a = [10, 20]
my_list_b = [30, 40]
print(f"my_list_a: {my_list_a} my_list_b: {my_list_b}")
my_list_a, my_list_b = value_swap_ref(my_list_a, my_list_b)
print(f"my_list_a: {my_list_a} my_list_b: {my_list_b}")
