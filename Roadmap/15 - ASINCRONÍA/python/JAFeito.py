"""
 EJERCICIO:
 Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 asíncrona una función que tardará en finalizar un número concreto de
 segundos parametrizables. También debes poder asignarle un nombre.
 La función imprime su nombre, cuándo empieza, el tiempo que durará
 su ejecución y cuando finaliza.

 DIFICULTAD EXTRA (opcional):
 Utilizando el concepto de asincronía y la función anterior, crea
 el siguiente programa que ejecuta en este orden:
 - Una función C que dura 3 segundos.
 - Una función B que dura 2 segundos.
 - Una función A que dura 1 segundo.
 - Una función D que dura 1 segundo.
 - Las funciones C, B y A se ejecutan en paralelo.
 - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""
import asyncio
async def delay (nombre , tiempo:int):
    print(f"Iniciando funcion {nombre}")
    await asyncio.sleep(tiempo)
    print(f"Han pasado {tiempo} segundos")
    print(f"Funcion {nombre} terminada")
#nombre =  input("Introduzca el el nombre de la tarea:")   
#tiempo = input("Introduzca el tiempo de espera:")
#asyncio.run(delay(nombre, tiempo))

#EXTRA
async def lanzador ():
    await asyncio.gather(delay("C",3),delay("B",2),delay("A",1))
    await delay("D",1)


asyncio.run(lanzador())