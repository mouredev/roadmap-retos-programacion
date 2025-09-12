import time


# Función simulada que toma un tiempo para completarse
def funcion_asincrona(callback):
    print("La función asincrónica está realizando alguna tarea...")
    time.sleep(2)  # Simulando una tarea que toma tiempo
    print("La función asincrónica ha completado su tarea.")
    callback()  # Llamada al callback después de completar la tarea


# Callback que se ejecutará después de que la función asincrónica termine
def mi_callback():
    print("¡El callback ha sido llamado!")


# Llamada a la función asincrónica pasando el callback como argumento
funcion_asincrona(mi_callback)


# Ejercicio extra

import random


# Función de procesamiento de pedidos
def procesar_pedido(
    nombre_plato, callback_confirmacion, callback_listo, callback_entrega
):
    # Confirmar que el pedido ha sido recibido
    print(f"Recibiendo el pedido para: {nombre_plato}")
    callback_confirmacion(nombre_plato)

    # Simular tiempo de preparación
    tiempo_preparacion = random.randint(1, 10)
    time.sleep(tiempo_preparacion)

    # Notificar que el plato está listo
    print(
        f"El plato {nombre_plato} está listo después de {tiempo_preparacion} segundos."
    )
    callback_listo(nombre_plato)

    # Simular tiempo de entrega
    tiempo_entrega = random.randint(1, 10)
    time.sleep(tiempo_entrega)

    # Notificar que el plato ha sido entregado
    print(
        f"El plato {nombre_plato} ha sido entregado después de {tiempo_entrega} segundos."
    )
    callback_entrega(nombre_plato)


# Callbacks
def confirmacion_pedido(nombre_plato):
    print(
        f"Confirmación: El pedido para {nombre_plato} ha sido recibido y está en proceso."
    )


def plato_listo(nombre_plato):
    print(f"Notificación: El pedido para {nombre_plato} está listo para servir.")


def entrega_pedido(nombre_plato):
    print(f"Notificación: El pedido para {nombre_plato} ha sido entregado al cliente.")


# Ejemplo
procesar_pedido("Pizza", confirmacion_pedido, plato_listo, entrega_pedido)
procesar_pedido("Hamburguesa", confirmacion_pedido, plato_listo, entrega_pedido)
procesar_pedido("Ensalada", confirmacion_pedido, plato_listo, entrega_pedido)
