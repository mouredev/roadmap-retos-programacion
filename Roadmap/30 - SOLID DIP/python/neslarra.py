"""
 EJERCICIO:
 Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
 de forma correcta e incorrecta.

 DIFICULTAD EXTRA (opcional):
 Crea un sistema de notificaciones.
 Requisitos:
 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 Instrucciones:
 1. Crea la interfaz o clase abstracta.
 2. Desarrolla las implementaciones específicas.
 3. Crea el sistema de notificaciones usando el DIP.
 4. Desarrolla un código que compruebe que se cumple el principio.
"""
from abc import ABC, abstractmethod

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Para entender fácilmente los 5 ppios SOLID recomiendo leer:

    https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/

en donde se explican de manera ordenada uno por uno, de manera sencilla y ejemplificada de manera progresiva (de hecho, de ahí
voy a tomar el ejemplo).

El quinto ppio SOLID es el ppio de inverción de dependencia (Dependency Inversion Principle) y establece que las clases abstractas no
deben depender de los detalles de las clases que las implementan y, a su vez, las clases de alto nivel no deberían depender de las de 
bajo nivel, sino que ambas edben depender de abstracciones. 

Retomando el ejemplo, tenemos la clase Communicator definiendo un "channel". Pero este canal es un detalle de implementación, el cual,
además, si debiera modificarse, estaría incumpliendo los ppios de responsabilidad única y abierto-cerrado.

Para corregir esta situación, separamos "channel" en su propia clase abstracta y, cuando Communicator la necesite, lo hará a través
de otra clase abstracta que le inyecte la clase edl canal.

De esta menera, la clase Communicator ya no depende de los detalles del canal puesto que ahora va a recibir a su clase abstracta, cuyos 
detalles solo se definiran cuando se implemente.

Integramos todo y resulta:

    from abc import ABC, abstractmethod
    from typing import final
    
    
    class Bird(ABC):
    
        def __init__(self, name):
            self.name = name
    
        @abstractmethod
        def do_sound(self) -> str:
            pass
    
    
    class FlyingBird(Bird):
    
        @abstractmethod
        def fly(self):
            pass
    
    
    class SwimmingBird(Bird):
    
        @abstractmethod
        def swim(self):
            pass
    
    
    class AbstractConversation:
    
        def do_conversation(self) -> list:
            pass
    
    
    class Conversation(AbstractConversation):
    
        def __init__(self, bird1: Bird, bird2: Bird):
            self.bird1 = bird1
            self.bird2 = bird2
    
        def do_conversation(self) -> list:
            sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, Hola {self.bird2.name}. ¿Cómo va?"
            sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, Todo bien {self.bird1.name} ¿Y tú?"
            return [sentence1, sentence2]
    
    
    class AbstractChannel(ABC):
    
        def get_channel_message(self) -> str:
            pass
    
    
    class AbstractCommunicator(ABC):
    
        def get_channel(self) -> AbstractChannel:
            pass
    
        @final
        def communicate(self, conversation: AbstractConversation):
            print(*conversation.do_conversation(), self.get_channel().get_channel_message(), sep='\n')
    
    
    class Communicator(AbstractCommunicator):
    
        def __init__(self, channel: AbstractChannel):
            self._channel = channel
    
        def get_channel(self) -> AbstractChannel:
            return self._channel
    
    
    class Duck(SwimmingBird, FlyingBird):
    
        def fly(self):
            print(f"{self.name} is flying not very high")
    
        def swim(self):
            print(f"{self.name} swims in the lake and quacks")
    
        def do_sound(self) -> str:
            return "Quack"
    
    
    class SMSChannel(AbstractChannel):
        def get_channel_message(self) -> str:
            return "Sending via SMS"
    
    
    class EMAILChannel(AbstractChannel):
        def get_channel_message(self) -> str:
            return "Sending an email"
    
    
    lucas = Duck("Lucas")
    saturnino = Duck("Saturnino")
    
    sms = SMSChannel()
    email = EMAILChannel()
    
    comm1 = Communicator(sms)
    comm2 = Communicator(email)
    
    print(comm1.communicate(Conversation(lucas, saturnino)))
    print(comm2.communicate(Conversation(lucas, saturnino)))
    
    Lucas: Quack, Hola Saturnino. ¿Cómo va?
    Saturnino: Quack, Todo bien Lucas ¿Y tú?
    Sending via SMS
    
    Lucas: Quack, Hola Saturnino. ¿Cómo va?
    Saturnino: Quack, Todo bien Lucas ¿Y tú?
    Sending an email
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")


class AbstractNotificationQueue(ABC):

    @abstractmethod
    def enqueue(self, message: str):
        pass

    @abstractmethod
    def dequeue(self):
        pass


class AbstracChannel(ABC):

    @abstractmethod
    def __init__(self, channel: str):
        self.channel = channel

    @abstractmethod
    def send_method(self, target: str):
        pass


class Notification(AbstractNotificationQueue):

    def __init__(self):
        self.queue = []

    def enqueue(self, message: str):
        self.queue.append(message)

    def dequeue(self):
        return self.queue.pop(0)

    def queued_messages(self):
        return self.queue.__len__()


class SMSChannel(AbstracChannel):

    def __init__(self, channel: str):
        super().__init__(channel)

    def send_method(self, target: str):
        return f"Sending via {self.channel} to {target}"


class EmailChannel(AbstracChannel):

    def __init__(self, channel: str):
        super().__init__(channel)

    def send_method(self, target: str):
        return f"Sending via {self.channel} to {target}"


class PushChannel(AbstracChannel):

    def __init__(self, channel: str):
        super().__init__(channel)

    def send_method(self, target: str):
        return f"Sending via {self.channel} to {target}"


class SendNotificacion:

    def __init__(self, notification: Notification, channel: AbstracChannel, target: str):

        self.notification = notification
        self.channel = channel
        self.target = target

    def send_notification(self):
        if self.notification.queued_messages():
            print(f"{self.channel.send_method(self.target)} => {self.notification.dequeue()}")
        else:
            print(f"{self.channel.__class__.__name__} NO encontró mensajes para enviar")


facebook = PushChannel("FaceBook")
whatsapp = PushChannel("WhatsApp")
celu = SMSChannel("SMS")
compu = EmailChannel("Gmail")

mis_mensajes = ["Solicitud de amistad", "Avisale al jefe que llego tarde", "Mirá whatsapp por favor",
                "Tenés una factura impaga", "Envió copia del documento solicitado", "No recibí la factura de este mes"]

notificaciones = Notification()
for msg in mis_mensajes:
    notificaciones.enqueue(msg)

envio_fcb = SendNotificacion(notificaciones, facebook, "Kathy Perry")
envio_fcb.send_notification()

envio_wsp = SendNotificacion(notificaciones, whatsapp, "Mi Compa")
envio_wsp.send_notification()

envio_celu = SendNotificacion(notificaciones, celu, "1234-5678")
envio_celu.send_notification()

envio_celu = SendNotificacion(notificaciones, celu, "1122-3344")
envio_celu.send_notification()

envio_compu = SendNotificacion(notificaciones, compu, "nuevo_curro@slavers.com")
envio_compu.send_notification()

envio_compu = SendNotificacion(notificaciones, compu, "servicio@el_gas.com")
envio_compu.send_notification()

envio_fcb.send_notification()
envio_wsp.send_notification()
envio_celu.send_notification()
envio_compu.send_notification()
