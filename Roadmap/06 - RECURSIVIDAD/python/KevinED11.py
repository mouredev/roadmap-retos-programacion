import functools


def decrement_counter(start_number: int = 100) -> None:
    if start_number >= 0:
        print(start_number)
        decrement_counter(start_number - 1)


@functools.lru_cache()
def factorial(number: int = 5) -> int:
    return 1 if number == 1 else number * factorial(number - 1)


@functools.lru_cache()
def fibonacci(number: int = 10) -> int:
    if number <= 1:
        return number

    return fibonacci(number - 2) + fibonacci(number - 1)


def main() -> None:
    decrement_counter(start_number=100)
    print(factorial(number=5))
    print(fibonacci(number=10))


if __name__ == "__main__":
    main()
