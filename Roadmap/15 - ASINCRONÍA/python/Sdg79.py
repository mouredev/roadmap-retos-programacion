
from datetime import datetime
import time
import asyncio

async def tarea(duracion, nombre):
        print(f"Tarea: {nombre}, Duracion:  {duracion} segundos, Inicio: {datetime.now()}")
        time.sleep(duracion)
        print(f"Tarea: {nombre}, Fin: {datetime.now()}")

asyncio.run(tarea(3, "Guardado"))
asyncio.run(tarea(2, "Prueba"))


# DIFICULTAD EXTRA:
"""* Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado."""


async def C(duracion):
        print(f"Tarea C {duracion} segundos, inicio {datetime.now()}")
        await asyncio.sleep(duracion)
        print(f"Tarea C {duracion} segundos, Fin {datetime.now()}")

async def B(duracion):
        print(f"Tarea B {duracion} segundos, inicio {datetime.now()}")
        await asyncio.sleep(duracion)
        print(f"Tarea B {duracion} segundos, Fin {datetime.now()}")
     
async def A(duracion):
        print(f"Tarea A {duracion} segundos, inicio {datetime.now()}")
        await asyncio.sleep(duracion)
        print(f"Tarea A {duracion} segundos, Fin {datetime.now()}")
       
async def D(duracion):
        print(f"Tarea D {duracion} segundos, inicio {datetime.now()}")
        await asyncio.sleep(duracion)
        print(f"Tarea D {duracion} segundos, Fin {datetime.now()}")

async def tareas_async():
        await asyncio.gather(C(3), B(2), A(1))

asyncio.run(tareas_async())
asyncio.run(D(1))
