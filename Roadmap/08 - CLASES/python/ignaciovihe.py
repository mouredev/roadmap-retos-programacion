"""
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Npc:

    total_npc = 0 # Atributo de clase compartido por todas las instancias. (para probar)

    def __init__(self, first_name = "unknown", last_name = "unknown", age = "unknown", location = "unknown"):
        self.fisrt_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        Npc.increment_count()

    @classmethod    # Decorador que indica que el siguiente metodo es de clase
    def increment_count(cls): # cls es igual que self pero para metodos de clase
        cls.total_npc += 1

    @classmethod
    def decrement_count(cls):
        if cls.total_npc > 0:
            cls.total_npc -= 1

    def delete(self)-> None:
        Npc.decrement_count()
        del self

    def set_first_name(self,f_n):
        self.fisrt_name = f_n

    def set_last_name(self,l_n):
        self.last_name = l_n

    def set_age(self,a):
        self.age = a

    def set_location(self,lct):
        self.location = lct

    def print(self):
        print(f"Fisrt name: {self.fisrt_name}\nLast name: {self.last_name}\nAge: {self.age}\nLocation:{self.location}")



person = Npc("Pedro", "Rodriguez", 45)
person.print()
person.set_location((4,7))
person.print()

person2 = Npc("Mike", "Jones", 29,)
person2.set_location((3,0))
person2.print()

print(f"Total Npc : {Npc.total_npc}")
person.delete()
print(f"Total Npc : {Npc.total_npc}")



"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""
from typing import Any, Optional

class Stack:


    def __init__(self):
        self.stack = []

    def push(self,element: Any) -> None:
        self.stack.append(element)

    def pull(self)->Optional[Any]:
        if self.stack:
            return self.stack.pop()
        print("La pila esta vacía")
        return None

    def get_len(self)-> int:
        return len(self.stack)
    
    def print(self)-> None:
        for item in reversed(self.stack):
            print(item)


saludos = Stack()
saludos.push("Hola")
saludos.push("Buenos días")
saludos.print()
print(saludos.get_len())
saludos.pull()
saludos.print()
saludos.pull()
saludos.print()
saludos.pull()
saludos.print()




class Queue:

    def __init__(self):
        self.queue = []

    def push(self,element: Any) -> None:
        self.queue.append(element)

    def pull(self)->Optional[Any]:
        if self.queue:
            return self.queue.pop(0)
        print("La cola esta vacía")
        return None

    def get_len(self)-> int:
        return len(self.queue)
    
    def print(self)-> None:
        print(self.queue)


persons = Queue()
persons.push("Antonio")
persons.push("Marcos")
persons.push("Roberto")
persons.print()
persons.pull()
persons.print()
persons.pull()
persons.print()
persons.push("Javier")
persons.print()
persons.pull()
persons.print()
persons.pull()
persons.print()
persons.pull()
persons.print()