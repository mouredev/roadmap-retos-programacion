"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asincrona una funcion que tardara en finalizar un numero concreto de
 * segundos parametrizables. Tambien debes poder asignarle un nombre.
 * La funcion imprime su nombre, cuando empieza, el tiempo que durara
 * su ejecucion y cuando finaliza.
"""

import asyncio


async def task_D(name: str, seconds: int ):
    print(f"[+] La tarea {name} comienza a ejecutarse....\n")
    await asyncio.sleep(seconds)
               
    print(f"[!] La tarea {name} ha finalizado\n")
    
asyncio.run(task_D("Tarea D", 5))



"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronia y la funcion anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una funcion C que dura 3 segundos.
 * - Una funcion B que dura 2 segundos.
 * - Una funcion A que dura 1 segundo.
 * - Una funcion D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La funcion D comienza su ejecucion cuando las 3 anteriores han
 *   finalizado.
""" 

async def task_C(name: str, seconds: int):
    print(f"[+] La tarea {name} comienza a ejecutarse....\n")
    await asyncio.sleep(seconds)
    print(f"[!] La tarea {name} ha finalizado\n")
    
async def task_B(name: str, seconds: int):
    print(f"[+] La tarea {name} comienza a ejecutarse....\n")
    await asyncio.sleep(seconds)
    print(f"[!] La tarea {name} ha finalizado\n")
    
async def task_A(name: str, seconds: int):
    print(f"[+] La tarea {name} comienza a ejecutarse....\n")
    await asyncio.sleep(seconds)
    print(f"[!] La tarea {name} ha finalizado\n")
    
async def main():
   
   print("[+] La 'Tarea D' Espera a que las demas terminen de ejecutarse....\n")
   await asyncio.gather(task_C("Tarea C", 3), task_B("Tarea B", 2), task_A("Tarea A", 1))
   await task_D("Tarea D", 5)
  
asyncio.run(main())
