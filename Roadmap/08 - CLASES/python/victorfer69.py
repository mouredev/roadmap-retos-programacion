#Clases

class Programmer:

    surname = None
    
    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languajes = languages

    def print(self):
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes {self.languajes}")

my_programmer = Programmer("Victor", 21, ["Python", "Java", "Swift"])
my_programmer.print()
my_programmer.surname = "Fer"
my_programmer.print()
my_programmer.age = 22
my_programmer.print()


#EJERCICIO EXTRA

#Pila
class Stack():

    def __init__(self):
        self.stack = []

    def agregarItem(self, item):
        self.stack.append(item)

    def sacarItem(self):
        if self.numElem() == 0:
            return None
        self.stack.pop()

    def numElem(self):
        return len(self.stack)

    def print(self):
        if self.numElem() == 0:
            print("Pila vacia")
        else:    
            for i in reversed(self.stack):
                print(i)


my_stack = Stack()
my_stack.agregarItem("A")
my_stack.agregarItem("B")
my_stack.agregarItem("C")
my_stack.agregarItem("D")
print(my_stack.numElem())
my_stack.print()
my_stack.sacarItem()
my_stack.sacarItem()
my_stack.sacarItem()
my_stack.sacarItem()
my_stack.sacarItem()
my_stack.sacarItem()
print(my_stack.numElem())
my_stack.print()

#Cola

class Queue():

    def __init__(self):
        self.queue = []

    def agregarItem(self, item):
        self.queue.append(item)

    def sacarItem(self):
        if self.numElem() == 0:
            return None
        self.queue.pop()

    def numElem(self):
        return len(self.queue)

    def print(self):
        if self.numElem() == 0:
            print("Cola vacia")
        else:    
            for i in self.queue:
                print(i)


my_queue = Queue()
my_queue.agregarItem("A")
my_queue.agregarItem("B")
my_queue.agregarItem("C")
my_queue.agregarItem("D")
print(my_queue.numElem())
my_queue.print()
my_queue.sacarItem()
my_queue.sacarItem()
my_queue.sacarItem()
my_queue.sacarItem()
my_queue.sacarItem()
my_queue.sacarItem()
print(my_queue.numElem())
my_queue.print()