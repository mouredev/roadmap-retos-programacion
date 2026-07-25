""" /*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */ """


# stacks

my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print(my_list)

my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)


# queue

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list)

del my_list[0]
print(my_list)
del my_list[0]
print(my_list)
del my_list[0]
print(my_list)
del my_list[0]
print(my_list)
del my_list[0]
print(my_list)

def web_navigation():
  stack = []
  forward_stack = []
  
  while True:
    action = input("agrega una url: ")

    if action == "salir":
      print("saliste del programa")
      break

    elif action == "adelante":
      if len(forward_stack) == 0:
        print("No hay pagina para donde coger papa bello")
      else:
        stack.append(forward_stack.pop())
        print(f"Volviste a la pagina --> {stack[len(stack) -1]}")

    elif action == "atras":
      if len(stack) > 1:
        forward_stack.append(stack.pop())
        print(f"has vuelto a la pagina --> {stack[-1]}")
      else:
        print("No puedo ir mas atras papa bello")


    elif action == "ver":
      print("Historial de navegacion", "".join(stack))

    else:
      stack.append(action)

    if len(stack) > 0:
      print(f"Has navegado a la web {stack[len(stack) -1]}")
    else:
      print("estas en la pagina de inicio")
    

web_navigation()

def impresora():
  queue = []

  while True:
    action = input("Añade un documento o escrime imprimir o salir: ")

    if action == "imprimir":
      if len(queue) > 0:
        print(queue.pop(0))
      else:
        print("No tienes nada que imprimir papa lindo")
    elif action == "ver":
      print("".join(queue))

    elif action == "salir":
      print("te saliste")
      break
    else:
      queue.append(action)

impresora()

