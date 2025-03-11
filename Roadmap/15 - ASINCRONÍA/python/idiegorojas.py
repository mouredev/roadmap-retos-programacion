# Asincronia

"""
Calves de la asincronia:

* Coroutines: 
    Se definen con la palabra 'async def'
    Suspenden o reanudan una ejecucion en puntos especificos usando 'await'
* Await: 
    Se usa dentro de una coroutina para suspender una ejecucion 
    Solamente puede ser usada dentro de una funcion 
* Event Loop:
    Administra las coroutina esperando y ejecutando las tareas asincronicas en el orden correcto
    Se puede usar 'asyncio' para manejar el evento loop
* Asyncio:
    Proporsiona la infraestructura para escribir codigo asincronico
"""

# Importar el modulo
import asyncio

async def main():
    print('Hola ...')
    await asyncio.sleep(5)
    print('... mundo.')

asyncio.run(main())


# Ejercicio
import asyncio
import datetime

async def tarea(nombre: str, duracion: int):
    print(f'Tarea: {nombre}. Duracion: {duracion}')
    print(f'Inicio: {datetime.datetime.now()}')
    await asyncio.sleep(duracion)
    print(f'Tarea: {nombre}. Duracion: {duracion}')
    print(f'Finalizo: {datetime.datetime.now()}')

nombre_tarea = 'Tarea 1'
duracion_tarea = 5

asyncio.run(tarea(nombre_tarea, duracion_tarea))

async def tareas():
    await asyncio.gather(tarea('A', 1),tarea('B', 2),tarea('C', 3))
    await tarea('D', 1)

asyncio.run(tareas())