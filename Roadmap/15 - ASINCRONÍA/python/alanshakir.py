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
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */
"""
import asyncio

async def fun_asyn(name: str, wait_seconds: int):
    print(f"La funcion {name}, tiene una duracion de: {wait_seconds}")
    await asyncio.sleep(wait_seconds)
    print(f"ha finalizado la ejecucion: {name}") 

asyncio.run(fun_asyn("Alan Ramirez", 1))
#Extra

async def multitask():
    await asyncio.gather(fun_asyn("C", 3), fun_asyn("B", 2), fun_asyn("A", 1))
    await fun_asyn("D", 1)

asyncio.run(multitask())
