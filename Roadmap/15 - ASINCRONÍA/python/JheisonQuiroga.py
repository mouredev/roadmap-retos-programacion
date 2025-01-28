import asyncio
import time
from datetime import datetime, timedelta

"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza."""

async def task(name, seconds):
    init_time = timedelta(seconds=datetime.now().second)
    print(f"Start fetching data from {name}")
    await asyncio.sleep(seconds)
    finish_time = timedelta(seconds=datetime.now().second)
    difference = finish_time - init_time
    print(f"Data fetched from {name} in {difference} seconds")
    return f"Data from {name}"



async def main():
    result = await asyncio.create_task(task("API_1", 5))
    return result


# if __name__ == "__main__":
#     asyncio.run(main())


""" * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */"""

async def main2():
    start_time = time.time()
    # Creamos las tareas explicitamente
    task_a = asyncio.create_task(task("A", 1))
    task_b = asyncio.create_task(task("B", 2))
    task_c = asyncio.create_task(task("C", 3))
    
    # Esperamos que terminen las tareas paralelas (se ejecutan en paralelo)
    results = await asyncio.gather(task_a, task_b, task_c)

    # Ejecutamos la función D
    result_d = await task("D", 1)
    
    results.append(result_d)

    end_time = time.time() - start_time

    print("Results:", results)
    print("Total time:", end_time, "seconds")

if __name__ == "__main__":
    asyncio.run(main2())