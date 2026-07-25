"""
EJERCICIO:
  - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
    su tipo de dato.
  - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
    "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 
"""

# VARIABLES POR VALOR (inmutables)
n1 = 10
n2 = n1 # n2 obtiene el valor de n1 pero en distinta dirreccion de memoria
n1 = 20
print(n1)
print(n2)

# VARIABLES POR REFERENCIA
list1 = [10, 20]
list2 = list1 # la list2 obtiene la misma direccion de memoria de la list1
list2.append(40)
print(list1) 
print(list2)

# FUNCIONES CON DATOS POR VALOR
my_int_a = 30

def int_func(my_int: int):
    my_int = 10
    print(my_int)

int_func(my_int_a)
print(my_int_a)

# FUNCIONES CON DATOS POR REFERENCIA
import copy
my_list_b = [10, 20]

def list_func(my_list: list):
    my_list.append(30)
    my_list_copy = copy.copy(my_list) # Manera de copiar los valores del objeto sin mutar el objeto original
    my_list_c = my_list
    my_list_c.append(40)

    print(my_list_c)
    print(my_list)
    print(my_list_copy) # Lista copiada sin mutar


list_func(my_list_b)
print(my_list_b)

"""
EJERCICIO EXTRA:
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

print('\n--- EJERCICIO EXTRA ---\n')

# VARIABLES POR VALOR
my_int_a = 30
my_int_b = 40

def func1(value_a: int, value_b: int) -> tuple:
    value_temp = value_a
    value_a = value_b
    value_b = value_temp
    return value_a, value_b

my_int_c, my_int_d = func1(my_int_a, my_int_b)
print(f"Valores originales: {my_int_a}, {my_int_b}")
print(f"Valores invertidos: {my_int_c}, {my_int_d}")

# VARIABLES POR REFERENCIA
my_list_a = [10, 20]
my_list_b = [30, 40]

def func1(value_a: list, value_b: list) -> tuple:
    value_temp = value_a # value_temp recibe el puntero de memoria de value_a 
    value_a = value_b # value_a recibe el puntero de memoria de value_b
    value_b = value_temp # value_b recibe el puntero de memoria de value_temp, que es el original de value_a
    return value_a, value_b

my_list_c, my_list_d = func1(my_list_a, my_list_b)
print(f"Valores originales: {my_list_a}, {my_list_b}")
print(f"Valores invertidos: {my_list_c}, {my_list_d}")

