# Problem #06 recursion

def countdown_from_100_to_0(count=100):
    print(count)
    if count == 0:
        return

    count -= 1

    return countdown_from_100_to_0(count)


countdown_from_100_to_0()


# Extra

# Factorial
def factorial(number: int) -> int:
    if number <= 0:
        return 1

    return number * factorial(number - 1)


print(f"{factorial(4) = }")
print(f"{factorial(6) = }")


def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(f"{fibonacci(9) = }")
