import asyncio
from typing import Callable, Iterable
import time


type Number = int | float
type VoidAsyncFunction = Callable[[], None]
type VariadicFunction[T] = Callable[[T, ...], T]


def set_function_name(func: VariadicFunction, new_name: str) -> None:
    func.__name__ = new_name


def get_function_name(func: VariadicFunction) -> str:
    return func.__name__


async def function_a() -> None:
    await sleep_program(1, name="Function A")


async def function_b() -> None:
    await sleep_program(2, name="Function B")


async def function_c() -> None:
    await sleep_program(3, name="Function C")


async def function_d() -> None:
    await sleep_program(1, name="Function D")


async def function_e() -> None:
    await sleep_program(11, name="Function E")


async def execute_void_async_functions(funcs: Iterable[VoidAsyncFunction]) -> None:
    tasks = [func() for func in funcs]
    await asyncio.gather(*tasks)


async def sleep_program(seconds: Number, name: str = "Sleep") -> None:
    set_function_name(sleep_program, name)
    current_name = get_function_name(sleep_program)

    print(f"{current_name} program started")
    print(f"Sleeping for {seconds} seconds")
    await asyncio.sleep(delay=seconds)

    print(f"{current_name} program finished")


async def goodbye() -> None:
    print("¡Adiós, mundo!")


async def main() -> None:
    await sleep_program(5)
    print("¡Hola, mundo!")

    await execute_void_async_functions(
        [
            function_e,
            function_c,
            function_b,
            function_a,
            function_d,
            goodbye,
        ]
    )
    await function_d()
    print("Adios")


if __name__ == "__main__":
    asyncio.run(main())
