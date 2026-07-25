"""
28 - Principios SOLID: Sustitucion de Liskov
"""
# Si B es un subtipo de A, entonces los objetos de tipo T pueden ser reemplazados por objetos de tipo S
# Las subclases deben poder sustituir a sus clases base sin que el programa falle o se ocmporte de manera inesperada.

"""
Beneficios
"""
# Garantiza la interoperabilidad: Las subclases pueden utilizarse donde se espera una clase base.
# Mejora la robustez: Reduce errores inesperados cuando se extienden las clases.
# Facilita el testing: Las pruebas funcionan correctamente tanto con la clase base como con sus derivadas.
# Promueve un mejor diseño: Te obliga a pensar cuidadosamente en las relaciones entre clases.

"""
Ejemplo:
"""

from abc import ABC, abstractmethod
from typing import List, Optional

# Definimos interfaces separadas con contratos claros
class Notificador(ABC):
    @abstractmethod
    def enviar_notificacion_simple(self, destinatario: str, asunto: str, mensaje: str) -> bool:
        """Envía una notificación básica sin archivos"""
        pass

class NotificadorConAdjuntos(Notificador):
    @abstractmethod
    def enviar_con_adjuntos(self, destinatario: str, asunto: str, mensaje: str, archivos: List[str]) -> bool:
        """Envía una notificación con archivos adjuntos"""
        pass

# Implementaciones concretas
class NotificadorEmail(NotificadorConAdjuntos):
    def enviar_notificacion_simple(self, destinatario, asunto, mensaje):
        print(f"Email enviado a {destinatario}: {asunto}")
        return True
        
    def enviar_con_adjuntos(self, destinatario, asunto, mensaje, archivos):
        print(f"Email enviado a {destinatario}: {asunto}")
        print(f"  Con {len(archivos)} archivos adjuntos")
        return True

class NotificadorSMS(Notificador):
    def enviar_notificacion_simple(self, destinatario, asunto, mensaje):
        # Los SMS tienen límite de caracteres
        if len(mensaje) > 160:
            # En lugar de fallar, truncamos el mensaje
            mensaje = mensaje[:156] + "..."
        
        print(f"SMS enviado a {destinatario}: {mensaje[:20]}...")
        return True

class NotificadorPush(Notificador):
    def enviar_notificacion_simple(self, destinatario, asunto, mensaje):
        print(f"Notificación push enviada a {destinatario}")
        return True

# Código cliente adaptado a las capacidades de cada notificador
def enviar_alerta_seguridad(usuario, notificadores):
    mensaje_completo = "Se detectó un inicio de sesión desde una ubicación desconocida. Por favor verifica tu cuenta."
    
    for notificador in notificadores:
        if isinstance(notificador, NotificadorConAdjuntos):
            notificador.enviar_con_adjuntos(
                destinatario=usuario.contacto,
                asunto="Alerta de seguridad",
                mensaje=mensaje_completo,
                archivos=["mapa.png"]
            )
        else:
            notificador.enviar_notificacion_simple(
                destinatario=usuario.contacto,
                asunto="Alerta de seguridad",
                mensaje=mensaje_completo
            )
    
    print("Alertas de seguridad enviadas por todos los canales disponibles")

# Simulación de usuario
class Usuario:
    def __init__(self, contacto):
        self.contacto = contacto

# Uso del sistema
usuario = Usuario("usuario@email.com")

# Configuramos múltiples notificadores
notificadores = [
    NotificadorEmail(),
    NotificadorSMS(),
    NotificadorPush()
]

# Esto funciona para todos los notificadores
enviar_alerta_seguridad(usuario, notificadores)


print("----------------------------")


"""
Extra
"""
from abc import ABC, abstractmethod


class Motor(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass
    

class MotorGasolina:
    def acelerar(self):
        return "Motor de gasolina en movimiento"
    
    def frenar(self):
        return "Motor de gasolina deteniendose."


class MotorDisel:
    def acelerar(self):
        return "Motor de Disel en movimiento"
    
    def frenar(self):
        return "Motor de Disel deteniendose."


class MotorElectrico:
    def acelerar(self):
        return "Motor Electrico en movimiento"
    
    def frenar(self):
        return "Motor Electrico deteniendose."


class Vehiculo:
    def __init__(self, motor: Motor):
        self.motor = motor

    def iniciar_marcha(self):
        resultado = self.motor.acelerar()
        return f'Vehiculo en marcha: {resultado}'
    
    def detener_marcha(self):
        resultado = self.motor.frenar()
        return f'Vehiculo deteniendose: {resultado}'
    

coche_gasolina = Vehiculo(MotorGasolina())
coche_disel = Vehiculo(MotorDisel())
coche_electrico = Vehiculo(MotorElectrico())

# Avanzando
print(coche_gasolina.iniciar_marcha())
print(coche_disel .iniciar_marcha())
print(coche_electrico.iniciar_marcha())

# Deteniendose
print(coche_gasolina.detener_marcha())
print(coche_disel .detener_marcha())
print(coche_electrico.detener_marcha())