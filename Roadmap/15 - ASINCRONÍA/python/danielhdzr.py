# #15 ASINCRONÍA
#### Dificultad: Difícil | Publicación: 08/04/24 | Corrección: 15/04/24

## Ejercicio


''' * EJERCICIO:
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
 *   finalizado.'''

import asyncio, datetime

def main():
    async def tarea(nombre: str, duerme: int, ejecuta: int, lock: asyncio.Lock):
        async with lock:
            print(f"Tarea {nombre} comenzara en {duerme} segundos ") 
            print(f"Tarea {nombre} comenzando en", end="")
            for i in range(duerme, 0, -1):
                await asyncio.sleep(1)
                print(f" {i}...", end="", flush=True)
            print("\n")

        async with lock: 
            print(f"Tarea {nombre} comenzo a las {datetime.datetime.now()}")
            print(f"Tarea {nombre} ejecutando", end="")
            for i in range(ejecuta, 0, -1):
                await asyncio.sleep(1)
                print(f" {i}...", end="", flush=True)
            print("\n")

        async with lock:
            print(f"Tarea {nombre} ha finalizado")
            print(f"Tarea {nombre} finalizo a las {datetime.datetime.now()}")

    async def ejecutable():
        lock = asyncio.Lock()
        await asyncio.gather(
            tarea("C", 2, 1, lock),
            tarea("B", 2, 2, lock),
            tarea("A", 2, 3, lock)
        )
        # Ejecutar una tarea después de que las anteriores hayan terminado
        await tarea("D", 2, 1, lock)

    asyncio.run(ejecutable())
if __name__=="__main__":
    main()