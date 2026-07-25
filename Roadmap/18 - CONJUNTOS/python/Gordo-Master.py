# 18 - Conjuntos

conjunto = {"a","e","i","o","u"}
print(conjunto)

# En los conjuntos no se repiten los valores y no esta en orden los valores.

# Añadir un elemento:
conjunto.add("b")
print(conjunto)

# Añade varios elementos
conjunto.update(["c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"])
print(conjunto)

# Eliminar un elemento
conjunto.remove("x") # Genera un error si no se encuentra el elemento
print(conjunto)
conjunto.discard("y") # No genera error si no se encuentra el elemento
print(conjunto)
print(conjunto.pop()) # Es aleatorio el que remueve
print(conjunto)

# Comprueba si un elemento se encuentra en el conjunto
print("d" in conjunto)

# Limpia el conjunto
conjunto.clear()
print(conjunto)

"""
Parte corregida con la trampa de Brais
"""

data = [1, 2, 3, 4, 5]
print(data)

# Añade un elemento
data.append(6)
print(data)

# Añade al principio
data.insert(0,0)
print(data)

# Añade varios elementos al final
data.extend([9,10])
print(data)

# Añade varios elementos en una posición
data[7:7]=[7,8]
print(data)

# Actualiza un posición en concreto
data[3]=-3
print(data)

# Elimina un dato segun su posición
print(data.pop(7))
print(data)
del data[1]
print(data)

# Comprueba que el valor este
print(4 in data)

# Vaciar
print(data.clear())

"""
Ejercicio Extra
"""

conj_1 = set([i for i in range(2,31,2)])
conj_2 = set([i for i in range(3,31,3)])

print(conj_1)
print(conj_2)

# Union
print(conj_1.union(conj_2))
print(conj_1|conj_2)

# Intersección
print(conj_1.intersection(conj_2))
print(conj_1&conj_2)

# Diferencia
print(conj_1.difference(conj_2))
print(conj_1 - conj_2)

# Diferencia simetrica
print(conj_1.symmetric_difference(conj_2))
print(conj_1^conj_2)