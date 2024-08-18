'''
/*
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
 */
'''

'''
EJERCICIO
'''

## SIN DIP
## Sistema muy acoplado

class Switch():

    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")

class Lamp():

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

## CON DIP

class AbstractSwitch():
    
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LampSwitch(AbstractSwitch):
    
    def turn_on(self):
        print("Enciende la lámpara")

    def turn_off(self):
        print("Apaga la lámpara")


class Lamp():

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

'''
DIFICULTAD EXTRA
'''


