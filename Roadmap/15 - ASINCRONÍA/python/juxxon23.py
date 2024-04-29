import asyncio
"""
 ╔═════════════════════════════════════╗
 ║ Autor:  Juxxon23                    ║
 ║ GitHub: https://github.com/juxxon23 ║
 ║ Python - 2024                       ║
 ║ Reto 15 - ASINCRONIA                ║
 ╚═════════════════════════════════════╝

EJERCICIO:
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
asíncrona una función que tardará en finalizar un número concreto de
segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará
su ejecución y cuando finaliza.
"""
async def func_g(name, sec):
    print(f'func_g started, this function will last {sec} seconds')
    await asyncio.sleep(sec)
    print(f"{sec} seconds have passed, func_g finished")

asyncio.run(func_g("test", 3))

"""
DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
Una función C que dura 3 segundos.
Una función B que dura 2 segundos.
Una función A que dura 1 segundo.
Una función D que dura 1 segundo.
Las funciones C, B y A se ejecutan en paralelo.
La función D comienza su ejecución cuando las 3 anteriores han
finalizado.
"""
async def func_C():
    print("func_C started, 3 sec")
    await asyncio.sleep(3)
    print("func_C finished")

async def func_B():
    print("func_B started, 2 sec")
    await asyncio.sleep(2)
    print("func_B finished")

async def func_A():
    print("func_A started, 1 sec")
    await asyncio.sleep(1)
    print("func_A finished")

async def func_D():
    print("func_D started, 1 sec")
    await asyncio.sleep(1)
    print("func_D finished")

async def parallel_func():
    _func_c = asyncio.create_task(func_C())
    _func_b = asyncio.create_task(func_B())
    _func_a = asyncio.create_task(func_A())

    await asyncio.gather(_func_c, _func_b, _func_a)

asyncio.run(parallel_func())
asyncio.run(func_D())
