'''
  EJERCICIO
'''

class Animal:
  def __init__(self, name, race):
    self.name = name
    self.race = race

  def __str__(self):
    return f'Nombre: {self.name}, Raza: {self.race}'  

class Dog(Animal):
  def __init__(self, name, race):
    super().__init__(name, race)

  def sound(self):
    print(f"{self.name} ladrando!!")

class Cat(Animal):
  def __init__(self, name, race):
    super().__init__(name, race)

  def sound(self):
    print(f"{self.name} maullando!!")

def animalSound(animal):
  animal.sound()


manchas = Cat("Manchas", "Calicó")
firulais = Dog("Firulais", "Labrador")

animalSound(manchas)
animalSound(firulais)

print(f'Manchas: {manchas.__str__()}')
print(f'Manchas es un perro?: {isinstance(manchas, Dog)}')
print(f'Manchas es un gato?: {isinstance(manchas, Cat)}')
print(f'Manchas es un animal?: {isinstance(manchas, Animal)}')
print(f'Firulais: {firulais.__str__()}')
print(f'Firulais es un perro?: {isinstance(firulais, Dog)}')
print(f'Firulais es un gato?: {isinstance(firulais, Cat)}')
print(f'Firulais es un animal?: {isinstance(firulais, Animal)}')

'''
  EXTRA
'''

class Stack:

  def __init__(self):
    self.data = []

  def push(self, element):
    self.data.append(element)

  def pop(self):
    try:
      element = self.data.pop()
    except IndexError as e:
      print(f'Error: {type(e).__name__}, empty stack')
      return
    print(f'Stack element out: {element}')

  def itemsNumber(self):
    return len(self.data)

  def showData(self):
    print(f'Stack: {self.data}')

class Queue:

  def __init__(self):
    self.data = []

  def enqueue(self, element):
    self.data.append(element)

  def dequeue(self):
    try:
      element = self.data.pop(0)
    except IndexError as e:
      print(f'Error: {type(e).__name__}, empty queue')
      return
    print(f'Queue element out: {element}')

  def itemsNumber(self):
    return len(self.data)  

  def showData(self):
    print(f'Queue: {self.data}')

veggies = Stack()
veggies.push('Cucumber')
veggies.push('Radish')
veggies.push('Tomato')
veggies.push('Orange')
veggies.push('Apple')
print(f'Cantidad de vegetales: {veggies.itemsNumber()}')
veggies.showData()
veggies.pop()
veggies.pop()
veggies.showData()
print(f'Cantidad de vegetales: {veggies.itemsNumber()}')

fruits = Queue()
fruits.enqueue('Banana')
fruits.enqueue('Melon')
fruits.enqueue('Strawberry')
fruits.enqueue('Onion')
fruits.enqueue('Garlic')
print(f'Cantidad de frutas: {fruits.itemsNumber()}')
fruits.showData()
fruits.dequeue()
fruits.dequeue()
fruits.showData()
print(f'Cantidad de frutas: {fruits.itemsNumber()}')