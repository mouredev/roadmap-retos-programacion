# Autor: Héctor Adán 
# GitHub: https://github.com/hectorio23

'''
EJERCICIO:
Explora el concepto de callback en tu lenguaje creando un ejemplo
simple (a tu elección) que muestre su funcionamiento.

DIFICULTAD EXTRA (opcional):
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estará formado por una función que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmación, una
de listo y otra de entrega.

- Debe imprimir un confirmación cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
  procesos.
- Debe invocar a cada callback siguiendo un orden de procesado.
- Debe notificar que el plato está listo o ha sido entregado.

'''

import asyncio
import random

#########################################################
##################### EJERCICIO 1 #######################
#########################################################

console_log = lambda message: print(f"Mensage impreso por el callback: { message }")

def do_something(msg: str, callback: callable) -> None:
    console_log(msg)


do_something("¡Hola Mundo!", console_log)

print("\n****************** EJERCICIO EXTRA *******************\n")

#########################################################
################### EJERCICIO EXTRA #####################
#########################################################

# Corrutina que confirma el pedido, por defecto es Falso
def confirmacion(nombre_plato: str, check: bool) -> bool:
    print(f"[Confirmacion] - ¿Usted desea confirmar el pedido llamado \"{ nombre_plato }\"?: { 'Yes' if check else 'No' }")

    if check: return True

    return False

# Corrutina que imprime si el pedido está listo
async def listo(nombre_plato: str, confirmado: bool) -> bool:
    await asyncio.sleep(random.randint(0, 10))
    print(f"[Listo] - El pedido \"{ nombre_plato }\" está listo para ser entregado")

# Corrutina que imprime si el pedido ya ha sido entregado
async def entrega(nombre_plato: str):
    await asyncio.sleep(random.randint(0, 10))
    print(f"[Entrega] - El pedido \"{ nombre_plato }\" ha sido entregado")

# Corrutina que procesa las ordenes
async def make_order(nombre_plato: str, confirmacion: callable, listo: callable, entrega: callable, check = False) -> None:
    confirmado = confirmacion(nombre_plato, check)
    if not check:
        print(f"[Cancelled] - El pedido \"{ nombre_plato }\" no se confirmó, por lo que se cancelo el pedido")
        return None
    
    await listo(nombre_plato, confirmado)
    await entrega(nombre_plato)


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(make_order("Papas a la francesa", confirmacion, listo, entrega, True))
        tg.create_task(make_order("Carne de Cocodrilo a la parrilla", confirmacion, listo, entrega, False))
        tg.create_task(make_order("Tacos de Pastor", confirmacion, listo, entrega, True))
        tg.create_task(make_order("Ensalada de Papas con albondigas", confirmacion, listo, entrega, True))


# Ejecucion del ejercicio extra
with asyncio.Runner() as rn:
    rn.run(main())