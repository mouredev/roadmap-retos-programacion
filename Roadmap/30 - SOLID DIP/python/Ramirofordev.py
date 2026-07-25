'''
Ejercicio: 
Explora el "Principio SOLID de Inversion de Dependencias (Dependency Invesrion Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
'''
from abc import ABC, abstractmethod

#! Forma incorrecta
class MotorGasolina:
    def arrancar(self):
        print("Motor a gasolina arrancando..")

class Coche:
    def __init__(self):
        self.motor = MotorGasolina()


class IMotor(ABC):
    @abstractmethod
    def arrancar(self):
        pass


class MotorGasolina(IMotor):
    def arrancar(self):
        print("Motor a gasolina arrancando..")

class MotorElectrico(IMotor):
    def arrancar(self):
        print("Motor electrico arrancando..")

class Coche:
    def __init__(self, motor: IMotor):
        self.motor = motor

    def encender(self):
        self.motor.arrancar()


'''
Dificultad extra:
Crea un sistema de notificaciones.

Requisitos:
    1. El sistema puede enviar, Email, PUSH y SMS (implementaciones especificas).
    2. El sistema de notificaciones no puede depender de las implementaciones especificas

Instrucciones:
    1. Crea la interfaz o clase abstracta.
    2. Desarrolla las implementaciones especificas.
    3. Crea el sistema de notificaciones usando el DIP.
    4. Desarrolla un codigo que compruebe que se cumple el principio.
'''

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje, destino):
        pass


class Email(Notificacion):
    def enviar(self, mensaje, destino):
        print(f"Enviando el email: {mensaje}.\n"
              f"Al destino: {destino}")
        
class Push(Notificacion):
    def enviar(self, mensaje, destino):
        print(f"Enviando el push: {mensaje}.\n"
              f"Al destino: {destino}.")
        
class Sms(Notificacion):
    def enviar(self, mensaje, destino):
        print(f"Enviando el sms: {mensaje}.\n"
              f"Al destino: {destino}.")
        
class GestorNotificaciones:
    def __init__(self, tipo: Notificacion):
        self.tipo = tipo

    def notificar(self, mensaje, destino):
        self.tipo.enviar(mensaje, destino)

def test_notificacion(notificacion: Notificacion):
    notificacion.enviar("Mensaje de prueba", "Usuarioyo")

email = GestorNotificaciones(Email())
email.notificar("Hola!", "yo22@gmail.com")

push = GestorNotificaciones(Push())
push.notificar("Sales?", "lalalal")

sms = GestorNotificaciones(Sms())
sms.notificar("Rebajas de invierno!", "55634345")

test_notificacion(Email())
test_notificacion(Push())
test_notificacion(Sms())