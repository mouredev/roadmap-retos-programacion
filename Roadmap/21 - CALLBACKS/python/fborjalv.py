import time
import random
import threading

"""
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""
def saludar(name):
    print(f"¿Cómo estás? {name}")

def ejecutar_callback(name, callback):
    print("Este saludo es está ejecutando desde una callback: ")
    callback(name)

saludar("Borja")

ejecutar_callback("Mouredev", saludar)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */

"""


def order_process(dish, confirm, ready, delivering):
    def process():
        print(f"Hemos recibido su pedido que incluye {dish}")
        time.sleep(random.randint(1, 10))
        confirm(dish)
        ready(dish)
        delivering(dish)
    threading.Thread(target=process).start()

def confirm_callback(dish):
    print(f"Su pedido que incluye {dish} se está procesando")
    time.sleep(random.randint(1, 10))

def ready_callback(dish):
    print(f"Su pedido que incluye {dish} está listo. Se entregará en los próximos minutos")
    time.sleep(random.randint(1, 10))

def deliver_callback(dish):
    print(f"Su pedido que incluye {dish} ha sido entregado correctamente")


order_process("gambas", confirm_callback, ready_callback, deliver_callback)
order_process("ternera", confirm_callback, ready_callback, deliver_callback)
order_process("mouse", confirm_callback, ready_callback, deliver_callback)