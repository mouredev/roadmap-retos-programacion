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

class Notification(ABC):
    @abstractmethod
    def enviar(self, emisor, receptor):
        pass


class Email(Notification):
    def enviar(self, emisor, receptor):
        print(f"Enviando email de {emisor} a {receptor}")

class SMS(Notification):
    def enviar(self, emisor, receptor):
        print(f"Enviando SMS de {emisor} a {receptor}")

class Push(Notification):
    def enviar(self, emisor, receptor):
        print(f"Enviando push de {emisor} a {receptor}")



class NotificationService: 
    def __init__(self, notification: Notification):
        self.notification = notification
    
    def notificar(self, emisor, receptor):
        self.notification.enviar(emisor, receptor)


service = NotificationService(Email())
service.notificar("aaaaaa@gmail.com", "bbbbb@gmail.com")