
def recursion(number: int) -> None:
    """
    The function `recursion` in Python prints numbers from the input number down to 0 using recursion.

    :param number: The `recursion` function takes an integer `number` as a parameter. The function will
    print the value of `number` and then recursively call itself with `number-1` until `number` is
    greater than 0
    :type number: int
    """
    print(f'{number}')
    if number > 0 :
        recursion(number-1)

recursion(100)

"""
    Exercise
"""

def factorial(number: int, result: int = 1) -> None:
    """
    The function calculates the factorial of a given number recursively.

    :param number: The `number` parameter in the `factorial` function represents the integer for which
    you want to calculate the factorial. It is the input number for which the factorial will be computed
    :type number: int
    :param result: The `result` parameter in the `factorial` function is used to keep track of the
    intermediate result of the factorial calculation as the function recursively calls itself. It starts
    with a default value of 1 and gets updated as the function progresses through the recursive calls,
    defaults to 1
    :type result: int (optional)
    """
    if number > 1 :
        factorial(number-1, result*number)
    else:
        print(f'{result}')

factorial(5)

def fibonacci(position: int) -> int:
    """
    This Python function calculates the Fibonacci number at a given position using recursion.

    :param position: The `position` parameter in the `fibonacci` function represents the position of the
    Fibonacci number in the sequence that you want to calculate. For example, if `position` is 5, the
    function will return the 5th Fibonacci number in the sequence
    :type position: int
    :return: the value of the Fibonacci sequence at the specified position.
    """
    if position > 2:
        return fibonacci(position-1)+fibonacci(position-2)
    else:
        return 1

print(fibonacci(7))