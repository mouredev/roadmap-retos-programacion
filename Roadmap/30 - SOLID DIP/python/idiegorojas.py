"""
# 30 - Prinicipio SOLID: Inversion de dependencias.
"""
# Lo modulos de alto nivel no deben depender de los modulos de bajo nivel. Ambos deben depender de abstracciones
# Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.
# Debemos programar hacia interfaces o clases abstractas en lugar de implementaciones concretas. 

"""
Beneficios
"""
# Desacoplamiento: Las clases de alto nivel no dependen de las implementaciones específicas.
# Flexibilidad: Facilita cambiar implementaciones sin modificar código existente.
# Facilita pruebas unitarias: Permite usar mocks o stubs para las dependencias.
# Mejor diseño: Fomenta pensar en términos de interfaces y comportamientos, no implementaciones.


"""
Ejemplo de violacion del principio
"""
# Interruptor depende directamente de LuzConcreta
# Si queremos usar otro tipo de luz, tendríamos que modificar la clase Interruptor
# Es difícil realizar pruebas unitarias

class LuzPasillo:
    def encender(self):
        print("Luz encendida")

    def apagar(self):
        print('Luz apagada')

class Interruptor:
    def __init__(self):
        self.luz = LuzPasillo()

    def operar(self):
        self.luz.encender()


"""
Ejemplo aplicando el principio
"""
from abc import ABC, abstractmethod

class DispositivoElectronico(ABC):
    @abstractmethod
    def encender(self):
        pass

    def apagar(self):
        pass


class Luz(DispositivoElectronico):
    def encender(self):
        print('Luz encendida.')

    def apagar(self):
        print('Luz apagada')


class Ventilador(DispositivoElectronico):
    def encender(self):
        print('Ventilador encendido')

    def apagar(self):
        print('Ventilador apagado')


class Interruptor:
    def __init__(self, dispositivo: DispositivoElectronico):
        self.dispositivo = dispositivo

    def operar(self, encender=True):
        if encender:
            self.dispositivo.encender()
        else:
            self.dispositivo.apagar()

luz = Luz()
ventilador = Ventilador()

interruptor_luz = Interruptor(luz)
interruptor_ventilador = Interruptor(ventilador)

interruptor_luz.operar(encender=True)
interruptor_luz.operar(encender=False)
interruptor_ventilador.operar(encender=True)


"""
Extra
"""
from abc import ABC, abstractmethod

class Notificar(ABC):
    @abstractmethod
    def enviar_notificacion(self):
        pass

    @abstractmethod    
    def cancelar_notificacion(self):
        pass


class Email(Notificar):
    def enviar_notificacion(self):
        print('Se ha enviado el email.')

    def cancelar_notificacion(self):
        print('Se ha cancelado el email.')

class Push(Notificar):
    def enviar_notificacion(self):
        print('Se ha enviado el Push.')

    def cancelar_notificacion(self):
        print('Se ha cancelado el Push.')

class Sms(Notificar):
    def enviar_notificacion(self):
        print('Se ha enviado el SMS.')

    def cancelar_notificacion(self):
        print('Se ha cancelado el SMS.')


class SistemaNotificaciones:
    def __init__(self, notificacion: Notificar):
        self.notificacion = notificacion

    def procesar_notificacion(self, enviar=True):
        if enviar:
            self.notificacion.enviar_notificacion()
        else:
            self.notificacion.cancelar_notificacion()


email = Email()
push = Push()
sms = Sms()

enviar_email = SistemaNotificaciones(email)
enviar_push = SistemaNotificaciones(push)
enviar_sms = SistemaNotificaciones(sms)

enviar_email.procesar_notificacion(enviar=True)
enviar_email.procesar_notificacion(enviar=False)
enviar_push.procesar_notificacion(enviar=True)
enviar_push.procesar_notificacion(enviar=False)
enviar_sms.procesar_notificacion(enviar=True)
enviar_sms.procesar_notificacion(enviar=False)