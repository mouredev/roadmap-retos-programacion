import datetime
import asyncio

async def cosa(nombre, duracion): # async se usa para definir una función asíncrona que puede contener una o más llamadas a await
    print(f"Tarea: {nombre}. Duración: {duracion}s. Inicio: {datetime.datetime.now()}") 
    await asyncio.sleep(duracion) # await se usa para esperar a que se complete una tarea asíncrona
    print(f"Tarea: {nombre}. Fin: {datetime.datetime.now()}")

asyncio.run(cosa("Prueba", 7)) # asyncio.run() se usa para ejecutar una función asíncrona

"""
DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundo.
- Una función D que dura 1 segundo.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""

async def tareas_asincronas():
    await asyncio.gather(cosa("C", 3), cosa("B", 2), cosa("A", 1)) # asyncio.gather() se usa para ejecutar varias tareas asíncronas en paralelo
    await cosa("D", 1) 
    
asyncio.run(tareas_asincronas())