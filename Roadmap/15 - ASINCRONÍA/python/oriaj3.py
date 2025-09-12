
"""	
15 - ASINCRONÍA
Autor de la solución: Oriaj3	
Teoría:	
La programación asíncrona es un paradigma de programación que permite que un 
programa realice múltiples tareas simultáneamente. En lugar de ejecutar una
tarea tras otra, las tareas se ejecutan de forma concurrente, lo que puede
mejorar significativamente el rendimiento y la eficiencia de un programa.

En Python, la programación asíncrona se puede implementar utilizando el módulo
asyncio, que proporciona una serie de funciones y clases para trabajar con
tareas asíncronas. Para definir una función asíncrona en Python, se utiliza la
palabra clave async antes de la definición de la función. Por ejemplo, la
siguiente función es asíncrona:

async def mi_funcion():
    # Código de la función
    return

Para ejecutar una función asíncrona en Python, se puede utilizar la función
asyncio.run(), que ejecuta la función de nivel superior y espera a que termine.

Por ejemplo, la siguiente función ejecuta una tarea asíncrona que tarda un
número de segundos determinado:

import asyncio
import time

async def execute_task(name, seconds):

    print("\nEjecutando la tarea de forma asíncrona...")
    #obtiene el tiempo actual del sistema
    start_time = time.time()

    # Simulamos una tarea que tarda un cierto número de segundos
    await asyncio.sleep(seconds)

    # Obtiene el tiempo actual del sistema
    end_time = time.time()
    
    # Muestra el nombre de la tarea, el tiempo de inicio, la duración y el tiempo de finalización
    print(f"Tarea: {name}")
    print(f"Tiempo de inicio: {start_time}")
    print(f"Duración: {seconds} segundos")
    print(f"Tiempo de finalización: {end_time}")

# Ejecuta la tarea de forma asíncrona
asyncio.run(execute_task("Tarea 1", 3))
"""

"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.

"""

import asyncio
import datetime

async def execute_task(name: str, seconds: int): 
    
    tiempo_inicial = datetime.datetime.now()
    tiempo_fin = tiempo_inicial + datetime.timedelta(seconds=seconds)  
    print(f"Tarea {name} iniciada a las {tiempo_inicial}, finalizará a las {tiempo_fin}, durando {seconds}s.")

    #Espera x seconds
    await asyncio.sleep(seconds)

    tiempo_final = datetime.datetime.now()

    print(f"**[FIN {name}]**: {tiempo_final}")

asyncio.run(execute_task("Tarea 1", 1))



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
 */
"""
print("***********************EXTRA***********************")
async def extra():
    await asyncio.gather(execute_task ("C", 3), execute_task("B", 2), execute_task("A", 1))
    await execute_task("D", 1)

asyncio.run(extra())