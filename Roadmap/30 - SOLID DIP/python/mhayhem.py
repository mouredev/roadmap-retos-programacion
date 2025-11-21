# @Author Daniel Grande (Mhayhem)

from abc import ABC, abstractmethod

# EJERCICIO:
# Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
# Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
# de forma correcta e incorrecta.

# incorrecta

class MySQLDatabase:
    def save(self, data):
        return "Guardando en MySQL."

class UserRepository:
    def __init__(self):
        self.db = MySQLDatabase()
    
    def save_user(self, user):
        self.db(user)

# correcta

class DataBase(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase:
    def save(self, data):
        return f"Guardando {data} En MySQL."

class PostSQLDatabase:
    def save(self, data):
        return f"Guardando {data} en PostSQL."

class MongoDBDatabase:
    def save(self, data):
        return f"Guardando {data} en MongoDB."

class UserRepository:
    def __init__(self):
        self.db = DataBase()
    
    def save_user(self, user):
        self.db.save(user)


# DIFICULTAD EXTRA (opcional):
# Crea un sistema de notificaciones.
# Requisitos:
# 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
# 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
# Instrucciones:
# 1. Crea la interfaz o clase abstracta.
# 2. Desarrolla las implementaciones específicas.
# 3. Crea el sistema de notificaciones usando el DIP.
# 4. Desarrolla un código que compruebe que se cumple el principio.

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class PushNotification(NotificationService):
    def send(self, message: str) -> str:
        return f"Enviando notificación push : {message}"

class EmailNotification(NotificationService):
    def send(self, message: str) -> str:
        return f"EWnviando email: {message}"

class SMSNotification(NotificationService):
    def send(self, message: str) -> str:
        return f"Enviando SMS: {message}"

class NotificationSystem:
    def __init__(self, service=NotificationService):
        self.service = service
    
    def notify(self, message: str):
        self.service.send(message)

system = NotificationSystem(NotificationService)
push = PushNotification()
email = EmailNotification()
sms = SMSNotification()

def test_notifications(array: list, message):
    for notify in array:
        print(notify.send(message))
    
    assert AttributeError

def test_system(element: NotificationSystem, message: str) -> str | None:
    result = element.notify(message)

    print(result)
    assert result is not None
    assert message in result