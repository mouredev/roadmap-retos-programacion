from abc import ABC, abstractmethod


# Incorrecto
# Vehiculo esta dependiendo de otro modulo y no de una interfaz
"""
class Surtidor:
    def reponer_gasoleo(self):
        pass

    def reponer_gasolina(self):
        pass

    def reponer_queroseno(self):
        pass


class Vehiculo1:
    def __init__(self):
        self.combustible = Surtidor

    def mostrar_repostaje(self):
        repostaje = self.combustible()
        print(f"Respostando {repostaje}")


vehiculo1 = Vehiculo1()
vehiculo1.mostrar_repostaje()"""


# Correcto


class Combustible(ABC):
    @abstractmethod
    def reponer(self) -> str:
        pass


class SurtidorGasoleo(Combustible):
    def reponer(self) -> str:
        return "Gasoleo"


class SurtidorGasolina(Combustible):
    def reponer(self) -> str:
        return "Gasolina"


class SurtidorQueroseno(Combustible):
    def reponer(self) -> str:
        return "Queroseno"


class Vehiculo:
    """Clase de alto nivel - recibe cualquier combustible"""

    def __init__(self, combustible: Combustible):
        self.combustible = combustible

    def mostrar_repostaje(self):
        repostaje = self.combustible.reponer()
        print(f"Respostando {repostaje}")


vehiculo1 = Vehiculo(SurtidorGasoleo())
vehiculo1.mostrar_repostaje()

vehiculo2 = Vehiculo(SurtidorGasolina())
vehiculo2.mostrar_repostaje()

vehiculo3 = Vehiculo(SurtidorQueroseno())
vehiculo3.mostrar_repostaje()


"""
extra
"""


# Interfaz
class InterfazNotificaciones(ABC):
    """Interfaz general de la que dependeran las clases de alto y bajo nivel"""

    @abstractmethod
    def notificar(self) -> str:
        pass


# Modulos de bajo nivel
class Email(InterfazNotificaciones):
    """Solo se usa para mandar emails"""

    def notificar(self) -> str:
        return "Enviando Email"


class Push(InterfazNotificaciones):
    """Solo se usa para mandar notificaciones push"""

    def notificar(self) -> str:
        return "Enviando push"


class Sms(InterfazNotificaciones):
    """Solo se usa para mandar Sms"""

    def notificar(self) -> str:
        return "Enviando Sms"


# Modulo alto nivel
class Notificador:
    """Se encarga de mandar notificaciones, no de saber su tipo"""

    def __init__(self, notificacion: InterfazNotificaciones):
        self.notificacion = notificacion

    def ejecutar_notificacion(self) -> None:
        notificacion = self.notificacion.notificar()
        print(notificacion)


print("=== Sistema de Notificaciones ===\n")

notificador_email = Notificador(Email())
notificador_email.ejecutar_notificacion()
notificador_push = Notificador(Push())
notificador_push.ejecutar_notificacion()
notificador_sms = Notificador(Sms())
notificador_sms.ejecutar_notificacion()
