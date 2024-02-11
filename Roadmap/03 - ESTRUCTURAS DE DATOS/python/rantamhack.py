#!/usr/bin/python3
#!/usr/bin/python3

print("\n\n======================LISTAS======================\n\n")

'''
LISTAS - Se representan entre corchetes y pueden tener elementos repetidos. Es una estructura ordenada y modificable en el tiempo
Pueden hacerse de de cualquier tipo de datos incluso mezclándolos
'''
list_strings = ["Luis", "María", "Helena",
                "Pedro", "Ignacio", "Jose", "Zoe", "Candela"]
print(list_strings)
list_numbers = [3, 7, 52, 45, 9, 8, 8, 8, 7, 5]
print(list_numbers)
list_mixed = ["Luis", 7, 52, 9, "Helena", "ignacio", 55]
print(list_mixed)

# Inserción
list_strings.append("Juan")  # Añade un elemento al final de la lista
print(list_strings)

list_strings.insert(3, "Cristina")  # Añade un elemento en la posición indicada
print(list_strings)

# Actualización
# Actualiza la lista cambiando la posición indicada por el nuevo elemento
list_strings[-1] = "Angel"
print(list_strings)

# Ordenación
list_strings.sort()  # Ordena la lista (en éste caso alfabeticamente)
print(list_strings)

# Borrado
list_strings.pop(0)  # Borra el elemento indicado de la lista
print(list_strings)

list_strings.pop()  # Borra el ultimo elemento de la lista
print(list_strings)


print("\n\n======================TUPLAS======================\n\n")

'''
Tuplas - Se representan entre parentesis y como las listas pueden tener elementos repetidos. Es una estructura ordenada y no
modificable. Puede hacerse de cualqier tipo de datos incluso mezclándolos
'''
tuple_strings = ("Luis", "María", "Helena", "Pedro",
                 "Ignacio", "Jose", "Zoe", "Candela")
print(tuple_strings)
tuple_numbers = (3, 7, 52, 45, 9, 8, 8, 8, 7, 5)
print(tuple_numbers)
tuple_mixed = ("Luis", 7, 52, 9, "Helena", "ignacio", 55)
print(tuple_mixed)

# Las tuplas son inmutables por lo que una vez creadas no se pueden transformar


print("\n\n======================DICCIONARIOS======================\n\n")

'''
Diccionarios - Se representan entre llaves y cada elemento consta de una combinación entre una llave y un valor. Es una estructura no organizada
y modificable en el tiempo. La clave y el valor deben de estar separados por dos puntos. Los pares de elementos iran separados por comas.
'''

evaluation = {
    "Luis": 5,
    "María": 7.5,
    "Helena": 9,
    "Pedro": 3.8,
    "Ignacio": 2
}
print(evaluation)

# Inserción

evaluation["Candela"] = 6.5  # Añade un elemento al diccionario
print(evaluation)

print(evaluation.keys())  # Lista las claves del diccionario

print(evaluation.values())  # Lista los valores del diccionario

# Borrado
evaluation.pop("Luis")  # También se podria usar "del evaluation["Luis"]"
print(evaluation)

# Ordenación

evaluation_sort = sorted(evaluation.items())
print(evaluation_sort)

# Actualización

evaluation.update({"Miguel": 5})
print(evaluation)

print("\n\n======================SETS======================\n\n")

'''
Sets - Se representan entre corchetes y a diferencia de listas y tuplas no pueden tener elementos repetidos es una estructura no organizada
modificable en el tiempo
'''

set_strings = set(["Luis", "María", "Helena", "Pedro",
                  "Ignacio", "Jose", "Zoe", "Candela"])
print(set_strings)
set_numbers = set([3, 7, 52, 45, 9, 8, 5])
print(set_numbers)
set_mixed = set(["Luis", 7.5, 9, "Helena", "ignacio", 55])
print(list_mixed)

# Inserción
set_strings.add("Miguel")
print(set_strings)

# Borrado
set_strings.remove("Pedro")  # Elimina el elemento indicado
print(set_strings)

set_strings.pop()  # Elimina un elemento aleatorio
print(set_strings)

# Ordenación
print(sorted(set_strings))

# Actualización
set_strings.update(set_numbers)
print(set_strings)
