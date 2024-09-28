# #07 PILAS Y COLAS

"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
"""
# PILAS
# https://docs.hektorprofe.net/python/colecciones-de-datos/pilas/
print("PILAS - Stacks LIFO (Last In First Out)")
"""
Son colecciones de elementos ordenados que únicamente permiten dos acciones:

- Añadir un elemento a la pila.
- Sacar un elemento de la pila.

La peculiaridad es que el último elemento en entrar es el primero en salir. En inglés se conocen como estructuras LIFO (Last In First Out).
"""
# Las podemos crear como listas normales
stack = [3, 5, 7, 9]
print(stack)

# Añadir elementos al final con el append():
stack.append(11)
stack.append(13)
print(stack)    # [3, 5, 7, 9, 11, 13]

# Para sacar los elementos utilizaremos el método pop(). 
# Al utilizar este método devolveremos el último elemento, pero también lo borraremos:
print(stack.pop())  # 13
print(stack)    # [3, 5, 7, 9, 11]

# Si queremos trabajar con él deberíamos asignarlo a una variable:
last_value = stack.pop()
print(last_value)   # 11

# Si vamos sacando elementos llegará un momento en que la pila estará vacía 
# y dará error porque no podrá sacar nada más:
stack.pop()     # 9
stack.pop()     # 7
stack.pop()     # 5
stack.pop()     # 3
# stack.pop()     # IndexError: pop from empty list
print(stack)


# COLAS
# https://docs.hektorprofe.net/python/colecciones-de-datos/colas/
# https://docs.python.org/es/3.8/library/queue.html
print("\nCOLAS - Queue FIFO (First In First Out)")

"""
Son colecciones de elementos ordenados que únicamente permiten dos acciones:

- Añadir un elemento a la cola.
- Sacar un elemento de la cola.

La peculiaridad es que el primer elemento en entrar es el primero en salir. En inglés se conocen como estructuras FIFO (First In First Out).

La mejor alternativa en Python para crear colas es usar el módulo queue
https://docs.python.org/es/3.8/library/queue.html
"""

import queue

# Crear una cola
cola = queue.Queue()

# Agregar elementos
def agregar_elemento(cola, elemento):
    cola.put(elemento)
    print(f"Elemento agregado a la cola: {elemento}")

# Recuperar elemmentos
def recuperar_elemento(cola):
    try:
        elemento = cola.get(timeout=1)  # Espera hasta 1 segundo para obtener un elemento
        print(f"Elemento recuperado de la cola: {elemento}")
        return elemento
    except queue.Empty:
        print("La cola está vacía, no hay elementos que recuperar.")

# Probar funciones
# Agregar elementos a la cola
agregar_elemento(cola, 1)
agregar_elemento(cola, 2)
agregar_elemento(cola, 3)

# Recuperar elementos de la cola
recuperar_elemento(cola)  # 1
recuperar_elemento(cola)  # 2
recuperar_elemento(cola)  # 3
recuperar_elemento(cola)  # La cola está vacía, no hay elementos que recuperar.


"""
* DIFICULTAD EXTRA (opcional):
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
"""
print("\nDIFICULTAD EXTRA")

print("\nSimular el mecanismo adelante/atrás de un navegador web".upper())

# Inicializar la pila para el historial y un índice para la posición actual
historial = []      # Lista que actúa como pila para el historial de páginas visitadas
indice_actual = -1  # Indica la posición actual en el historial (inicialmente no hay páginas visitadas)

def navegar(pagina):
    # Ir a una nueva página.
    global indice_actual  # Usamos la variable global
    
    # Verifica si el indice_actual es menor que la longitud del historial menos uno.
    if indice_actual < len(historial) - 1:
        # Si estamos en medio del historial y vamos a una nueva página, descartamos adelante
        historial[indice_actual + 1:] = []  # Limpiar el historial hacia adelante
    historial.append(pagina)  # Agregar nueva página al historial
    indice_actual += 1  # Actualizar la posición
    print(f"Navegando a: {pagina}")

def atras():
    # Navegar hacia atrás en el historial.
    global indice_actual  # Usamos la variable global
    
    # Comprueba si indice_actual es mayor que 0. 
    # Si es así, significa que hay una página anterior a la que puede navegar.
    if indice_actual > 0:
        # Decrementa indice_actual en uno para moverse hacia atrás en el historial.
        indice_actual -= 1  # Mover hacia atrás
        # Muestra el nombre de la página a la que ha retrocedido.
        print(f"Navegando a: {historial[indice_actual]}")
    else:
        # Si no hay páginas anteriores, se muestra un mensaje indicando que no se puede retroceder.
        print("No hay más páginas en el historial para ir hacia atrás.")

def adelante():
    # Navegar hacia adelante en el historial.
    global indice_actual  # Usamos la variable global
    
    # Comprueba si indice_actual es menor que el último índice del historial. 
    # Esto indica que hay una página hacia adelante.
    if indice_actual < len(historial) - 1:
        indice_actual += 1 # Mover hacia adelante
        # Muestra el nombre de la página a la que ha avanzado.
        print(f"Navegando a: {historial[indice_actual]}")
    else:
        # Si no hay páginas hacia adelante, se muestra un mensaje indicando que no se puede avanzar.
        print("No hay más páginas para avanzar.")

# Interacción con el usuario

# Se usa un bucle while True para permitir que el usuario 
# siga interactuando con el simulador.
while True:
    # Se le pide al usuario que ingrese un comando. 
    # strip() elimina los espacios en blanco al principio y al final, y
    # lower() convierte la entrada a minúsculas para que la comparación 
    # sea insensible a mayúsculas.
    comando = input("Ingresa una página web, 'adelante', o 'atras' (o 'salir' para terminar): ").strip().lower()
    
    # Si el usuario ingresa 'salir', se imprime un mensaje y se rompe el bucle, 
    # terminando el programa.
    if comando == "salir":
        print("Saliendo del simulador del navegador")
        break
    # Si el comando es 'atras', se llama a la función atras().
    elif comando == "atras":
        atras()
    # Si el comando es 'adelante', se llama a la función adelante().
    elif comando == "adelante":
        adelante()
    # Para cualquier otra entrada, se considera que es una nueva página, 
    # por lo que se llama a ir_a_pagina(comando).
    else:
        navegar(comando)


"""
* DIFICULTAD EXTRA (opcional):
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
"""