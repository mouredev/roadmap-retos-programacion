# EJERCICIO:
# Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# asíncrona una función que tardará en finalizar un número concreto de
# segundos parametrizables. También debes poder asignarle un nombre.
# La función imprime su nombre, cuándo empieza, el tiempo que durará
# su ejecución y cuando finaliza.
#
# DIFICULTAD EXTRA (opcional):
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# - Las funciones C, B y A se ejecutan en paralelo.
# - La función D comienza su ejecución cuando las 3 anteriores han
#   finalizado.

import datetime
import asyncio

async def duration_task(name: str,duration: int):
    start = datetime.datetime.now()

    print(f"Tarea {name.upper()} <<< INICIO: {datetime.datetime.now()}s")

    await asyncio.sleep(duration)

    print(f"{name.upper()}     >>> FIN:{datetime.datetime.now()}s")        


asyncio.run(duration_task("Correr",3))

async def contexto_async():
    await asyncio.gather(duration_task("C",3),duration_task("B",2),duration_task("A",1))
    await duration_task("D",1)
    

asyncio.run(contexto_async())


