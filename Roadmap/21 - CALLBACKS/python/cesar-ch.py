"""
    * 20 PETICIONES HTTP 
"""


def greet(name, callback):
    print(f"Hello, {name}!")
    callback()


def say_goodbye():
    print("Goodbye!")


greet("Mouredev", say_goodbye)


"""
    * DIFICULTAD EXTRA
"""
import time
import random


def procesar_pedido(plato, confirmacion_callback, listo_callback, entrega_callback):
    print(f"Procesando pedido para: {plato}")
    confirmacion_callback(plato)

    tiempo_preparacion = random.randint(1, 10)
    print("El tiempo de preparacion es: " + str(tiempo_preparacion))
    time.sleep(tiempo_preparacion)
    listo_callback(plato)

    tiempo_entrega = random.randint(1, 10)
    print("El tiempo de entrega es: " + str(tiempo_entrega))
    time.sleep(tiempo_entrega)
    entrega_callback(plato)


def confirmar_pedido(plato):
    print(f"Pedido confirmado para: {plato}")


def plato_listo(plato):
    print(f"El plato {plato} está listo para ser entregado.")


def entregar_pedido(plato):
    print(f"El plato {plato} ha sido entregado.")


if __name__ == "__main__":
    procesar_pedido("Pizza", confirmar_pedido, plato_listo, entregar_pedido)
