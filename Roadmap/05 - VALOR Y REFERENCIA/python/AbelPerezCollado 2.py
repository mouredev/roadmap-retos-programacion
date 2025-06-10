# Asignación de variables por VALOR
a = 5
b = a
b = 10
print(a)
print(b)

# Asignación de un flotante
x = 3.14
y = x  # y ahora es una copia de x

# Modificando y no afecta a x
y = 2.71
print(x)  # Output: 3.14
print(y)  # Output: 2.71

# Asignación de una cadena de caracteres
s1 = "Hola"
s2 = s1  # s2 ahora es una copia de s1

# Modificando s2 no afecta a s1
s2 = "Adiós"
print(s1)  # Output: Hola
print(s2)  # Output: Adiós


# Asignación de una tupla
t1 = (1, 2, 3)
t2 = t1  # t2 ahora es una copia de t1

# Modificando t2 no afecta a t1
t2 = (4, 5, 6)
print(t1)  # Output: (1, 2, 3)
print(t2)  # Output: (4, 5, 6)

# Asignación de variables por REFERENCIA

# Listas
# Asignación de una lista
list1 = [1, 2, 3]
list2 = list1  # list2 se refiere a la misma lista que list1

# Modificando list2 también afecta a list1
list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]

# Asignación de un diccionario
dict1 = {'a': 1, 'b': 2}
dict2 = dict1  # dict2 se refiere al mismo diccionario que dict1

# Modificando dict2 también afecta a dict1
dict2['c'] = 3
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(dict2)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Asignación de un conjunto
set1 = {1, 2, 3}
set2 = set1  # set2 se refiere al mismo conjunto que set1

# Modificando set2 también afecta a set1
set2.add(4)
print(set1)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {1, 2, 3, 4}


# DIFICULTAD EXTRA
# VALOR
def intercambia_valor(param_1, param_2):
    return param_2, param_1

param_1 = input("Introduce primer parametro: ")
param_2 = input("Introduce segundo parametro: ")

nuevo_param_1 , nuevo_param_2 = intercambia_valor(param_1,param_2)
print(f"Variables originales param_1 = {param_1}")
print(f"Variables originales param_2 = {param_2}")
print(f"Variables nuevo_param_1 = {nuevo_param_1}")
print(f"Variables nuevo_param_2 = {nuevo_param_2}")

# REFERENCIA
lista_1 = [1,2,3]
lista_2 = [4,5,6]

def intercambia_referencia(val_1, val_2):
    val_1 = val_2
    val_2 = val_1
    return val_1, val_2

nueva_lista_1, nueva_lista_2 = intercambia_referencia(lista_1,lista_2)

print(f"Variables originales lista_1 = {lista_1}")
print(f"Variables originales lista_2 = {lista_2}")
print(f"Variables nueva_lista_1 = {nueva_lista_1}")
print(f"Variables nueva_lista_2 = {nueva_lista_2}")