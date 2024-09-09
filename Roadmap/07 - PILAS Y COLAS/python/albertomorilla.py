# #07 PILAS Y COLAS

"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
  pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
  o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# PILAS/Stack (LIFO)

stack = []

# Push

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# Pop

stack_item = stack[len(stack)-1]
del stack[len(stack)-1]
print(stack_item)

print(stack.pop())

print(stack)

#COLAS/Queue (FIFO)
queue = []

#enqueue
queue.append(1)
queue.append(2)
queue.append(3)

#dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))


print(queue)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
    Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
    el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
    impresora compartida que recibe documentos y los imprime cuando así se le indica.
    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
    interpretan como nombres de documentos.
"""

# WEB

def web_oficial():
    
   stack = []

   while True:
    
      action = input("¿Qué deseas hacer? (adelante, atrás, página):")

      if action == "salir":
         print("Saliendo")
         break
      elif action == "adelante":
         pass
      elif action == "atras":
         if len(stack) > 0:
            stack.pop() 
      else:
         stack.append(action)

      if len(stack) > 0:
         print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
      else: 
         print("Estas en la pagina de inicio")

web_oficial()

def shared_print():

   queue = []

   while True:

      action = input("Añade un documento o selecciona imprimir/salir:")

      if action == 'salir':
         break
      elif action == 'imprimir':
         if len(queue) > 0:
            print(f"Imprimiendo: {queue.pop(0)}")
      else:
         queue.append(action)

      print(f"Cola de impresion: {queue}")

shared_print()

