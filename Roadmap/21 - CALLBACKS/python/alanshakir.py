"""
/*
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
 */
"""
import time
import random

def called(n):
    return n[0] * n[1]

def caller(func, n):
    return func(n)

num = (8, 5)
ans = caller(called, num)

print(f"Multiplicación = {ans}")

def orders(food, order_process, order_confirmation, order_delivered):
    print(f"su pedido es {food}")
    order_process(food)
    time.sleep(random.randint(1, 10))
    order_confirmation(food)
    time.sleep(random.randint(1, 10))
    order_delivered(food)

def order_process(food):
    print(f"Su orden de {food} esta siendo procesada")

def order_confirmation(food):
    print(f"Su orden de {food} esta lista")

def order_delivered(food):
    print(f"Su orden de {food} esta siendo entregada")

orders("Pizza", order_process, order_confirmation, order_delivered)
orders("Hamburguesa", order_process, order_confirmation, order_delivered)
orders("sushi", order_process, order_confirmation, order_delivered)
