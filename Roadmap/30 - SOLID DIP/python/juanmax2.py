"""
Ejercicio

"""


# Incorrecto

class Switch:
    
    def encender(self):
        print("Enciende la lámpara")
        
    def apagar(self):
        print("Apaga la lámpara")

class Lampara:
    
    def __init__(self):
        self.switch = Switch()
        
    def operate(self, command):
        if command == "on":
            self.switch.encender()
        elif command == "off":
            self.switch.apagar()

lampara = Lampara()

lampara.operate("on")
lampara.operate("off")

# Correcto

class AbstractSwitch:
    
    def encender(self):
        pass
        
    def apagar(self):
        pass

class LampSwitch(AbstractSwitch):
    
    def encender(self):
        print("Enciende la lámpara")
        
    def apagar(self):
        print("Apaga la lámpara")
    
class Lampara:
    
    def __init__(self, switch : AbstractSwitch):
        self.switch = switch
        
    def operate(self, command):
        if command == "on":
            self.switch.encender()
        elif command == "off":
            self.switch.apagar()

lampara = Lampara(LampSwitch())

lampara.operate("on")
lampara.operate("off")



"""

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

from abc import ABC, abstractmethod

class Notificador(ABC):
    
    @abstractmethod
    def send(self, mensaje : str):
        pass

class Email(Notificador):
    
    def send(self, mensaje):
        print(f"Enviando email con mensaje {mensaje}")

class Push(Notificador):
    
    def send(self, mensaje):
        print(f"Enviando push con mensaje {mensaje}")
        
class SMS(Notificador):
    
    def send(self, mensaje):
        print(f"Enviando SMS con mensaje {mensaje}")
        

class ServicioNotificacion:
    
    def __init__(self, notificador = Notificador):
        self.notificador = notificador
    
    def notificar(self, mensaje : str):
        self.notificador.send(mensaje)
    
servicio = ServicioNotificacion(Email())
servicio.notificar("Juanma")
servicio_1 = ServicioNotificacion(Push())
servicio_1.notificar("González")
servicio_2 = ServicioNotificacion(SMS())
servicio_2.notificar("Espinosa")