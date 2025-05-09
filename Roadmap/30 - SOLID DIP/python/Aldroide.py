"""
    Explora el principio SOLID fde Inversión de Dependencias(Dependency Inversion
    Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
    de forma correcta e incorrecta.
"""

# Forma Sin DIP


from abc import ABC, abstractmethod


class Switch:
    def turn_on(self):
        print("Enciende la lampara")

    def turn_off(self):
        print("Apaga la lampara")


class Lamp:
    def __init__(self) -> None:
        self.switch = Switch()

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()


lamp = Lamp()
lamp.operate("on")
lamp.operate("off")

# Con DIP


class AbstractSwitch:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class LampSwitch(AbstractSwitch):

    def turn_on(self):
        print("Enciende la lampara")

    def turn_off(self):
        print("Apaga la lampara")


class Lamp:

    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()


lamp = Lamp(LampSwitch())
lamp.operate("on")
lamp.operate("off")


"""
Extra
"""


class Notifier(ABC):

    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando email con texto: {message}")


class PUSHNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando Push con texto: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS con texto: {message}")


class NotificationService:

    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)


service = NotificationService(EmailNotifier())
service.notify("hola notificador")
service = NotificationService(PUSHNotifier())
service.notify("hola notificador")
service = NotificationService(SMSNotifier())
service.notify("hola notificador")
