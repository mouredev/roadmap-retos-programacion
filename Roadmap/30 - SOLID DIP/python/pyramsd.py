from abc import ABC, abstractmethod

# USO INCORRECTO
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

class Application:
    def __init__(self):
        self.database = MySQLDatabase()

    def run(self):
        self.database.connect()
        print("Running the application...")
        self.database.disconnect()

app = Application()
app.run()

"""
La clase Application depende directamente de la clase MySQLDatabase. Si se quiere cambiar a otra base de datos,
por ejemplo, PostgreSQL, habrá que modificar la clase Application, lo que puede romper la aplicación o complicar
el mantenimiento.
"""


# USO CORRECTO
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

class Application:
    def __init__(self, database: Database):
        self.database = database

    def run(self):
        self.database.connect()
        print("Running the application...")
        self.database.disconnect()

# Puedes cambiar la base de datos sin modificar la clase Application
mysql_db = MySQLDatabase()
app = Application(mysql_db)
app.run()

postgres_db = PostgreSQLDatabase()
app = Application(postgres_db)
app.run()


"""
EXTRA
"""
class Notification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending Email to {recipient}: {message}")

class PushNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending PUSH notification to {recipient}: {message}")

class SMSNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")

class NotificationService:
    def __init__(self, notifier: Notification):
        self.notifier = notifier

    def notify(self, message: str, recipient: str):
        self.notifier.send(message, recipient)


def main():
    email_notifier = EmailNotification()
    push_notifier = PushNotification()
    sms_notifier = SMSNotification()

    # Crear el servicio de notificaciones usando el notificador de Email
    email_service = NotificationService(email_notifier)
    email_service.notify("Hello via Email!", "email@example.com")

    # Crear el servicio de notificaciones usando el notificador de PUSH
    push_service = NotificationService(push_notifier)
    push_service.notify("Hello via PUSH!", "user_device_token")

    # Crear el servicio de notificaciones usando el notificador de SMS
    sms_service = NotificationService(sms_notifier)
    sms_service.notify("Hello via SMS!", "123-456-7890")

if __name__ == "__main__":
    main()
