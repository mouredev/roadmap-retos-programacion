# Teoria

# Una clase en Python es como un molde que define 
# las características y comportamientos que tendrán 
# los objetos creados a partir de ella. 
# Es una forma de organizar y estructurar el código para crear y 
# manipular objetos de manera consistente.

#Un objeto en Python es una instancia de una clase. 
# Piensa en una clase como un molde y un objeto como una
# pieza creada a partir de ese molde. Un objeto tiene atributos (datos) 
# y métodos (funciones) que definen su comportamiento. 
# Por ejemplo, si tienes una clase llamada "Perro", un objeto de esa 
# clase podría tener atributos como "nombre" y "edad", y métodos como "ladrar" o "correr".

# El inicializador en una clase de Python es un método especial llamado __init__()
# que se ejecuta automáticamente al crear un nuevo objeto de esa clase.
# Sirve para inicializar los atributos del objeto con los valores que se le pasan como parámetros.

# Los parámetros en el inicializador son variables que se pasan al crear un objeto
# y se utilizan para asignar valores a los atributos del objeto.

# Los métodos en una clase son funciones que están definidas dentro de la clase
# y se utilizan para realizar operaciones con los objetos de esa clase.
# Pueden acceder a los atributos del objeto utilizando la palabra clave self.


# Ejercicio

# Definición de la clase Persona
class Persona:
    # Inicializador (__init__) con atributos nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método para imprimir los atributos de la persona
    def imprimir_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

# Creación de un objeto persona1
# persona1 = Persona("Juan", 30)
# Impresión de la información de persona1
# print("Información de persona1:")
# persona1.imprimir_info()
# Modificación de los atributos de persona1
# persona1.nombre = "María"
# persona1.edad = 25
# Impresión de la información actualizada de persona1
# print("\nInformación actualizada de persona1:")
# persona1.imprimir_info()


# Extra_1
import sys
import time
import random
from collections import  deque

class Navigate():
    web_history = []
    back_url = ''
    forward_url = ''
    
    def __init__(self, current_url):
        self.current_url = current_url
    
    def show_history(self):
        print(f'\n[i] Informacion. ')
        print(f'[i] {self.web_history}')
        print(f'[i] Url_Anterior: {self.back_url}')
        print(f'[i] Url_Actual: {self.current_url}')
        print(f'[i] Url_posterior: {self.forward_url}')
    
    def back(self):
        if not self.back_url:
            print(f'[i] No existe una URL anterior')
        else:
            self.forward_url = self.current_url
            self.current_url= self.back_url
            if len(self.web_history) > 0:
                self.back_url = self.web_history.pop()
            else:
                self.back_url = ""
    
    def forward(self):
        if not self.forward_url:
            print(f'[i] Se encuentra en el final')
        else:
            if self.back_url:
                self.web_history.append(self.back_url)
        
            self.back_url = self.current_url
            self.current_url = self.forward_url
            self.forward_url=''

    def navigate(self, new_url):
        if  new_url != '':
            if self.back_url:
                self.web_history.append(self.back_url)
            self.back_url = self.current_url
            self.current_url = new_url
            print(f'[+] Navegando a ---> {self.current_url}')  
        else:
            print(f'[+] Ingrese una url.')  

    def exit(self):
        return sys.exit(0)

def navegando():
    my_session = Navigate(current_url='google')
    while True:
        my_session.show_history()
        user_intput = input("\n[+] Ingrese 'adelante', 'atras' o la URL de una nueva página para navergar.\n[+] Use 'salir' para cerrar.\n")
        
        if user_intput.lower() == "adelante":
            my_session.forward()
        elif user_intput.lower() == "atras":
            my_session.back()
        elif user_intput.lower() == "exit":
            my_session.exit()
        else:
            my_session.navigate(user_intput)

# Extra_2

class Printer():
    print_queue = deque()

    def __init__(self, document):
        self.document = document
    
    def add_doc(self, new_doc):
        self.print_queue.append(self.document)
        self.document = new_doc
        print(f'\n[i] Añadido documento {new_doc} a la cola de impresión')
        print(f'[i] Archivos en cola: {len(self.print_queue)}\n\n') 
    
    def print_doc(self):
        try:
            print(f'[i] Imprimiendo {self.print_queue.popleft()}...')
        except IndexError:
            print('[i] No hay documentos en la cola para imprimir')


def printer():
    cont = 0
    printing = False
    my_printer = Printer(document='doc.txt')

    while True:
        if not printing:
            new_doc = f'{cont}.txt'
            my_printer.add_doc(new_doc)
            time.sleep(0.5)

            if len(my_printer.print_queue) > 3:
                printing = True
            else:
                num = random.randint(1, 5)
                if num % 2 != 0:
                    printing = True
            cont += 1
        
        else:
            my_printer.print_doc()
            printing = False



# navegando()
# printer()
