# Función sin parámetros ni retorno
def name():
    print("Mi nombre es: Miguel Angel López Monroy")


# Función con un parámetro
def square_area(side):
    return side * side


# Función con varios parametros
def polygon_area(side, n, aphotem):
    return ((side * n) * aphotem) / 2


# Función con Función
def polygon_area_2(aphotem, side, n):

    def polygon_perimeter(side, n):
        return side * n

    return polygon_perimeter(side, n) * aphotem


# Funciones ya credaas en el lenguaje
def python_functions():
    import math

    print(f"El residuo de la divisón 10 / 2 es: {math.remainder(10,2)}")
    print(f"La raiz cuadrada de 25 es: {math.sqrt(25)}")


# Variables globales y locales
global_variable = 9


def variables():
    local_variable = 2
    print("La variable global tiene un valor de: {global_variable}")
    print(f"La variable local tiene un valor de: {local_variable}")
    print(f"La suma de las variables es: {global_variable + local_variable}")


# Extra
def extra_numbers(first_string: str, second_string: str) -> int:
    count_of_numbers = 0
    for number in range(1, 101):

        if number % 3 == 0 and number % 5 == 0:
            print(f"{first_string} {second_string}")
        elif number % 3 == 0:
            print(first_string)
        elif number % 5 == 0:
            print(second_string)
        else:
            print(number)
            count_of_numbers += 1

    return count_of_numbers


if __name__ == "__main__":
    name()
    print(f"El área de un cuadrado de 5 unidades por lado es: {square_area(5)}")
    print(
        f"El área de un poligono con 7 lados, de 5 unidades por lado y un apotema de 1.5 unidades es: {polygon_area(5, 7, 1.5)}"
    )
    print(
        f"El área de un poligono con 9 lados, de 3 unidades por lado y un apotema de 3.5 unidades es: {polygon_area_2(3, 9, 3.5)}"
    )
    python_functions()
    variables()
    numbers = extra_numbers("múltiplo de 3", "múltiplo de 5")
    print(f"El número de veces que se ha impreso un número es: {numbers} veces")
