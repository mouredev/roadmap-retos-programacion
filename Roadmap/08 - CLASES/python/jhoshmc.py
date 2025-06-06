class Mamifero:
  #? atributos
  def __init__(self,especie,nombre,edad):
    self._especie = especie
    self._nombre = nombre
    self._edad = edad
  def saludar(self):
    if self._especie == "humano":
      print(f"\nhola mi nombre es {self._nombre} y tengo {self._edad}, mucho gusto")
    else:
      print(f"\nmi nombre es {self._nombre} y saludo dando la pata")

class Pila:
  #?atributos
  def __init__(self):
    self.stack=[]
  #? metodos
  #*metodo para saber si la cola está vacia, true: vacio, false: tiene elementos
  def empy(self)->bool:
    return self.stack == []
  #*metodo para agregar un elemento al final de la pila
  def push(self,elemento):
    self.stack.append(elemento)
  #* metodo para retornar el ultimo elemento sin eliminarlo
  def back(self):
    if not self.empy():
      return self.stack[-1]
  #* metodo para eliminar el ultimo elemento de la pila y retornarlo
  def pop(self):
    if not self.empy():
      return self.stack.pop()
  #* metodo para mostrar el tamaño de la pila
  def size(self)->int:
    return len(self.stack)
  #* mostar pila
  def print(self):
    if not self.empy():
      
      print(self.stack)
    else:
      print("\nno hay elementos en la pila para mostrar")
    
class Cola:
  #? atributos
  def __init__(self):
    self.queque=[]
  #?metodos
  #* metodo para saber si la cola esta vacia, true:vacia, false: hay elementos
  def empty(self)->bool:
    return self.queque == []
  #* metodo para agregar un elemnto al final de la cola
  def push(self,elemento):
    self.queque.append(elemento)
  #* metodo para mostrar el primer elemento de la cola, sin eliminarlo
  def front(self):
    if not self.empty():
      return self.queque[0]
    else:
      print(f"\nno hay elementos en la cola")
  #* metodo para eliminar el primer elemento de la cola
  def pop(self):
    if not self.empty():
      return self.queque.pop(0)
    print(f"\nno hay elementos para mostrar")
  #* metodo para saber el tamaño de la cola
  def size(self):
    return len(self.queque)
  #* metodo para mostrar la cola
  def print(self)->None:
    if not self.empty():
      print(self.queque)
    else:
      print("\nno hay elementos que mostrar en la cola")

#todo funciones
def ejercicio():
  martin =  Mamifero(edad=20,especie="humano",nombre="martin")
  chester = Mamifero("canina","chester",3)
  laila = Mamifero("canina","laila",2)
  lita = Mamifero("felina","lita",1)
  martin.saludar()
  chester.saludar()
  laila.saludar()
  lita.saludar()
def extraPila():
  pila = Pila()
  print(f"la pila esta vacia?: {pila.empy()}")
  print("agregano elementos a la pila: ")
  pila.push(1)
  pila.push(2)
  pila.push(3)
  print(f"el tamaño de la pila es: {pila.size()}")
  print(f"mostrando el ultimo elemento: {pila.back()}")
  print("mostrando pila")
  pila.print()
  print(f"eliminado ultimo elemento de la pila: {pila.pop()}")
  pila.print()
  print(f"eliminado ultimo elemento de la pila: {pila.pop()}")
  pila.print()
  print(f"eliminado ultimo elemento de la pila: {pila.pop()}")
  pila.print()
def extraCola():
  cola = Cola()
  print(f"la cola esta vacia?: {cola.empty()}")
  print("agregando elementos a la cola")
  cola.push(1)
  cola.push(2)
  cola.push(3)
  print(f"tamaño de la cola: {cola.size()}")
  print(f"el primer elemto de la cola es: {cola.front()}")
  print("los elementos de la cola son : ")
  cola.print()
  print(f"eliminado el primer elemento de la cola: {cola.pop()}")
  cola.print()
  print(f"eliminado el primer elemento de la cola: {cola.pop()}")
  cola.print()
  print(f"eliminado el primer elemento de la cola: {cola.pop()}")
  cola.print()

#todo ejecutando 
ejercicio()
extraPila()
extraCola()
  