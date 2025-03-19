import time
import random


def cuando_procesamiento_termina(resultado):
    print(f"El procesamiento ha terminado con el resultado: {resultado}")


def procesar_datos(data, callback):
    print("Procesando datos...")
    resultado = sum(data)
    print("Datos procesados.")
    callback(resultado)


datos = [1, 2, 3, 4, 5]

procesar_datos(datos, cuando_procesamiento_termina)


'''
  EXTRA
'''


def procesador_pedidos(plato, confirmacion, listo, entrega):
    print(f'Procesando plato: {plato}')
    tiempo_confirmacion = random.randint(1, 10)
    print(
        f"Confirmación del pedido, tiempo estimado {tiempo_confirmacion} segundos")
    time.sleep(tiempo_confirmacion)
    confirmacion()

    tiempo_procesamiento = random.randint(1, 10)
    print(f"Tiempo de procesamiento estimado: {tiempo_procesamiento} segundos")
    time.sleep(tiempo_procesamiento)
    listo()

    tiempo_entrega = random.randint(1, 10)
    print(f"Tiempo de entrega estimada: {tiempo_entrega} min")
    print("Entregando plato...")
    time.sleep(tiempo_entrega)
    entrega()


def confirmar_pedido():
    print("Pedido confirmado.")


def plato_listo():
    print("El plato está listo.")


def plato_entregado():
    print("El plato ha sido entregado al cliente.")


procesador_pedidos("Pizza", confirmar_pedido, plato_listo, plato_entregado)
procesador_pedidos("Pollo frito", confirmar_pedido,
                   plato_listo, plato_entregado)
procesador_pedidos("Tacos", confirmar_pedido, plato_listo, plato_entregado)
