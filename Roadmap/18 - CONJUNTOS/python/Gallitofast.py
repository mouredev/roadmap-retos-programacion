# * Ejercicio 18 Conjuntos
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.

galloconjunto =[1,2,3,4]
print(f"Galloconjuntos inicio con {galloconjunto}")
galloconjunto.append(4) #Insertando dato al final
print(f"Galloconjuntos inserto un dato al final{galloconjunto}")
galloconjunto.insert(0,0) #Insertando un elemento al principio
print(f"Galloconjunto inserto un dato al principio {galloconjunto}")
galloconjunto.extend([9,9,9])
print(f"Se añadieron tres 9 al final del galloconjunto: {galloconjunto}")
galloconjunto[2:2]=[5,5,5]
print(f"Se añadieron tres \"5\" en una posicion concreta {galloconjunto}")
del galloconjunto [-1::]
print(f"Se elimino un conjunto en especifico {galloconjunto}")
galloconjunto[0]=0
print(f"Se actualizo un valor")


print(f"Comprobar si elemento existe {0 in galloconjunto}")
print(f"Eliminar contenido {galloconjunto.clear()}")
print(f"Ahora galloconjunto es: {galloconjunto}")

"""Dificultad extra"""

conjunto_1={0,1,2,3,4,5,6}
conjunto_2={4,5,6,7,8,9,10}

print(f"Union {conjunto_1.union(conjunto_2)}")

print(f"Interseccion {conjunto_1.intersection(conjunto_2)}")
print(f"Diferencia: {conjunto_1.difference(conjunto_2)}")
print(f"Diferencia: {conjunto_2.difference(conjunto_1)}")
print(f"Diferencia simetrica: {conjunto_1.symmetric_difference(conjunto_2)}")

print(f"Haciendo mi propia diferencia simetrica: {[conjunto_1.difference(conjunto_2)]+[conjunto_2.difference(conjunto_1)]}")
