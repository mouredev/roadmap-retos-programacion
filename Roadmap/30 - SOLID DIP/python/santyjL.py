#30 SOLID: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)


"""
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
"""

from abc import ABC, abstractmethod


class SaludoIngles:
    def generar_saludo(self):
        return "Hello!"

class Saludador:
    def __init__(self):
        self.saludo = SaludoIngles()  # Dependencia concreta

    def saludar(self):
        print(self.saludo.generar_saludo())

# Uso
saludador = Saludador()
saludador.saludar()

# Definimos una interfaz o clase abstracta
class Saludo(ABC):
    @abstractmethod
    def generar_saludo(self):
        pass

# Implementación concreta en inglés
class SaludoIngles(Saludo):
    def generar_saludo(self):
        return "Hello!"

# Implementación concreta en español
class SaludoEspanol(Saludo):
    def generar_saludo(self):
        return "¡Hola!"

# Clase que sigue el IDP
class Saludador:
    def __init__(self, saludo: Saludo):  # Dependencia abstracta
        self.saludo = saludo

    def saludar(self):
        print(self.saludo.generar_saludo())

# Uso con diferentes saludos
saludador_ingles = Saludador(SaludoIngles())
saludador_espanol = Saludador(SaludoEspanol())

saludador_ingles.saludar()  # "Hello!"
saludador_espanol.saludar()  # "¡Hola!"


# Extra
class Notificador(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje: str):
        pass

class Email(Notificador):
    def enviar_notificacion(self, mensaje: str):
        print("Se envió el mensaje por Email: ", mensaje)

class Push(Notificador):
    def enviar_notificacion(self, mensaje: str):
        print("Se envió el mensaje por Push: ", mensaje)

class SMS(Notificador):
    def enviar_notificacion(self, mensaje: str):
        print("Se envió el mensaje por SMS: ", mensaje)

class SistemaNotificador:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def enviar(self, mensaje: str):
        self.notificador.enviar_notificacion(mensaje)

# Ejemplo de uso
notificador_sms = SistemaNotificador(SMS())
notificador_push = SistemaNotificador(Push())
notificador_email = SistemaNotificador(Email())

notificador_sms.enviar("Hola mundo")
notificador_push.enviar("Hola mundo")
notificador_email.enviar("Hola mundo")
