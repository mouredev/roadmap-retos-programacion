# /*
#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  */

#clases en python, se crean con la palabra reservada class

class Persona:
    
    def __init__(self,nombre,edad,profesion): # creamos un constructor con la palabra init y asignamos a el todos los atributos de la clase
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def greetings(self): # creamos una funcion la cual sera un metodo, un metodo es una funcion que realiza diferentes funcionalidades, en este caso la funcion greetins envia un saludo
        print(f'{self.nombre} te saluda! ')

    def presentation(self):
        print(f'Hola, soy {self.nombre}. Tengo {self.edad} y soy un {self.profesion} :) ')
persona_1 = Persona('Raul',25,'informatico') # para crear una instancia de la clase creamos una variable y le asignamos el nombre de la clase junto con los atributos que queremos asignarle

persona_1.greetings() # para utilizar el metodo utilizamos la variable que hemos creado junto con su metodo
persona_1.presentation()

persona_1.profesion = 'Programador' #podemos acceder a un metodo para cambiarlo si asi lo deseamos
persona_1.presentation()

#extra

#pila o stack

class Stack:

    # stack_elements = []
    def __init__(self):
        self.elements = []
    
    def add_element(self,element):
        self.elements.append(element)
        print(f'{element} ha sido agregado con exito al stack')
    
    def delete_element(self):
        if self.count_elements() == 0:
            print(0)
        else:
            print(f"{self.elements.pop()} ha sido eliminado del stack")
    
    def show_elements(self):
        print(f"Los elementos presentes en el stack son {self.elements}")

    def count_elements(self):
        print(f"hay {len(self.elements)} elementos en el stack ")

my_stack = Stack()
my_stack.count_elements()
my_stack.add_element('raul')
my_stack.add_element("yander")
my_stack.show_elements()
my_stack.count_elements()
my_stack.delete_element()
my_stack.count_elements()

class Queue:

    def __init__(self):
        self.elements = []

    def add_element(self,element):
        self.elements.append(element)
        print(f'{element} ha sido agregado con exito al queue')
    
    def delete_element(self):
        if self.count_elements() == 0:
            print(0)
        else:
            print(f"{self.elements.pop(0)} ha sido eliminado del queue")
    
    def show_elements(self):
        print(f"Los elementos presentes en el queue son {self.elements}")

    def count_elements(self):
        print(f"hay {len(self.elements)} elementos en el queue ")

my_queue = Queue()
my_queue.count_elements()
my_queue.add_element('raul')
my_queue.add_element("yander")
my_queue.show_elements()
my_queue.count_elements()
my_queue.delete_element()
my_queue.count_elements()