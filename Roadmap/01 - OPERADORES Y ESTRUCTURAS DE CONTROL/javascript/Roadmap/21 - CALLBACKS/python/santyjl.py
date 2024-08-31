#21 - CALLBACKS
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
# los callback son funciones que llaman a otra funciones tipo decoradores
def funcion_principal(callback):
    print("Ejecutando función principal")
    callback()

def mi_callback():
    print("Ejecutando el callback")

funcion_principal(mi_callback)

# extra
import random
import time


# Función principal que procesa los pedidos
def procesar_pedido(nombre_plato, confirmacion_callback, listo_callback, entrega_callback):
    print(f"Confirmando pedido para {nombre_plato}...")
    confirmacion_callback(nombre_plato)

    # Simular tiempo de preparación
    tiempo_preparacion = random.randint(1, 10)
    time.sleep(tiempo_preparacion)
    print(f"El plato {nombre_plato} está listo después de {tiempo_preparacion} segundos.")
    listo_callback(nombre_plato)

    # Simular tiempo de entrega
    tiempo_entrega = random.randint(1, 10)
    time.sleep(tiempo_entrega)
    print(f"El plato {nombre_plato} ha sido entregado después de {tiempo_entrega} segundos.")
    entrega_callback(nombre_plato)

# Callback de confirmación
def confirmacion(nombre_plato):
    print(f"Pedido confirmado para {nombre_plato}.")

# Callback de plato listo
def listo(nombre_plato):
    print(f"El plato {nombre_plato} está listo para ser servido.")

# Callback de entrega
def entrega(nombre_plato):
    print(f"El plato {nombre_plato} ha sido entregado al cliente.")

# Ejemplo de uso del simulador de pedidos
nombre_plato = "Pizza Margherita"
procesar_pedido(nombre_plato, confirmacion, listo, entrega)
