"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""

# Correcto

from abc import ABC, abstractmethod

class IMotor(ABC):
    @abstractmethod
    def encender(self):
        pass

class Motor(IMotor):
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self, motor: IMotor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

motor = Motor()
coche = Coche(motor)
coche.arrancar()


# Incorrecto

class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()

coche = Coche()
coche.arrancar()


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
 * 4. Desarrolla un código que compruebe que se cumple el principio.
"""

from abc import ABC, abstractmethod

class INotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass


class EmailNotificacion(INotificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando Email: {mensaje}")

class PushNotificacion(INotificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando Notificación PUSH: {mensaje}")

class SMSNotificacion(INotificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")


class SistemaNotificaciones:
    def __init__(self, notificador: INotificacion):
        self.notificador = notificador

    def notificar(self, mensaje: str):
        self.notificador.enviar(mensaje)

# Crear instancias de las implementaciones específicas
email_notificacion = EmailNotificacion()
push_notificacion = PushNotificacion()
sms_notificacion = SMSNotificacion()

# Crear el sistema de notificaciones con diferentes implementaciones
sistema_email = SistemaNotificaciones(email_notificacion)
sistema_push = SistemaNotificaciones(push_notificacion)
sistema_sms = SistemaNotificaciones(sms_notificacion)

# Enviar notificaciones
sistema_email.notificar("Hola por Email")
sistema_push.notificar("Hola por PUSH")
sistema_sms.notificar("Hola por SMS")

