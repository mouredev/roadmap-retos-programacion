# EJERCICIO:
# Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
# y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.
from abc import ABC, abstractmethod

# Incorrecto:
class SistemaNotificaciones:
    def enviar_notificaciones(self, tipo, mensaje):
        if tipo == "email":
            print(f"Enviando notificacion por email: {mensaje}")
        elif tipo == "sms":
            print(f"Enviando notificacion por sms: {mensaje}")
        # Si quiero agregar whatsapp, tendria que agregar un elif para whatsapp
        # estaria modificando y no extendiendo la clase
    
# Correcto:
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando notificacion por email: {mensaje}")
class NotificadorSms(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando notificacion por sms: {mensaje}")

# Aqui extendi sin modificar el codigo existente
class NotificadorWhatsapp(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando notificacion por whatsapp: {mensaje}")


# uso
def notificar_usuario(notificador: Notificador, mensaje: str):
    notificador.enviar(mensaje)



notificar_usuario(NotificadorEmail(), "Hola, este es un mensaje de prueba")
notificar_usuario(NotificadorSms(), "Hola, este es un mensaje de prueba")
notificar_usuario(NotificadorWhatsapp(), "Hola, este es un mensaje de prueba")


#
# DIFICULTAD EXTRA (opcional):
# Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
# Requisitos:
# - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
# Instrucciones:
# 1. Implementa las operaciones de suma, resta, multiplicación y división.
# 2. Comprueba que el sistema funciona.
# 3. Agrega una quinta operación para calcular potencias.
# 4. Comprueba que se cumple el OCP.

class Operacion:
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b
class Resta(Operacion):
    def calcular(self, a, b):
        return a - b
class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b
class Division(Operacion):
    def calcular(self, a, b):
        return a / b



class Calculadora:
    operaciones = []
    def calcular(self, operacion, a, b):
        return operacion.calcular(a, b)
    def agregar_operacion(self, operacion):
        self.operaciones.append(operacion)
# Uso
print("------------- DIFICULTAD EXTRA ----------------")
calc = Calculadora()
calc.agregar_operacion(Suma())
calc.agregar_operacion(Resta())
calc.agregar_operacion(Multiplicacion())
calc.agregar_operacion(Division())
print("Resultado de la suma: ", calc.calcular(Suma(), 1, 2))
print("Resultado de la resta: ", calc.calcular(Resta(), 1, 2))
print("Resultado de la multiplicacion: ", calc.calcular(Multiplicacion(), 1, 2))
print("Resultado de la division: ", calc.calcular(Division(), 1, 2))

# Aqui extendi sin modificar el codigo existente
class Potencia(Operacion):
    def calcular(self, a, b):
        return a**b
        
        
calc.agregar_operacion(Potencia())
print("Resultado de la potencia: ", calc.calcular(Potencia(), 1, 2))