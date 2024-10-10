# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

from abc import ABC, abstractmethod

# Interfaz para el servicio de notificación
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

# Implementación específica para Email
class EmailNotification(NotificationService):
    def send_notification(self, message: str) -> None:
        print(f"[+] - Enviando Email: {message}")

# Implementación específica para PUSH
class PushNotification(NotificationService):
    def send_notification(self, message: str) -> None:
        print(f"[+] - Enviando Push Notification: {message}")

# Implementación específica para SMS
class SMSNotification(NotificationService):
    def send_notification(self, message: str) -> None:
        print(f"[+] - Enviando SMS: {message}")

# Sistema de Notificaciones usando DIP
class NotificationSystem:
    def __init__(self):
        self.services = []

    def add_service(self, service: NotificationService) -> None:
        self.services.append(service)

    def notify_all(self, message: str) -> None:
        for service in self.services:
            service.send_notification(message)

# Función principal para demostrar el DIP
if __name__ == "__main__":
    # Correcto: El sistema de notificaciones no depende directamente de las implementaciones concretas
    notification_system = NotificationSystem()
    
    notification_system.add_service(EmailNotification())
    notification_system.add_service(PushNotification())
    notification_system.add_service(SMSNotification())

    notification_system.notify_all("Mensaje de prueba.")

    # Incorrecto: Dependencia directa de las implementaciones concretas (violación del DIP)
    email_notification = EmailNotification()
    email_notification.send_notification("Mensaje directo sin sistema de notificaciones.")
