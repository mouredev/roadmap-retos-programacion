"""
    #18 CONJUNTOS
"""

conjunto = set()

# añade un elemento
conjunto.add("elemento 1")

# añade un elemento al inicio
lista = list(conjunto)
lista.insert(0, "elemento 0")
conjunto = set(lista)

# añade varios elementos en bloque al final
conjunto.update(["elemento 2", "elemento 3"])

# añade varios elementos en bloque en una posición concreta
lista = list(conjunto)
lista[1:1] = ["elemento 0.25", "elemento 0.5", "elemento 0.75"]
conjunto = set(lista)

# elimina un elemento en la posición concreta
elemento_eliminar = "elemento 0.25"
conjunto.discard(elemento_eliminar)

# actualiza el valor de un elemento en una posición concreta
lista = list(conjunto)
posicion = lista.index("elemento 0.5")
lista[posicion] = "elemento 0.4"
conjunto = set(lista)

# comprueba si un elemento existe
print("elemento 1" in conjunto)

# elimina todo el contenido del conjunto
conjunto.clear()

print(conjunto)


# Eliminar todo el contenido del conjunto
conjunto.clear()

"""
    DIFICULTAD EXTRA
"""
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Unión
union = conjunto1.union(conjunto2)
print("Unión:", union)

# Intersección
interseccion = conjunto1.intersection(conjunto2)
print("Intersección:", interseccion)

# Diferencia
diferencia = conjunto1.difference(conjunto2)
print("Diferencia:", diferencia)

# Diferencia simétrica
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica:", diferencia_simetrica)
