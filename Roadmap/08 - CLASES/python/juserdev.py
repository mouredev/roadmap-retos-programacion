""" /*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */ """

class Person:
  def __init__(self, name, surname, age, alias="sin alias"):
    self.name = name
    self.surname = surname
    self.age = age
    self.__alias = alias

  def get_name(self):
    return (f"Mi nombre es: {self.name}, mi apellido es: {self.surname}, tengo {self.age} años y mi alias es: {self.__alias}")
  
  def get_alias(self): 
    return (f"Mi alias es: {self.__alias}")
  
  def set_alias(self, new_alias):
    self.__alias = new_alias

person_one = Person("juan", "rodriguez",35, "juserdev")

print(person_one.get_name())
print(person_one.get_alias()) # para poder acceder al alias debo crear una funcion para poder acceder al alias tuve que crear una funcion get_alias
person_one.set_alias("JuserDev")
print(person_one.get_name())
print(person_one.get_alias())


### DIFICULTAD EXTRA ###

'''
  ->  declaro una clase Stack
  ->  creo una funcion add para agregar contendio a stack
  ->  creo una funcion count para contar los elementos dentro de stack
  ->  creo una funcion delete con un condicional donde dice que si stack es igual a o retorna una resputa informando que el stack esta vacio
      de lo contrario elimina el ultimo elemento y muestra el elemento eliminado
  ->  cfeo una fucion printElement que recorre la lista e imprime el contenido

  ->  en Queue la diferencia es que el primer elemento en ingresar es el primer elemento en salir
'''

class Stack:
  def __init__(self): # de esta manera lo inicializamos vacio
    self.stack = []
  
  def add(self, item: int):
    self.stack.append(item)
    return f"Item agregado correctamente --> {item}"

  def count(self):
    return len(self.stack)

  def delete(self):
    if self.count() == 0:
      return "No hay elemento que eliminar"
    else:
      item = self.stack.pop()
      return f"Elemento elminado correctamente --> {item}"
  
  def printElements(self):
    for item in self.stack:
      print(item)
    
number = Stack()

print(number.add(1))
print(number.add(2))
print(number.add(3))
print(number.add(4))

number.printElements() # aqui imprime todos los elementos uno despues de otro
print(number.stack) # aqui imprime todos los elemento en una lista
print(number.count()) # aqui cuenta todos los elementos
print(number.delete())
print(number.count()) # aqui elimina el ultimo elemento agregado

# QUEUE

class Queue:
  def __init__(self): # de esta manera lo inicializamos vacio
    self.queue = []
  
  def add(self, item: int):
    self.queue.append(item)
    return f"Item agregado correctamente --> {item}"

  def count(self):
    return len(self.queue)

  def delete(self):
    if self.count() == 0:
      return "No hay elemento que eliminar"
    else:
      item = self.queue.pop(0)
      return f"Elemento elminado correctamente --> {item}"
  
  def printElements(self):
    for item in self.queue:
      print(item)

queue = Queue()

print(queue.add(1))
print(queue.add(2))
print(queue.add(3))
print(queue.add(4))

queue.printElements()
print(queue.count())
print(queue.delete())
queue.printElements()
print(queue.count())