# Ejercicio
from functools import reduce
from itertools import count, islice


def iteration_with_for():
    for index in range(1, 11):
        print(index)


def iteration_with_while():
    index = 1
    while index <= 10:
        print(index)
        index += 1


def iteration_with_for_in():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index in array:
        print(index)


# Extra
def iteration_with_for_each():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for element in array:
        print(element)


def recursive_count(number=1):
    if number <= 10:
        print(number)
        recursive_count(number + 1)


def iteration_with_comprehension():
    print(*[index for index in range(1, 11)], sep="\n")


def iteration_with_map():
    print(*map(lambda x: x, range(1, 11)))


def iteration_with_filter():
    print(*filter(lambda x: True if x <= 10 else False, range(1, 101)))


def iteration_with_reduce():
    print(reduce(lambda x, y: x + y, range(1, 11)))


def iteration_with_islice():
    print(*islice(count(1), 10))


def iteration_with_zip():
    print(*zip(range(1, 11), range(11, 21)))


def iteration_with_enumerate():
    print(*enumerate([x for x in range(1, 11)], 1))


def iteration_with_comprehension_2():
    print(*[(x, y) for x in range(1, 11) for y in range(x, 11)])


def iteration_with_comprehension_3():
    print(*[(x, y) for x in range(1, 11) for y in range(x, 11) if x != y])


def iteration_with_comprehension_4():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z
        ]
    )


def iteration_with_comprehension_5():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x < y < z
        ]
    )


def iteration_with_comprehension_6():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x > y > z
        ]
    )


def iteration_with_comprehension_7():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x == y == z
        ]
    )


def iteration_with_comprehension_8():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x < y > z
        ]
    )


def iteration_with_comprehension_9():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x > y < z
        ]
    )


def iteration_with_comprehension_10():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x < y == z
        ]
    )


def iteration_with_comprehension_11():
    print(
        *[
            (x, y, z)
            for x in range(1, 11)
            for y in range(x, 11)
            for z in range(y, 11)
            if x != y != z and x > y == z
        ]
    )


if __name__ == "__main__":
    print("Con For")
    iteration_with_for()
    print("Con While")
    iteration_with_while()
    print("Con For In")
    iteration_with_for_in()
    print("Con For Each")
    iteration_with_for_each()
    print("Con Recursividad")
    recursive_count()
    print("Con list comprehension")
    iteration_with_comprehension()
    print("Con Map")
    iteration_with_map()
    print("Con Filter")
    iteration_with_filter()
    print("Con Reduce")
    iteration_with_reduce()
    print("Con Islice")
    iteration_with_islice()
    print("Con Zip")
    iteration_with_zip()
    print("Con Enumerate")
    iteration_with_enumerate()
    print("Con Comprehension v2")
    iteration_with_comprehension_2()
    print("Con Comprehension v3")
    iteration_with_comprehension_3()
    print("Con Comprehension v4")
    iteration_with_comprehension_4()
    print("Con Comprehension v5")
    iteration_with_comprehension_5()
    print("Con Comprehension v6")
    iteration_with_comprehension_6()
    print("Con Comprehension v7")
    iteration_with_comprehension_7()
    print("Con Comprehension v8")
    iteration_with_comprehension_8()
    print("Con Comprehension v9")
    iteration_with_comprehension_9()
    print("Con Comprehension v10")
    iteration_with_comprehension_10()
    print("Con Comprehension v11")
    iteration_with_comprehension_11()
