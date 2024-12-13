"""
  EJERCICIO:
 Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)"
 y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.

  DIFICULTAD EXTRA (opcional):
 Crea un gestor de impresoras.
 Requisitos:
 1. Algunas impresoras sólo imprimen en blanco y negro.
 2. Otras sólo a color.
 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 Instrucciones:
 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 2. Aplica el ISP a la implementación.
 3. Desarrolla un código que compruebe que se cumple el principio.
"""
from abc import ABC, abstractmethod


print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Para entender fácilmente los 5 ppios SOLID recomiendo leer:

    https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/

en donde se explican de manera ordenada uno por uno, de manera sencilla y ejemplificada de manera progresiva (de hecho, de ahí
voy a tomar el ejemplo).

El cuarto ppio SOLID es el ppio de segregación de interfaz (Interface Segregation Principle) y establece que las clases "hijas" 
no deberían estar obligadas a implementar métodos que no han de usar.

En el ejemplo anterior vemos que la clase abstracta "Bird" tiene métodos "fly" y "swim", pero como el "Cuervo" no nada, no debería
su clase estar obligada a implementar dicho método (como así también una clase "Pingüino" no debiera implementar "fly".

Para evitar este problema, separamos en distintas interfaces la implementación de aquellos métodos de la clase Bird que no son 
realemente comunes a cualquier clase de pájaros.

    from abc import ABC, abstractmethod
    from typing import final
    
    class Bird(ABC):
    
        def __init__(self, name):
            self.name = name
    
        @abstractmethod
        def do_sound(self) -> str:
            pass
    
    class FlyingBird(Bird):
    
        @abstractmethod
        def fly(self):
            pass
    
    class SwimmingBird(Bird):
    
        @abstractmethod
        def swim(self):
            pass
    
    class Crow(FlyingBird):
       
        def fly(self):
            print(f"{self.name} is flying high and fast!")
    
        def do_sound(self) -> str:
            return "Caw"
    
    class Duck(SwimmingBird, FlyingBird):
       
        def fly(self):
            print(f"{self.name} is flying not very high")
    
        def swim(self):
            print(f"{self.name} swims in the lake and quacks")
    
        def do_sound(self) -> str:
            return "Quack"

    lucas = Duck("Lucas")
    lucas.fly()
    lucas.swim()
    
    dandy = Crow("Dandy")
    dandy.fly()
    
    Lucas is flying not very high
    Lucas swims in the lake and quacks

    Dandy is flying high and fast!
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")


class Spooler(ABC):

    @abstractmethod
    def enqueue(self, docname: str):
        pass

    @abstractmethod
    def dequeue(self):
        pass


class Printer(Spooler):

    def __init__(self):
        self.queue = []

    def enqueue(self, docname: str):
        self.queue.append(docname)
        print(f"Document {docname} enqueued.")

    def dequeue(self):
        return self.queue.pop(0)

    @abstractmethod
    def cartridge_level(self):
        pass

    @abstractmethod
    def add_cartridge(self, color: str):
        pass


class Fax(Spooler):
    @abstractmethod
    def send_document(self, target_number: str):
        pass

    @abstractmethod
    def receive_document(self, docname: str, from_number: str):
        pass


class Scanner(Spooler):
    @abstractmethod
    def save_document(self):
        pass


class PrinterBN(Printer):

    def __init__(self):
        super().__init__()
        self.black_cartridge_level = 100

    def cartridge_level(self):
        return self.black_cartridge_level

    def print_document(self):
        if self.queue.__len__() > 0:
            if self.black_cartridge_level > 1:
                print(f"Printing {self.dequeue()}")
                self.black_cartridge_level -= 1
            else:
                print("RAISE Black Cartridge is EMPTY")
                return
        else:
            print("RAISE No documents enqueued")

    def add_cartridge(self, color: str="black"):
        if color == "black":
            self.black_cartridge_level = 100
            print("Cartridge black SET")
        else:
            print("This printer accepts BLACK cartridge only")


class PrinterColor(Printer):

    def __init__(self):
        super().__init__()
        self.cartridges_status = {"black": 100, "yellow": 4, "magenta": 2, "cyan": 100}

    def cartridge_level(self):
        return self.cartridges_status

    def print_document(self):

        if self.queue.__len__() > 0:
            for color, level in self.cartridges_status.items():
                if level == 0:
                    print(f"RAISE {color.capitalize()} cartridge is EMPTY")
                    return
            print(f"Printing {self.dequeue()}")
            for color in self.cartridges_status.keys():
                self.cartridges_status[color] -= 1
        else:
            print("RAISE No documents enqueued")

    def add_cartridge(self, color: str):
        if color in self.cartridges_status.keys():
            self.cartridges_status[color] = 100
            print(f"Cartridge {color} SET")
        else:
            print(f"RAISE {color.upper()} is not a valid cartridge")


class Multifunction(PrinterColor, Scanner, Fax):

    def save_document(self):
        print(f"Saving document {self.dequeue()} to Documents Folder")

    def send_document(self, target_number: str):
        print(f"Sending document {self.dequeue()} to {target_number}")

    def receive_document(self, docname: str, from_number: str):
        self.enqueue(docname + "_" + from_number)


prn_01 = PrinterBN()
prn_02 = PrinterColor()
prn_03 = Multifunction()

prn_01.enqueue("Fichero_1.txt")
prn_01.print_document()
prn_01.print_document()

prn_02.enqueue("Album.pdf")
prn_02.enqueue("MapaGoogle.png")
prn_02.enqueue("DiplomaPython.pdf")
prn_02.print_document()
prn_02.print_document()
prn_02.print_document()
prn_02.add_cartridge("Majenta")
prn_02.add_cartridge("magenta")
prn_02.print_document()
prn_02.print_document()

prn_03.receive_document("Notificacion.docx", "+5491112345678")
prn_03.save_document()
prn_03.enqueue("Respuesta_Notificacion.docx")
prn_03.send_document("+5491112345678")
prn_03.enqueue("Git y GitHub desde cero.pdf")
prn_03.enqueue("Git y GitHub desde cero.pdf")
prn_03.enqueue("Git y GitHub desde cero.pdf")
prn_03.enqueue("Git y GitHub desde cero.pdf")
prn_03.enqueue("Git y GitHub desde cero.pdf")
prn_03.print_document()
prn_03.print_document()
prn_03.print_document()
prn_03.add_cartridge("magenta")
prn_03.print_document()
prn_03.print_document()
prn_03.print_document()
prn_03.add_cartridge("yellow")
prn_03.print_document()
