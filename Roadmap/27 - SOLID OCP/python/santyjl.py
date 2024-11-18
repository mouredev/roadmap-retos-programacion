#27 SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */
"""

class Usuario:
    def __init__(self, nombre, email=None, sms=None):
        self.nombre = nombre
        self.email = email
        self.sms = sms

class Notificar:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por una subclase.")

class NotificarEmail(Notificar):
    def notificar(self):
        if self.usuario.email:
            return f"Enviamos el mensaje: '{self.mensaje}' por Email a {self.usuario.email}"
        else:
            return "Este usuario no tiene email registrado."

class NotificarSMS(Notificar):
    def notificar(self):
        if self.usuario.sms:
            return f"Enviamos el mensaje: '{self.mensaje}' por SMS a {self.usuario.sms}"
        else:
            return "Este usuario no tiene número de SMS registrado."

# Ejemplo de uso:
usuario_uno = Usuario("Santiago", email="santiago@correo.com")
usuario_dos = Usuario("George", sms="123456789")

notificacion_uno = NotificarEmail(usuario_uno, "Los números amigos no sirven de nada.")
notificacion_dos = NotificarSMS(usuario_dos, "Enseñame a soldar.")

print(notificacion_uno.notificar())  # Correcto, tiene email
print(notificacion_dos.notificar())  # Correcto, tiene SMS

# Extra

class Calculadora:
    """
    Clase base para operaciones de cálculo.
    Esta clase debe ser heredada para implementar operaciones específicas.
    """

    def calcular(self, valores: list[float]) -> float:
        """
        Método que debe ser sobrescrito en las clases derivadas.

        :param valores: Lista de valores a operar.
        :return: Resultado de la operación.
        """
        raise NotImplementedError("Este método debe ser sobrescrito por una clase derivada.")

class Sumar(Calculadora):
    """
    Clase que implementa la operación de suma.
    """

    def calcular(self, valores: list[float]) -> float:

        return sum(valores)

class Resta(Calculadora):
    """
    Clase que implementa la operación de resta.
    """

    def calcular(self, valores: list[float]) -> float:

        resultado = valores[0]
        for valor in valores[1:]:
            resultado -= valor
        return resultado

class Multiplicar(Calculadora):
    """
    Clase que implementa la operación de multiplicación.
    """

    def calcular(self, valores: list[float]) -> float:

        resultado = 1
        for valor in valores:
            resultado *= valor
        return resultado

class Division(Calculadora):
    """
    Clase que implementa la operación de división.
    """

    def calcular(self, valores: list[float]) -> float:

        resultado = valores[0]
        for valor in valores[1:]:
            if valor == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado /= valor
        return resultado

class Potencia(Calculadora):
    """
    Clase que implementa la operación de potencia.
    """

    def calcular(self, valores: list[float]) -> float:

        resultado = valores[0]
        for valor in valores[1:]:
            resultado **= valor
        return resultado

# Ejemplo de uso

suma = Sumar()
resta = Resta()
multiplicacion = Multiplicar()
division = Division()
potencia = Potencia()

# Valores para operar
valores = [10, 2, 3]

# Realizar las operaciones y mostrar los resultados
print(f"Suma: {suma.calcular(valores)}")          # Suma: 15
print(f"Resta: {resta.calcular(valores)}")        # Resta: 5
print(f"Multiplicación: {multiplicacion.calcular(valores)}")  # Multiplicación: 60
print(f"División: {division.calcular([100, 2, 5])}")  # División: 10.0
print(f"Potencia: {potencia.calcular([2, 3, 2])}")    # Potencia: 64
