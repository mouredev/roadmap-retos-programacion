import os
#os.system('clear') #MAC/LINUX
os.system('cls') #WINDOWS
""" * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
"""


class MyClass: #Declaración de clase
    def __init__(self) -> None: #Definición del constructor de clase o método de instancia
        self.my_num_list = [] #Objeto con el que trabajaremos en la clase
        
    def my_iterator(self,init_num, end_num):#Función de clase que en este caso llenará de valores
     for i in range(init_num,end_num):# numéricos la lista que creamos como objeto recibiendo los
          self.my_num_list.append(i)# parámetros que indiquen el rango de numeración a incluir
     self.show_list(self.my_num_list)#Dentro de esta función llamaremos a la otra función que se
                                     # encarga de imprimir la lista
    def show_list(self, my_num_list):# Función de clase que imprime la lista
       print(self.my_num_list)

result = MyClass()#Instanciamos la clase en una variable
result.my_iterator(1,11)#a partir de esa instancia ya podemos 
                       # llamar a las funciones y pasarle sus parámetros si son necesarios
print("\n\n")


       



""" * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""

class Stack(): #Clase pila (LIFO)
    def __init__(self) -> None:
      self.my_stack_list = []

    def add (self, init_number, end_number):
      for num in range (init_number, end_number):
       self.my_stack_list.append(num)

    def unstack (self):#Método de clase que elimina el último elemento añadido
      self.my_stack_list.pop()
    
    def leght (self):
       return len(self.my_stack_list)
    
    def show (self):
       print(self.my_stack_list)


class Queue():  #Clase cola (FIFO)
    def __init__(self) -> None:
      self.my_stack_list = []

    def add (self, init_number, end_number):
     for num in range (init_number, end_number):
       self.my_stack_list.append(num)

    def dequeue (self):#Método de clase que elimina el primer elemento añadido
      self.my_stack_list.pop(0)
    
    def leght (self):
       return len(self.my_stack_list)
    
    def show (self):
       print(self.my_stack_list)

stack_instance = Stack()#Instacia de clase
queue_instance = Queue()#Instacia de clase

stack_instance.add(1,11)
stack_instance.show()
print(f"La lista tiene {stack_instance.leght()} números\n")
stack_instance.unstack()
stack_instance.show()
print(f"La lista tiene {stack_instance.leght()} números\n")

queue_instance.add(1,11)
queue_instance.show()
print(f"La lista tiene {queue_instance.leght()} números\n")
queue_instance.dequeue()
queue_instance.show()
print(f"La lista tiene {queue_instance.leght()} números\n")

"""
En este caso concreto hemos hecho una clase para cada uno de los requerimientos de pila y cola
tal y como pide el enunciado del ejercicio pero en un caso real lo ideal sería hacer una sola 
clase para ambos casos dada la semejanza que existe entre ambos casos, en la misma clase incluiríamos
un método para eliminar el primer elemento de la lista y otro para eliminar el último ya que el resto
de métodos son idénticos para ambos propósitos como vemos en la clase creada mas abajo 
"""

class ListModificator:
    def __init__(self):
        self.my_num_list = []
 
    def add (self, init_number, end_number):
     for num in range (init_number, end_number):
       self.my_stack_list.append(num)

    def pop_first(self):#Elimina el primer elemento para un ejeplo de cola (FIFO)
        return self.my_num_list.pop(0)
 
    def pop_last(self):#Elimina el último elemento para un ejeplo de pila (LIFO)
        return self.my_num_list.pop()

    def leght(self):
        return len(self.my_num_list)
   
   