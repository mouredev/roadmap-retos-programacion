""""
Clases
"""

class Student:
    surname : str = None
    def __init__(self, name:str, age:int, notes:list) :
         self.name = name
         self.age = age
         self.notes = notes
    
    def print(self):
      print(
          f"name:{self.name},surname:{self.surname} ,age:{self.age}, notes:{self.notes}"
      )   

my_student = Student("Yenner Alayon", 21 ,[12,54,67,87])
my_student.print()
my_student.surname = "Benavides"
my_student.print()
my_student.age = 22
my_student.print()


#LIFO

class Pila:

    def __init__(self):
        self.pila = []
    
    def push(self,item):
        self.pila.append(item)
    
    def pop(self):
        if self.count() == 0:
            return None
        return self.pila.pop()

    def count(self):
        return len(self.pila)

    def print(self):
        for i in reversed(self.pila):
            print(i)

my_pila = Pila()
my_pila.push("A")
my_pila.push("B")
my_pila.push("C")
print(my_pila.count())
my_pila.print()
print(my_pila.pop())
my_pila.print()
print(my_pila.pop())
print(my_pila.pop())
print(my_pila.pop())
print(my_pila.count())


#FIFO

class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)        
    
    def print(self):
        for i in self.queue:
            print(i)

my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
my_queue.print()