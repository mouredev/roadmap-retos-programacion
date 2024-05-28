"""/*
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
 */"""

"""callback"""

import asyncio
import random
async def async_task(llamarDevuelta):
    print("Iniciando Tarea...")
    await asyncio.sleep(2)
    print("Tarea completa ")
    llamarDevuelta()
    
def my_callback():
    print("Callback ejecutando despues de la tarea asincrona")
    
asyncio.run(async_task(my_callback))


"""DIFICULTAD EXTRA"""

async def procesoOrden(idOrden,callback):
    print(f"Pedido {idOrden} recibido. Procesando....")
    await asyncio.sleep(random.uniform(1,3))
    print(f"Pedido {idOrden} completado")
    callback(idOrden)
    
def notifyPersona(idOrden):
    print(f"Notificacion: El pedido {idOrden} esta listo para ser recojido/enviado.")
    
async def main():
    ordenesIds=[1,2,3]
    tareas=[procesoOrden(idOrden,notifyPersona) for idOrden in ordenesIds]
    await asyncio.gather(*tareas)

asyncio.run(main())