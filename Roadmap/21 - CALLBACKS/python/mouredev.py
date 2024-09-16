import random
import time
import threading

"""
Ejercicio
"""


def greeting_process(name: str, callback):
    print("Ejecutando el proceso de saludo...")
    callback(name)


def greet_callback(name: str):
    print(f"Hola, {name}!")


greeting_process("Brais", greet_callback)

"""
Extra
"""


def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    def process():
        confirm_callback(dish_name)
        time.sleep(random.randint(1, 10))
        ready_callback(dish_name)
        time.sleep(random.randint(1, 10))
        delivered_callback(dish_name)

    threading.Thread(target=process).start()


def confirm_order(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido confirmado.")


def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name} está listo.")


def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado.")


order_process("Pizza Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza 4 Quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Margarita", confirm_order, order_ready, order_delivered)
order_process("Pizza con Piña", confirm_order, order_ready, order_delivered)
