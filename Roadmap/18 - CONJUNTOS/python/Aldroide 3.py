"""
    Ejercicio
    Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
    operaciones (debes utilizar una estructura que las soporte):
    * Añade un elemento al final.
    * Añade un elemento al principio.
    * Añade varios elementos en bloque al final.
    * Añade varios elementos en bloque en una posición concreta.
    * Elimina un elemento en una posición concreta.
    * Actualiza el valor de un elemento en una posición concreta.
    * Comprueba si un elemento está en un conjunto.
    * Elimina todo el contenido del conjunto.
"""
my_set1 = set(['Anahi', 'Sebastian', 'Samira', 'Emmanuel'])
print(my_set1)

# Añadir un elemento
my_set1.add('Erwin')
print(f"Añadimos Erwin: {my_set1}")
# Eliminar elemento
my_set1.remove('Anahi')
print(f"Se removio Anahi: {my_set1}")


"""
    EJERCICIO EXTRA:
    * Muestra ejemplos de las siguientes operaciones con conjuntos:
    * Unión.
    * Intersección.
    * Diferencia.
    * Diferencia simétrica.
"""
my_set1 = set([1, 2, 3, 4])
my_set2 = set([3, 4, 5, 6])

print(f"\nSets a usar {my_set1} y {my_set2}")
mysetR = my_set1.union(my_set2)
print(f"Union {mysetR}")

mysetR = my_set1.intersection(my_set2)
print(f"Interseccion {mysetR}")

mysetR = my_set1.difference(my_set2)
print(f"diferencia {mysetR}")

mysetR = my_set1.symmetric_difference(my_set2)
print(f"Diferencia simetrica {mysetR}")
