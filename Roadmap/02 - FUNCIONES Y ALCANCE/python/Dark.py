# Funciones

# Sin parámtros pero sin retorno
def default():
    print("Hello")


default()


# Sin parámtros pero con retorno
def with_return():
    return 2


with_return()


# Con parámtros y sin retorno y posicionales
def suma(a, b):
    print(a + b)


suma(4, 8)


# Con parámetros y con retorno
def substraction(a, b):
    return a - b


print(7, 5)


# parámtro predeterminado
def def_alr(a=21):
    print(a)


def_alr()


# Con retorno 2 valores
def multiple_return():
    return "Hola", "Python"


greet, name = multiple_return()
print(greet)
print(name)


# Argumentos de longitud variable
def sum(
    *numbers,
):  # se usa * para que la función pueda recibir tuplas, de lo contrario se recibiría un array
    total = 0
    for i in numbers:
        total += i
    print(total)


sum(1, 2, 3, 4)


# Funciones dentro de Funciones
def outher_function():
    def inner_function():
        print("Hola, python")

    inner_function()


outher_function()

# Built-in functions
print(len("Martín"))
print(type(34))
print(abs(-45))  # Calcula la magnitud de un número y devuelve el resultado positivo o 0
print("Martín".lower())

"""
Variables Globales y locales
"""
# Global
x = "Awesome"  # global


def my_function():
    print("Python is " + x)


my_function()


# Or
def my_function2():
    global y
    y = "Fantastic"


my_function2()
print("Python is " + y)


# Local variable
def my_function3():
    z = 2  # Without global, just local function
    print(z)


z = 4

my_function3()


# OPTIONAL
def function(a, b):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(a + b)
        elif i % 3 == 0:
            print(a)
        elif i % 5 == 0:
            print(b)
        print(i)


function("BIZZ", "BUZZ")
