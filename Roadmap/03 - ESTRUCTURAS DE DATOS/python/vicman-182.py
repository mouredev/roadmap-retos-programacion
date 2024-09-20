'''
03 ESTRUCTURAS DE DATOS
Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24
'''

''' * EJERCICIO: '''

'''
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


'''
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

''' *** Listas *** '''

# Declarar una lista
mi_lista = [1,2,3,4,5,6]

# Insertar un elemento al final de la lista.
mi_lista.append(2)
print(mi_lista)

# Modificar un elemento
mi_lista[2] = 8
print(mi_lista)

# Borrar el ultimpo elemento de una lista
mi_lista.append("Este elemento sera borrado") # Añadimos un elemento al final de la lista para borrarlo en las siguientes lineas del codigo
print(mi_lista)

mi_lista.pop()
print(mi_lista)

# Ordenar los datos de la lista usando el metodo sort()

mi_lista.sort()
print(mi_lista)


''' *** Tuplas *** '''


''' *** Sets *** '''


''' *** Diccionarios *** '''