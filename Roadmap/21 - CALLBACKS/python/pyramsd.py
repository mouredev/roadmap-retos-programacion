import asyncio
import random
import time

def handle_response(response):
    print("Respuesta recibida:", response)

async def async_request(callback):
    print("Iniciando solicitud asincrona")
    await asyncio.sleep(2)  # Simulando una operación asíncrona como una solicitud de red
    response = "Respuesta simulada"
    callback(response)

async def main():
    print("Haciendo solicitud asincrona")
    await async_request(handle_response)
    print("Solicitud realizada")

if __name__ == "__main__":
    asyncio.run(main())

'''
EXTRA
'''

def procesar_plato(plato, callback_confirm, callback_listo, callback_entrega):
    callback_confirm(plato)

    tiempo_procesamiento = random.randint(1, 10)
    time.sleep(tiempo_procesamiento)

    callback_listo(plato)

    tiempo_entrega = random.randint(1, 10)
    time.sleep(tiempo_entrega)

    callback_entrega(plato)

def confirmar_pedido(plato):
    print(f"Confirmación: El pedido del plato {plato} ha sido recibido y está en proceso.")


def pedido_listo(plato):
    print(f"Listo: El plato {plato} está listo para ser entregado.")


def entregar_pedido(plato):
    print(f"Entregado: El plato {plato} ha sido entregado al cliente.")


plato = "Empanadas de Pollo"
procesar_plato(plato, confirmar_pedido, pedido_listo, entregar_pedido)
