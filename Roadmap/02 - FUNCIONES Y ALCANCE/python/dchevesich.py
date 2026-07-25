# 02- Funciones y Alcance

def my_first_function():
    print('Esta es una funcion sin parametros ni retorno')


def my_second_function(name, lastname):  # funcion con parametros
    print(f"Welcome to Python {name} {lastname}")


my_first_function()
my_second_function("David", "Parrado")


def sum_function(num_one, num_two):  # funcion con parametros y retorno
    sum = num_one + num_two
    return sum


print(sum_function(4, 87))


def sqr_function(number):  # Funcion dentro de otra funcion
    number = float(number)
    return (number)**(0.5)


def operacion_function(f, num):
    return f(num)


print(operacion_function(sqr_function, 9))


def dificultad_extra(letra, letra1):
    contador = 0
    for num in range(1, 101):
        if num % 3 == 0:
            print(letra)
            contador += 1
        if num % 5 == 0:
            print(letra1)
            contador += 1
        elif num % 3 == 0 and num % 5 == 0:
            print(letra+letra1)
            contador += 1
    return contador


print(dificultad_extra("a", "b"))
