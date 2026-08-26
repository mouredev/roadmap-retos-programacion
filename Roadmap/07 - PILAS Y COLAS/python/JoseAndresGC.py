# PILAS (STACKS):

# INTRODUCCIÓN

"""
Principio LIFO (Last In, First Out)
Ejemplo: Una pila de platos, el último plato que se coloca en la pila es el primero que se retira. En pocas palabras último que entra, ultimo que sale.
"""

maximo = 3 # capacidad máxima de la pila
pila = [None] * maximo # inicializo la pila [None, None, None]
tope = 0 # indica el número o puesto del último elemento agregado a la pila

def push(element):
    # tomo la pila (por ahora "vacía") y lleno el espacio numerado por el tope con el elemento que quiera agregar
    # luego incremento el tope para que se llene el siguiente espacio de la pila

    global tope

    pila[tope] = element
    tope += 1

# RECUPERACION

def pop():
    # resto al tope -1 para obtener el número o posición del último elemento agregado a la pila
    # luego, guardo el elemento que se encuentra en esa posición dada
    # por último, borro o limpio el espacio de la pila
    # retorno el elemento guardado

    global tope
    global pila

    tope -= 1
    nuevoElemento = pila[tope]
    pila[tope] = None

    return nuevoElemento

# COLAS (QUEUES):

# INTRODUCCIÓN (QUEUE)

"""
Principio FIFO (First In, First Out)
Ejemplo: Una fila de personas esperando para comprar boletos, la primera persona que llega a la fila es la primera que es atentida,
en pocas palabras, el primero que entra, es el primer que sale.
"""

cantidad = 0 # cantidad de elementos que hay en la cola, se incrementa cada vez que se agrega un elemento y se resta cada vez que se elimina un elemento
frente = 0 # indica el número o puesto del primer elemento agregado a la cola, se va incrementando cada vez que se quita un elemento de la cola
final = 0 # indica el número o puesto del último elemento agregado a la cola, se va incrementando cada vez que se agrega un elemento a la cola
cola = [None, None, None] # la cola sin más...

def enqueue(element):
    # tomo la cola (por ahora "vacía") y lleno el asiento númerado por el final con el elemento que quiera agregar
    # incremento el valor de final para mover el asiento a la derecha (se usa el residuo para que vuelva al inicio de la cola cuando alcance el final de la misma)
    # incremento la cantidad de elementos que hay en la cola +1

    global final, cantidad

    cola[final] = element
    final = (final + 1) % maximo
    cantidad += 1

# RECUPERACIÓN (DEQUEUE)

def dequeue():
    # primero guardar el elemento "atendido" que se encuentra en el frente de la cola
    # luego, limpiar el espacio del frente de la cola
    # luego, usar el residuo para mover el frente a la derecha
    # por último, restarle a cantidad -1 para indicar que se eliminó un elemento de la cola
    # retornar el elemento "atendido" guardado

    global frente, cantidad

    atendido = cola[frente]
    cola[frente] = None
    frente = (frente + 1) % maximo
    cantidad -= 1

    return atendido

# DIFICULTAD EXTRA:

# Simulación de adelante/atrás de un navegador web usando pilas (stacks)

# primero saludar al usuario 
# todo esto metido en un ciclo infinito que solo se rompe cuando el usuario escriba "salir" para finalizar el programa 
# seguido de ello, decirle que ingrese una dirección web o el comando escrito "salir" para finalizar el programa con un mensaje de despedida "¡Adios!"
# cuando el usuario escriba la dirección web simplemente se le mostrará un texto que diga "Estás navegando en [dirección web ingresada]"
# al meter la URL en la pila, el programa le preguntará al usuario si desea ir "atrás" o "adelante" ("adelante" solo aparecerá si hay algo adelante en la pila) o "salir"
# si el usuario escribe "atrás":
# 1 - se volverá a mostrar el mensaje de que ingrese una dirección web o el comando "salir"
# 2 - además, se mostrará un mensaje debajo que dirá "puedes ir hacia delante escribiendo "adelante" (si es que hay algo en la pila de adelante)
# Si el usuario escribe "adelante":
# 1 - se mostrará la web que se encuentra adelante de la pila 
# ejemplo: si en la pila no hay lugar a donde ir no se muestra el mensaje de "adelante" y si luego el usuario decide ir hacia atrás volvería al menú
# en ese momento el programa le preguntará si quiere ingresar otra dirección web, salir, ir hacia atrás o ir hacia adelante (si es que hay algo en la pila de adelante)

def navegador_web():
    url_actual = ""
    historial_atras = []
    historial_adelante = []

    bienvenida = print("¡Bienvenido a tu navegador web!")

    while True:

        if url_actual == '':
            entrada = input("Ingresa una dirección web o el comando 'salir' para finalizar el programa: ").strip()
        else:
            print(f"¡Estás navegando en {url_actual}!")
            
            # opciones para el usuario:
            mensaje_opciones = "¿Qué desea hacer ahora? ['atras' / 'salir'"

            # si hay algo en el historial de adelante entonces se muestra la opción para ir hacia adelante
            if len(historial_adelante) > 0:
                mensaje_opciones += " / adelante"

            # para completar el mensaje de opciones independientemente de si se muestra o no la opción de "adelante"
            mensaje_opciones += " ]: "
            entrada = input(mensaje_opciones).strip().lower()

        if entrada == 'salir':
            print("¡Adios! Esperamos volver a verte pronto.")
            break

        if url_actual == "":
            url_actual = entrada
        elif entrada != "atras" and entrada != "adelante":
            historial_atras.append(url_actual)
            url_actual = entrada
            historial_adelante.clear() # limpio el historial de adelante cada vez que se ingresa una nueva URL
        elif entrada == "atras":
            if len(historial_atras) > 0:
                historial_adelante.append(url_actual)
                url_actual = historial_atras.pop()
            else:
                print("No hay páginas para ir atrás... Ingrese otra URL o escriba 'salir' para terminar su navegación")
        elif entrada == "adelante":
            if len(historial_adelante) > 0:
                historial_atras.append(url_actual)
                url_actual = historial_adelante.pop()

# navegador_web()

# Mecanismo de una impresora compartida usando colas (QUEUE)

# definir la cantidad de elementos que hay en la cola
# definir el maximo de elementos que pueden ingresar en la cola
# definir el frente y final de la cola
# definir la cola

# saludar al usuario
# decirle al usuario que ingrese el nombre del documento o escribir "salir" para terminar el proceso
# si es "salir" termina el programa
# decirle al usuario que al escribir "imprimir" se inicirá el proceso de impresión
# todo lo demás que sea escrito se interpretará como nombres de documentos INTRODUCIENDO en ese momento los elementos en la cola hasta que el usuario meta la palabra "imprimir"

# a la posicion final de la cola se le asigna el elemento entrante
# a final se le asigna el resultado de la operación (final + 1) % maximo esto es para mover un puesto en la cola sumandola +1 al final y procurando que si el final llega al maximo vuelva al inicio y no genere errores de desbordamiento entiendo
# aumento la cantidad +1

# definir y almacenar la posicion del frente de la cola en atendido (se marca como atendido el puesto)
# se limpia la memoria de la posicion del frente de la cola
# se usa exacamente la misma operación del módulo, pero ésta vez con el frente de la cola
# restamos -1 a la cantidad porque se eliminó un elemento de la cola

def impresora():

    bienvenida = print("Bienvenido a tu impresora!")

    cantidad = 0
    maximo = 3
    frente = 0
    final = 0
    cola = [None] * maximo

    

    while True:

        # INTRODUCCIÓN (ENQUEUE)

        entrada = input("Ingrese el nombre de sus documentos a imprimir, o escriba 'salir' para terminar el proceso: ").lower().strip()

        if entrada == "salir":
            print("Apagando la impresora...")
            break
        elif entrada == "imprimir":
            
            if cantidad == 0:
                print("Lo siento, No hay nada qué imprimir")
            else:
                # RECUPERACIÓN (DEQUEUE)
                atendido = cola[frente]
                cola[frente] = None
                frente = (frente + 1) % maximo
                cantidad -= 1
                print(f"El documento '{atendido}' se ha impreso con éxito!")

        else:
            if cantidad == maximo:
                print("La cola está llena!")
            else:
                cola[final] = entrada
                final = (final + 1) % maximo
                cantidad += 1
                print(f"Documento '{entrada}' agregado a la cola con éxito!")

# impresora()
