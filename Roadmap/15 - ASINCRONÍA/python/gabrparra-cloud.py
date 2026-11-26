"""/*
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
 */"""

import datetime
import time
import asyncio

async def funtion(name:str, duration:int):
    print(
        f"Función :{name}, duración: {duration} Seg. Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(
        f"Función :{name}, Fin: {datetime.datetime.now()}")

asyncio.run(funtion("1",3))
asyncio.run(funtion("2",2))

async def async_funtion():
    await asyncio.gather(
    funtion("C",3),
    funtion("B",2),
    funtion("A",1))
    await funtion("D",1)

asyncio.run(async_funtion())
