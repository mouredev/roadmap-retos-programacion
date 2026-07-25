import os

"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """

#listas son ordenadas y se pueden modificar

my_list = [1, "mateo", 2, 3, 8, 4, 5, 5]
print(my_list)

#tuplas son desordenadas pero no se pueden modificar

my_tupla = {1, 2, 3, 5, 6, 7, "yo solo yo"}
print(my_tupla)

# diccionarios son estructuras de clave-valor para busquedas rapidas

my_dict = {"name": "mateo", "age": "20"}
print(my_dict)

#conjuntos ordenada pero no acepta repetidos

my_set = {1, 9, 2, 3, 4, 4}
print (my_set)



name = input("Como te llamas? ")
print(f"hola, {name}")

my_list.remove(1)
print(my_list)

print(my_set)
my_order_list = my_list.sort

print(my_order_list)


