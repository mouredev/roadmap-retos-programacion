'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
'''

# Listas 

#Creación de una lista
mi_lista = [1,2,3,4,5,6]

#Inserción de un elemento en la lista
mi_lista.append(7) 
print("Esta es la lista con un valor nuevo añadido:",mi_lista)

#Borrado de un elemento de la lista 
mi_lista.remove(3)
print("Esta es la lista pero con el número tres quitado:",mi_lista)

#Actualización de la lista 
mi_lista[3]= 33 # ahora el 4º elemento de la lista será 33
print("Hemos cambiando el valor del número que ocupa la 4º plaza por 33", mi_lista)
#Ordenación de la lista
mi_lista.sort()
print("Aquí tenemos la lista ordenada de menor a mayor", mi_lista)

print("/----------------/")
#Tuplas

#Creación de una tupla 
mi_tupla = (1,2,3,4,5,6)

#Inserción de un elemento en la tupla
numero = 18 #las tuplas son inmutables por lo que para añadir un nuevo elemento debemos crear una
nueva_tupla = mi_tupla + (numero,) 
print ("así añadimos un nuevo elemento a una tupla",nueva_tupla)

#Borrado de un elemento de la tupla 
numero_a_eliminar = 3 #las tuplas son inmutables por lo que para eliminar un elemento debemos crear una
mi_tupla_2 = tuple(x for x in mi_tupla if x != numero_a_eliminar)
print("esta es una tupla nueva sin el número 3",mi_tupla_2)

#Actualización de la tupla 
numero_actualizado = 33 #las tuplas son inmutables por lo que para actualizar un elemento debemos crear una
mi_tupla_3 = tuple (numero_actualizado if x == 1 else x for x in mi_tupla)
print("esta es una tupla nueva pero cambiando el 1 por un 33", mi_tupla_3)

#Ordenación de la tupla
tupla_ordenada = tuple(sorted(list(mi_tupla_3)))
print ("esta es la tupla anterior ordenada de menor a mayor",tupla_ordenada)

print("/----------------/")
#conjuntos (los diccionarios se crean igual pero los elementos son pares clave-valor)

#Creacción de un conjunto
mi_conj = {1,2,3,4,5,6} 

#Inserción de un elemento en el conjunto
mi_conj.add(9)
print("Este es el conjunto con un valor nuevo añadido:",mi_conj)

#Borrado de un elemento del conjunto  
mi_conj.remove(3)
print("Este es el conjunto pero con el número tres quitado:",mi_conj)

#Actualización del conjunto
mi_conj.remove(1)
mi_conj.add (33)
print("para actualizar un conjunto hay que quitar y añadir un numero",mi_conj)
#Ordenación del conjunto
conjuto_ordenado = set(sorted(list(mi_conj)))
print("esta es la manera de ordenar un conjunto",conjuto_ordenado)





