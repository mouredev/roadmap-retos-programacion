"""
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Person:

    def __init__(self, first_name = "unknown", last_name = "unknown", age = "unknown", nationality = "unknown"):
        self.fisrt_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality


    def set_first_name(self,f_n):
        self.fisrt_name = f_n

    def set_last_name(self,l_n):
        self.last_name = l_n

    def set_age(self,a):
        self.age = a

    def set_nationality(self,nty):
        self.nationality = nty

    def print_person(self):
        print(f"Fisrt name: {self.fisrt_name}\nLast name: {self.last_name}\nAge: {self.age}\nNationality:{self.nationality}")



person = Person("Pedro", "Rodriguez", "45")
person.print_person()
person.set_last_name("Rodríguez")
person.print_person()
person.set_nationality("Spain")
person.print_person()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""
from typing import Any, Optional

class Stack:

    total_stacks = 0 # Atributo de clase compartido por todas las instancias. No pedido(para probar)

    def __init__(self):
        self.my_stack = []
        Stack.increment_count()

    @classmethod    # Decorados que indica que el siguiente metodo es de clase
    def increment_count(cls)-> None: # cls es igual que self pero para metodos de clase
        cls.total_stacks += 1

    @classmethod
    def decrement_count(cls)-> None:
        if cls.total_stacks > 0:
            cls.total_stacks -= 1

    def delete(self)-> None:
        Stack.decrement_count()
        del self

    def push(self,element: Any) -> None:
        self.my_stack.append(element)

    def pull(self)->Optional[Any]:
        if self.my_stack:
            return self.my_stack.pop()
        print("La pila esta vacía")
        return None

    def get_len(self)-> int:
        return len(self.my_stack)
    
    def print_content(self)-> None:
        print(self.my_stack)


saludos = Stack()
print(saludos.pull())
saludos.push("Hola")
saludos.push("Buenos días")
saludos.print_content()
print(saludos.get_len())
print(saludos.pull())
saludos.print_content()
despedidas = Stack()
despedidas.push("Adios")
despedidas.print_content()
print(despedidas.total_stacks)  # Imprime el valor del atributo de clase aunque lo llame desde la instacia
print(Stack.total_stacks)       # Esto es asi porque loas atributos y metodos de clase son heredados por las instancias. 
despedidas.delete()
print(Stack.total_stacks)




class Queue:

    def __init__(self):
        self.my_queue = []

    def push(self,element: Any) -> None:
        self.my_queue.append(element)

    def pull(self)->Optional[Any]:
        if self.my_queue:
            return self.my_queue.pop(0)
        print("La cola esta vacía")
        return None

    def get_len(self)-> int:
        return len(self.my_queue)
    
    def print_content(self)-> None:
        print(self.my_queue)


persons = Queue()
persons.push("Antonio")
persons.print_content()
persons.push("Marcos")
persons.print_content()
persons.push("Roberto")
persons.print_content()
print(persons.pull())
persons.print_content()
print(persons.pull())
persons.print_content()
persons.push("Javier")
persons.print_content()
print(persons.pull())
persons.print_content()
print(persons.pull())
persons.print_content()
print(persons.pull())
persons.print_content()