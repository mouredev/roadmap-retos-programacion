""" /*
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
 */ """

#EJERCICIO
import asyncio
import time

async def funcion_asincrona(segundos):
    nombre = "Hola Mundo asíncrono"
    print(nombre)
    print(time.strftime("%H:%M:%S"))
    print(segundos)
    await asyncio.sleep(segundos)    
    print(time.strftime("%H:%M:%S"))

asyncio.run(funcion_asincrona(3))

#DIFICULTAD EXTRA
async def funcion_a():
    print("Soy la función A")
    await asyncio.sleep(1)

async def funcion_b():
    print("Soy la función B")
    await asyncio.sleep(2)

async def funcion_c():
    print("Soy la función C")
    await asyncio.sleep(3)

async def funcion_d():
    print("Soy la función D")
    await asyncio.sleep(1)

async def extra():
    await asyncio.gather(funcion_a(), funcion_b(), funcion_c())
    await funcion_d()
    

asyncio.run(extra())
