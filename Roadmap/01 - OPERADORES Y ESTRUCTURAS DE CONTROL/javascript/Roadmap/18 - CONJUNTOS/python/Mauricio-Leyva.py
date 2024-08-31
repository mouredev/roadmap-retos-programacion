# conjunto de datos (lista)
datos = [1, 2, 3, 4, 5]

# Añade un elemento al final
datos.append(6)
print("Añadir un elemento al final:", datos)  

# Añade un elemento al principio
datos.insert(0, 0)
print("Añadir un elemento al principio:", datos)  

# Añade varios elementos en bloque al final
datos.extend([7, 8, 9])
print("Añadir varios elementos en bloque al final:", datos)  

# Añade varios elementos en bloque en una posición concreta
datos[3:3] = [10, 11]
print("Añadir varios elementos en bloque en una posición concreta:", datos)  

# Elimina un elemento en una posición concreta
del datos[5]
print("Eliminar un elemento en una posición concreta:", datos)  

# Actualiza el valor de un elemento en una posición concreta
datos[3] = 12
print("Actualizar el valor de un elemento en una posición concreta:", datos)  

# Comprueba si un elemento está en un conjunto
print("¿Está el elemento 4 en el conjunto?", 4 in datos)  
print("¿Está el elemento 10 en el conjunto?", 10 not in datos)  

# Elimina todo el contenido del conjunto
datos.clear()
print("Eliminar todo el contenido del conjunto:", datos)  