"""
EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Person():
    def __init__(self,name, lastname):
        self.__fullname = f"Tu nombre es {name} y tu apellido es {lastname}"
    
    def show(self):
        print(self.__fullname)

my_person = Person("Alex","Valderrama")
my_person.show()
my_person = Person("Brais","Moure")
my_person.show()
"""
DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""
class Stack:
    def __init__(self):
        self.__stack = list()

    def push(self,item): #apilar
        temp = list()
        if len((self.__stack)) == 0:
            self.__stack.append(item)
        else:
            temp= self.__stack.copy()
            self.__stack.clear()
            self.__stack.append(item)
            self.__stack.extend(temp)
        return self.__stack
    
    def pop(self): #desapilar
        if self.empty():
            print("La pila está vacía, no se puede desapilar nada")
        else:
            self.__stack = self.__stack[1:]
        return self.__stack
    
    def top(self): #devuelve el primer elemento de la pila
        return self.__stack[0]
    
    def size(self): #devuelve la longitud de la pila
        return len(self.__stack)

    def show(self): #muestra la pila
        print(self.__stack)

    def empty(self): #devuelve un boolean según la pila esté vacía o no
        if self.size() == 0:
            return True
        else:
            return False
        
my_stack = Stack()
print(my_stack.empty())
my_stack.pop()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.show()
my_stack.pop()
my_stack.show()
print(my_stack.top())
my_stack.size()
    
class Queue():
    def __init__(self):
        self.__queue = list()

    def enqueue (self,item): #encolar
        return self.__queue.append(item)

    def dequeue(self): #desencolar
        try:
            self.__queue = self.__queue[1:]
        except IndexError:
            print("La cola está vacía, no se puede desencolar nada")
        finally:
            return self.__queue
        
    def front(self): #devuelve el primer item que entró en la cola
        return self.__queue[0]
    
    def size(self): #según he investigado, la estructura "cola" no debería tener un método que muestre su longitud
        return len(self.__queue) #aún así queda implementado en estas líneas
    
    def show(self): #imprime la cola
        if self.size() == 0:
            print("La cola está vacía")
        else:
            print(self.__queue)
    
my_queue = Queue()
my_queue.show()
my_queue.enqueue("Mi nombre")
my_queue.enqueue("es Alex")
my_queue.enqueue("Valderrama")
my_queue.show()
print(my_queue.front())
my_queue.dequeue()
my_queue.show()
print(my_queue.size())
