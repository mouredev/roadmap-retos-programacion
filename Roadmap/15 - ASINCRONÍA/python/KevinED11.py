import asyncio
from typing import Callable, Iterable, Awaitable
from functools import partial


type Number = int | float
type VoidCoroutine = Awaitable[None]
type VoidCoroutineFn = Callable[[], VoidCoroutine]
type VariadicFunction[T] = Callable[..., T] | Awaitable[T]


def set_function_name(func: VariadicFunction, new_name: str) -> None:
    func.__name__ = new_name


def get_function_name(func: VariadicFunction) -> str:
    return func.__name__


async def generic_function(wait_time: Number, func_name: str) -> None:
    await sleep_program(seconds=wait_time, name=func_name)


function_a = partial(generic_function, wait_time=1, func_name="Function A")
function_b = partial(generic_function, wait_time=2, func_name="Function B")
function_c = partial(generic_function, wait_time=3, func_name="Function C")
function_d = partial(generic_function, wait_time=1, func_name="Function D")
function_e = partial(generic_function, wait_time=11, func_name="Function E")


async def execute_void_coroutines_simultaneously(
    coros: Iterable[VoidCoroutineFn],
) -> None:
    async with asyncio.TaskGroup() as tg:
        for coro in coros:
            tg.create_task(coro())


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

    await execute_void_coroutines_simultaneously(
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
