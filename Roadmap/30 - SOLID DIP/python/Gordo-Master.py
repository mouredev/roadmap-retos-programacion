# 30 - Solid DIP (Dependency Inversion Principle), Principio de inversión de dependecia

# Se basa en dos puntos:
# 1- Las dependencias deben estar en abstracciones, no en detalles. (Las de alto nivel emplean abstracciones, y las de bajo nivel las implementan).
# 2- Los modulos de alto nivel no deben depender de modulos de bajo nivel. Sino que ambos deben depender de abstracciones.


"""
Forma incorrecta
"""

"""
class MailService:
    def send_email(self, destination, subject, messenge):
        print(f"Enviando correo a {destination}: {subject}\n{messenge}")

class NotificationSystem:
    def __init__(self):
        self.mail_service = MailService()

    def send_notification(self, destination, messenge): 
        self.mail_service.send_email(destination,"Notificación",messenge)
"""


"""
Forma correcta y ejercicio extra
"""

from abc import ABC, abstractmethod

class NotificationService(ABC):

    @abstractmethod
    def send(self, destination, messenge):
        pass

class MailService(NotificationService):

    def send(self, destination, messenge):
        print(f"Enviando correo a {destination}: \n{messenge}")

class SMSService(NotificationService):

    def send(self, destination, messenge):
        print(f"Enviando SMS a {destination}: \n{messenge}")

class PushService(NotificationService):

    def send(self, destination, messenge):
        print(f"Enviando PUSH a {destination}: \n{messenge}")

class NotificationSystem:
    
    def __init__(self, service: NotificationService):
        self.service = service

    def send_notification(self, destination, messenge):
        self.service.send(destination, messenge)

system_1 = NotificationSystem(MailService())

system_2 = NotificationSystem(SMSService())

system_3 = NotificationSystem(PushService())

def test():
    system_1.send_notification("user_1@user.com","Tienes una nueva notificación")
    system_2.send_notification("user_2@user.com", "Tienes un nuevo SMS")
    system_3.send_notification("user_1@user.com", "Tienes una nueva Push")

test()

