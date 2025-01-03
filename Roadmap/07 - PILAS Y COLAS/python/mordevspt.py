"""
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).
"""

'''
LIFO
'''
print("\nLIFO\n")

# LIST
print("\nLISTA\n")

mi_list_stack = []

# Añadimos elementos a la pila, usamos el métdo que tenemos en las listas => append() 
# como si fuera la function push
mi_list_stack.append("Hola")
mi_list_stack.append("Python")
mi_list_stack.append("!")

print("\nPila rellenada\n")
print(mi_list_stack)

# Usamos pop() para eliminar e último elemento introducido => LIFO
print("\nBorrado de elementos de la pila:\n")
print(mi_list_stack.pop())
print(mi_list_stack.pop())
print(mi_list_stack.pop())

print('\nTras el borrado de elementos de la pila:')
print(mi_list_stack)

# QUEUE MODULE
print("\nQUEUE MODULE\n")

from queue import LifoQueue

# Inicializamos el stack con un tamaño máximo
stack = LifoQueue(maxsize=3)

# Con la función qsize() vemos el número de elementos
# que tiene la pila
print(stack.qsize())

# Hacemos uso de la función put() para hacer el push
stack.put("Hola")
stack.put("Python")
stack.put("!")

print("\nPila rellenada\n")
print("Lleno: ", stack.full())
print("Tamaño: ", stack.qsize())

# Hacemos uso de la función get() para hacer pop => LIFO
print('\nBorrado de elementos de la pila:\n')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nVaciar: ", stack.empty())

# NODE CLASS
print("\nNODE CLASS\n")

# Class Node
class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

# Class Stack
class Stack:

    # Inicializamos una pila haciendo uso de un 
    # modo ficticio, que es más sencillo de
    # manejar en casos extremos
    def __init__(self):
      self.head = Node("head")
      self.size = 0

    # Representación de un String en la pila
    def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
          out += str(cur.value) + "->"
          cur = cur.next
      return out[:-2]

    # Obtener el tamaño actual de la pila
    def getSize(self):
      return self.size

    # Comprobar si la pila está vacía
    def isEmpty(self):
      return self.size == 0

    # Obtener el elemento superior de la pila por medio de peek
    def peek(self):
      #  Comprobación para ver si estamos viendo una pila vacía
      if self.isEmpty():
          return None
      return self.head.next.value

    # Introducir un valor en la pila por medio de push
    def push(self, value):
      node = Node(value)
      node.next = self.head.next # Make the new node point to the current head
      self.head.next = node #!!! # Update the head to be the new node
      self.size += 1

    # Elimina un valor de la pila por medio de pop y lo devuelve.
    def pop(self):
      # Comprobamos que la pila no esté vacía 
      if self.isEmpty():
          raise Exception("Eliminando desde una pila vacía")
      remove = self.head.next
      self.head.next = remove.next #!!! changed
      self.size -= 1
      return remove.value

# Ejecución

# Creamos una instancia de la pila
stack = Stack()

# Introducimos varios valores creados desde un bucle for
for i in range(1, 11):
    stack.push(i)

# Imprimimos la pila tras el rellenado
print("\nPila rellenada\n")
print(stack)

# Eliminamos varios valores pasados desde un bucle for
print("\nBorrado de elementos de la pila:\n")
for _ in range(1, 6):
    top_value = stack.pop()
    print(f"Eliminado: {top_value}") # variable name changed

# Imprimimos la pila tras el borrado
print('\nTras el borrado de elementos de la pila\n:')
print(stack)

'''
FIFO
'''
print("\nFIFO\n")

# Creamos una lista a modo de Queue

q = []

# Añadimos varios elementos, por ejemplo desde un for
# a nuestra Queue
for i in range(5):
	q.append(i)

# Mostramos el contenido de l Queue una vez rellenada
print("Elementos en la Queue: " , q)

# Al eliminar elementos, lo hacemos por el primer
# elemento en la cola, es decir, índice 0
removedele = q.pop(0)
print("Elmento eliminado: " , removedele)

print(q)

# Mostrar el elemento en cabeza en la Queue
head = q[0]
print("Primer elemento (Head) en la Queue:" , head)

# Tamaño de la Queue, es decir, el número
# de elementos que la forman
size = len(q)
print("Tamaño de la Queue: " , size)


"""
* DIFICULTAD EXTRA (opcional):
"""

"""
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.
"""

# EJERCICIO 1
# Usaremos LIFO
print("\nEJERCICIO 1 - CON ADELANTE (COMO LISTA)\n")

# Nuestra pila
mi_list = []

# Posición inicial
posicion_pila = 0

# Pregunta inicial
def preguntarAlUsuario(position = 0):
  return input("Escribe una página a navegar o navega Adelante (adelante) o Atrás (atras): ")

# Respuesta Atrás
def goAfter(position):
  if position <= 0:
    print("Ha llegado al principio")
    position = 0
  elif position > 0:
    position -= 1
  # Sea lo que sea lo devolvemos
  return position

# Respuesta Adelante
def goBefore(position):
  if position == (len(mi_list) - 1):
    print("Ha llegado al final")
    position = (len(mi_list) - 1)
  elif position < (len(mi_list) - 1):
    position += 1
  # Sea lo que sea lo devolvemos
  return position

# Navegación
def showWebSite(position):
  print(f"Navegando por la web: {mi_list[position]}")

# Programa inicial
def navegacion():
  respuesta = preguntarAlUsuario() 
  while True:
    match respuesta:
      case "atras":
        # Comprobamos
        if len(mi_list) == 0:
          print("No hay más registros")
          respuesta = preguntarAlUsuario()
        else:
          posicion_pila = goAfter(posicion_pila)
          showWebSite(posicion_pila)
          respuesta = preguntarAlUsuario()
          
      case "adelante":
        # Comprobamos
        if len(mi_list) == 0:
          print("No hay más registros")
          respuesta = preguntarAlUsuario()
        else:
          posicion_pila = goBefore(posicion_pila)
          showWebSite(posicion_pila)
          respuesta = preguntarAlUsuario()
      case "salir":
        print("\n¡HASTA LUEGO!\n")
        break
      case _:
        if len(respuesta) >= 1:
          mi_list.append(respuesta)
          posicion_pila = mi_list.index(respuesta)
          showWebSite(posicion_pila)
        else:
          print("Escriba una palabra u opción.")
        # Pase lo que pase
        respuesta = preguntarAlUsuario()

# Ejecución programa 1
navegacion()

print("\nEJERCICIO 1 - SIN ADELANTE (COMO PILA)\n")

# Nuestra pila
mi_stack = []

# Navegación
def showWebSiteUser(position):
  print(f"Navegando por la web: {mi_stack[position]}")

# Programa Inicial
def navegacionWeb():
  respuesta = preguntarAlUsuario()
  while True:
    match respuesta:
      case "atras":
        if len(mi_stack) >= 1:
          # Eliminamos el último registro
          mi_stack.pop()
          # Para no provocar un problema en caso de no quedar elementos en la pila
          if (len(mi_stack) > 0):
            showWebSiteUser(len(mi_stack)-1)
          else:
            print("Ha llegado al principio")
        # Pase lo que pase
        
        respuesta = preguntarAlUsuario()
      case "adelante":
        print("No es posible")
        respuesta = preguntarAlUsuario()
      case "salir":
        print("\n¡HASTA LUEGO!\n")
        break
      case _:
        if len(respuesta) >= 1:
          mi_stack.append(respuesta)
          showWebSiteUser(len(mi_stack)-1)
        # Pase lo que pase
        respuesta = preguntarAlUsuario()

# Ejecución programa 1
navegacionWeb()

"""
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.
"""

# EJERCICIO 2
# Usaremos FIFO
print("\nEJERCICIO 2\n")

# Nuestra pila
pool = []

# Pregunta inicial
def preguntarAlUsuarioPool():
  return input("Escribe si deseas imprimir (imprimir) o agrega a la cola de impresión: ")

# Programa inicial
def poolPrinter():
  respuestaUsuario = preguntarAlUsuarioPool()
  while True:
    match respuestaUsuario:
      case "imprimir":
        # Comprobamos
        if len(pool) == 0:
          print("No hay documentos en la cola de impresión, agregue uno antes")
          respuestaUsuario = preguntarAlUsuarioPool()
        else:
          print(f"Imprimimos el documento {pool[0]}")
          pool.pop(0)
          respuestaUsuario = preguntarAlUsuarioPool()
      case "salir":
        print("\n¡HASTA LUEGO!\n")
        break
      case _:
        if len(respuestaUsuario) >= 1:
          pool.append(respuestaUsuario)
          print(f"Agregamos el documento {respuestaUsuario} a la cola de impresión")
        else:
          print("Escriba el nombre de un documento o si desea imprimir")
        # Pase lo que pase
        respuestaUsuario = preguntarAlUsuarioPool()

# Ejecución programa 2
poolPrinter()