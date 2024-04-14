import asyncio


async def async_func(name: str, delay: int) -> None:
    print(f"[{name.upper()}] Empezamos a ejecutar {name}, que tardará {delay} segundos")
    await asyncio.sleep(delay)
    print(f"[{name.upper()}] Hemos tardado {delay} segundos en terminar")


async def main(delay: int) -> None:
    coro = async_func("tontería", delay)
    print("Hemos definido la corrutina, pero todavía no se está ejecutando nada")

    task = asyncio.create_task(coro)
    print("Definimos una tarea con la corrutina, y empieza a ejecutar")

    await asyncio.sleep(0.1)
    print("Hemos esperado 0.1s para que este print salga tras arrancar la corrutina e imprimir la línea anterior.")

    print("Ahora esperamos a que la tarea termine...")
    await task

    print("Tras el await, la tarea ya terminó")


if __name__ == "__main__":
    asyncio.run(main(delay=3))
