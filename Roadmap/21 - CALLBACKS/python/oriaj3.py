""" 
21 - CALLBACKS
Autor de la solución: Oriaj3

Teoría:
Un callback es una función que se pasa como argumento a otra función y que se
llama cuando un evento ocurre. En Python, los callbacks se pueden implementar
utilizando funciones o clases.

Los callbacks se utilizan para manejar eventos asíncronos, como la finalización
de una tarea o la recepción de una respuesta de un servidor. También se utilizan
para ejecutar código después de que se haya completado una tarea.

Los callbacks se utilizan en muchos lenguajes de programación, como JavaScript,
Java, C++ y Python. En Python, los callbacks se pueden implementar utilizando
funciones o clases.

Un callbacks en una clase sirve para que una función se ejecute después de que
otra función haya terminado de ejecutarse.

Ejemplo de funcion:
def callback_function():
    print("Callback function called")

def main_function(callback):
    print("Main function called")
    callback()

main_function(callback_function)
"""

"""
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""

def funcion_callback(nombre):
    print(f"Hola, {nombre}!")

def funcion_principal(nombre, callback):
    print("Procesando saludo.")
    callback(nombre)

funcion_principal("Jairo", funcion_callback)

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

import random
from time import sleep

def confirmacion(plato: str):
    print(f"[{plato}] - confirmado")

def listo(plato: str):
    print(f"[{plato}] - listo")

def entrega(plato: str):
    print(f"[{plato}] - entregado")


def procesar_pedido(nombre: str, confirm_callback, ok_callback, entrega_callback):
    confirm_callback(nombre)
    sleep(random.randint(1, 10))
    ok_callback(nombre)
    sleep(random.randint(1, 10))
    entrega_callback(nombre)

procesar_pedido("Pizza hawaiana", confirmacion, listo, entrega)
procesar_pedido("Pizza BBQ", confirmacion, listo, entrega)
procesar_pedido("Pizza Carbonara", confirmacion, listo, entrega)
    