""" /*
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
 */ """

""" Paso directo al ejercicio
    En sisntesis el principio plantea que las clases concretas no pueden depender de otras clases concretas
    solo pueden depender de clases abstractas.
    Otra manera de ppantearlo es que las clases de alto nivel no pueden depender de las clases de bajo nivel.
 """

from abc import ABC, abstractmethod


class AbstractChannel(ABC):

    @abstractmethod
    def get_channel_message(self) -> str:
        pass


class SMSChannel(AbstractChannel):

    def get_channel_message(self) -> str:
        return "(via SMS)"


class PUSHChannel(AbstractChannel):

    def get_channel_message(self) -> str:
        return "(via PUSH)"


class EmailChannel(AbstractChannel):

    def get_channel_message(self) -> str:
        return "(via Email)"


class Notificator:

    def __init__(self, channel: AbstractChannel):
        self.channel = channel

    def get_channel(self) -> str:
        return self.channel

    def notify(self, notification: str):
        print(notification, self.get_channel().get_channel_message(), sep="\n")

notificator_sms = Notificator(SMSChannel())
notificator_push = Notificator(PUSHChannel())
notificator_email = Notificator(EmailChannel())

notificator_email.notify("This is a notification")
notificator_push.notify("This is a notification")
notificator_sms.notify("This is a notification")