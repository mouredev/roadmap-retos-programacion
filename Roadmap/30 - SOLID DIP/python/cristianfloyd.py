# EJERCICIO:
# Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
# Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.
from abc import ABC, abstractmethod


# Implementacion incorrecta
class MySQLDatabase:
    """Implementacion concreta de una base de datos MySQL"""

    def connect(self) -> str:
        return "Conectando a MySQL..."

    def save_order(self, order_data: dict) -> str:
        return f"Guardando orden: {order_data}"


class EmailService:
    """Implementacion concreta de un servicio de email"""

    def send_email(self, to: str, subject: str, body: str) -> str:
        return f"Enviando email a {to} con asunto {subject}"


class GestorPedidos:
    """
    Clase de alto nivel que depende de implementaciones concretas
    """

    def __init__(self, database):
        """
        Dependencia directa de implementaciones concretas
        """
        self.database = MySQLDatabase()
        self.email_service = EmailService()

    def process_order(self, order_data: dict, customer_email: str) -> None:
        """
        Logica de negocio mezclada con detalles de implementacion
        """
        self.database.connect()
        self.database.save_order(order_data)
        self.email_service.send_email(
            customer_email,
            "Orden procesada",
            "La orden ha sido procesada correctamente",
        )


# Implementacion correcta
# =======================================================
# Abstracciones
class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

    @abstractmethod
    def save_order(self, order_data: dict) -> str:
        pass


class NotificacionInterface(ABC):
    @abstractmethod
    def send(self, recipient: str, subject: str, message: str) -> str:
        pass


# implementaciones concretas
class MySQLDatabaseV2(DatabaseInterface):
    """Implementacion concreta que depende de la abstraccion"""

    def connect(self) -> str:
        return "Conectando a MySQL..."

    def save_order(self, order_data: dict) -> str:
        return f"Guardando orden: {order_data}"


class PostgresDatabase(DatabaseInterface):
    """Implementacion concreta que depende de la abstraccion"""

    def connect(self) -> str:
        return "Conectando a Postgres..."

    def save_order(self, order_data: dict) -> str:
        return f"Guardando orden: {order_data}"


class EmailNotification(NotificacionInterface):
    """Implementacion concreta que depende de la abstraccion"""

    def send(self, recipient: str, subject: str, message: str) -> str:
        return f"Enviando email a {recipient} con asunto {subject}"


class SmsNotification(NotificacionInterface):
    """Implementacion concreta que depende de la abstraccion"""

    def send(self, recipient: str, subject: str, message: str) -> str:
        return f"Enviando SMS a {recipient} con asunto {subject}"


# =======================================================
# Modulo de alto nivel


class GestorPedidosV2:
    """
    Clase de alto nivel que depende de abstracciones
    Puede trabajar con cualquier implementacion que cumpla con el contrato de la interfaz
    """

    def __init__(
        self, database: DatabaseInterface, notification: NotificacionInterface
    ):
        """
        Dependencia de abstracciones
        """
        self.database = database
        self.notification = notification

    def process_order(self, order_data: dict, customer_email: str) -> None:
        """
        Logica de negocio
        """
        self.database.connect()
        self.database.save_order(order_data)
        print(self.database.connect())
        print(self.database.save_order(order_data))
        print(
            self.notification.send(
                customer_email,
                "Orden procesada",
                "La orden ha sido procesada correctamente",
            )
        )
        print("Orden procesada correctamente")


# Test
db_mysql = MySQLDatabaseV2()
notif_email = EmailNotification()
gestor1 = GestorPedidosV2(db_mysql, notif_email)

pedido1 = {"id": 1234, "producto": "Laptop", "cantidad": 1}
gestor1.process_order(pedido1, "cliente@email.com")


db_postgres = PostgresDatabase()
notif_sms = SmsNotification()
gestor2 = GestorPedidosV2(db_postgres, notif_sms)

pedido2 = {"id": 5678, "producto": "Mouse", "cantidad": 2}
gestor2.process_order(pedido2, "+34612345678")


#
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


# Interfaz de notificacion
class NotificadorInterface(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

    @abstractmethod
    def get_notification_type(self) -> str:
        pass


# Implementaciones concretas
class NotificadorEmail(NotificadorInterface):
    def __init__(self, smtp_server: str = "smtp.gmail.com"):
        self.smtp_server = smtp_server
        self.send_count = 0

    def send(self, recipient: str, message: str) -> bool:
        try:
            if "@" not in recipient:
                raise ValueError("Email invalido")

            print(f"Conectando a {self.smtp_server}")
            print(f"Enviando email a {recipient}")
            print(f"Mensaje: {message}")
            print("Email enviado exitosamente")
            self.send_count += 1
            return True

        except Exception as e:
            print(f"Error al enviar email: {e}")
            return False

    def get_notification_type(self) -> str:
        return "EMAIL"


class NotificadorSms(NotificadorInterface):
    def __init__(self, provider: str = "twilio") -> None:
        self.provider = provider
        self.send_count = 0

    def send(self, recipient: str, message: str) -> bool:
        try:
            if "+" not in recipient:
                raise ValueError("Numero de telefono invalido")

            print(f"Conectando a {self.provider}")
            print(f"Enviando SMS a {recipient}")
            print(f"Mensaje: {message}")
            print("SMS enviado exitosamente")
            self.send_count += 1
            return True

        except Exception as e:
            print(f"Error al enviar SMS: {e}")
            return False

    def get_notification_type(self) -> str:
        return "SMS"


class NotificadorPush(NotificadorInterface):
    def __init__(self, service: str = "firebase") -> None:
        self.service = service
        self.send_count = 0

    def send(self, recipient: str, message: str) -> bool:
        try:
            if "app_id" not in recipient:
                raise ValueError("App ID invalido")

            print(f"Conectando a {self.service}")
            print(f"Token del dispositivo: {recipient[:5]}")
            print(f"Enviando Push a {recipient}")
            print(f"Mensaje: {message}")
            print("Push enviado exitosamente")
            self.send_count += 1
            return True

        except Exception as e:
            print(f"Error al enviar Push: {e}")
            return False

    def get_notification_type(self) -> str:
        return "PUSH"


# =======================================================
# Modulo de alto nivel
class NotificadorService:
    """
    Clase de alto nivel que depende de abstracciones
    Puede trabajar con cualquier implementacion que cumpla con el contrato de la interfaz
    """

    def __init__(self) -> None:
        """
        No rea Notificadores internamente
        los recibe desde fuera (Inyeccion de dependencias)
        """
        self._notificadores: list[NotificadorInterface] = []
        self.count_send = 0

    def registrar_notificador(self, notificador: NotificadorInterface) -> None:
        """
        Registra un nuevo canal de notificacion
        """
        self._notificadores.append(notificador)
        print(f"Canal de notificacion {notificador.get_notification_type()} registrado")

    def enviar_todo(self, recipient: str, message: str) -> dict:
        """Envia notificaciones a todos los canales registrados"""
        if not self._notificadores:
            print("No hay canales de notificacion registrados")
            return {}

        resultados = {}
        for notificador in self._notificadores:
            try:
                resultado = notificador.send(recipient, message)
                resultados[notificador.get_notification_type()] = resultado
                if resultado:
                    self.count_send += 1

            except Exception as e:
                resultados[notificador.get_notification_type()] = f"Error: {e}"
        return resultados

    def enviar_por_canal(self, canal: str, recipient: str, message: str) -> bool:
        """Envia notificacion por un canal especifico"""
        if not self._notificadores:
            print("No hay canales de notificacion registrados")
            return False

        for notificador in self._notificadores:
            if notificador.get_notification_type() == canal.upper():
                return notificador.send(recipient, message)
        print(f"Canal de notificacion {canal} no encontrado")
        return False

    def get_registered_channels(self) -> list[str]:
        """Retorna lista de canales registrados"""
        return [n.get_notification_type() for n in self._notificadores]

    def get_stats(self) -> dict:
        """Retorna estadísticas del sistema"""
        return {
            "total_channels": len(self._notificadores),
            "channels": self.get_registered_channels(),
            "total_sent": self.count_send,
        }


# =======================================================
# Pruebas


def demostrar_sistema_notificaciones():
    """Demuestra el funcionamiento del sistema de notificaciones"""
    print("Iniciando sistema de notificaciones")
    notificador_service = NotificadorService()
    print("Registrando canales de notificacion")
    notificador_service.registrar_notificador(NotificadorEmail())
    notificador_service.registrar_notificador(NotificadorSms())
    notificador_service.registrar_notificador(NotificadorPush())

    print("Enviando notificaciones a todos los canales")
    notificador_service.enviar_todo(
        "cliente@email.com", "Hola, este es un mensaje de prueba"
    )
    print("Enviando notificacion por canal email")
    notificador_service.enviar_por_canal(
        "email", "cliente@email.com", "Hola, este es un mensaje de prueba"
    )
    print("Enviando notificacion por canal sms")
    notificador_service.enviar_por_canal(
        "sms", "+34612345678", "Hola, este es un mensaje de prueba"
    )
    print("Enviando notificacion por canal push")
    notificador_service.enviar_por_canal(
        "push", "app_id_1234567890", "Hola, este es un mensaje de prueba"
    )

    print("Mostrando estadisticas del sistema")
    print(notificador_service.get_stats())

    print("Creando un nuevo notificador 'Telegram'")

    class NotificadorTelegram(NotificadorInterface):
        def __init__(self, api_key: str = "1234567890") -> None:
            self.api_key = api_key
            self.send_count = 0

        def send(self, recipient: str, message: str) -> bool:
            try:
                print(f"Conectando a {self.api_key}")
                print(f"Enviando notificacion a {recipient}")
                print(f"Mensaje: {message}")
                print("Notificacion enviada exitosamente")
                self.send_count += 1
                return True

            except Exception as e:
                print(f"Error al enviar notificacion: {e}")
                return False

        def get_notification_type(self) -> str:
            return "TELEGRAM"

    notificador_service.registrar_notificador(NotificadorTelegram())

    print("Enviando notificacion por canal telegram")
    notificador_service.enviar_por_canal(
        "telegram", "cliente@telegram.com", "Hola, este es un mensaje de prueba"
    )

    print("Mostrando estadisticas del sistema")
    print(notificador_service.get_stats())


if __name__ == "__main__":
    demostrar_sistema_notificaciones()
