
# * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.


                                       #estructuras##

lista = [1, 2, 3, 4]
lista.sort()  # Ordena la lista en orden ascendente
print(lista)
lista.sort(reverse=True)    # Ordena la lista en orden descendente
print(lista)
lista.append(6)      # Agrega 6 al final de la lista [1, 2, 3, 4, 6]
print(lista)  
del lista[0]       #elimina el elemento "0"(primero) de la lista [2, 3, 4, 6]
print(lista)
lista.remove(3)      #elimina el valor n=3 de la lista
print(lista)
elemento = lista.pop()     #elimina el último elemento de la lista
print(lista)
elemento = lista.pop()     #elimina el último elemento de la lista
print(lista)
lista1 = [3, 1, 4, 1, 5, 9]    ##ordenar creciente-decreciente
lista_ordenada = sorted(lista1) 
print(lista_ordenada)   # Ordena la lista en orden ascendente
lista_ordenada_desc = sorted(lista1, reverse=True) 
print(lista_ordenada_desc)



tupla = (1, 3, 2, 4)
print(tupla)      # sin modificacion
lista = list(tupla)  
print(lista)      #imprime en forma de lista []
lista.remove(3)   
print(lista)       #elimina el 3 elemento (4) e imprime en forma de lista []
tupla = tuple(lista)
print(tupla)       #imprime en forma de tupla
lista_ordenada = sorted(tupla) 
print(lista_ordenada) # Ordena la tupla convirtiéndola a lista
tupla_ordenada = tuple(lista_ordenada)
print(tupla_ordenada)



conjunto = {1, 2, 3, 4}
lista_ordenada = sorted(conjunto) #imprime en forma de lista
print(lista_ordenada)
conjunto.add(7)     # Agrega 7 al conjunto
print(conjunto)
conjunto.remove(2)     #remueve el numero 2
print(conjunto) 



diccionario = {"clave2":"clave2" , "clave1":"clave1","clave3":"clave3"}
diccionario_ordenado_claves = dict(sorted(diccionario.items()))
print(diccionario_ordenado_claves)     # Ordenar por claves
diccionario_ordenado_valores = dict(sorted(diccionario.items(), key=lambda item: item[1]))
print(diccionario_ordenado_valores)     #ordenar por valores
diccionario["clave7"] = "clave7"    # Agrega  nuevos pares de clave-valor 7
diccionario['clave5']='clave5'      # Agrega  nuevos pares de clave-valor 5
print(diccionario)
del diccionario['clave2']    #elimina clave-valor 2
print(diccionario)
valor = diccionario.pop('clave7')   #elimina clave-valor 7
print(valor)



                # Crea una agenda de contactos por terminal

agenda = {"maria":"25" , "zulay":"17","rosa":"70" , "jose":"33"}
print(agenda)
agenda["felipe"] = "45"   # agregar elemento clave-valor a la agenda
print(agenda)
agenda_ordenado_claves = dict(sorted(agenda.items()))
print(agenda_ordenado_claves) #ordenda la agenda por clave (orden alfabetico de contactos)
agenda_ordenado_valores = dict(sorted(agenda.items(), key=lambda item: item[1]))
print(agenda_ordenado_valores)  #ordenada por valores
del agenda['zulay']   #eliminar elemento (clave) de la agenda
print(agenda)
valor = agenda.pop('jose') # imprime el valor de un elemento sin eliminarlo jose=33
print(valor)





