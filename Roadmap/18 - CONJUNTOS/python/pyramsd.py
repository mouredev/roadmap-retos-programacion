conjunto = [1, 2, 3, 4]
print(f'Inicial: {conjunto}')

# Añadir al final
conjunto.append(5)
print(conjunto)

# Añadir al principio
conjunto.insert(0, 0)
print(conjunto)

# Añadir varios en bloque al final.
conjunto.extend([6, 7])
print(conjunto)

# Añadir varios en bloque en una posición concreta
conjunto[3:3] = [2.3, 2.5]
print(conjunto)

# Eliminar de una posicion concreta
conjunto.pop(3)
print(conjunto)

# Actualizar un valor de una posición concreta
conjunto[8] = 6.5
print(conjunto)

# verificar si un elemento se encuntra
print(5 in conjunto)

# Limpiar todo el conjunto
conjunto.clear()
print(conjunto)


'''
EXTRA
'''
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}

# UNION
print(set1.union(set2))

# INTERSECCION
print(set1.intersection(set2))

# DIFERENCIA
print(set1.difference(set2))

# DIFERENCIA SIMETRICA
print(set1.symmetric_difference(set2))
