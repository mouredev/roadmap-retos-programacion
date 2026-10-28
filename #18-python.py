'''
 EJERCICIO:
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
'''
print("="*60)
Datos = [1, 2, 3, 4, 5]
print(Datos)
print("-"*60)
Datos.append(6)
print(Datos)
print("-"*60)
Datos.insert(0,0)
print(Datos)
print("-"*60)
Datos.extend([7, 8, 9])
print(Datos)
print("-"*60)
Datos[2:3] = [-1, -2, -3]
print(Datos)
print("-"*60)
del Datos[5]
print(Datos)
print("-"*60)
Datos[5] = -4
print(Datos)
print("-"*60)
print(5 in Datos)
print("-"*60)
Datos.clear()
print(Datos)
print("="*60)




'''
* DIFICULTAD EXTRA (opcional):
* Muestra ejemplos de las siguientes operaciones con conjuntos:
* - Unión.
* - Intersección.
* - Diferencia.
* - Diferencia simétrica.
'''

ConjuntoA = {1, "a", "b", "c"}
ConjuntoB = {"a", 1, 2}

print(ConjuntoA)
print(ConjuntoB)

print("-"*60)

print(ConjuntoA.union(ConjuntoB))

print("-"*60)

print(ConjuntoA.intersection(ConjuntoB))

print("-"*60)

print(ConjuntoA.difference(ConjuntoB))

print("-"*60)

print(ConjuntoB.difference(ConjuntoA))

print("-"*60)

print(ConjuntoA.symmetric_difference(ConjuntoB))

print("*"*60)
