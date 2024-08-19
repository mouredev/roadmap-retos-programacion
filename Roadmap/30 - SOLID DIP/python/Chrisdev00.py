"""
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

# Forma incorrecta de aplicar el principio DIP

class SQLStorage:
    def save_user(self, user:dict):
        print(f"Guardando usuario en SQL: {user}")

class UsersService:
    def __init__(self):
        self.storage = SQLStorage()   # dependencia directa

    def user_register(self, name: str, email: str):
        user = {"nombre": name, "email": email}
        self.storage.save_user(user)

service = UsersService()
service.user_register("Juan", "juan@example.com")


# Forma Correcta de aplicar el principio DIP

from abc import ABC, abstractmethod

class AlmacenamientoUsuarios(ABC):
    @abstractmethod
    def save_user(self, user: dict):
        pass

class AlmacenamientoSQL(AlmacenamientoUsuarios):
    def save_user(self, user: dict):
        print(f"Guardando usuario en SQL: {user}")

class AlmacenamientoNoSQL(AlmacenamientoUsuarios):
    def save_user(self, user: dict):
        print(f"Guardando usuario en NoSQL: {user}")

class ServicioUsuarios:
    def __init__(self, almacenamiento: AlmacenamientoUsuarios):
        self.almacenamiento = almacenamiento

    def user_register(self, name: str, email: str):
        user = {"nombre": name, "email": email}
        self.almacenamiento.save_user(user)

almacenamiento_sql = ServicioUsuarios(AlmacenamientoSQL())
almacenamiento_sql.user_register("Juan", "juan@example.com")

almacenamiento_nosql = ServicioUsuarios(AlmacenamientoNoSQL())
almacenamiento_nosql.user_register("Pedro", "pedro@example.com")


##################### --------------------------- EXTRA --------------------------------- ########################

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send_notify(self, recipient: str, message: str):
        pass

class NotificacionByEmail(Notifier):
    def send_notify(self, recipient: str, message: str):
        print(f"Enviando email a {recipient} con el mensaje: {message}")

class NotificacionBySMS(Notifier):
    def send_notify(self, recipient: str, message: str):
        print(f"Enviando sms a {recipient} con el mensaje: {message}")

class NotificacionByPush(Notifier):
    def send_notify(self, recipient: str, message: str):
        print(f"Enviando push a {recipient} con el mensaje: {message}")

class NotificationService:
    def __init__(self, notification: Notifier):
        self.notification = notification

    def send_notification(self, recipient: str, message: str):
        self.notification.send_notify(recipient, message)

notification_email = NotificationService(NotificacionByEmail())
notification_email.send_notification("user@example.com", "Hola, este es un message por email")

notification_sms = NotificationService(NotificacionBySMS())
notification_sms.send_notification("user@example.com", "Hola, esta es una notificaion por sms")

notification_push = NotificationService(NotificacionByPush())
notification_push.send_notification("user@example.com", "Hola, esta es una notificacion via push")