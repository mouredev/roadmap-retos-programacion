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
import random
import time
import asyncio

# EJERCICIO:


async def procesar_evento(callback):
    print("Iniciamos proceso asincrono")
    await asyncio.sleep(1)
    print("Llamando al callback")
    callback()


def mi_callback():
    print("Callback ejecutado")


asyncio.run(procesar_evento(mi_callback))

# DIFICULTAD EXTRA:


def procesar_pedido(plato, callback_confirmacion, callback_listo, callback_entrega):
    callback_confirmacion(plato)

    tiempo_procesamiento = random.randint(1, 10)
    time.sleep(tiempo_procesamiento)

    callback_listo(plato)

    tiempo_entrega = random.randint(1, 10)
    time.sleep(tiempo_entrega)

    callback_entrega(plato)


def confirmar_pedido(plato):
    print(f"Confirmación: El pedido del plato {
          plato} ha sido recibido y está en proceso.")


def pedido_listo(plato):
    print(f"Listo: El plato {plato} está listo para ser entregado.")


def entregar_pedido(plato):
    print(f"Entregado: El plato {plato} ha sido entregado al cliente.")


plato = "Empanadas de Pollo"
procesar_pedido(plato, confirmar_pedido, pedido_listo, entregar_pedido)
