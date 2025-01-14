"""EJERCICIO:
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
asíncrona una función que tardará en finalizar un número concreto de
segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará
su ejecución y cuando finaliza."""

import asyncio


async def async_function(function_name, delay):
    print(f'The function "{function_name}", is starting it will take {delay} seconds to be completed...')
    await asyncio.sleep(delay)
    print(f'"{function_name}" was completed after {delay} seconds')


async def exercise():
    await async_function(function_name='First Exercise', delay=1)


"""DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundo.
- Una función D que dura 1 segundo.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han finalizado."""


async def function_a():
    await async_function('Function A', 1)


async def function_b():
    await async_function('Function B', 2)


async def function_c():
    await async_function('Function C', 3)


async def function_d():
    await async_function('Function D', 1)


async def parallel_execution():
    exe_c = asyncio.create_task(function_c())
    exe_b = asyncio.create_task(function_b())
    exe_a = asyncio.create_task(function_a())

    await asyncio.gather(exe_c, exe_b, exe_a)


async def sequential_execution():
    await function_d()


async def main():
    print('**** Basic exercise ****')
    await exercise()
    print('\n**** Extra ****')
    await parallel_execution()
    await sequential_execution()


asyncio.run(main())
