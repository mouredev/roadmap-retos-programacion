# -- exercise
def recursive(n):
    if n >= 0:
        print(n)
        recursive(n - 1)


recursive(100)


# -- extra challenge
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(f"Factorial of 5: {factorial(5)}")


def fibonacci(position):
    if position <= 0:
        return "Position must be a positive integer."
    elif position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, position):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[position - 1]


print(f"Fibonacci at position 10: {fibonacci(10)}")
