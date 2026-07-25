import random
from datetime import datetime as dt , UTC
from time import sleep as s

# EJERCICIO:
# Explora el concepto de callback en tu lenguaje creando un ejemplo
# simple (a tu elección) que muestre su funcionamiento.

def its_a_numbers(elem1: str, elem2: str, add: callable):
    try:
        elem1, elem2 = int(elem1), int(elem2)
        return add(elem1, elem2)
    except ValueError as e:
        return f"Error: {e}"
    
def add(num1: int, num2: int):
    return num1 + num2

# DIFICULTAD EXTRA (opcional):
# Crea un simulador de pedidos de un restaurante utilizando callbacks.
# Estará formado por una función que procesa pedidos.
# Debe aceptar el nombre del plato, una callback de confirmación, una
# de listo y otra de entrega.
# - Debe imprimir un confirmación cuando empiece el procesamiento.
# - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#   procesos.
# - Debe invocar a cada callback siguiendo un orden de procesado.
# - Debe notificar que el plato está listo o ha sido entregado.

def food_order(confirm_order: callable, ready_order: callable, delivered_order: callable):
    order = input("¿Qué plato desea pedir?\n")
    print(confirm_order(order))
    s(random.randint(1, 11))
    print(ready_order(order))
    s(random.randint(1, 11))
    print(delivered_order(order))

def confirm_order(text: str):
    return f"El plato: {text}, ha sido confirmado. Hora: {dt.now(UTC).strftime('%H:%M:%S')}"

def ready_order(text: str):
    return f"El plato: {text}, esta listo para entregar. Hora: {dt.now(UTC).strftime('%H:%M:%S')}"

def delivered_order(text: str):
    return f"plato: {text}, ha sido entregado. Hora: {dt.now(UTC).strftime('%H:%M:%S')}"

food_order(confirm_order, ready_order, delivered_order)