import asyncio
from typing import Callable, Iterable
import time


type Number = int | float
type VoidAsyncFunction = Callable[[], None]


def set_function_name(func: Callable, new_name: str) -> None:
    func.__name__ = new_name


def get_function_name(func: Callable) -> str:
    return func.__name__


async def function_a() -> None:
    await sleep_program(1, name="Function A")
    print("function a finished")


async def function_b() -> None:
    await sleep_program(2, name="Function B")
    print("function b finished")


async def function_c() -> None:
    await sleep_program(3, name="Function C")
    print("function c finished")


def func_d() -> None:
    print("function d started")
    time.sleep(1)
    print("function d finished")


async def execute_void_async_functions(funcs: Iterable[VoidAsyncFunction]) -> None:
    for func in funcs:
        await func()


async def sleep_program(seconds: Number, name: str = "Sleep") -> None:
    set_function_name(sleep_program, name)
    current_name = get_function_name(sleep_program)

    print(f"{current_name} program started")
    print(f"Sleeping for {seconds} seconds")
    await asyncio.sleep(delay=seconds)

    print(f"{current_name} program finished")


async def main() -> None:
    await sleep_program(5)
    print("¡Hola, mundo!")

    await execute_void_async_functions([function_c, function_b, function_a])
    func_d()

    print("¡Adiós, mundo!")


if __name__ == "__main__":
    asyncio.run(main())
