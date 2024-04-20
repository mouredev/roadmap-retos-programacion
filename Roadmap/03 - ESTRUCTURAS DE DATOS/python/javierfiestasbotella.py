''''EJERCICIO:
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
 * - También se debe proponer una operación de finalización del programa.'''
print('_______LISTAS___________')
ejemplo=[1,45,876,7,34,2]
print(sorted(ejemplo))#lista ordenada
print(ejemplo.pop())#borrado ultimo elemnto de la lista
print(ejemplo)#lista actualizada
print(ejemplo.clear())#borrado de la lista

print('_______TUPLAS___________')
ejemplo_2=(3,654,57,2,9)
print(sorted(ejemplo_2))#tupla ordenada
print(ejemplo_2)#tupla actualizada
#del ejemplo_2();borrado de la tupla


print('_______DICCIONARIOS___________')
ejemplo_3={1:'azul',2:'rojo',3:'verde',4:'blanco'}

claves_ordenadas = sorted(ejemplo_3.keys())
valores_ordenados = [ejemplo_3[clave] for clave in claves_ordenadas]#ordena 

print("Claves ordenadas:", claves_ordenadas)
print("Valores ordenados:", valores_ordenados)
del ejemplo_3[3]#elimina clave y su valor
ejemplo_3[1] = 'rosa'#cambiamos el valor
ejemplo_3.clear()#Elimina el diccionario

print("Diccionario después de borrar:", ejemplo_3)

