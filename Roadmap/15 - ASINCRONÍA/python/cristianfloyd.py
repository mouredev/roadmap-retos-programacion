import asyncio
import datetime

# Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# asíncrona una función que tardará en finalizar un número concreto de
# segundos parametrizables. También debes poder asignarle un nombre.
# La función imprime su nombre, cuándo empieza, el tiempo que durará
# su ejecución y cuando finaliza.

async def funcion_asincrona(tarea: str, tiempo: int) -> None:
    """
    Args: tarea : string con el nombre de la tarea
          tiempo: entero en segundos, tiempo que tardara en finalizar
    """
    print(f"Tarea: {tarea} - Inicio: {datetime.datetime.now().strftime(format='%H:%M:%S')}")
    await asyncio.sleep(tiempo)
    print(f"Tarea: {tarea} - Fin: {datetime.datetime.now().strftime(format='%H:%M:%S')}")
    print(f"Tarea: {tarea} - Duración: {tiempo} segundos")

async def main():
    await funcion_asincrona(tarea="Tarea 1", tiempo=3)
    await funcion_asincrona(tarea="Tarea 2", tiempo=2)
    await funcion_asincrona(tarea="Tarea 3", tiempo=1)

asyncio.run(main())

#
# DIFICULTAD EXTRA (opcional):
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# - Las funciones C, B y A se ejecutan en paralelo.

async def main_extra():
    await asyncio.gather(
        funcion_asincrona(tarea="C", tiempo=3),
        funcion_asincrona(tarea="B", tiempo=2),
        funcion_asincrona(tarea="A", tiempo=1)
    )
    await funcion_asincrona(tarea="D", tiempo=1)

asyncio.run(main_extra())