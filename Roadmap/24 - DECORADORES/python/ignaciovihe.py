"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""
import time

# Decorador para medir el tiempo de ejecución de la funcion que decore.
def measure_time(funcion):                  # Se crea una funcion externa a la que le pasamos la funcion.  
    def wrapper(*args, **kwargs):      # Definimos una nueva fucnion que sera la que sustituya a la original, añadiendo nueva fucnionalidad. Aqui pasamos los parametros.
        inicio = time.perf_counter()
        funcion(*args, **kwargs)            # dentro llamamos a la funcion.
        fin = time.perf_counter()  
        print(f"\nTiempo total de ejecución de la funcion '{funcion.__name__}': {fin - inicio:.10f} segundos")
    return wrapper                     # retornamos la nueva funcion

@measure_time                               # Con esto le decimos que hay una funcion decaradora. Para entenderlo facil: cambia la funcion que decora por la interna del decorador.
def saludar(name):                          # la cual contiene la funcion que se la pasamos como parametro.
    print(f"hola {name}")

@measure_time                               # podemos decorar varias funciones con el mismo decorador.
def sumar(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

saludar("Pedro")
sumar(4, 8)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""

def count_calls(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        wrapper.counter += 1
        print(f"La funcion {function.__name__} se ha llamado {wrapper.counter} veces.")
    wrapper.counter = 0
    return wrapper

@count_calls
def saludar(name):
    print(f"hola {name}")

@count_calls                               
def sumar(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

saludar("Ignacio")
saludar("Lorena")
sumar(2,8)
sumar(2,8)
saludar("Pedro")


"""
Estudio extra patrón decorator con clases (https://refactoring.guru/)
"""
print("-------------------decorador con clases----------------------")

class Notificador:
    def enviar(self, mensaje: str):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando notificación por correo: {mensaje}")


class NotificadorDecorator(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    @property
    def notificador(self) -> Notificador:
        return self._notificador

    def enviar(self, mensaje: str):
        self._notificador.enviar(mensaje)

class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensaje: str):
        self.notificador.enviar(mensaje)
        print(f"Enviando notificación por SMS: {mensaje}")


class NotificadorSlack(NotificadorDecorator):
    def enviar(self, mensaje: str):
        self.notificador.enviar(mensaje)
        print(f"Enviando notificación por Slack: {mensaje}")


if __name__ == "__main__":
    notificador_base = NotificadorEmail()
    
    notificador_con_sms = NotificadorSMS(notificador_base)
    notificador_con_slack_y_sms = NotificadorSlack(notificador_con_sms)

    notificador_con_slack_y_sms.enviar("¡Hola! Esto es un mensaje importante.")

