"""
EJERCICIO:
Explora el concepto de callback en tu lenguaje creando un ejemplo
simple (a tu elección) que muestre su funcionamiento.

DIFICULTAD EXTRA (opcional):
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estará formado por una función que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmación, una
de listo y otra de entrega.
- Debe imprimir un confirmación cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre 
procesos.
- Debe invocar a cada callback siguiendo un orden de procesado.
- Debe notificar que el plato está listo o ha sido entregado.

by adra-dev
"""

"""
CALLBACKS:
    Un callback es un concepto general en Python como en otros 
    lenguajes como Javascript, C, etc. Como sabemos Pyton es un
    lenguaje orientado a objetos y las funciones en python son 
    ciudadanos de primer orden. Esto significa que podemos asignar
    el valor devuelto por una funcion a una variable y devolver el 
    resultado de una funcion llamandola desde el interior de otra.
    documentacion: https://www.askpython.com/python/built-in-methods/callback-functions-in-python 
"""

"""
Se desea mostrar un mensaje que muestre si un alumno aprobo el curso
o no segun su promedio
"""

# Definimos la funcion promedio

promedio = lambda *args: sum(args) / len(args)

# definimos la condicion de si el promedio es aprobatorio o no 
aprobatorio = lambda calificacion : calificacion >=7

# Definimos la funcion mostrar mensaje que va llamar a las otras 2 funciones como argumentos
def mostrar_mensaje(func_promedio, func_aporbatorio, *args):
    promedio = func_promedio(*args)

    if func_aporbatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}.')
    else:
        print('No aprobaste la materia.')

mostrar_mensaje(promedio, aprobatorio, 10, 10 , 8, 7, 7)
mostrar_mensaje(promedio, aprobatorio, 0, 2, 5, 6, 9, 3)

"""
EXTRA
"""
import random
import time
import threading



def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    def process():
            confirm_order(dish_name)
            time.sleep(random.randint(1,10))
            order_ready(dish_name)
            time.sleep(random.randint(1,10))
            order_delivered(dish_name)


    threading.Thread(target=process).start()


def confirm_order(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido confirmado.")


def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name} esta listo.")


def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado.")


order_process("Pizza Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza 4 Quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Margarita", confirm_order, order_ready, order_delivered)
order_process("Pizza Pepperoni", confirm_order, order_ready, order_delivered)