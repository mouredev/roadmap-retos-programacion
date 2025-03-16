# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝

# ----------------------------------------
# Concepto de clases:
# ----------------------------------------
# Las clases proporcionan una forma de organizar y estructurar
# el código de manera más modular y reutilizable.
#_________________________________________
class Employee:
    # Atributos de clase (compartidos por todas las instancias)
    base_salary = 25000
    vacation_days = 15

    # Constructor con argumentos (instanciación)
    def __init__(self, name, hire_date):
        self.name = name
        self.hire_date = hire_date

    # Métodos de instancia
    def edit(self, name, hire_date):
        self.name = name
        self.hire_date = hire_date

    def println(self):
        print(f"Name: {self.name} - Hire date: {self.hire_date}")

# Crear objeto
employee_instance = Employee("Ben", "2024-02-01")

# Acceder a los atributos
print(f"""
Name:          {employee_instance.name}
Hire date:     {employee_instance.hire_date}
Base salary:   {employee_instance.base_salary}
Vacation days: {employee_instance.vacation_days}
""")

# Utilizar metodos.
employee_instance.edit("Ben edit", "2024-03-01")
employee_instance.println()

# ----------------------------------------
# Ejercicio:
# ----------------------------------------
"""
* Implementa dos clases que representen las estructuras de Pila y Cola 
* (estudiadas en el ejercicio número 7 de la ruta de estudio)
* Deben poder inicializarse y disponer de operaciones para añadir, 
* eliminar, retornar el número de elementos e imprimir todo su contenido.
"""
#_________________________________________
# Pilas(stack - LIFO):
class Stack:
    def __init__(self):
        self.elements = []
    
    def __len__(self): # total elementos.
        return len(self.elements)

    def is_empty(self): # es vacia.
        return len(self) == 0
    
    def push(self, item): # Agregar elemento.
        self.elements.append(item)
    
    def push_batch(self, items): # Agregar multiples.
        # use <history.push_batch(["1", "2", "3"])">
        self.elements.extend(items)
    
    def pop_get(self): # Eliminar y obtener.
        if not self.is_empty():
            return self.elements.pop()
        else: 
            return None
    
    def get_top(self): # Obtener sin eliminar.
        if not self.is_empty():
            return self.elements[-1]
        else: 
            return None
    
    def get_tuple(self): # retornar pila como tupla.
        return tuple(reversed(self.elements))
    
    def clear(self): # vaciar pila.
        self.elements.clear()

#_________________________________________
# Colas (Queue - FIFO):
from collections import deque
class Queue:
    def __init__(self):
        self.elements = deque()

    def __len__(self): # total elementos.
        return len(self.elements)

    def is_empty(self): # es vacia.
        return len(self) == 0
    
    def enqueue(self, item): # agregar
        self.elements.append(item)

    def enqueue_all(self, items): # Agregar multiples.
        self.elements.extend(items)

    def dequeue(self): # Eliminar y devolver
        if not self.is_empty():
            return self.elements.popleft()
        else:
            return None
    
    def peek(self): # Obtener sin eliminar.
        if not self.is_empty():
            return self.elements[-1]
        else: 
            return None
    
    def get_tuple(self): # retornar cola como tupla.
        return tuple(self.elements)

    def clear(self): # vaciar cola.
        self.elements.clear()

#_________________________________________
print("Uso de pila:")
mystack = Stack()
mystack.push("Zoe")
mystack.push_batch(["Ben", "Dan"])
if not mystack.is_empty():
    print(mystack.pop_get())
print(f"número de elementos: {len(mystack)}")
for name in mystack.get_tuple():
    print(name)

#_________________________________________
print("Uso de Cola:")
myqueue = Queue()
myqueue.enqueue("Zoe")
myqueue.enqueue_all(["Ben", "Dan"])
if not myqueue.is_empty():
    print(myqueue.dequeue())
print(f"número de elementos: {len(myqueue)}")
for name in myqueue.get_tuple():
    print(name)
