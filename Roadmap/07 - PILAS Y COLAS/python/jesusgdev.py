'''
JERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
   pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
   o lista (dependiendo de las posibilidades de tu lenguaje).
  
 * DIFICULTAD EXTRA (opcional):
 *   Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
     de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
     que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
     el nombre de una nueva web.
 *   Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
     impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
     interpretan como nombres de documentos.
  
'''

# Pilas

# 1. Stacks - LIFO

# Creamos una pila vacia usando una lista
stack_lifo = []

# Agregamos elementos a la pila
# Al usar append(), cada nuevo elemento se añade en la parte superior de la pila.
# El último elemento en entrar será el primero en salir.
stack_lifo.append("book1")
stack_lifo.append("book2")
stack_lifo.append("book3")

print("Pila actual:", stack_lifo)

# Eliminamos el último elemento de la pila con pop()
top = stack_lifo.pop()    
print("Quitamos:", top)

# Mostramos el estado de la pila después de quitar el elemento
print("Pila despues de quitar el ultimo elemento: ", stack_lifo)

# 2. Colas (Queues) - FIFO (First In, First Out)

# Creamos una cola vacía utilizando una lista
queue = []

# Agregamos elementos a la cola con append()
# Los elementos se añaden al final de la lista, simulando una cola.
queue.append("Person1")
queue.append("Person2")
queue.append("Person3")

print("Cola actual:", queue)

# Eliminamos el primer elemento agregado usando pop(0)
# Esto simula el comportamiento de una cola FIFO.
first = queue.pop(0)
print("Pago en la fila del supermercado:", first)

# Mostramos el estado de la cola después
print("Fila despues:", queue)


'''
Extra
'''

# Navegador Web (Simulado con pilas LIFO)

# Simulación de un navegador web utilizando pilas (LIFO)
# La pila backward_history almacena las páginas visitadas anteriormente
# La pila forward_history almacena las páginas a las que se puede volver si el usuario presiona "adelante"
# current_page contiene la página actual en la que se encuentra el usuario

backward_history = []
forward_history = []

def browser():
    current_page = "www.solarflare/home.org"  # Página inicial del navegador
    print("\n🌐 Bienvenido al navegador Solarflare")
    print(f"Actualmente estás en: {current_page}")
    print('- Escribe el nombre de una nueva página para visitarla.')
    print('- Escribe "atras" para regresar a la página anterior.')
    print('- Escribe "adelante" para avanzar a una página siguiente.')
    print('- Escribe "salir" para cerrar el navegador.')

    while True:
        action = input("\n🔍 ¿Qué acción deseas realizar?: ")

        # Acción: salir
        # Esta condición permite al usuario salir del bucle principal y finalizar la simulación
        if action == "salir":
            print("\n👋 Saliendo del navegador...")
            break

        # Acción: adelante
        # Permite al usuario avanzar a una página previamente visitada (si ha retrocedido antes)
        elif action == "adelante":
            if len(forward_history) > 0:
                # Guardamos la página actual en el historial hacia atrás antes de avanzar
                backward_history.append(current_page)
                # Extraemos la siguiente página desde el historial hacia adelante
                current_page = forward_history.pop()
                # Mostramos al usuario la página a la que ha avanzado
                print(f"\n➡️ Avanzando a: {current_page}")
            else:
                # Si no hay historial hacia adelante, notificamos al usuario
                print("⚠️ No hay páginas siguientes disponibles.")

        # Acción: atrás
        # Permite al usuario volver a la página que visitó justo antes de la actual
        elif action == "atras":
            if len(backward_history) > 0:
                # Guardamos la página actual en el historial hacia adelante antes de retroceder
                forward_history.append(current_page)
                # Extraemos la última página visitada desde el historial hacia atrás
                current_page = backward_history.pop()
                # Mostramos al usuario la página a la que ha retrocedido
                print(f"\n⬅️ Regresando a: {current_page}")
            else:
                # Si no hay historial hacia atrás, notificamos al usuario
                print("⚠️ No hay páginas anteriores disponibles.")

        # Acción: visitar nueva página
        # Cualquier entrada que no sea una palabra clave se interpreta como una nueva URL
        else:
            # Antes de cambiar la página actual, la guardamos en el historial hacia atrás
            backward_history.append(current_page)
            # Establecemos la nueva página como la actual
            current_page = action
            # Borramos el historial hacia adelante, ya que se inicia un nuevo camino de navegación
            forward_history.clear()
            # Mostramos la nueva página al usuario
            print(f"\n🌍 Visitando nueva página: {current_page}")



# Impresora Compartida (Simulada con Cola - FIFO)

# Simulación de una impresora compartida utilizando una cola (FIFO)
# La lista printer_queue funciona como una cola de impresión
# Los documentos se agregan al final de la cola y se imprimen por orden de llegada

printer_queue = []

def printer():
    print("\n🖨️ Bienvenido al sistema de impresión Lexar Plus")
    print('- Escribe el nombre de un documento para agregarlo a la cola de impresión.')
    print('- Escribe "imprimir" para imprimir el documento más antiguo en la cola.')
    print('- Escribe "salir" para cerrar el sistema de impresión.')

    while True:
        action = input("\n📎 ¿Qué deseas hacer?: ")

        # Acción: salir
        # Finaliza la simulación de la impresora y sale del bucle principal
        if action == "salir":
            print("\n👋 Cerrando el sistema de impresión...")
            break

        # Acción: imprimir
        # Extrae el documento más antiguo de la cola y lo "imprime"
        elif action == "imprimir":
            if len(printer_queue) > 0:
                # Mostramos al usuario qué documento se está imprimiendo
                print(f"\n🖨️ Imprimiendo documento: {printer_queue[0]}")
                # Eliminamos el documento de la cola después de imprimirlo
                printer_queue.pop(0)
            else:
                # Si no hay documentos en la cola, se informa al usuario
                print("⚠️ La cola de impresión está vacía. Agrega un documento.")

        # Acción: agregar documento
        # Cualquier texto distinto a "imprimir" o "salir" se considera un nombre de documento
        else:
            # Añadimos el nuevo documento al final de la cola
            printer_queue.append(action)
            # Notificamos que el documento fue agregado correctamente
            print(f"\n✅ Documento '{action}' agregado a la cola de impresión.")    









