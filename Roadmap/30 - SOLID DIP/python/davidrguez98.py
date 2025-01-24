""" /*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
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
 */ """

#EJERCICIO

""" 
Incorrecta
"""

class Switch:

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")

class Lamp:

    def __init__(self):
        self.switch = Switch()

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp = Lamp()
lamp.operate("on")
lamp.operate("off")

""" 
Correcta
"""

class AbstractSwitch:

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LampSwitch(AbstractSwitch):

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")

class Lamp:

    def __init__(self, switch: AbstractSwitch):
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp  = Lamp(LampSwitch())
lamp.operate("on")
lamp.operate("off")

#DIFICULTAD EXTRA

from abc import ABC, abstractmethod

class Notifier(ABC):

    def send(self, message: str):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Enviando email con texto: {message}")

class PushNotifier(Notifier):
    def send(self, message):
        print(f"Enviando push con texto: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Enviando SMS con texto: {message}")

class NotificationService:

    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)

service = NotificationService(EmailNotifier())
service.notify("Hola!")
service = NotificationService(PushNotifier())
service.notify("Hola!")
service = NotificationService(SMSNotifier())
service.notify("Hola!")