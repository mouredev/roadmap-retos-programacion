###############################################  CONJUNTOS EN PYTHON  ###################################################################

# Para la definición de un conjunto de datos usaremos {} o la función set()
# Los conjuntos no pueden tener elementos repetidos y no es necesario que estén ordenados
# Los conjuntos no pueden tener elementos que no sean inmutables (no pueden ser modificados)

c1 = {1,2,3,7,5}

# Agregar un elemento
c1.add(6)

print(c1)

# Eliminar un elemento
c1.remove(7) # Da error si no existe el elemento dentro del conjunto
print(c1)

# Podemos eliminar y no generar error si el elemento no existe con discard
c1.discard(7)

# Vaciar completamente el conjunto con clear
c1.clear()

# Operaciones matemáticas de conjutos (union |   intersección &   diferencia -   diferencia simétrica ^)
c1 = {1,2,3,7,5}
c2 = {1,2,3,7,8}

print(f"Unión: {c1 | c2}")
print(f"Intersección: {c1 & c2}" )
print(f"Diferencia: {c1 - c2}")
print(f"Diferencia simétrica: {c1 ^ c2}")


# Ejercicio

c2 = {3,5,2,1}
print(c2)

c2.add(7) # Añade un elemento
print(c2)

'''
En Python, los conjuntos (set) son colecciones desordenadas, por lo que no tienen un concepto de "inicio" o "final". 
Los elementos no se almacenan en un orden específico. Por esta razón, 
no podemos "añadir un elemento al inicio" como lo haríamos con una lista.

Podemos convertir el conjunto en lista, añadir, eliminar etc en las posiciones que queramos y posteriormente convertila
a un conjunto
'''

c2_list = list(c2)

print(type(c2_list))
print(len(c2_list))

c2_list.extend([i for i in range(11,21)]) # Añadimos varios elementos en bloque a la lista
c2_list[5] = 1000 # Actualizamos el valor en una posición concreta
c2 = set(c2_list) # Acabamos de añadir varios elementos en bloque a un conjunto

print(c2)

# Si queremos eliminar uno o varios elementos concretos de un conjunto tendríamos que operar de la misma forma
c2_list = list(c2)

c2_list.pop() # Para eliminar un elemento
c2_list.pop(0) # Para eliminar un elemento en una posición concreta
c2_list.remove(12) # Para eliminar un elemento concreto

c2 = set(c2_list)
print(c2)

# Comprobaciones de pertenencia
print(1 in c2)
print(1000 in c2)
print(12 in c2)

# Por último limpiar todo el conjunto
c2.clear()

print(c2)



###############################################  EJERCICIO EXTRA  ###################################################################
# Mostrar operaciones con conjuntos:
l1 = [i for i in range(1, 100)]
l2 = [i for i in range(50, 150)]
c1 = set(l1)
c2 = set(l2)

print(c1)
print(c2)

print(f"Union: {c1.union(c2)}")
print(f"Intersección: {c1.intersection(c2)}")
print(f"Diferencia: {c1.difference(c2)}")
print(f"Diferencia simétrica: {c1.symmetric_difference(c2)}")


###############################################  FIN EJERCICIO EXTRA  ###################################################################

###############################################  FIN CONJUNTOS EN PYTHON  ###################################################################