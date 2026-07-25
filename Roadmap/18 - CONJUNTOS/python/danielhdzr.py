# #18 CONJUNTOS
#### Dificultad: Fácil | Publicación: 29/04/24 | Corrección: 06/05/24

'''
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
'''
# Añade un elemento al final.
datos = [1,2,3,4]
datos.append(5)
print(datos)

# Añade un elemento al principio.
datos.insert(0,0)
print(datos)

# Añade varios elementos en bloque al final.
un_set = {1,2,3}
print(un_set)
nuevo_set = {4,5,6}
print(nuevo_set)
un_set.update(nuevo_set)
print(un_set)

# Añade varios elementos en bloque en una posición concreta.
diccionario = {"k1":1, "k5":5, "k6":6}
print(diccionario)
otro_dicc = {"k2":2, "k3":3, "k4":4}
print(otro_dicc)
diccionario.update(otro_dicc)
nuevo_dict = [key for key in sorted(diccionario)]
print(f"Sin mostrar values {nuevo_dict}")
nuevo_dict = {key: diccionario[key] for key in sorted(diccionario)}
print(f"Mostrando values: {nuevo_dict}")

# Elimina un elemento en una posición concreta.
datos.remove(4) # lista
print(datos)

my_set = {1, 2, 3} # set
my_set.remove(3)
print(my_set)

del nuevo_dict["k6"] # dicc
print(nuevo_dict)

 # Actualiza el valor de un elemento en una posición concreta.
datos[1] = 4 # lista
print(datos)
nuevo_dict["k1"] = 0.5 # dicc
print(nuevo_dict)

# Comprueba si un elemento está en un conjunto.
print(2 in datos)
print("k1" in nuevo_dict)
print(1 in my_set)


# Elimina todo el contenido del conjunto.
datos.clear() # lista
print(datos)

nuevo_dict.clear() # dicc
print(nuevo_dict)

my_set.clear() # set
print(my_set)