from array import array
from collections import deque
'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación
'''

# Listas ----------------------------------------
# Colección ordenada y modificable de elementos. Puedes acceder a los elementos de una lista mediante índices.

mi_lista= ["Troy", "Brais", "Moure"]
mi_lista.append ("Dev") # Inserción al final de la lista
print (mi_lista[3])  # Output Dev
mi_lista.remove ("Brais") # Debo decirle cual sino retorna ValueError
print(mi_lista)
mi_lista.pop(1) # Elimina la posición 1 que es Moure, si no le digo el índicie borra el último
print(mi_lista)
mi_lista.insert (0, "Nebula") # Inserción en una posición concreta
print(mi_lista)
veces= mi_lista.count("Troy") # cuenta las veces que sale la palabra Troy
print (veces, "vez / veces")
mi_lista.sort()  # Ordenación
print(mi_lista)
mi_lista.reverse()  # invierte la lista
print(mi_lista)
mi_lista_copiada= mi_lista.copy() # hago una copia
mi_lista.clear() # La limpio
print(mi_lista)
print(mi_lista_copiada)
print(type(mi_lista))

# Tuplas ----------------------------------------
# Inmutable, no se puede modificar una vez creada
mi_tupla= (20,10,30)
print(mi_tupla[1])  # Acceso
mi_tupla = tuple(sorted(mi_tupla))  # Ordenación
print(mi_tupla)
print(type(mi_tupla))

# Conjunto o set ----------------------------------------
# Colección no ordenada de elementos únicos. Para verificación de pertenencia y eliminación de entradas duplicadas. No se puede ordenar.
conjunto = {1, 2, 3, 3, 4, 5}
conjunto.add(6)  # Inserción
print(conjunto)
conjunto.remove(6)  # Eliminación
print(conjunto)
print(type(conjunto))

# Diccionario ----------------------------------------
# Colección no ordenada clave-valor. Se accede a los valores por las claves.
mi_dict = {"clave": "valor", 
           "nombre": "Troy", 
           "nick": "Nebula",
           "lista": mi_lista,
           "lista2": [1,2,3]
           }
print(mi_dict)
mi_dict["email"] = "troynebula@gmail.com"  # Inserción
print(mi_dict)
del mi_dict["clave"]  # Eliminación
print(mi_dict)
print(mi_dict["nombre"])  # Acceso
mi_dict["nick"] = "Troy Nebula"  # Actualización
print(mi_dict)
mi_dict = dict(sorted(mi_dict.items())) # Ordenación, pero me la da en una lista de tupla ordenadas.
# tengo que volver a pasarlo a diccionario usando dict pero en la misma frase como he puesto
print(mi_dict)
print(type(mi_dict))

# Colas y Pilas ----------------------------------------

pila = []
pila.append(10) # Inserción
pila.append(20)
pila.append(30)
print ("pila:", pila)

# Eliminar elementos de la pila (pop) El último en entrar es el primero en salir
elemento = pila.pop()  # Elimina y retorna el último elemento agregado (30)
print(elemento)  # Output: 30

print(pila)  # Output: [10, 20]

# Deque  ----------------------------------------
# (double-ended queue)  Mucho más rápido que colas y pilas
# Lista doblemente finalizada, fácil para insertar/eliminar en principios o finales

mi_deque = deque()

mi_deque.append(10)
mi_deque.append(20)
mi_deque.append(30)
print (mi_deque)

mi_deque.appendleft(5)  #inserta al principio
print (mi_deque)

print(mi_deque[1]) # la posicioon 1 es el 10, la 0 es el 5 que acabamos de añadir

mi_deque.pop() #elimina el último
mi_deque.popleft() #elimina el primero

print(mi_deque) 

# Arrays ----------------------------------------
# Como las listas, pero más eficientes para almacenar elementos del mismo tipo. 
# Es necesaria la importación del módulo array.

mi_array = array('i', [1, 2, 3])

'''
DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 '''

# Podría hacerlo con if cada opcion pero hay una nueva que es match
# Uso match porque solo reviso el valor de una variable (opcion)
# Necesito un bucle para que se ejecute mientras no le de a salir, un while
    
def agenda():

    dict_agenda = {}  # Creo mi diccionario agenda vacío

    def insertar_contacto(nombre):  # No me funcionaba ni guardaba porque no pasaba la variable nombre en esta función y no estaba definida
        telef = input("Introduce el teléfono del contacto:")
        if telef.isdigit() and len(telef) ==13:  # podría poner len(telef) >0 and len(telef) <=13
            dict_agenda[nombre] = telef
            print (f"Has introducido, Nombre: {nombre} y teléfono: {telef}")
            print (dict_agenda) 
        else:
            print ("Introduce un número de teléfono válido. Ejemplo 0034666123123")

    navegando= True  # Podría poner solamente while True y luego un break donde fuese a salir
    while navegando:  # Mientras sea True se sigue repiendo la agenda son más lineas pero por el momento lo veo más claro

        opcion = input ("---------------------\n1. Introduce contacto\n2. Busca contacto\n3. Actualiza contacto\n4. Elimina contacto\n5. Salir\n---------------------\nIntroduce una opción y pulsa Enter:")

        match opcion:  # un switch
            case "1":
                nombre= input("Introduce el nombre del contacto:")
                insertar_contacto(nombre)  # No olvidar pasar el  nombre
                
            case "2":
                nombre= input("Introduce el nombre del contacto a buscar:")
                if nombre in dict_agenda:
                    print (f"El número te teléfono del contacto: {nombre} es {dict_agenda[nombre]}")
                else:
                    print (f"El nombre introducido {nombre} no existe, prueba de nuevo")
            case "3":
                nombre = input("Introduce el nombre del contacto a actualizar:")
                if nombre in dict_agenda:
                    nuevo_nombre = input("Introduce el nuevo nombre del contacto:")
                    if nuevo_nombre != nombre:
                        del dict_agenda[nombre]
                        insertar_contacto(nuevo_nombre)
                    else:
                        print("El nuevo nombre debe ser diferente al nombre original.")
                else:
                    print(f"El nombre introducido {nombre} no existe, prueba de nuevo.")
            case "4":
                nombre= input("Introduce el nombre del contacto a exterminar:")
                if nombre in dict_agenda:
                    del dict_agenda[nombre]
                    print (f"{nombre} Exterminate!")
                else:
                    print (f"El nombre introducido {nombre} no existe, prueba de nuevo")
            case "5":
                print ("¡Gracias por usar nuestro sistema de agenda!")
                navegando = False
            case _: # Si escribre una opción distinta a las propuestas
                print ("No reconocido. Escribe del 1 al 5, ¡gracias!")

agenda()