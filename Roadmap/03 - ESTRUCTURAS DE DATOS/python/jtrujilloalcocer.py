# ESTRUCTURAS DE DATOS

#   EJERCICIO:
#   - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#   - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  
#   DIFICULTAD EXTRA (opcional):
#   Crea una agenda de contactos por terminal.
#   - Debes implementar funcionalidades de búsqueda, inserción, actualización
#    y eliminación de contactos.
#   - Cada contacto debe tener un nombre y un número de teléfono.
#   - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#     y a continuación los datos necesarios para llevarla a cabo.
#   - El programa no puede dejar introducir números de teléfono no númericos y con más
#     de 11 dígitos (o el número de dígitos que quieras).
#   También se debe proponer una operación de finalización del programa.
 
# ESTRUCTURA DE DATOS
#-LAS LISTAS son mutables esto quiere decir que se pueden modificar
list_1 = [1,2,3,4,5] 
list_2 = [6,7,8,9,10]

#INSERTAR / BORRAR / ACTUALIZAR / ORDENAR
list_1.append(6) #Agrega un elemento al final de la lista
list_2.insert(0,5) #Agrega un elemento en la posición 0   
list_1.extend([7,8,9,10]) #Agrega varios elementos al final de la lista
list_2.append([11,12,13,14,15]) #Agrega una lista al final de la lista
list_1.pop() #Elimina el último elemento de la lista
list_2.remove(6) #Elimina el elemento 6 de la lista
list_1.clear() #Elimina todos los elementos de la lista
list_2[0] = 1 #Actualiza el elemento en la posición 0
list_1.sort() #Ordena la lista
list_2.reverse() #Invierte la lista
list_1.count(1) #Cuenta cuantas veces aparece el elemento 1 en la lista

#-LAS TUPLAS son inmutables esto quiere decir que no se pueden modificar
tuppla_1 = (1,2,3,4,5)
tuppla_2 = (6,7,8,9,10)

#INSERTAR / BORRAR / ACTUALIZAR / ORDENAR
tuppla_1.count(1) #Cuenta cuantas veces aparece el elemento 1 en la tupla
tuppla_2.index(6) #Devuelve el índice del elemento 6 en la tupla
tuppla_1 + tuppla_2 #Concatena las tuplas
tuppla_1 * 2 #Repite la tupla 2 veces

#-LOS DICCIONARIOS son mutables 
dict_1 = {'nombre':'Juan', 'edad': 25, 'cursos': ['Python','Django','Flask']}
dict_2 = {'nombre':'Maria', 'edad': 30, 'cursos': ['Python','Django','Flask']}

#INSERTAR / BORRAR / ACTUALIZAR / ORDENAR
dict_1['nombre'] = 'Juan Carlos' #Actualiza el valor de la clave nombre
dict_2['cursos'].append('MongoDB') #Agrega un elemento a la lista de cursos 
dict_1.pop('edad') #Elimina la clave edad
dict_2.popitem() #Elimina el último elemento insertado
dict_1.clear() #Elimina todos los elementos del diccionario
dict_2.update({'nombre':'Maria', 'edad': 30, 'cursos': ['Python','Django','Flask']}) #Actualiza el diccionario
    
#-LOS CONJUNTOS son mutables
conjunto_1 = {1,2,3,4,5}
conjunto_2 = {6,7,8,9,10}

#-LAS COLAS son mutables
cola_1 = [1,2,3,4,5]
cola_2 = [6,7,8,9,10]

#-LAS PILAS son mutables
pila_1 = [1,2,3,4,5]
pila_2 = [6,7,8,9,10]

 