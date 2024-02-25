"""
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
 """
"""Estructuras"""
#listas
lista:list=[1,2,343,4,5,6]
print(lista)
print(type(lista))
lista.pop() #borra segun indice, por defecto -1
print(lista)
lista.append(123)#inserta un valor en la ultima posicion
print(lista)
lista.insert(254,3)#inserta un valor en el indice indicado
print(lista)
lista.remove(4)#elimina el valor indicado
print(lista)
lista.sort()
print(lista)
print(lista[4])#Acceso al valor en la posicion indicada
lista[0]=555 #actualizacion
print(lista)

#tuplas
tupla:tuple=(1,2,3,4,564,645,2323,23)
print(tupla,type(tupla))
print("ordenando de mayor a menor: ", sorted(tupla, reverse=True)) #ordenado de mayor a menor
print("ordenando de menor a mayor: ", sorted(tupla)) #ordenado de menor a mayor

#sets
