"""
Asincronia
"""

#Ejecutar tareas sin esperar a que terminen para seguir con otras. Permite que un programa siga funcionando mientras espera respuestas de operaciones lentas (como leer un archivo, consultar una API, etc).

import datetime  # Para trabajar con fechas y horas
import time      # Para simular una pausa (bloqueante)
import asyncio   # Para manejar asincronía


# Definimos una función asíncrona (puede ser pausada sin bloquear)
async def task(name: str, duration: int):
     # Mostramos el nombre de la tarea, su duración y la hora de inicio
    print(f"Tarea: {name}. Duracion: {duration}s. Inicio {datetime.datetime.now()}") #Aquí usamos datetime.datetime.now() porque: datetime es el módulo. Dentro de él hay una clase datetime. Y dentro de esa clase está el método now().
#Si hubiéramos hecho from datetime import datetime, podríamos escribir solo datetime.now().

    #Mal uso de time.sleep() en función async. Debe ser await asyncio.sleep() para no bloquear.
    #time.sleep(duration) # Simulamos que la tarea toma tiempo (bloqueante)

    await asyncio.sleep(duration) #pausa la corrutina durante duration segundos, pero permite que otras tareas sigan ejecutándose mientras.

    # Mostramos la hora al terminar
    print(f"Tarea: {name}. Fin {datetime.datetime.now()}")

# Ejecutamos la corrutina en un event loop
asyncio.run(task("1", 2))

"""* DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado."""

 #Definimos otra función asíncrona que se encargará de manejar varias tareas a la vez.
async def async_tasks():
    #asyncio.gather() permite ejecutar varias corrutinas al mismo tiempo.
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1)) #Aquí las tareas C, B y A se lanzan juntas y terminan según su duración.
    await task("D", 2) #Se espera a que terminen C, B y A, y luego se ejecuta D.

#Ejecutar todo el grupo de tareas
asyncio.run(async_tasks())


# async def	Define una función asincrónica (corrutina).
# await	Espera sin bloquear. Permite continuar otras tareas.
# asyncio.sleep()	Pausa la corrutina de forma no bloqueante.
# asyncio.gather()	Ejecuta varias corrutinas en paralelo.
# asyncio.run()	Inicia y maneja el event loop asincrónico.
# datetime.datetime.now()	Obtiene la fecha y hora actual.
