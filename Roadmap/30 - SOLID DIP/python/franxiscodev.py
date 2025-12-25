'''
SOLID - DIP
Principio SOLID de Inversión de Dependencias (Dependency Inversion Principle, DIP)
#
# El principio de inversión de dependencias establece que las clases de alto nivel no deben depender de las clases de bajo nivel. 
# Ambas deben depender de abstracciones (interfaces o clases abstractas). 
# Además, las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones.
 
'''
# Sin DIP
# el switch es una clase de bajo nivel y la bombilla es una clase de alto nivel
# la bombilla depende del switch, lo que significa que la bombilla no puede funcionar sin el switch


from abc import ABC, abstractmethod


class Switch:

    def turn_on(self):
        print("encender lámpara")

    def turn_off(self):
        print("apagar lámpara")


class Bulb:
    def __init__(self) -> None:
        self.switch = Switch()

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()
        else:
            print("comando no válido")


bulb = Bulb()
bulb.operate("on")
bulb.operate("off")
bulb.operate("office")

# con DIP


class AbstractSwitch:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class BulbSwitch(AbstractSwitch):
    def turn_on(self):
        print("encender lámpara dip")

    def turn_off(self):
        print("apagar lámpara dip")


class Bulb:
    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()
        else:
            print("comando no válido dip")


# la bombilla no depende del switch, sino de la abstracción AbstractSwitch
# y el switch puede ser cualquier clase que implemente la interfaz AbstractSwitch
# por lo que se puede cambiar el switch sin afectar a la bombilla
# y la bombilla puede funcionar sin el switch
bulb = Bulb(BulbSwitch())
bulb.operate("on")
bulb.operate("off")
bulb.operate("office")

# Extra


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando correo: {message}")


class PUSHNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando PUSH: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS: {message}")


class NotificationService:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)


service = NotificationService(EmailNotifier())
service.notify("Hola mundo x email")
service = NotificationService(PUSHNotifier())
service.notify("Hola mundo x PUSH")
service = NotificationService(SMSNotifier())
service.notify("Hola mundo x SMS")
