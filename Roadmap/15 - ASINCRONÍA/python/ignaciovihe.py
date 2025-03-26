"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
"""

import asyncio
from datetime import datetime

async def task(name, seconds):
    start = datetime.now()
    print(f"La tarea {name} empieza en {start}")
    print(f"La tarea {name} se ejecuta durante {seconds} segundos")
    await asyncio.sleep(seconds)
    finish = datetime.now()
    print(f"La tarea {name} termina en {finish}")

asyncio.run(task("1", 5))


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

async def async_tasks():
    # Se crea una tarea en segundo plano que no para a las demas. No pedido en el ejercicio.
    tarea_grande = asyncio.create_task(task("SEGUNDO PLANO",6)) #para probar

    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)
    await tarea_grande

asyncio.run(async_tasks())









"""
Pruebas adicionales
"""
"""Ejemplo funciones asincronas y sincronas al mismo tiempo"""
import asyncio
import time  #Importamos time para medir el tiempo

# Simula la consulta a la base de datos (tarda 2 seg)
async def leer_bd(nombre_bd):
    print(f"Consultando {nombre_bd}...")
    await asyncio.sleep(5)  # Simula el tiempo de consulta
    return f"Datos de {nombre_bd}"  # Simula datos obtenidos

# Simula el procesamiento de datos (bloqueante)
def procesar_datos(datos):
    print(f"Procesando {datos}...")
    return f"{datos} - Procesado"

# Simula guardar datos en la base de datos (tarda 2 seg)
async def guardar_bd(nombre_bd, datos):
    print(f"Guardando en {nombre_bd}: {datos}...")
    await asyncio.sleep(5)  # Simula el tiempo de guardado
    print(f"Datos guardados en {nombre_bd}.")

# Función principal
async def main():

    inicio = time.perf_counter()  #Iniciamos el cronómetro

    nombres_bd = ["DB1", "DB2", "DB3", "DB4", "DB5"]

    # Leer de las 5 bases de datos en paralelo
    resultados = await asyncio.gather(*(leer_bd(nombre) for nombre in nombres_bd))

    # Procesar cada conjunto de datos (esto es síncrono)
    datos_procesados = [procesar_datos(datos) for datos in resultados]

    # Guardar los datos procesados en las 5 bases de datos en paralelo
    await asyncio.gather(*(guardar_bd(nombre, datos) for nombre, datos in zip(nombres_bd, datos_procesados)))

    fin = time.perf_counter()  #Finalizamos el cronómetro
    print(f"\n Tiempo total de ejecución: {fin - inicio:.2f} segundos")

# Ejecutar
asyncio.run(main())



