#30 - Python
# EJERCICIO:
# Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
# Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
# de forma correcta e incorrecta.
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
# 

class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

contador = iter(Counter())

def separacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena} {'-.-' * 20}')

from abc import ABC, abstractmethod

#-----Incorrecto-----
separacion('Incorrecto fundamento')

class SwitchA:

    def turn_on(self)    :
        print("Enciende la lámpara.")

    def turn_off(self):
        print("Apaga la lámpara.")

class LampA:

    def __init__(self) -> None:
        self.switchA = SwitchA()

    def operate(self, command):
        if command == "on":
            self.switchA.turn_on()
        elif command == "off":
            self.switchA.turn_off()

lamp = LampA()
lamp.operate("on")
lamp.operate("off")
lamp.operate("True")

#-----Correcto-----
separacion('Correcto fundamento')

class AbstractSwtich:

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LampSwitch(AbstractSwtich):

    def turn_on(self):
        print("Enciende la lámpara.")
    
    def turn_off(self):
        print("Apaga la lámpara.")

class TVSwitch(AbstractSwtich):

    def turn_on(self):
        print("Enciende la TV.")
    
    def turn_off(self):
        print("Apaga la TV.")

class OnOff:

    def __init__(self, switch: AbstractSwtich) -> None:
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp = OnOff(LampSwitch())
lamp.operate("on")
lamp.operate("off")
lamp.operate("True")
television = OnOff(TVSwitch())
television.operate("on")
television.operate("off")

#-----EXTRA-----
separacion('EXTRA')

# Crea un sistema de notificaciones.
# Requisitos:
# 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
# 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
# Instrucciones:
# 1. Crea la interfaz o clase abstracta.
# 2. Desarrolla las implementaciones específicas.
# 3. Crea el sistema de notificaciones usando el DIP.
# 4. Desarrolla un código que compruebe que se cumple el principio.

class AbstractNotification:
    
    def send_notification(self):
        pass

class EmailNofified(AbstractNotification):
    
    def send_notification(self):
        print('Notificación enviada al e-mail del usuario.')

class SmsNotified(AbstractNotification):

    def send_notification(self):
        print('Notificación enviada por SMS al usuario.')

class PushNotified(AbstractNotification):

    def send_notification(self):
        print('Notificado al usuario mediante el explorador.')

class Notified:

    def __init__(self, notified_method: AbstractNotification) -> None:
        self.notified_method = notified_method

    def send_notification(self):
        self.notified_method.send_notification()

email = Notified(EmailNofified())
sms = Notified(SmsNotified())
push = Notified(PushNotified())

def test_send_notified(notified_type):
    notified_type.send_notification()

test_send_notified(email)
test_send_notified(sms)
test_send_notified(push)
