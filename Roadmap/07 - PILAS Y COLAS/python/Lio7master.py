#  EJERCICIO:
#  Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  o lista (dependiendo de las posibilidades de tu lenguaje).

#  DIFICULTAD EXTRA (opcional):
#  - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#    Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#    el nombre de una nueva web.
#  - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#    impresora compartida que recibe documentos y los imprime cuando así se le indica.
#    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#    interpretan como nombres de documentos.


# Pila/Stack (LIFO - Last In, First Out)

stack = []
stack.append("1") #push 
stack.append("2")
stack.append("3")

print(stack)
#pop
stack_item = stack[len(stack) - 1] 
del stack[len(stack) - 1]



print(stack_item)
print(stack)
print(stack.pop()) #es un mecanismo nativo de las listas (no en todos los  lenguanjes), internamente en python la lista funciona como una pila/cola con pop.
print(stack)

# Cola/Queue (FIFO - Primero en entrar, primero en salir)

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)
# dequeue
queue_item = queue[0]
del queue[0]

print(queue_item)
print(queue)
print(queue.pop(0)) #el pop lo hacemos del elemento cero porque seria el primero entrar y el primero que debe salir

print(queue)

# Extra

# WEB

def web_nav():
    stack = []

    while True:

        action = input( "añande una URL o interactua con palabras Adelante/Atras/salir: ")

        if action == "salir":
            print("saliendo del programa")
            break
        elif action == "adelante":
            pass 
            #El stack no es fincional para ir para adelante ya que cada que sacamos
            #un elemento de la pila este desaparece de la mismaa por lo que no 
            #podriamos recuperar amenos que estemos aplicando logica extra que no sea parte del stack
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        if len(stack) > 0:
            print(stack[len(stack)-1])
        else:
            print("Estas en el inicio.")

web_nav()

#Impresora compartida

def share_printed():
    queue = []

    while True:
          action = input("Añade documenteso o selecciona instruccion imprimir/salir: ")

          if action == "salir":
              break
          elif action == "imprimir":
            print("------IMPRIMIENDO------")
            if len(queue) > 0:
                print(queue.pop(0))
            else:
                print("cola de impresion vacia.")
          else:
              queue.append(action)

share_printed()