# /bin/python3
# Author: Héctor Adán 
# GitHub: https://github.com/hectorio23

import asyncio
import time

'''
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
'''

async def imprimir_nombre(delay: int, name: str ) -> None:
    '''
    Esta corrutina esta diseñada para que se ingresen los datos correctos,
    de lo contrario, dará un error porque no se implementaron validaciones.
    '''
    print(f"Hola { name }, es un gusto verte de nuevo por aqui!")
    print(f"Espera { delay } seg")
    await asyncio.sleep(delay)


# Corrutina -> Funcion Asincrona en python
async def do_something(name: str, delay:int) -> None:
    print(f"Una funcion { name } que dura { delay } segundos")
    await asyncio.sleep(delay)


async def main() -> None:
    # Creating a Task group for schedule the tasks
    # Task Group es la mejor manera para ejecutar tareas asincronas de manera
    # concurrente
    async with asyncio.TaskGroup() as tg:
        print(f"Iniciando la ejecucion concurrente de las tareas C,B y A en: { time.strftime('%X') }")
        tg.create_task(do_something("C", 3), name="Task C")
        tg.create_task(do_something("B", 2), name="Task B")
        tg.create_task(do_something("A", 1), name="Task A")
        # Las tareas se ejcutan de manera implicita cuando se sale del manejador de contexto
    
    print(f"Finalizando la ejecucion de las tareas C,B y A en: { time.strftime('%X') }")

    # La tarea C se ejecuta cuando las demas tareas se hayan ejecutado, ya que
    # al no formar parte del grupo, no se ejecuta de manera concurrente con las
    # tareas anteriores.
    await do_something("D", 1 )


# Se crea un gestor de contexto asincrono para ejecutar la corrutine principal.
# Tambien de puede crear una corrutina de la siguiente manera:
# asyncio.run(coro())
# Los argumentos debug -> default: None, loop_factory -> default: new_event_loop() se pueden omitir 
with asyncio.Runner(debug=True, loop_factory=asyncio.new_event_loop) as runner:
    # Codigo que da resolucion al ejercicio de la semana
    print("Ejecucion del ejercicio de la semana")
    name = input("Ingresa tu nombre: ")
    delay = int(input("Ingresa el tiempo de retraso: "))
    runner.run(imprimir_nombre(delay, name))

    # Ejecucion para la resolucion del ejercicio extra
    print("\nEjecucion del EJERCICIO EXTRA")
    runner.run(main())
