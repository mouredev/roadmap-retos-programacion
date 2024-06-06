from typing import Callable, NoReturn
from functools import wraps


type Number = float | int
type OperationFn = Callable[[Number, Number], Number]


class OnlyNumbersException(Exception):
    pass


def raise_only_numbers_exception(msg: str) -> NoReturn:
    raise OnlyNumbersException(msg)


def is_number(n: Number) -> bool:
    return isinstance(n, (int, float))


def validate_operation(fn: OperationFn) -> OperationFn:
    @wraps(fn)
    def wrapper(a: Number, b: Number) -> Number:
        if not is_number(a) or not is_number(b):
            raise_only_numbers_exception("a y b deben ser números")

        return fn(a, b)

    return wrapper


@validate_operation
def division(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")

    return a / b


@validate_operation
def multiply(a: Number, b: Number) -> Number:
    return a * b


def main() -> None:
    try:
        result = division(10, 0)
        print(result)
    except ZeroDivisionError as err:
        print(repr(err))
    except Exception as err:
        print(repr(err), "error inesperado")
    else:
        print("la ejecución ha sido exitosa")
    finally:
        print("la ejecución ha finalizado")


if __name__ == "__main__":
    main()
