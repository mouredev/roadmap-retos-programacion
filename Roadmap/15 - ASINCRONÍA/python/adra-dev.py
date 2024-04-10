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

"""
Ejercicio
"""

async def hello_world():
    print("Name: hello_world")
    print("This function will last 3 seconds")
    await asyncio.sleep(3)
    return print("ends: Hello Wolrd!")

asyncio.run(hello_world())


"""
Extra
"""

async def A():
    await asyncio.sleep(1)
    return print("Function A complete")

async def B():
    await asyncio.sleep(2)
    return print("Function B complete")

async def C():
    await asyncio.sleep(3)
    return print("Function C complete")

async def D():
    await asyncio.sleep(1)
    return print("Function D complete")

async def do_task():
    funcC = asyncio.create_task(C())
    funcB = asyncio.create_task(B())
    funcA = asyncio.create_task(A())

    resultados = await asyncio.gather(funcC, funcB, funcA,)

    return resultados

asyncio.run(do_task())
asyncio.run(D())