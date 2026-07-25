# Clases

class Programador:

    apellido = None

    def __init__(self, nombre: str, edad: int, lenguajes: list) -> None:
        self.nombre = nombre
        self.edad = edad
        self.lenguajes = lenguajes        
        
    def print(self):
        print(f"Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad} | Lenguajes: {self.lenguajes}")


mi_programador = Programador("Nicolás", 22, ["Python", "Javascript", "Typescript"])
mi_programador.print()

mi_programador.apellido = "Heguaburu"
mi_programador.print()



#Dificultad extra

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def count(self):
        return(len(self.stack))                          
    
    def pop(self):
        if self.count() == 0:
            return None
        else:
            self.stack.pop()
        

        
    def printer(self):
        for i in self.stack:
            print(i)



my_stack = Stack()

my_stack.push("nico")
my_stack.push("fede")
my_stack.push("uli")
my_stack.push("marcos")

print(my_stack.count())

my_stack.pop()


print(my_stack.count())
 
my_stack.printer()


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def count(self):
        return(len(self.queue))
    
    def pop(self):
        if self.count() > 0:
            self.queue.pop(0)
        else:
            print("No hay mas valores en la lista para eliminar")
    
    def printer(self):
        for i in self.queue:
            print(i)



my_queue = Queue()

my_queue.push("danet")
my_queue.push("serenito")
my_queue.push("conamigos")
my_queue.push("danonino")

my_queue.printer()
my_queue.pop()
my_queue.printer()

print(my_queue.count())



