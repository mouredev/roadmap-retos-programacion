import random
import time

# ------ Ejercicio

def say_hello_callback(name: str, callback):
    print("Imprimiendo Callback...")
    time.sleep(1)
    callback(name)


def my_callback(name: str):
    print(f"Hola, soy un Callback y me llamo: '{name}'")


say_hello_callback("callback1", my_callback)


# ------ Extra

def procesar_pedido(nombre_plato, callback_confirmacion, callback_listo, callback_entrega):
    callback_confirmacion(nombre_plato)
    tiempo_preparacion = random.randint(1, 10)
    time.sleep(tiempo_preparacion)

    callback_listo(nombre_plato)

    tiempo_entrega = random.randint(1, 10)
    time.sleep(tiempo_entrega)

    callback_entrega(nombre_plato)

def confirmar_pedido(nombre_plato):
    print(f"Pedido confirmado: {nombre_plato}.")

def plato_listo(nombre_plato):
    print(f"El plato '{nombre_plato}' está listo para ser servido.")

def entregar_pedido(nombre_plato):
    print(f"El plato '{nombre_plato}' ha sido entregado al cliente.")


procesar_pedido("Spaghetti Carbonara", confirmar_pedido, plato_listo, entregar_pedido)
