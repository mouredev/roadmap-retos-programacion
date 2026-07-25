'''
EJERCICIO:
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera 
asincrona una función que tardará en finalizar un número concreto de
segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará
su ejecución y cuando finaliza.
'''
import datetime, asyncio 

async def tik_tak(name: str, duration: int):
    
    print(f"Tarea: {name}. Duración: {duration}s. \n    - Inicio de tarea: {datetime.datetime.now()}")
                
    await asyncio.sleep(duration) # Tiempo de espera
    
    print(f"- Fin de tarea {name}: {datetime.datetime.now()}")
    
asyncio.run(tik_tak("1", 2))


    

'''DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundo.
- Una función D que dura 1 segundo.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han
finalizado.
'''

async def async_tik_tak():
    await asyncio.gather( # GATHER es una función que espera a que todos los 
                          # parámetros de su llamada se ajecuten antes de 
                          # continuar
        tik_tak("C", 3), 
        tik_tak("B", 2),  
        tik_tak("A", 1)
    )
    await tik_tak("D", 1) # AWAIT es una palabra reservada que espera a que 
                          # la función que está a su lado se complete antes 
                          # de continuar
    
asyncio.run(async_tik_tak()) # .run es una función que ejecuta una función asincrona

    