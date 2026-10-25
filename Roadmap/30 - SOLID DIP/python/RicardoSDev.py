'''
 Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
* Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
* de forma correcta e incorrecta.
'''
# Sin DIP

class Interruptor:

    def Enciende(self):
        print("Enciende la lampara")
    def Apaga(self):
        print("Apaga la lampara")

class Lampara(Interruptor):

    def Enciende(self):
        return super().Enciende()
    def Apaga(self):
        return super().Apaga()

Bombilla = Lampara()
Bombilla.Enciende()
Bombilla.Apaga()

# Sin DIP

class Interruptor:

    def Enciende(self):
        print("Enciende la lampara")
    def Apaga(self):
        print("Apaga la lampara")

class Lampara:

    def __init__(self):
        self.interruptor = Interruptor()

    def operacion(self, operacion):
        if operacion == "on":
            self.interruptor.Enciende()
        if operacion == "off":
            self.interruptor.Apaga()        

Bombilla = Lampara()
Bombilla.operacion("on")
Bombilla.operacion("off")

# Con DIP

class InterruptorAbstracto:
    
    def Enciende(self):
        pass
    def Apaga(self):
        pass

class InterruptorDeLampara(InterruptorAbstracto):

    def Enciende(self):
        print("Lampara encendida")
    def Apaga(self):
        print("Lampara apagada")

class InterruptorDeTV(InterruptorAbstracto):

    def Enciende(self):
        print ("Tele encendida")
    def Apaga(self):
        print ("Tele apagada")

class Aparato:

    def __init__(self, interruptor:InterruptorAbstracto):
        self.interruptor = interruptor

    def operacion(self, operacion):
        if operacion == "on":
            self.interruptor.Enciende(self)
        if operacion == "off":
            self.interruptor.Apaga(self)                  

Bombilla = Aparato(InterruptorDeLampara)
Bombilla.operacion("on")
Bombilla.operacion("off")
Television = Aparato(InterruptorDeTV)
Television.operacion("on")
Television.operacion("off")


'''
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
'''

class Notificador:
    def envia(self, mensaje):
        pass

class NoficaEmail(Notificador):
    def envia(self, mensaje):
        print(f"Email enviado con el mensaje {mensaje}")

class NotificaPUSH(Notificador):
    def envia(self, mensaje):
        print(f"Notificacion PUSH {mensaje} enviada")

class NotificaSMS(Notificador):
    def envia(self, mensaje):
        print(f"{mensaje} enviado como SMS")


class Servicio:
    def __init__(self, notificacion:Notificador):
        self.notificacion = notificacion

    def notifica(self, mensaje):
        self.notificacion.envia(mensaje)

def prueba_servicio(mensaje="Mensaje de prueba"):
    email = Servicio(NoficaEmail())
    PUSH = Servicio(NotificaPUSH())
    SMS = Servicio(NotificaSMS())

    email.notifica(mensaje)
    PUSH.notifica(mensaje)
    SMS.notifica(mensaje)            

prueba_servicio()