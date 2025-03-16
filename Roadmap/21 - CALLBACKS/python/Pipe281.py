'''
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
'''
import time
import random

def mi_callback(name: str):
    print(f"Hola", name)

def llamadora(name: str, callback):
    print("Antes del callback")
    callback(name)
    print("Después del callback")

llamadora("Pipe", mi_callback)


'''
Tarea extra
'''

def orden (nombre_plato: str, confirmacion_orden, orden_lista, orden_entregada):
    confirmacion_orden(nombre_plato)
    time.sleep(random.randint(1,10))
    orden_lista(nombre_plato)
    time.sleep(random.randint(1,10))
    orden_entregada(nombre_plato)

def confirmacion_orden (nombre_plato: str):
    print (f"Tu pedido {nombre_plato} a sido confirmado.")

def orden_lista (nombre_plato: str):
    print (f"Tu pedido {nombre_plato} esta listo.")

def orden_entregada (nombre_plato: str):
    print (f"Tu pedido {nombre_plato} a sido entregado.")

orden ("Churrasco", confirmacion_orden, orden_lista, orden_entregada)