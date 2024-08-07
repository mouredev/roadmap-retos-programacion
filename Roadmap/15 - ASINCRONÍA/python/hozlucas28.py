import asyncio


"""
    Asynchrony...
"""

print("Asynchrony...")


async def parallel_instructions(*, sleep_time: int) -> None:
    """Parallel instructions"""
    print("\nparallel_instructions start...")

    await asyncio.sleep(delay=sleep_time)
    print("\n> Parallel instructions executed")

    print(f"\nparallel_instructions: {sleep_time} seconds of execution")
    print("\nparallel_instructions end!")


async def async_fn(*, sleep_time: int) -> None:
    """Async function example"""
    print("\nasyncFn start...")

    await asyncio.sleep(delay=sleep_time)

    print(f"\nasyncFn: {sleep_time} seconds of execution")
    print("\nasyncFn end!")


async def main_challenge() -> None:
    """Main challenge function"""
    await asyncio.gather(
        parallel_instructions(sleep_time=2),
        async_fn(sleep_time=5),
    )

    print("\nmain_challenge: 5 seconds to execute async_fn and parallel_instructions")


asyncio.run(main=main_challenge())


"""
    Additional challenge...
"""

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

print("Additional challenge...")


async def delayed_fn(*, sleep_time: int, title: str) -> None:
    """Asynchronous function"""
    await asyncio.sleep(delay=sleep_time)
    print(f"\n{title}: {sleep_time} seconds of execution")


async def main_additional_challenge() -> None:
    """Main additional challenge function"""
    await asyncio.gather(
        delayed_fn(sleep_time=1, title="A"),
        delayed_fn(sleep_time=2, title="B"),
        delayed_fn(sleep_time=3, title="C"),
    )

    await delayed_fn(sleep_time=1, title="D")

    print("\nmain_additional_challenge: 4 seconds to execute A, B, C, and D")


asyncio.run(main=main_additional_challenge())
