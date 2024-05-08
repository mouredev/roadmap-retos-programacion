# Creamos un conjunto
conjunto = set(["elemento"])
print(conjunto)

# Añadir un elemento al final
conjunto.add("elemento_final")
print(conjunto)

# Añadir un elemento al principio (no se puede directamente en un conjunto, ya que no tienen un orden específico)
# Sin embargo, podemos usar otro tipo de estructura de datos como una lista para simularlo
lista_conjunto = list(conjunto)
lista_conjunto.insert(0, "elemento_inicio")
conjunto = set(lista_conjunto)
print(conjunto)

# Añadir varios elementos en bloque al final
conjunto.update(["bloque1", "bloque2", "bloque3"])
print(conjunto)

# Añadir varios elementos en bloque en una posición concreta (no se puede directamente en un conjunto)
# Pero podemos usar una lista para luego convertirla en conjunto
lista_conjunto = list(conjunto)
lista_conjunto[2:2] = ["nuevo_bloque1", "nuevo_bloque2"]
conjunto = set(lista_conjunto)
print(conjunto)

# Eliminar un elemento en una posición concreta (no se puede directamente en un conjunto)
# Pero podemos usar una lista para luego convertirla en conjunto
lista_conjunto = list(conjunto)
lista_conjunto.pop(1)
conjunto = set(lista_conjunto)
print(conjunto)

# Actualizar el valor de un elemento en una posición concreta (no se puede directamente en un conjunto)
# Pero podemos usar una lista para luego convertirla en conjunto
lista_conjunto = list(conjunto)
lista_conjunto[0] = "nuevo_valor"
conjunto = set(lista_conjunto)
print(conjunto)

# Comprobar si un elemento está en el conjunto
if "nuevo_valor" in conjunto:
    print('El elemento "nuevo_valor" está en el conjunto')
print(conjunto)

# Eliminar todo el contenido del conjunto
conjunto.clear()

# Mostrar el conjunto
print(conjunto)


# Ejercicio extra

conjunto1 = set([1, 2, 3, 4, 5])
conjunto2 = set([4, 5, 6, 7, 8])
print(f"Conjunto 1: {conjunto1}\nConjunto 2: {conjunto2}")
# Unión
print(f"Unión: {conjunto1.union(conjunto2)}")
# Intersección
print(f"Intersección: {conjunto1.intersection(conjunto2)}")
# Diferencia
print(f"Diferencia 1: {conjunto1.difference(conjunto2)}")
print(f"Diferencia 2: {conjunto2.difference(conjunto1)}")
# Diferencia simétrica
print(f"Diferencia simétrica: {conjunto1.symmetric_difference(conjunto2)}")
