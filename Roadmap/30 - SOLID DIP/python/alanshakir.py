""""
/*
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
 */
"""
#SIN DIP
class EmailService():
    def send_email(self, message):
        print(f"Enviando email: {message}")    

class SMSService():
    def send_sms(self, message):
        print(f"Enviando sms: {message}")

class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
        
    def notification_manager(self, message):
        self.email_service = message
        self.sms_service = message

    def send_notification(self, message):
        self.email_service.send_email(message)
        self.sms_service.send_sms(message)

manager = NotificationManager()
manager.send_notification("Aprendiendo Python")

#CON DIP
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"Enviando email: {message}")    

class SMSService(NotificationService):
    def send(self, message):
        print(f"Enviando sms: {message}")

class NotificationManager:
    def __init__(self, service : NotificationService):
        self.notification_service = service
        
    def notification_manager(self, message):
        self.notification_service = message

    def send_notification(self, message):
        self.notification_service.send(message)

email_service = EmailService()
manager = NotificationManager(email_service)
manager.send_notification("Aprendiendo Python")

sms_service = SMSService()
manager = NotificationManager(sms_service)
manager.send_notification("Aprendiendo Python")

#Extra

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"Enviando email: {message}")    

class PushService(NotificationService):
    def send(self, message):
        print(f"Enviando push: {message}")  

class SMSService(NotificationService):
    def send(self, message):
        print(f"Enviando sms: {message}")

class NotificationManager:
    def __init__(self, service : NotificationService):
        self.notification_service = service

    def send_notification(self, message):
        self.notification_service.send(message)

manager = NotificationManager(EmailService())
manager.send_notification("Aprendiendo Python, ruta de programacion")
manager = NotificationManager(PushService())
manager.send_notification("Aprendiendo Python, ruta de programacion")
manager = NotificationManager(SMSService())
manager.send_notification("Aprendiendo Python, ruta de programacion")
