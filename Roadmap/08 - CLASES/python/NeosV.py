

class Programador:

    def __init__(self, nombre:str, edad:int, lenguaje:list):
        self.nombre = nombre
        self.edad = edad
        self.lenguaje = lenguaje

    def impri(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad} Lenguaje: {self.lenguaje}")





my_programador = Programador("Andres", 22 , ["css","Python"])
my_programador.impri()      
my_programador.edad = 24
my_programador.impri()


class Stack:
    def __init__(self):
        self.stack = []
        
    def anadir(self,item):

        self.stack.append(item)
        print("Accion completada")

    def eliminar(self):

        self.stack.pop() 

        print("Eliminacion completada")

    def cont(self):

        print(len(self.stack))

    def imprimir(self): 

        for item in reversed(self.stack):
            print(item)
       



my_stack = Stack()  
my_stack.anadir("a")   
my_stack.anadir("b")   
my_stack.anadir("c")      
my_stack.imprimir()
my_stack.cont()
my_stack.eliminar()
my_stack.imprimir()


class Queue:
    def __init__(self):
        self.queue = []
        
    def anadir(self,item):

        self.queue.append(item)
        print("Accion completada")

    def eliminar(self):

        self.queue.pop(0) 

        print("Eliminacion completada")

    def cont(self):

        print(len(self.queue))

    def imprimir(self): 

        for item in (self.queue):
            print(item)
       



my_queue = Queue()  
my_queue.anadir("a")   
my_queue.anadir("b")   
my_queue.anadir("c")      
my_queue.imprimir()
my_queue.cont()
my_queue.eliminar()
my_queue.imprimir()
