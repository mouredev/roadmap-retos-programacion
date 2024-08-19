"""
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
"""

import asyncio

async def main():
    await task_callback(tarea(), callback)

async def task_callback(tarea, callback):
    await tarea
    callback()

async def tarea():
    print("Sumando numeros..")
    await asyncio.sleep(2)
    print("Task finished")

def callback():
    print("Funcion callback invocada despues de completar task")

asyncio.run(main())


#############  ---------------------------- EXTRA --------------------------  #################

import random

menu = ["Hamburguesa", "Pizza", "Tacos", "Ensalada Cesar", "Pollo Frito"]

async def order_process(plato, confir_callback, ready_callback, entrega_callback):
    
    confir_callback(plato)
    preparation_time = random.randint(1,10)
    print(f"Preparando {plato}... (espera {preparation_time} segundos)")
    await asyncio.sleep(preparation_time)

    ready_callback(plato)
    delivery_time = random.randint(1,10)
    print(f"Entregando {plato}... (espera {delivery_time} segundos)")
    await asyncio.sleep(delivery_time)

    entrega_callback(plato)

def confir_callback(plato):
    print(f"Pedido Confirmado: {plato}")

def ready_callback(plato):
    print(f"Pedido listo: {plato}")

def entrega_callback(plato):
    print(f"Pedido entregado: {plato}")


def mostrar_menu_y_pedido():
    print("Menu de platos disponible:")
    for id, plato in enumerate(menu, start=1):
        print(f"{id}: {plato}")

    while True:
        try:
            pedido= int(input("\nIngrese el numero de plato que desea pedir: "))
            if 1 <= pedido <= len(menu):
                return menu[pedido - 1]
            else:
                print("Numero invalido, porfavor intente nuevamente.")
        except ValueError:
            print("Entrada invalida, porfavor ingrese un numero.")


async def realizar_pedido():
    print("Simulador de pedidos de un restaurante\n")

    plato_elegido = mostrar_menu_y_pedido()
    tarea = order_process(plato_elegido, confir_callback, ready_callback, entrega_callback)

    await tarea    

if __name__ == "__main__":
    asyncio.run(realizar_pedido())


