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
dict_1.keys() #Devuelve las claves del diccionario
dict_2.values() #Devuelve los valores del diccionario
    
#-LOS CONJUNTOS son mutables
conjunto_1 = {1,2,3,4,5}
conjunto_2 = {6,7,8,9,10}

#INSERTAR / BORRAR / ACTUALIZAR / ORDENAR
conjunto_1.add(6) #Agrega un elemento al conjunto
conjunto_2.remove(6) #Elimina el elemento 6 del conjunto
conjunto_1.discard(6) #Elimina el elemento 6 del conjunto
conjunto_2.pop() #Elimina un elemento aleatorio del conjunto
conjunto_1.clear() #Elimina todos los elementos del conjunto
conjunto_2.update([11,12,13,14,15]) #Agrega varios elementos al conjunto

#-LAS COLAS son mutables
cola_1 = [1,2,3,4,5]
cola_2 = [6,7,8,9,10]

#INSERTAR / BORRAR / ACTUALIZAR / ORDENAR
cola_1.append(6) #Agrega un elemento al final de la cola
cola_2.insert(0,5) #Agrega un elemento en la posición 0
cola_1.pop(0) #Elimina el elemento en la posición 0
cola_2.remove(6) #Elimina el elemento 6 de la cola
cola_1.clear() #Elimina todos los elementos de la cola
cola_2[0] = 1 #Actualiza el elemento en la posición 0   

#-LAS PILAS son mutables
pila_1 = [1,2,3,4,5]
pila_2 = [6,7,8,9,10]

#INSERTAR / BORRAR / ACTUALIZAR / ORDENAR
pila_1.append(6) #Agrega un elemento al final de la pila
pila_2.insert(0,5) #Agrega un elemento en la posición 0
pila_1.pop() #Elimina el último elemento de la pila
pila_2.pop(0) #Elimina el elemento en la posición 0
pila_1.clear() #Elimina todos los elementos de la pila
pila_2[0] = 1 #Actualiza el elemento en la posición 0

#PROGRAMA DE AGENDA DE CONTACTOS    
agenda = {} #Diccionario para almacenar los contactos

def insertar_contacto(): #Función para insertar un contacto
    print('Insertar contacto:')
    nombre = input('Nombre:') #Solicita el nombre del contacto   
    telefono = input('Teléfono:') #Solicita el teléfono del contacto 
    if nombre in agenda: #Verifica si el contacto ya existe
        print('El contacto ya existe')
    else:
        agenda[nombre] = telefono #Agrega el contacto a la agenda
        print('Contacto agregado')

def buscar_contacto(): #Función para buscar un contacto
    print('Buscar contacto:')
    nombre = input('Nombre:') #Solicita el nombre del contacto
    if nombre in agenda: #Verifica si el contacto existe
        print('Teléfono:', agenda[nombre]) #Muestra el teléfono del contacto
    else:
        print('El contacto no existe') 

def actualizar_contacto(): #Función para actualizar un contacto
    print('Actualizar contacto:')
    nombre = input('Nombre:') #Solicita el nombre del contacto
    if nombre in agenda: #Verifica si el contacto existe
        telefono = input('Teléfono:') #Solicita el nuevo teléfono del contacto
        agenda[nombre] = telefono #Actualiza el teléfono del contacto
        print('Contacto actualizado')
    else:
        print('El contacto no existe')
        
def eliminar_contacto(): #Función para eliminar un contacto
    print('Eliminar contacto:')
    nombre = input('Nombre:') #Solicita el nombre del contacto
    if nombre in agenda: #Verifica si el contacto existe
        del agenda[nombre] #Elimina el contacto de la agenda
        print('Contacto eliminado')
    else:
        print('El contacto no existe')        
               
def menu(): #Función para mostrar el menú
    print('Agenda de contactos')
    print('1. Buscar contacto')
    print('2. Insertar contacto')
    print('3. Actualizar contacto')
    print('4. Eliminar contacto')
    print('5. Salir')
    opcion = int(input('Seleccione una opción: '))  #Solicita la opción a realizar
    return opcion
    
#funcion main
def main():
    opcion = 0
    while opcion != 5: #Muestra el menú hasta que se seleccione la opción 5
        opcion = menu()
        if opcion == 1:
            buscar_contacto()
        elif opcion == 2:
            insertar_contacto()
        elif opcion == 3:
            actualizar_contacto()
        elif opcion == 4:
            eliminar_contacto()
        elif opcion == 5:
            print('Fin del programa')
        else:
            print('Opción no válida')  
                     
main() #Ejecuta el programa
            