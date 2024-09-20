"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.

"""


"""
# ------------------------------------------
# |   DEPENDENCY INVERSION PRINCIPLE (DIP)  |  Información extraída de -> https://devexpert.io/principios-solid-guia-gratis/ 
# ------------------------------------------
# 
# Las clases de alto nivel no deberían depender de las clases de bajo
# nivel. Ambas deberían depender de las abstracciones.
# 
# Las abstracciones no deberían depender de los detalles. Los detalles
# deberían depender de las abstracciones.
# 
# 
# ¿CÓMO DETECTAR QUE ESTAMOS VIOLANDO EL PRINCIPIO DE INVERSION DE DEPENDENCIAS?
# - cualquier instanciación de clases complejas o modulos es una violacion a este principio
# - cuando no se pueda probar una clase con facilidad porque depende del codigo de otra clase
#  
#  SOLUCION: Utilizar alguna alternativa para suministrarle dependencias (constructor, setters, inyector de dependencias) 
"""


# DEPENDENCY INVERSION PRINCIPLE FORMA INCORRECTA

class Shopping:
    def __init__(self) -> None:
        pass

"""
ShoppingBasket incumple el principio ya que depende de clases de bajo nivel como CreditCard y SqlDatabase

- ¿que pasa si queremos guardar la informacion en un servidor en vez de la base de datos?
- ¿que pasa si queremos agregar otros medios de pago?

Respuesta: se desmontaria toda la logica
"""
class ShoppingBasket:
    def buy(self, shopping: Shopping):
        db = SqlDatabase()
        db.save(shopping)
        creditCard =  CreditCard()
        creditCard.pay()

class SqlDatabase:
    def save(self, shopping: Shopping):
        print("Guardando en base de datos")

class CreditCard:
    def pay(self, shopping: Shopping):
        print("Pago utilizando tarjeta de credito")


# DEPENDENCY INVERSION PRINCIPLE FORMA CORRECTA
"""
Solución: dejar de depender de concresiones.
se crearán interfaces que definan el comportamiento que debe dar una clase
para poder funcionar como mecanismo de persistencia o como metodo de pago.
"""

from abc import ABC, abstractmethod

# Clase que actua como interface para definir metodo de persistencia
class Persistence(ABC):
    @abstractmethod
    def save(self, shopping: Shopping):
        pass

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, shopping: Shopping):
        pass

class SqlDatabase(Persistence):
    def save(self, shopping: Shopping):
        print("Guardando los datos en la Base de datos")

class Server(Persistence):
    def save(self, shopping: Shopping):
        print("Guardando los datos en el servidor")

class CreditCard(PaymentMethod):
    def pay(self, shopping: Shopping):
        print("Se ha hecho el pago con tarjeta de credito")

class DebitCard(PaymentMethod):
    def pay(self, shopping: Shopping):
        print("Se ha hecho el pago con tarjeta de debito")

class ShoppingBasket:
    
    def __init__(self, persistence: Persistence, paymentMethod: PaymentMethod) -> None:
        self.persistence = persistence
        self.paymentMethod = paymentMethod
    
    @property
    def persistence(self):
        return self._persistence
    
    @property
    def paymentMethod(self):
        return self._paymentMethod
    
    @persistence.setter
    def persistence(self,persistence: Persistence):
        self._persistence = persistence
    
    @paymentMethod.setter
    def paymentMethod(self, paymentMethod: PaymentMethod):
        self._paymentMethod = paymentMethod

    def buy(self, shopping: Shopping):
        self.persistence.save(shopping)
        self.paymentMethod.pay(shopping)

def testDependencyInversion(shopping):
    shoppingBasket = ShoppingBasket(SqlDatabase(), DebitCard())
    shoppingBasket.buy(shopping)
    
    shoppingBasket.paymentMethod = CreditCard()
    shoppingBasket.persistence = Server()
    shoppingBasket.buy(shopping)
    

testDependencyInversion(Shopping())


"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
 */
"""

print(" ----------------- Dificultad Extra ------------------------")

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, msg: str):
        pass

class Email(Notifier):
    def send(self, to: str, msg: str):
        print(f"se ha enviado un Email a {to}.")
        print(f"Contenido: {msg}")

class Sms(Notifier):
    def send(self, to: str, msg: str):
        print(f"se ha enviado un SMS a {to}.")
        print(f"Contenido: {msg}")

class Push(Notifier):
    def send(self, to: str, msg: str):
        print(f"se ha enviado una notificacion PUSH a {to}.")
        print(f"Contenido: {msg}")


class NotificationService():
    def __init__(self,notifier: Notifier ) -> None:
        self.notifier = notifier
    
    @property
    def notifier(self):
        return self._notifier
    
    @notifier.setter
    def notifier(self, notifier):
        self._notifier = notifier
    
    def sendMsg(self, to: str,msg: str):
        self.notifier.send(to,msg)
        

def comprobarDependencyInversion():
    system = NotificationService(Sms())
    system.sendMsg("Martin", "Hola martin, un gusto")
    
    system.notifier = Email()
    system.sendMsg("Martin", "Hola martin, un gusto")
    
    system.notifier = Push()
    system.sendMsg("Martin", "Hola martin, un gusto")


comprobarDependencyInversion()