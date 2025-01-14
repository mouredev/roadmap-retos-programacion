"""/*
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
 */"""

# Ejercicio Base y Extra

import asyncio
import time

class Proceso:
    def __init__(self,nombre:str,tiempo:int) -> None:
        if type(nombre) == str and type(tiempo) == int:
            self.nombre = nombre
            self.tiempo = tiempo

    async def ejecutar(self):
        inicio = time.time()
        print(f"Iniciando: {self.nombre}\nTiempo: {self.tiempo} segundos\n")
        await asyncio.sleep(self.tiempo)
        print(f"Terminado: {self.nombre} en {time.time()-inicio} segundos\n")

async def main():
    proceso_1 = Proceso("A",1)
    proceso_2 = Proceso("B",2)
    proceso_3 = Proceso("C",3)
    proceso_4 = Proceso("D",1)

    a = loop.create_task(proceso_1.ejecutar())
    b = loop.create_task(proceso_2.ejecutar())
    c = loop.create_task(proceso_3.ejecutar())
    await asyncio.gather(a,b,c)
    d = loop.create_task(proceso_4.ejecutar())
    await asyncio.gather(d)
    
if __name__ == "__main__":
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
