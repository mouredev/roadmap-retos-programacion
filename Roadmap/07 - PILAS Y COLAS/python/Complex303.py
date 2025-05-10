"""
Pilas & Colas
"""

#Pila(Stack): Estructura donde el último en entrar es el primero en salir (LIFO). Las pilas se suelen utilizar con listas

stack = []

#push
stack.append(1) 
stack.append(3) 
stack.append(5) 
stack.append(7) 
print(stack)

#pop: pop quita el ultimo elemento en entrar
elemento = stack.pop()
print(elemento)
print(stack)

#otra forma de hacer el pop
# # stack_item = stack[len(stack) - 1]
# # del stack[len(stack) - 1]
# # print(stack_item)
# # print(stack)


#Cola (Queue): Estructura donde el primero en entrar es el primero en salir (FIFO).

queue = []
#enqueue
queue.append(2)
queue.append(4)
queue.append(6)
queue.append(8)
print(queue)

#dequeue. eleminamos el primer elemento
print(queue.pop(0))
print(queue)

#otra forma de eliminar el primer elemento
queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue)

"""
OTRA FORMA DE IMPLEMENTAR QUEUE"""
from collections import deque

cola = deque()

# Agregar elementos (enqueue)
cola.append(1)
cola.append(2)
cola.append(3)

print("Cola:", cola)

# Quitar elemento (dequeue)
primero = cola.popleft()
print("Elemento quitado:", primero)
print("Cola ahora:", cola)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos."""



#Con lista
# Definimos la función paginaweb
def paginaweb():
    # Creamos una lista vacía para guardar las URLs
    lista = []
    # Definimos la variable 'posicion' en -1, indicando que no hay ninguna página visitada al inicio
    posicion = -1

    # Iniciamos un bucle infinito que solo se romperá cuando se escriba 'salir'
    while True:
        # Pedimos al usuario que escriba una URL o una palabra clave
        opcion = input("Añade una url o interactua con palabras adelante/atras/salir: ")
        
        # Si el usuario escribe 'salir', terminamos el bucle y cerramos la función
        if opcion.lower() == 'salir':
            print("Saliendo del navegador...")
            break

        # Si el usuario escribe 'adelante'
        elif opcion.lower() == 'adelante':
            # Verificamos si se puede avanzar (es decir, que no esté ya en la última posición)
            if posicion < len(lista) - 1:
                # Avanzamos una posición
                posicion += 1
                # Mostramos la página actual
                print(f"Página actual: {lista[posicion]}")
            else:
                # Si no se puede avanzar, avisamos al usuario
                print("No hay páginas hacia adelante")

        # Si el usuario escribe 'atras'
        elif opcion.lower() == 'atras':
            # Verificamos si se puede retroceder (es decir, que no esté ya al inicio)
            if posicion > 0:
                # Retrocedemos una posición
                posicion -= 1
                # Mostramos la página actual
                print(f"Página actual: {lista[posicion]}")
            else:
                # Si no se puede retroceder, avisamos al usuario
                print("No hay páginas hacia atrás")

        # Si el usuario escribe cualquier otra cosa (una URL nueva)
        else:
            # Agregamos esa URL al final de la lista
            lista.append(opcion)
            # Actualizamos la posición actual para que apunte a esa nueva página
            posicion = len(lista) - 1
            # Mostramos la página actual
            print(f"Página actual: {lista[posicion]}")

        # Si la lista de páginas está vacía (lo cual nunca pasará aquí, pero está de precaución)
        if len(lista) == 0:
            print("Estas en la página principal")

# Llamamos a la función para que empiece a ejecutarse
paginaweb()



#Ejercicio de la impresora

# Definimos una función llamada shared_printed
def shared_printed():
    # Creamos una lista vacía llamada queue, que actuará como cola de impresión
    queue = []

    # Ciclo infinito: se repetirá hasta que el usuario escriba 'salir'
    while True:
        # Pedimos al usuario que escriba una opción: documento, 'imprimir' o 'salir'
        opcion = input("Añade un documento o selecciona imprimir/salir: ")

        # Si el usuario escribe 'salir' (ignorando mayúsculas/minúsculas)
        if opcion.lower() == "salir":
            print("Saliendo...")
            break  # Rompe el ciclo y termina la función

        # Si el usuario escribe 'imprimir'
        elif opcion.lower() == 'imprimir':
            # Verificamos si la cola no está vacía
            if len(queue) > 0:
                # quitamos e imprimimos el primer documento de la cola (FIFO)
                print(f"Imprimiendo: {queue.pop(0)}")

        # Si no es 'salir' ni 'imprimir', se considera un nombre de documento
        else:
            # Lo agregamos al final de la cola
            queue.append(opcion)

        # Mostramos el estado actual de la cola de impresión
        if len(queue) > 0:
            print(f'Cola de impresion {queue}')
        else:
            print("No hay archivos que imprimir")

# Llamamos a la función para que empiece a ejecutarse
#shared_printed()


