# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * ASINCRONÍA
# -----------------------------------

"""
* EJERCICIO #1:
* Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
* asíncrona una función que tardará en finalizar un número concreto de
* segundos parametrizables. También debes poder asignarle un nombre.
* La función imprime su nombre, cuándo empieza, el tiempo que durará
* su ejecución y cuando finaliza.
"""

import asyncio

async def process(name: str, time: int):
    print(f"- Iniciar función: {name} -> Duración: {time}")
    await asyncio.sleep(time)
    print(f"* Función {name} finaliza.")

async def test():
    await asyncio.gather(
        process("Test 2", 4),
        process("Test 1", 2)
    )

#asyncio.run(test())

"""
* EJERCICIO #2:
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

async def in_parallel():
    await asyncio.gather(
        process("C", 3),
        process("B", 2),
        process("A", 1)
    )

async def main():
    await test()
    await in_parallel()
    await process("D", 1)

if __name__ == "__main__":
    asyncio.run(main())

