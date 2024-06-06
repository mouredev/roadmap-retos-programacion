def print_down_to_zero(start: int) -> None:
    """
    Given a starting integer 'start', print it, and all integers below it,
    down to zero.

    Args:
        start (int):
            Starting integer.

    Returns:
        Nothing. Just prints the numbers out.
    """
    if not isinstance(start, int):
        raise TypeError("Esta función sólo acepta enteros.")

    if start < 0:
        raise ValueError("Esta función no acepta números negativos (si lo hiciera, no pararía nunca).")

    if start > 1000:
        raise ValueError("Vamos, muchacho, ¿para qué quieres imprimir más de 1000 números? Sé razonable.")

    print(start)

    if start > 0:
        print_down_to_zero(start-1)


def factorial(n: int) -> int:
    """
    Given an integer 'n', return its factorial.

    Args:
        n (int):
            Integer whose factorial we want to calculate.

    Returns:
        Factorial of n.
    """
    if not isinstance(n, int):
        raise TypeError("Esta función sólo acepta enteros (pregunta a tus papás por la función Gamma).")

    if n < 0:
        raise ValueError("Esta función sólo acepta enteros positivos (busca la función Gamma en la Wikipedia).")

    if n > 25:
        raise ValueError("Estás jugando a ser dios con factoriales tan grandes.")

    if n in (0, 1):
        return 1

    return n * factorial(n-1)


def fibonacci_bad(n: int) -> int:
    """
    Given an integer "n", return n-th member of the Fibonacci sequence.

    This function uses the naïve recursive implementation, which is a terribly inefficient way
    of performing the calculation. No one in their right mind would or should use this rubbish.
    Use fibonacci_good() instead.

    Args:
        n (int):
            The position in the Fibonacci sequence that we want to calculate.

    Return:
        Given n, returns fib(n).
    """
    if not isinstance(n, int):
        raise TypeError("Esta función sólo acepta enteros.")

    if n < 0:
        raise ValueError("Esta función sólo acepta enteros positivos.")

    if n > 35:
        raise ValueError("Esta implementación de fib(n) es una mierda. Para valores grandes usa fibonacci_good().")

    if n == 0:
        return 0

    if n in (1, 2):
        return 1

    return fibonacci_bad(n-1) + fibonacci_bad(n-2)


def fibonacci_good(n: int) -> int:
    """
    More sensible implementation of fib(n) than fibonacci_bad(). The only downside is that
    it is not recursive, so it is not fit for the '#06 - Recursividad' task :)

    A better implementation yet could be to use Binet's formula.

    Args:
        n (int):
            The position in the Fibonacci sequence that we want to calculate.

    Return:
        Given n, returns fib(n).
    """
    if not isinstance(n, int):
        raise TypeError("Esta función sólo acepta enteros.")

    if n < 0:
        raise ValueError("Esta función sólo acepta enteros positivos.")

    if n == 0:
        return 0

    prev, curr = 0, 1  # we are sitting at n=1
    for _ in range(2, n+1):
        curr, prev = curr + prev, curr

    return curr


def extra():
    print(f"25! = {factorial(25)}")
    print(f"fib(25) = {fibonacci_bad(25)}")


def main():
    print_down_to_zero(100)


if __name__ == "__main__":
    main()
    extra()
