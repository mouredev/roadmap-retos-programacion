import os, platform
from abc import ABC, abstractmethod

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
 *
"""


"""
El Principio de Inversión de Dependencia (DIP) establece que las clases de alto nivel
 no deben depender de clases de bajo nivel.
En el siguiente caso no se cumple el principio ya que hay una clase Fruta que establece la
especie de fruta y la impresión con la lógica para que el artículo en el mensaje se adapte a
si la especie de fruta se nombre con género masculino o femenino y a su vez las clases que crean
objetos de esos tipos de fruta sólo setean su nombre heradando de Fruta que crea todo el trabajo"""

class Fruit:
    def __init__(self, object) -> None:
        self.object = object
        self.name = object.name

    def print_fruit(self):
        self.article = "un"
        
        if self.object.name.endswith('a'):
            self.article = "una"
        print (f"La fruta es {self.article} {self.name} ")
        
class Pear(Fruit):
    def __init__(self) -> None:
        self.name = "pera"

class Apple(Fruit):
    def __init__(self) -> None:
        self.name = "manzana"

class Melon(Fruit):
    def __init__(self) -> None:
        self.name = "melón"

 
pera = Fruit(Pear()).print_fruit()
melon = Fruit(Melon()).print_fruit()
manzana = Fruit(Apple()).print_fruit()

"""En el siguiente caso creamos 2 clases abstractas, una que establece el seteo del nombre
y otra que gestiona la impresión, las clases que generen objetos de tipos de fruta heredan
de ambas clases abstractas , setean su nombre y sólo llaman a sus métodos que son comunes a todas la frutas."""

class FruitDIP(ABC):
    @abstractmethod
    def set_name(self, name):
        self.name = name
class PrintFruitDIP(ABC):
    @abstractmethod
    def print_fruit(self):
        self.article = "un"
        if self.name.endswith('a'):
            self.article = "una"
        print (f"La fruta es {self.article} {self.name} ")

class Orange(FruitDIP, PrintFruitDIP):
    name = "naranja"
    def set_name(self, name):
        return super().set_name(name)
    def print_fruit(self):
        return super().print_fruit()
    
class WaterMelon(FruitDIP, PrintFruitDIP):
    name = "sandía"
    def set_name(self, name):
        return super().set_name(name)
    def print_fruit(self):
        return super().print_fruit()
    
class Lemon(FruitDIP, PrintFruitDIP):
    name = "limón"
    def set_name(self, name):
        return super().set_name(name)
    def print_fruit(self):
        return super().print_fruit()
    
naranja = Orange().print_fruit()
sandia = WaterMelon().print_fruit()
limon = Lemon().print_fruit()

"""En Python el concepto de clase abstracta o interface es algo ambiguo, en el caso mostrado las clases
FruitDIP y PrintFruitDIP se pueden interpretar como clases abstractas ya que aunque todos sus métodos sean
abstractos y por lo tanto es obligatorio implementarlos en las clases que hereden de esas clases ya tienen
su lógica y por lo tanto es más adecuado interpretarlas como clases abstractas, en otros lenguajes como Java
la declaración de interface se hace tal cual y no permite crear lógica alguna en los métodos que se declaren dentro
de la misma, además se pueden crear clases abstractas como tal y en este caso sí se pueden crear métodos con lógica
y llamarlos desde las clases que hereden de la clase abstracta con la particularidad de que no permite la herencia
múltiple de varias clases abstractas pero sí de varias interfaces, por ello Python permite mayor flexibilidad pero 
tambien puede crear mayor confusión en estructuras de clases"""

    
""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio."""


class MessageInterface(ABC):
    @abstractmethod
    def email(self):
        pass
    @abstractmethod
    def push(self):
        pass
    @abstractmethod
    def sms(self):
        pass

class SendNotification(MessageInterface):

    def email(self, message):
        self.message = message
        print (self.message , "--> Enviando email...")
    def push(self,message):
        self.message = message
        print (self.message, "--> Enviando push...")
    def sms(self,message):
        self.message = message
        print (self.message,"--> Enviando SMS...")

class Confirmation(MessageInterface): 
    def email(self, message):
        self.message = message
        print (self.message,"--> Email enviado")
    def push(self,message):
        self.message = message
        print (self.message,"--> Mensaje PUSH enviado")
    def sms(self,message):
        self.message = message
        print (self.message,"--> Mensaje SMS enviado")
    
class Email(SendNotification, Confirmation):
    def __init__(self):
        self.message = "Esto es un mensaje de email..."
        super().email(self.message)
    def confirmation(self):
        super(SendNotification,self).email(self.message)

class Push(SendNotification, Confirmation):
    def __init__(self):
        self.message = "Esto es un mensaje PUSH..."
        return super().push(self.message)
    def confirmation(self):
        super(SendNotification,self).push(self.message)
    
class Sms(SendNotification, Confirmation):
    def __init__(self):
        self.message = "Esto es un mensaje SMS..."
        return super().sms(self.message)
    def confirmation(self):
        super(SendNotification,self).sms(self.message)
    
email = Email()
email.confirmation()
push = Push()
push.confirmation()
sms = Sms()
sms.confirmation()





