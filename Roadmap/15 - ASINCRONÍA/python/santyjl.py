"""
/*
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
 */
"""

import asyncio  # asyncio es el modulo para funciones asincronas
import time


async def funcion_tareas(nombre : str , duracion : int) -> str: #async para definir que es una funcion asincrona
    "esta funcion permite el uso de funciones asicronas"

    inicio = time.time()
    print(f"El nombre de la tarea es {nombre} y dura {duracion} segundos")

    await asyncio.sleep(duracion)   #await para que espera pero sin afectar a otras funciones asincronas
    final = time.time()
    resultado : int = final - inicio

    print(f"La tarea {nombre} termino en {round(resultado , 1)} ")

async def ejecuciones_paralelas():
    "muestra el uso de funciones asicronas multiples"

    await asyncio.gather(       # asyncio.gatcher permite que que las funciones se ejecuten en paralelo
        funcion_tareas("tarea uno" , 4),
        funcion_tareas("tarea dos" , 1),
        funcion_tareas("tarea tres" , 2),
        funcion_tareas("tarea cuatro" , 5)
        )

    await asyncio.gather(funcion_tareas("tarea cinco" , 3))

asyncio.run(ejecuciones_paralelas())