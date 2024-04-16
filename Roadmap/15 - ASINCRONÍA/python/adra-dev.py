"""
EJERCICIO:
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera 
asincrona una función que tardará en finalizar un número concreto de
segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará
su ejecución y cuando finaliza.

DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundo.
- Una función D que dura 1 segundo.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han
finalizado.

by adra-dev
"""


"""
Funciones Asíncronas:

Desde python 3.5 es posible crear funciones asíncronas utilizando las 
palabras reservadas async y wait. La primera se usa para definir que 
una funcion es asíncrona, y la segunda, que el valor esperado es de 
tipo asíncrono.

El uso de la programacion asíncrona permite que una funcion no se 
ejecute continuamente cuando este esperando a que un evento ocurra, 
por ejemplo, que haya una respuesta desde una peticion web, una 
respuesta de una consulta a una base de datos, apertura de un fichero
en disco o cualquier otro tipo de acceso a un sistema o proceso que 
provoque que la funcion deba esperar haciendo una operacion de 
entrada/salida y pueda cambiar de contexto hasta que el recurso este 
disponible.
"""

import asyncio
import datetime

"""
Ejercicio
"""

"""
Ejercicio
"""


async def task(name: str, duration: int):
    print(
        f"Tarea: {name}. Duración: {duration}s. Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(
        f"Tarea: {name}. Fin: {datetime.datetime.now()}")


asyncio.run(task("1", 2))

"""
Extra
"""


async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

asyncio.run(async_tasks())