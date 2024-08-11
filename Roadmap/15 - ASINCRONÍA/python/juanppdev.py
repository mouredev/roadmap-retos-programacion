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

async def tarea_asincrona(nombre, duracion):
    print(f"{nombre} empieza. Durará {duracion} segundos.")
    inicio = time.time()
    await asyncio.sleep(duracion)
    fin = time.time()
    print(f"{nombre} ha terminado. Duración real: {fin - inicio:.2f} segundos.")

async def main():
    # Crear y ejecutar tareas asincrónicas
    tareas = [
        tarea_asincrona("Tarea 1", 3),
        tarea_asincrona("Tarea 2", 5),
        tarea_asincrona("Tarea 3", 2)
    ]
    await asyncio.gather(*tareas)

# Ejecutar el bucle de eventos
asyncio.run(main())


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

import asyncio
import time

async def tarea_asincrona(nombre, duracion):
    print(f"{nombre} empieza. Durará {duracion} segundos.")
    inicio = time.time()
    await asyncio.sleep(duracion)
    fin = time.time()
    print(f"{nombre} ha terminado. Duración real: {fin - inicio:.2f} segundos.")

async def main():
    # Crear tareas asincrónicas para C, B y A
    tarea_C = tarea_asincrona("Función C", 3)
    tarea_B = tarea_asincrona("Función B", 2)
    tarea_A = tarea_asincrona("Función A", 1)
    
    # Ejecutar C, B y A en paralelo
    await asyncio.gather(tarea_C, tarea_B, tarea_A)
    
    # Ejecutar la tarea D después de que C, B y A hayan terminado
    await tarea_asincrona("Función D", 1)

# Ejecutar el bucle de eventos
asyncio.run(main())
