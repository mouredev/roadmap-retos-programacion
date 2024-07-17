"""
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 */
"""

# Callback

def mi_callback(numero):
    for n in range(numero):
        print(f"Llamada a Callback nº {n+1} de {numero}")

def ping(numero,callback):
    if numero > 0:
        callback(numero)
    else:
        print(f"{numero} no es mayor a 0")

ping(20,mi_callback)

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
from time import sleep
from random import randint
import threading

def proceso_pedido(plato,confirmacion,listo,entregado):
    def proceso():
        confirmacion(plato)

        tiempo_listo = randint(1,10)
        sleep(tiempo_listo)
        listo(plato,tiempo_listo)

        tiempo_entregado = randint(1,10)
        sleep(tiempo_entregado)
        entregado(plato,tiempo_entregado)
    threading.Thread(target=proceso).start()
def confirmacion(plato):
    print(f"{plato} ha sido confirmado, pronto estara listo.")

def listo(plato,tiempo):
    print(f"{plato} esta listo en {tiempo}s")

def entregado(plato,tiempo):
    print(f"{plato} ha sido entregado en {tiempo}s")

proceso_pedido("Tortilla de patatas",confirmacion,listo,entregado)
proceso_pedido("Burger XXL",confirmacion,listo,entregado)
proceso_pedido("Cordero Asado",confirmacion,listo,entregado)