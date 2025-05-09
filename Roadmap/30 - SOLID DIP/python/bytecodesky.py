# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
#  * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
#  * de forma correcta e incorrecta.
#  *

# forma incorrecta de implementar el principio DIP
class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()
        self.bulb.turn_off()

bulb = LightBulb()
switch = Switch(bulb)
switch.operate()

# forma correcta de implementar el principio DIP
class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()
        self.device.turn_off()

bulb = LightBulb()
switch = Switch(bulb)
switch.operate()

fan = Fan()
switch = Switch(fan)
switch.operate()

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un sistema de notificaciones.
#  * Requisitos:
#  * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
#  * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
#  * Instrucciones:
#  * 1. Crea la interfaz o clase abstracta.
#  * 2. Desarrolla las implementaciones específicas.
#  * 3. Crea el sistema de notificaciones usando el DIP.
#  * 4. Desarrolla un código que compruebe que se cumple el principio.
#  */

from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"EmailNotification: {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"PushNotification: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"SMSNotification: {message}")

class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message: str):
        self.notification.send(message)

email = EmailNotification()
push = PushNotification()
sms = SMSNotification()

service = NotificationService(email)
service.send("Hello, Email!")

service = NotificationService(push)
service.send("Hello, Push!")

service = NotificationService(sms)
service.send("Hello, SMS!")
