if __name__ == '__main__':
    # Método 1
    for i in range(1, 11):
        print(i)

    # Método 2
    i = 1
    while i <= 10:
        print(i)
        i += 1

    # Método 3
    list(map(print, range(1, 11)))

    # Método 4
    numbers = list(range(1, 11))
    iterator = iter(numbers)

    try:
        while True:
            number = next(iterator)
            print(number)
    except StopIteration:
        pass
