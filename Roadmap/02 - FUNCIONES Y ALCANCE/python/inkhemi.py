# Función sin parámetros ni retorno
def hello():
    print("Hello World")


hello()


# Función con un parámetro
def hello_name(name: str):
    print(f'Hello {name}')


hello_name("Inkhemi")


# Función con varios parámetros
def name(name: str, surname: str):
    print(f'Hello {name} {surname}')


name("Inkhemi", "Dev")


# Función con retorno
def sum(a: int, b: int) -> int:
    return a + b


print(sum(1, 2))


# Función dentro de una función
def par_fibonacci(number: int) -> bool:
    def is_par(number: int) -> bool:
        return number % 2 == 0

    def is_fibonacci(number: int) -> bool:
        a, b = 0, 1
        while a < number:
            a, b = b, a + b
        return a == number

    if is_par(number) and is_fibonacci(number):
        return True
    return False


print(par_fibonacci(8))


# Variable local y global
def local():
    number = 1
    print(f'local: {number}')


number = 2
local()
print(f'global: {number}')


# Dificultad extra
print("\nDificultad extra:")


def fizzbuzz(text1: str, text2: str) -> int:
    number = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            number += 1
    return number


print(fizzbuzz("Fizz", "Buzz"))
