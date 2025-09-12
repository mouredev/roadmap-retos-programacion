# Clases
# Las clases deben estar escritas en CamelCase, ej: ClaseProgramador, HuesosDelCuerpo.

class Programmer:

  surname: str = None # Se pueden crear variables utilizables a futuro.
  def __init__(self, name, age, languages):
    self.name = name
    self.age = age
    self.languages = languages
  

  def print(self):
    print(f'Nombre {self.name}, Apellido: {self.surname}, edad: {self.age}, lenguajes: {self.languages}')

name = 'Cesar'
age = 21
languages = ['Spanish', 'English', 'Portugese']

my_programmer = Programmer(name, age, languages) # Instancio la clase.
my_programmer.print() # La muestro dandole print a la variable my_programmer, instancia de la clase Programmer.
my_programmer.surname = 'Moran' # Accedo a la clase 'Programmer' ya instanciada, y luego a la variable 'surname' dentro de ella, le asigno un valor después.
my_programmer.print()
my_programmer.age = 22 # Actualizamos el valor de la misma forma que accedimos a surname.
my_programmer.print()

'''
Ejercicio
'''

# LIFO

class Stack:
  def __init__(self):
    self.stack: list = []
  
  def push(self, item):
    return self.stack.append(item)
  
  def pop(self):
    if self.count() == 0:
      return print('No hay suficientes elementos para imprimir.')
    else:
      return self.stack.pop()
  
  def count(self):
    return len(self.stack)
  
  def print(self):
    for item in reversed(self.stack):
      print(f'Imprimiendo {item}')

my_stack = Stack()
my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()


# FIFO

class Cola:
  def __init__(self):
    self.queue: list = []

  def push(self, item):
    return self.queue.append(item)

  def pop(self):
    if len(self.queue) > 0:
      self.queue.pop(0)
    else:
      return print('No hay mas elementos para imprimir.')

  def print(self):
    print(f'Imprimiendo {self.queue[0]}')
    self.pop()

  def count(self):
    for item in self.queue:
      print(f'Tienes {item} elementos para imprimir.')

my_cola = Cola()
my_cola.push('1')
my_cola.push('2')
my_cola.push('3')
print(my_cola.queue)
my_cola.print()
print(my_cola.queue)
my_cola.pop()
print(my_cola.queue)
my_cola.pop()
my_cola.pop()