### Python Classes ###

class Worker:
  def __init__(self, name, age, job):
    self.name = name
    self.age = age
    self.job = job
    
  def print_attributes(self):
    print(self.name, self.age, self.job)
  
first_worker = Worker('jonh', 45, 'teacher')

first_worker.print_attributes()

#! Optional Challenge

#* Stack Class

class Stack:
  def __init__(self):
    self.stack = []
    
  def add(self, elem):
    self.stack.append(elem)
    
  def remove(self):
    self.stack.pop()
    
  def clear(self):
    self.stack.clear()
    
  def size(self):
    return len(self.stack)
    
  def is_empty(self):
    if len(self.stack) > 0:
      return 'Stack is not empty'
    else:
      return 'The stack is empty'
      
my_stack = Stack()

my_stack.add(4)
my_stack.add(10)
my_stack.add(50)
my_stack.add(15)

print(my_stack.stack)
print(my_stack.size())

my_stack.remove()
print(my_stack.stack)


#* Queue Class

class Queue:
  def __init__(self):
    self.queue = []
    
  def add(self, elem):
    self.queue.append(elem)
    
  def remove(self):
    self.queue.pop(0)
    
  def clear(self):
    self.queue.clear()
    
  def size(self):
    return len(self.queue)
    
  def is_empty(self):
    if len(self.stack) > 0:
      return 'Queue is not empty'
    else:
      return 'The queue is empty'
    
my_queue = Queue()

my_queue.add(10)
my_queue.add(45)
my_queue.add(8)
my_queue.add(12)
my_queue.add(5)

print(my_queue.queue)
print(my_queue.size())

my_queue.remove()
print(my_queue.queue)
