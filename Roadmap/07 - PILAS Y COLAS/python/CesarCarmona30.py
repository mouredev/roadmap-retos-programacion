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

  def showData(self):
    print(f'Queue: {self.data}')

veggies = Stack()
veggies.push('Cucumber')
veggies.push('Radish')
veggies.push('Tomato')
veggies.push('Orange')
veggies.push('Apple')
veggies.showData()
veggies.pop()
veggies.pop()
veggies.showData()

fruits = Queue()
fruits.enqueue('Banana')
fruits.enqueue('Melon')
fruits.enqueue('Strawberry')
fruits.enqueue('Onion')
fruits.enqueue('Garlic')
fruits.showData()
fruits.dequeue()
fruits.dequeue()
fruits.showData()