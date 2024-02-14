"""
05 - VALOR Y REFERENCIA
Autor de la solución: Oriaj3

Teoría:
En Python, las variables pueden ser asignadas por valor o por referencia, dependiendo del tipo de dato que almacenan.
- Asignación por valor: Cada variable tiene su propio valor independiente. Esto sucede con tipos de datos primitivos como enteros, flotantes y cadenas.
- Asignación por referencia: Se comparte la referencia al objeto en la memoria. Esto sucede con tipos de datos mutables como listas y diccionarios. Modificar un objeto afecta a todas las variables que hacen referencia a él.
- Dentro de una clase, las variables de instancia se pasan por referencia, mientras que las variables de clase se pasan por valor.
"""

# EJERCICIOS 
# Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
# Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
# (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)


# Asignación de variables "por valor" y "por referencia"
# Por valor (tipos primitivos)
a = 5
b = a  # a y b son independientes
b = 10
print(a)  # a sigue siendo 5
print(b)  # b es 10

# Por referencia (tipos compuestos)
list_1 = [1, 2, 3]
list_2 = list_1  # list_2 apunta al mismo objeto que list_1
list_2.append(4)
print(list_1)  # list_1 se ve afectada, [1, 2, 3, 4]
print(list_2)  # list_2 es [1, 2, 3, 4]

# Funciones con parámetros "por valor" y "por referencia"
# Por valor
def modify_value(value):
    value = 10
    return value

# Ejemplo de uso
a = 5
print(modify_value(a))  # 10
print(a)  # 5

# Por referencia
def modify_reference(list):
    list.append(4)
    return list

# Ejemplo de uso
list_1 = [1, 2, 3]
print(modify_reference(list_1))  # [1, 2, 3, 4]
print(list_1)  # [1, 2, 3, 4]


# DIFICULTAD EXTRA (opcional):
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#   Comprueba también que se ha conservado el valor original en las primeras.

# Programa 1: Intercambio de parámetros por valor
def exchange_values(value_1, value_2):
    tmp = value_1
    value_1 = value_2
    value_2 = tmp
    return value_1, value_2

# Ejemplo de uso
original_value_1 = 'Hola'
original_value_2 = 'Mundo'

new_value_1, new_value_2 = exchange_values(original_value_1, original_value_2)

print(f"Original Values: {original_value_1}, {original_value_2}")  # Original Values: Hola, Mundo
print(f"New Values: {new_value_1}, {new_value_2}")  # New Values: Mundo, Hola

# Programa 2: Intercambio de parámetros por referencia
# En este caso, se intercambiará el primer elemento de cada lista entre sí (siendo un seudo-puntero). 
def exchange_references(puntero_1, puntero_2):
    puntero_1[0], puntero_2[0] = puntero_2[0], puntero_1[0]
    return puntero_1, puntero_2

# Ejemplo de uso
original_list_1 = ['Hola']
original_list_2 = ['Python']

new_list_1, new_list_2 = exchange_references(original_list_1, original_list_2)

print(f"Original Lists: [{original_list_1[0]}], [{original_list_2[0]}]")  # Original Lists: [Python], [Hola]
print(f"New Lists: [{new_list_1[0]}], [{new_list_2[0]}]")  # New Lists: [Python], [Hola]

# Programa 2: Intercambio de parámetros por referencia (con listas)
# En este caso, se intercambiara todo el contenido de las listas entre sí.
def exchange_references(list_1, list_2):
    if len(list_1) != len(list_2):
        return None
    for i in range(len(list_1)):
        list_1[i], list_2[i] = list_2[i], list_1[i]
    return list_1, list_2

# Ejemplo de uso
original_list_1 = ['Lista 1 Elemento 0', 'Lista 1 Elemento 1']
original_list_2 = ['Lista 2 Elemento 0', 'Lista 2 Elemento 1']

new_list_1, new_list_2 = exchange_references(original_list_1, original_list_2)

print(f"Original Lists: {original_list_1}, {original_list_2}")  # Original Lists: ['Hola', 'Mundo'], ['Python', '3.10.11']
print(f"New Lists: {new_list_1}, {new_list_2}")  # New Lists: ['Python', '3.10.11'], ['Hola', 'Mundo']


#Corrección del programa 2 después de ver directo Mouredev
#Intercambio de parámetros por referencia (con listas)

def references(list_1: list, list_2: list) -> tuple:
    list_1, list_2 = list_2, list_1
    return list_1, list_2


# Ejemplo de uso 1
original_list_1 = ['Hola']
original_list_2 = ['Python']

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = references(my_list_e, my_list_f)
print(f"Original: {my_list_e}, {my_list_f}")
print(f"Modificadas: {my_list_g}, {my_list_h}")

def references2(list_1: list, list_2: list) -> tuple:
    temp = list_1
    list_1 = list_2
    list_2 = temp
    return list_1, list_2

# Ejemplo de uso 2
my_list_i = [10, 20]
my_list_j = [30, 40]
my_list_k, my_list_l = references2(my_list_i, my_list_j)
print(f"Original: {my_list_i}, {my_list_j}")
print(f"Modificadas: {my_list_k}, {my_list_l}")
