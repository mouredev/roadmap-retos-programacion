from typing import Generator
from functools import reduce


def iteration_1() -> None:
    for n in range(1, 11):
        print(n)


def iteration_2() -> None:
    numbers = [num for num in range(1, 11)]
    print(numbers, sep="\n")


def iterarion_3() -> None:
    counter = 1
    while counter <= 10:
        print(counter)
        counter += 1


def iteration_4() -> None:
    iter = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(next(iter))
    print(next(iter))


def iteraration_5() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    doubled = list(map(lambda x: x * 2, numbers))
    print(doubled)


def iteration_6() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    print(filtered)


def iteration_7() -> None:
    square_dict = {x: x * 2 for x in range(1, 11)}
    print(square_dict)


def iteration_7() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = reduce(lambda x, y: x + y, numbers, 0)
    print(result)


def iteration_8() -> None:
    numbers = tuple(num for num in range(1, 11))
    print(numbers)


def iteration_9() -> None:
    numbers = {num for num in range(1, 11)}
    print(numbers)


def iteration_10() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i, item in enumerate(numbers):
        print(f"elemento {item} en la posición {i}")


def iteration_11() -> None:
    numbers = [n for n in range(1, 11)]

    for n in range(len(numbers)):
        print(f"elemento {numbers[n]} en la posición {n}")


def even_number_generator() -> Generator[int, None, None]:
    num = 0
    while True:
        yield num
        num += 2


def main() -> None:
    even_numbers = even_number_generator()

    for _ in range(11):
        print(next(even_numbers))

    iteration_8()
    iteration_9()
    iteration_10()
    iteration_11()


if __name__ == "__main__":
    main()
