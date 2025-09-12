"""* EJERCICIO:
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
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado."""

import  datetime
import asyncio # Librería de Python para asincronía

async def  funcion_asincrona(nombre, tiempo): # Declaración de función asíncrona
    print(f"Comienza la función {nombre}")
    print(f"La función {nombre} durará {tiempo} segundos y comienza {datetime.datetime.now()}")
    await asyncio.sleep(tiempo) # Permite que se detenga un hilo asíncrono
    print(f"Finaliza la función {nombre} en {datetime.datetime.now()}")
    

asyncio.run(funcion_asincrona('Función asíncrona UNO', 5)) # Se usa asyncio con el método run para ejecutar la función asíncrona
asyncio.run(funcion_asincrona('Función asíncrona DOS', 5)) # Se usa asyncio con el método run para ejecutar la función asíncrona

#EXTRA
#Es necesario crear una función para la ejecución en paralelo
async def ejecuta_paralelo():
    # Ejecución asíncrona en paralelo, las 3 a la vez, se lanzan las 3, pero finaliza primero la que tenga menor duración
    await asyncio.gather(funcion_asincrona('Función C', 3), funcion_asincrona('Función B', 2), funcion_asincrona('Función A', 1)) # Permite que se detenga un hilo asíncrono
    await funcion_asincrona('Función D', 1)

asyncio.run(ejecuta_paralelo())