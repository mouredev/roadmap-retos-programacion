# Función recursiva 100 a 0
def cuenta_regresiva(number: int):
    if number == 0:
        print(number)
        print("Final de la cuenta regresiva")
    else:
        print(number)
        cuenta_regresiva(number-1)


cuenta_regresiva(100)

# Dificultad extra


# Optimización de funciones recursivas
def moize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


# Factorial
@moize
def factorial(number: int) -> int:
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(f"el factorial de 10 es {factorial(10)}")


# Fibonacci
@moize
def fibonacci(position: int) -> int:
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)


print(
    f" el número equivalente a la posición 30 en la sujeción de fibonacci es {fibonacci(30)}")
