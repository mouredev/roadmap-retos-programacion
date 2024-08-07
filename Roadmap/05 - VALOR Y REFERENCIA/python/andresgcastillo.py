# Asignación por valor (inmutable)
num1 = 5
num2 = num1  # Asignación por valor
num2 = 10
print(num1)  # Imprime: 5
print(num2)  # Imprime: 10

# Asignación por referencia (mutable)
list1 = [1, 2, 3]
list2 = list1  # Asignación por referencia
list2.append(4)
print(list1)  # Imprime: [1, 2, 3, 4]
print(list2)  # Imprime: [1, 2, 3, 4]

# Función con parámetros por valor (inmutable)
def change_num(num):
    num = 10

num = 5
change_num(num)
print(num)  # Imprime: 5

# Función con parámetros por referencia (mutable)
def change_list(lst):
    lst.append(4)

lst = [1, 2, 3]
change_list(lst)
print(lst)  # Imprime: [1, 2, 3, 4]

#Dificultad Extra
"""
En Python, todos los parámetros se pasan por referencia. Sin embargo, los tipos primitivos son inmutables, por lo que no puedes cambiar su valor:
"""

# Programa 1: Pasando parámetros primitivos (inmutables)
def swap_values(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp
    return val1, val2

a = 5
b = 10
print(f"Original a: {a}, b: {b}")  # Original a: 5, b: 10

new_a, new_b = swap_values(a, b)
print(f"Swapped a: {new_a}, b: {new_b}")  # Swapped a: 10, b: 5
print(f"After swap a: {a}, b: {b}")  # After swap a: 5, b: 10

# Programa 2: Pasando listas (mutables)
def swap_list_values(lst):
    temp = lst[0]
    lst[0] = lst[1]
    lst[1] = temp
    return lst[:]

lst = [5, 10]
print(f"Original lst: {lst}")  # Original lst: [5, 10]

new_lst = swap_list_values(lst)
print(f"Swapped lst: {new_lst}")  # Swapped lst: [10, 5]
print(f"After swap lst: {lst}")  # After swap lst: [10, 5]


