# 15 ASINCRONÍA

"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
"""

import asyncio
import time

async def main(name):

    print(f"Start function:  {time.strftime('%X')}")
    print(name)
    print ("Wait 4 seconds to finish")
    await asyncio.sleep(4)
    print(f"Finish function {time.strftime('%X')}")

asyncio.run(main("Async Function"))

print ("-"*100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 """

print ("Ejercicio Extra\n")

async def a_function():
    await asyncio.sleep(1)
    return print("Function A")

async def b_function():
    await asyncio.sleep(2)
    return print ("Function B")

async def c_function():
    await asyncio.sleep(3)
    print ("Function C")
    
async def asinc():

    task_a = asyncio.create_task(a_function()) # Asigno tareas
    task_b = asyncio.create_task(b_function())
    task_c = asyncio.create_task(c_function())
    await asyncio.gather(task_a,task_b,task_c) # Ejecución de las 3 tareas juntas

async def d_function():
    await asyncio.sleep(1)
    return print("Function D")

asyncio.run(asinc())
asyncio.run(d_function())