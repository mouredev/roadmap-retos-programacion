class MyException(Exception):
    message = "The list is empty"


def divideBy(numbers: list, divisor: int, size: int):

    if len(numbers) == 0:
        raise MyException
    elif divisor == 0:
        raise ZeroDivisionError
    elif len(numbers) != size:
        raise Exception

    for index in range(0, size):
        print(numbers[index] / divisor)

    print("No error found")


try:
    divideBy([1, 2, 3, 4], 2, 3)
except (MyException):
    print(MyException.message)
except (ZeroDivisionError):
    print("Divisor should no be 0")
except Exception:
    print("Numbers size should be size")
finally:
    print("Ejecución finalizada")
