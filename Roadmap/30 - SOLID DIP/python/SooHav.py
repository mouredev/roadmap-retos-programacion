# 30 SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)

# siguiendo los principios SOLID con los patos .....

# Ejemplo Pato
from abc import ABC, abstractmethod


class Pato (ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def vuela(self):
        pass

    @abstractmethod
    def nada(self):
        pass

    @abstractmethod
    def dice(self):
        pass


class PatoSalvaje(Pato):
    def __init__(self):
        super().__init__("salvaje")

    def vuela(self):
        print("El pato salvaje vuela.")

    def nada(self):
        print("El pato salvaje nada.")

    def dice(self):
        print("El pato salvaje dice Quack.")


class PatoDomestico(Pato):
    def __init__(self):
        super().__init__("domestico")

    def vuela(self):
        print("El pato doméstico vuela.")

    def nada(self):
        print("El pato doméstico nada.")

    def dice(self):
        print("El pato doméstico dice Quack.")


class PatoPlastico(Pato):
    def __init__(self):
        super().__init__("plastico")

    def vuela(self):
        print("El pato de plástico no puede volar.")

    def nada(self):
        print("El pato de plástico no puede nadar.")

    def dice(self):
        print("El pato de plástico dice Squeak.")


# Uso
print("Sin DIP:\n")
pato1 = PatoSalvaje()
pato2 = PatoDomestico()
pato3 = PatoPlastico()

pato1.vuela()
pato1.nada()
pato1.dice()

pato2.vuela()
pato2.nada()
pato2.dice()

pato3.vuela()
pato3.nada()
pato3.dice()
print("\n")
# Ejemplo Pato con DIP
# clases abstractas con acciones que puede hacer un pato


class Volador(ABC):
    @abstractmethod
    def vuela(self):
        pass


class Nadador(ABC):
    @abstractmethod
    def nada(self):
        pass


class Hablador(ABC):
    @abstractmethod
    def dice(self):
        pass


class Flotador(ABC):
    @abstractmethod
    def flota(self):
        pass


class Tipo(ABC):
    @abstractmethod
    def tipo(self):
        pass

# Implementaciones concretas de las acciones de los patos


class VuelaConAlas(Volador):
    def vuela(self):
        print("Vuela con alas.")


class NadaEnLago(Nadador):
    def nada(self):
        print("Nada en el lago.")


class DiceQuack(Hablador):
    def dice(self):
        print("Dice Quack.")


class DiceQuick(Hablador):
    def dice(self):
        print("Dice Quick.")


class FlotaEnBañadera(Flotador):
    def flota(self):
        print("Flota en la bañadera.")


class TipoPato(Tipo):
    def __init__(self, tipo):
        self._tipo = tipo

    def tipo(self):
        print(f"Es un {self._tipo}.")

# Implementación en las distintas clases de patos


class PatoSalvaje:
    def __init__(self, tipo: Tipo, volador: Volador, nadador: Nadador, hablador: Hablador):
        self._tipo = tipo
        self.volador = volador
        self.nadador = nadador
        self.hablador = hablador

    def tipo(self):
        self._tipo.tipo()

    def vuela(self):
        self.volador.vuela()

    def nada(self):
        self.nadador.nada()

    def dice(self):
        self.hablador.dice()


class PatoDomestico:
    def __init__(self, tipo: Tipo, nadador: Nadador, hablador: Hablador):
        self._tipo = tipo
        self.nadador = nadador
        self.hablador = hablador

    def tipo(self):
        self._tipo.tipo()

    def nada(self):
        self.nadador.nada()

    def dice(self):
        self.hablador.dice()


class PatoPlastico:
    def __init__(self, tipo: Tipo, hablador: Hablador, flotador: Flotador):
        self._tipo = tipo
        self.hablador = hablador
        self.flotador = flotador

    def tipo(self):
        self._tipo.tipo()

    def dice(self):
        self.hablador.dice()

    def flota(self):
        self.flotador.flota()


# Uso
print("Con DIP:\n")
vuela_con_alas = VuelaConAlas()
nada_en_lago = NadaEnLago()
dice_quack = DiceQuack()
dice_quick = DiceQuick()
flota_en_bañadera = FlotaEnBañadera()

tipo_salvaje = TipoPato("Pato Salvaje")
tipo_domestico = TipoPato("Pato Domestico")
tipo_plastico = TipoPato("Pato de Plastico")

pato4 = PatoSalvaje(tipo_salvaje, vuela_con_alas, nada_en_lago, dice_quack)
pato5 = PatoDomestico(tipo_domestico, nada_en_lago, dice_quack)
pato6 = PatoPlastico(tipo_plastico, dice_quick, flota_en_bañadera)

pato4.tipo()
pato4.vuela()
pato4.nada()
pato4.dice()

pato5.tipo()
pato5.nada()
pato5.dice()

pato6.tipo()
pato6.dice()
pato6.flota()
print("\n")
# Dificultad Extra
# Clase notificación


class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

# Implementaciones concretas de tipos de notificaciones


class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando Email: {mensaje}")


class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando Notificación Push: {mensaje}")


class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")

# Sistema para las notificaciones


class Sistema_Notificacion:
    def __init__(self, notificador: Notificacion):
        self.notificador = notificador

    def notificar(self, mensaje: str):
        self.notificador.enviar(mensaje)


# Uso
print("Dificultad Extra:\n")
notificacion_email = NotificacionEmail()
notificacion_push = NotificacionPush()
notificacion_sms = NotificacionSMS()

envio1 = Sistema_Notificacion(notificacion_email)
envio2 = Sistema_Notificacion(notificacion_push)
envio3 = Sistema_Notificacion(notificacion_sms)

envio1.notificar("Hola este es un correo electrónico")
envio2.notificar("Hola este es un push")
envio3.notificar("Hola este es un sms")
