# PILAS Y COLAS

# stack o pila - LIFO (Last In, First Out)
stack = []
print("Pila (stack) inicial =>", stack) # -> []
stack.append(1) # Añade valores a la pila (stack)
stack.append(2)
stack.append(3)
print(f"Pila (stack) después de varios appends: stack.append(x) => {stack}") # -> [1, 2, 3]
popped = stack.pop() # Elimina el último elemento de la pila (stack)
print(f"Último elemento de la pila (stack) eliminado: stack.pop() => {popped}") # -> 3
print(f"Pila (stack) después de eliminar el último elemento => {stack}\n") # -> [1, 2]

# queue o cola - FIFO (First In, First Out)
queue = []
print("Cola (queue) inicial =>", queue) # -> []
queue.append("a") # Añade valores a la cola (queue)
queue.append("b")
queue.append("c")
print(f"Cola (queue) después de varios appends: queue.append(x) => {queue}") # -> ['a', 'b', 'c']
popFirst = queue.pop(0) # Elimina el primer elemento de la cola (queue)
print(f"Último elemento de la cola (queue) eliminado: queue.pop(0) => {popFirst}") # -> a
print(f"Cola (queue) después de eliminar el primer elemento => {queue}\n") # -> ['b', 'c']

""" 
DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.
"""
def web_navigation():
    stack = []
    while True:
        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )
        if action == "salir":
            print("Saliendo...")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        if len(stack) > 0:
            print(f"Estás en la web: {stack[len(stack) - 1]}.")
        else:
            print("Estás en la página de inicio.")

def shared_printed():
    queue = []
    while True:
        action = input("Añade un documento o selecciona imprimir o salir: ")
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}...")
            else:
                print("No hay documentos en la cola de impresión.")
        else:
            queue.append(action)
        print(f"Cola de impresión: {queue}")

web_navigation()
shared_printed()
