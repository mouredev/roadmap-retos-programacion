"""
* EJERCICIO:
* Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
* asíncrona una función que tardará en finalizar un número concreto de
* segundos parametrizables. También debes poder asignarle un nombre.
* La función imprime su nombre, cuándo empieza, el tiempo que durará
* su ejecución y cuando finaliza.
*
* DIFICULTAD EXTRA (opcional):
* Utilizando el concepto de asincronía y la función anterior, crea
* el siguiente programa que ejecuta en este orden:
* - Una función C que dura 3 segundos.
* - Una función B que dura 2 segundos.
* - Una función A que dura 1 segundo.
* - Una función D que dura 1 segundo.
* - Las funciones C, B y A se ejecutan en paralelo.
* - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""

import asyncio
import time

async def run_task (name, duration):

    #print(f"Task '{name}' started.")
    start_time = time.time()

    await asyncio.sleep(duration)

    end_time = time.time()
    elapsed_time = end_time - (start_time)

    print(f"Task '{name}' started at {time.ctime(start_time)}, will run for '{duration}' seconds. Took {elapsed_time:.2f} seconds to complete.")

async def main():

    tasks = [
        run_task("Tarea 1", 3),
        run_task("Tarea 2", 1),
        run_task("Tarea 3", 4)
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())


##########  ------------------------  EXTRA  ---------------------------------- ##################


async def function_c():
    
    print("La funcion 'C' comenzo a ejecutarse.")
    await asyncio.sleep(3)
    print("Funcion 'C' completada.")

async def function_b():

    print("La funcion 'B' comenzo a ejecutarse.")
    await asyncio.sleep(2)
    print("Funcion 'B' completada.")

async def function_a():

    print("La funcion 'A' comenzo a ejecutarse.")
    await asyncio.sleep(1)
    print("Funcion 'A' completada.")

async def function_d():

    print("Funcion 'D' esperando que las funciones C,B y A se completen.")
    await asyncio.gather(function_c(), function_b(), function_a())
    print("Funcion 'D' comenzo a ejecutarse.")
    await asyncio.sleep(1)
    print("Funcion 'D' completada")

async def main():

    await asyncio.gather(function_c(), function_b(), function_a())  # Ejecuta las funciones C,B y A en paralelo

    await function_d()    # Una vez finalizadas C, B y A, ejecuta la función D  

asyncio.run(main())