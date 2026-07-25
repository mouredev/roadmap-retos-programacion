# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta."""

# Violación del DIP

class MySQLDatabase:
    """Simulación de una base de datos MySQL"""
    def save(self, data):
        print(f"Guardando  {data} en la base de datos MySQL...")

# Módulo de alto nivel, depende de un módulo de bajo nivel.
class OrderProcessor:
    def __init__(self) -> None:
        self.db = MySQLDatabase() # Implementación o dependencia concreta
    def process_order(self, order):
        self.db.save(order)

# OrderProcessor depende de MySQLDatabase el cual es un detalle técnico o implementación especifica
# si cambiamos de base de datos, OrderProcessor no funcionará, por ende habrá que modificarlo.

# Siguiendo el DIP
from abc import ABC, abstractmethod

# Definimos una abstracción (interfaz/clase abstracta)
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Módulo de alto nivel depende de una abstracción
class OrderProcessor:
    def __init__(self, db: Database) -> None:
        self.db = db # Inyección de dependencia por constructor

    def proccess_order(self, order):
        self.db.save(order)

# Implementación concreta de la abstracción en módulo de bajo nivel
class MySQLDatabase(Database):
    def save(self, data):
        print(f"Guardando {data} en la base de datos MySQL...")

class MongoDBDatabase(Database):
    def save(self, data):
        print(f"Guardando {data} en la base de datos MongoDB...")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Guardando {data} en la base de datos PostgreSQL...")

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

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Notification:
    """Clase que representa una notificación"""
    message: str
    recipient: str
    timestamp: datetime = datetime.now()

# Abstracción para el envio de las notificaciones
class NotificationSender(ABC):
    """Interfaz para el envio de las notificaciones"""
    @abstractmethod
    def send(self, notification: Notification) -> None:
        """Envia la notificación"""
        pass

# Implementaciones concretas o especificas
class EmailNotificationSender(NotificationSender):
    def send(self, notification: Notification) -> None:
        print(
            f"Enviando Email a {notification.recipient}: {notification.message} - {notification.timestamp}"
            )
        
class PushNotificationSender(NotificationSender):
    def send(self, notification: Notification) -> None:
        print(f"Enviando Push a {notification.recipient}:" 
            f"{notification.message} - {notification.timestamp}"
            )
        
class SMSNotificationSender(NotificationSender):
    def send(self, notification: Notification) -> None:
        print(f"Enviando SMS a {notification.recipient}:" 
            f"{notification.message} - {notification.timestamp}"
            )
        
# Sistema de notificaciones - Módulo de alto nivel(depende de la abstracción)
class NotificationSystem:
    def __init__(self, notifier: NotificationSender):
        self.notifier = notifier    # Inyección de dependencias por constructor
    
    def send(self, notification: Notification):
        self.notifier.send(notification)

# Test de la implementación
def test_notification_system(notification: Notification, notifier: NotificationSender):
    notification_system = NotificationSystem(notifier)
    notification_system.send(notification)

# Caso de uso

if __name__ == "__main__":
    
    # Creando una notificación
    notification1 = Notification(
        message="Hola, este es un mensaje de prueba.",
        recipient="Duban Quiroga"
    )
    
    # Creando los notificadores
    email = EmailNotificationSender()
    push = PushNotificationSender()
    sms = SMSNotificationSender()

    # Enviando la notificación
    for notifier in [email, push, sms]:
        test_notification_system(notification1, notifier)