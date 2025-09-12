"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
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
"""


def greeting(user: str, callback):
    print("This is the greeting process...")
    callback(user)


def greet_user(user: str):
    print(f"Welcome {user}!")


greeting("nlarrea", greet_user)


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
"""


from random import randint
import time


def order_process(
    dish: str, confirm_callback, ready_callback, delivered_callback
):
    confirm_callback(dish)
    time.sleep(randint(1, 5))
    ready_callback(dish)
    time.sleep(randint(1, 5))
    delivered_callback(dish)


def order_confirmation(dish: str):
    print(f"The order '{dish}' is confirmed.")


def order_ready(dish: str):
    print(f"The order '{dish}' is ready.")


def order_delivered(dish: str):
    print(f"The order '{dish}' has been delivered.")


order_process(
    "Tonkotsu Ramen", order_confirmation, order_ready, order_delivered
)
