from collections import deque
"""
todo stack pila 
* segun interner, hay varias formas de implementar las pilas en python
* una seria con una lista o usando una clase (deque) del modulo (collections)
"""
#* implementacion de una pila usando una lista
class Stack:
  #? este seria el costructor de la clase
  def __init__(self):
    self.stack=[]
  #? motodos
  #* metodo para saber si la pila esta vacia o no
  def is_empty(self):
    return self.stack == []
  
  #* agregar elemento a la pila
  def push(self,element):
    self.stack.append(element)

  #* eliminar el ultimo elemento de la pila y retornar el valor eliminado  
  def pop(self):
    return self.stack.pop()
  
  #* mostrar el ultimo elemento de la pila sin eliminarlo
  def peek(self):
    return self.stack[-1]
  
  #* retornar el tamaño de la pila 
  def size(self):
    return len(self.stack)
  
  def print(self):
    print(self.stack)

def ejecutandoStack():
  pila =  Stack()
  print(f"la pila esta vacia: {pila.is_empty()}")
  print("agegando elementos a la pila: ")
  pila.push(1)
  pila.push(2)
  pila.push(3)
  print(f"size de la pila: {pila.size()}")
  print("mostrando pila: ")
  pila.print()
  print(f"eliminando elemento de la pila: {pila.pop()}")
  pila.print()
  print(f"mostrando ultimo elemento de la pila: { pila.peek()}")

# ejecutandoStack()

"""
! usando deque
* una alternativa es usar deque del módulo collections, que es más eficiente para operaciones de insercion y
* eliminación de ambos extremos de la estructura
"""
def usandoDeque():
  d_stack=deque() #*creando pila
  print("agregando elementos a la cola")
  d_stack.append(1)
  d_stack.append(2)
  d_stack.append(3)
  print("mostrando pila")
  print(d_stack)

  print(f"eliminando ultimo elemento de la pila: {d_stack.pop()}")
  print(d_stack)

# usandoDeque()

# todo cola 

class Queque:
  #? constructor
  #* propiedades, creando una cola vacia
  def __init__(self):
    self.queque=[]

  #* retorna si la cola está vacia o no
  def is_empty(self):
    return self.queque == []
  
  #* añade un elemento al final de la cola
  def enqueque(self,element):
    self.queque.append(element)
  
  #* eliminando el primer elemento de la cola y retornando el valor, si está vacia levanta una excepcion
  def dequeque(self):
    if self.is_empty():
      raise Exception("la cola esta vacia")
    return self.queque.pop(0)
  
  #* retorna el tamaño de la cola
  def size(self):
    return len(self.queque)
  
  #* mostrar cola
  def print(self):
    print(self.queque)
  
  #* mostrar el primer elemento de la cola si eliminarlo
  def front(self):
    return self.queque[0]

def ejecutarQueque():
  cola= Queque()
  print(f"la cola esta vacia?: {cola.is_empty()}")
  print("agregando elementos a la cola: ")
  cola.enqueque(1)
  cola.enqueque(2)
  cola.enqueque(3)
  print(f"size de la cola: {cola.size()}")
  print("mostrando cola: ")
  cola.print()
  print(f"eliminando primer elemento de la cola: {cola.dequeque()}")
  cola.print()

# ejecutarQueque()

#todo ejercicios extra

#? historial web

def historial_web():
  historial_Atras= Stack()
  historial_siguiente= Stack()
  pagina_Actual="inicio"
  print("\n---------------------------------------------------------------------------------")
  print("\n\thistorial web\n")
  print("vienvenido al historial web, hay algunas opciones que puedes ingresar")
  print("para ingresar un sitio web, ingresa: el nombre del sitio")
  print("para volver a una pagina anterior( si es que la hay ), ingresa: b")
  print("para ir a una pagaina siguiente( si es que hay ), ingresa: n")
  print("para salir del programa ingresa: s")
  print("-------------------------------------------------------------------------------\n")
  while True:
    print(f"\npagina actual: {pagina_Actual}")
    option= input("ingresa la opcion: ")
    copia = option.lower()
    if copia == "b" or copia =="n" or copia =="s":
      if copia =="b":
        if not historial_Atras.is_empty():
          historial_siguiente.push(pagina_Actual)
          pagina_Actual= historial_Atras.pop()
        else:
          print("\n no hay mas registros")
      if copia =="n":
        if not historial_siguiente.is_empty():
          historial_Atras.push(pagina_Actual)
          pagina_Actual= historial_siguiente.pop()
        else:
          print("\n no hay mas registros")
      if copia == "s":
        print("\n saliendo del historial........")
        break
    else:
      historial_Atras.push(pagina_Actual)
      pagina_Actual= option

# historial_web()

#? impresora compartida
def impresora():
  cola=Queque()
  print("\n---------------------------------------------")
  print("\timpresora compartida\n")
  print("vienvenido a la impresora compartida, hay algunas opciones que puedes hacer")
  print("para ingresar un documento(nombre) ingresa: el nombre")
  print("para imprimir el documento que este en cola ingresa: i")
  print("para salir de la impresora, ingresa: s")
  print("---------------------------------------------------\n")
  while True:
    if not cola.is_empty():
      print(f"\ndocumentos en cola: {cola.size()}, documento: {cola.front()}")
      option= input("ingrese la opcion: ")
      copia= option.lower()
      if copia == "i" or copia =="s":
        if copia =="i":
          print(f"\nimprimiendo el documento: {cola.dequeque()}")
        if copia == "s":
          print("\n saliendo de la impresora....\n")
          break
      else:
        cola.enqueque(option)
    else:
      print("impresora sin documentos")
      option= input("ingrese un documento: ")
      if option == "s":
        print("saliendo........")
        break;
      cola.enqueque(option)

impresora()