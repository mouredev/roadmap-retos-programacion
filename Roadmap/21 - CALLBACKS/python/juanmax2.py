"""
Ejercicio
"""

def funcion_saludo(name: str, saludo):
    saludo(name)
    
def saludar_base(name: str):
    print(f"Hola, {name}")

funcion_saludo("Juanma", saludar_base)
import random
import time
import threading
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

def proceso_pedido(nombre_plato: str, confirmar_callback, pedido_callback, estado_callback):
    def process():
        confirmar_callback(nombre_plato)
        time.sleep(random.randint(1, 10))
        pedido_callback(nombre_plato)
        time.sleep(random.randint(1, 10))
        estado_callback(nombre_plato)
    threading.Thread(target=process).start()

def confirmar_pedido(nombre_plato: str):
    print(f"Tu pedido {nombre_plato} ha sido confirmado")
    
def pedido_listo(nombre_plato: str):
    print(f"Tu pedido {nombre_plato} está listo")

def estado_pedido(nombre_plato: str):
    print(f"Tu pedido {nombre_plato} ha sido entregado")

proceso_pedido("Carbonara", confirmar_pedido, pedido_listo, estado_pedido )
proceso_pedido("Barbacoa", confirmar_pedido, pedido_listo, estado_pedido )
proceso_pedido("Nona", confirmar_pedido, pedido_listo, estado_pedido )
proceso_pedido("4 quesos", confirmar_pedido, pedido_listo, estado_pedido )