"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
"""
class Stack:
    def __init__(self):
        self.__stack = list()

    def push(self,item):
        if len(self.__stack) == 0:
            self.__stack.append(item)
        else:
            temp = list()
            temp = self.__stack.copy()
            self.__stack.clear()
            self.__stack.append(item)
            for element in temp:
                self.__stack.append(element)
        return self.__stack
    
    def pop(self):
        if len(self.__stack) == 1:
            self.__stack.clear()
        else:
            self.__stack = self.__stack[1:]
        return self.__stack
    
    def top(self):
        return self.__stack[0]
    
    def size(self):
        return len(self.__stack)
    
    def empty(self):
        return self.__stack.clear()

    def show(self) -> None:
        print(self.__stack)

class Queue():
    def __init__(self) -> None:
        self.__queue = list()
    
    def enqueue(self,item):
        return self.__queue.append(item)
    
    def dequeued(self):
        self.__queue = self.__queue[1:]
        return self.__queue
    
    def front(self):
        return self.__queue[0];
    
    def show(self):
        print(self.__queue)

my_stack = Stack()
my_stack.show()
my_stack.push(3)
my_stack.show()
my_stack.push(2)
my_stack.show()
my_stack.push(5)
my_stack.show()
my_stack.push(9)
my_stack.show()
my_variable = my_stack.top()
print(f"El valor accesible de la pila es el: {my_variable}")
my_stack.pop()
my_stack.show()
print(f"La longitud de la pila es: {my_stack.size()}")
my_stack.empty()
my_stack.show()

my_queue = Queue()
my_queue.show()
my_queue.enqueue("hola")
my_queue.enqueue("mi nombre")
my_queue.show()
my_queue.enqueue("es Alex")
my_queue.show()
my_queue.dequeued()
my_queue.show()
print(f"El primer valor de la cola es: \"{my_queue.front()}\"")

"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""
class Web_Navigator(Stack):
    def go(self,web):
        return self.push(web)
        
    def back(self):
        try:
            popped = (self.top())
        except IndexError:
            print("no hay sitios web almacenados")
        else:
            self.pop()
            return self,popped
        finally:
            time.sleep(1)
            print("\n")
    
    def forward(self,popped:list):
        if len(popped) == 1:
            self.push(popped[0])
        else:
            self.push(popped[-1])
        popped = popped.pop()

    def show(self):
        try:
            print(f"Ahora estas en la web: {self.top()}")
        except IndexError:
            print("No hay más web almacenadas hacia atrás")
        finally:
            time.sleep(1)
            print("\n")    

def go_to_website(navigator,pop_list):
    pop_list.clear()
    website = input("Perfecto. Dime por favor la web a la que quieres navegar: ")
    navigator.go(website)
    navigator.show()
    return navigator

def go_back(navigator,pop_list):
    if navigator.size() != 0:
        navigator,temp = navigator.back()
        pop_list.append(temp)
        navigator.show()


def go_forward(navigator,pop_list):
    if len(pop_list)!= 0:
        navigator.forward(pop_list)
        navigator.show()
    else:
        print("No hay más webs en adelante")
        time.sleep(1)
        print("\n")


my_web_navigator = Web_Navigator()
my_popped_list = list()
import time
print("\n")
def web_navigation():
    web_option = ""
    while web_option != "4":
        web_option = input("Elije una de las opciones:\n1. Navegar a un sitio web.\n2. Ir hacia adelante.\n3. Ir hacia atrás.\n4. Salir\n ---> ")
        match web_option:
            case "1":
                go_to_website(my_web_navigator,my_popped_list)
            case "2":
                go_forward(my_web_navigator,my_popped_list)
            case "3":
                go_back(my_web_navigator,my_popped_list)
            case "4":
                break
            case _:
                print("La opción introducida no es correcta")
                time.sleep(2)
                print("\n")
    print("Gracias por usar el sistema de navegación web")
    print("\n")
web_navigation()

"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""
class Printer(Queue):
    def send_doc(self,doc):
        self.enqueue(doc)
        print(f"El documento {doc} ha quedado encolado en la impresora")
        time.sleep(1)
        print("\n")
    
    def print_doc(self):
        try:
            doc = self.front()
        except IndexError:
            print("No hay más documentos en la cola de impresión")
        else:
            self.dequeued()
            print(f"El documento impreso es: {doc}")
        finally:
            time.sleep(1)
            print("\n")

    def pending_docs(self):
        print("Los documentos que faltan por imprimit son: ")
        self.show()
        time.sleep(1)
        print("\n")

def printer():
    my_printer = Printer()
    print_option = ""
    while print_option != 4:
        print_option = input ("Elije una de las cuatro opciones:\n1. Enviar documento a la impresora\n2. Imprimir documento\n3. Mostrar cola de impresión\n4. Salir\n----> ")
        match print_option:
            case "1":
                document = input("Dame el nombre del documento: ")
                my_printer.send_doc(document)
            case "2":
                my_printer.print_doc()
            case "3":
                my_printer.pending_docs()
            case "4":
                break
            case _:
                print("La opción elegida no es válida. Prueba de nuevo")
                time.sleep(1)
                print("\n")
    print("Gracias por usar este sistema de impresión")

printer()
