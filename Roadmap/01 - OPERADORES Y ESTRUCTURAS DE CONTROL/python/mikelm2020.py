# Operadores Aritméticos
def suma(a, b):
    return a + b


def sustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Operador inválido")


def int_division(a, b):
    if b != 0:
        return a // b
    else:
        print("Operador inválido")


def resiudue(a, b):
    if b != 0:
        return a % b
    else:
        print("Operador inválido")


def power(a, b):
    return a**b


# Operadores lógicos y de comparación
def greather_than(a, b, c):
    if a > b and a > c:
        return a
    elif a < c and b < c:
        return c
    else:
        return b


# Operadores de asignación e identidad
def identity():
    a = 100
    b = 100

    print(f"Dados las asignaciones a = 100 y b = 100 , a pertenece a b es: {a is b}")
    return None


def identity_negative():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]

    print(f" Dada las lista a {a}")
    print(f"Y la lista b {b}")
    print(f" a no pertenece a b es: {a is not b}")
    return None


# Operadores de pertenencia
def belonging():
    s = set([1, 2, 3, 4, 5])
    print(f"Dado el conjunto s {s}")
    print(f"{3} pertenece a s: {3 in s}")
    print(f"{8} pertenece a s: {8 in s}")
    print(f"{8} no pertenece a s: {8 not in s}")
    return None


# Operadores de bit
def bit_operators(a, b):
    binary_a = bin(a)
    binary_b = bin(b)
    print(f"Operador 1 El número {a} convertido a binario es: {binary_a}")
    print(f"Operador 2 El número {b} convertido a binario es: {binary_b}")
    print("Las operaciones serían:")

    print(f"El operador And (&) aplicado a {a} y {b} es: {bin(a & b)}")
    print(f"El operador Or (|) aplicado a {a} y {b} es: {bin(a | b)}")
    print(f"El operador Not (~) aplicado a {a} y {b} es: {bin(~a)} y {bin(~b)}")
    print(f"El operador Xor (^) aplicado a {a} y {b} es: {bin(a ^ b)}")
    print(
        f"El operador desplazamiento a la derecha (>>) aplicado a {a} 2 unidades y {b} 4 unidades es: {bin(a>>2)} y {bin(b>>4)}"
    )
    print(
        f"El operador desplazamiento a la iquierda (<<) aplicado a {a} 2 unidades y {b} 4 unidades es: {bin(a<<2)} y {bin(b<<4)}"
    )
    return None


# Estructuras de control
def control_structures():
    # Ciclo while
    # Se detiene hasta que el número se haya incrementado en 5 unidades

    print("Ejemplo con ciclo while inicia en 1 y se detiene en 5")
    number = 1
    while number <= 5:
        print(f"El número es: {number}")
        number += 1

    # Ciclo for
    # Se imprimen los primeros 10 números enteros a partir del 1

    print("Ejemplo de ciclo for se imprimen los primeros 10 números empezando en 1")
    for number in range(1, 11):
        print(f"El número es: {number}")

    return None


# EXTRA
def extra():
    print(
        """Programa que imprime por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""
    )
    for number in range(10, 55, 2):
        if number != 16 and number % 3 != 0:
            print(f"El número es: {number}")
    return None


if __name__ == "__main__":
    # Lee los 3 números
    number_1, number_2, number_3 = map(
        int, input("Dame 3 números:").rstrip().split(" ")
    )

    print(f"La suma de {number_1} y {number_2} es: {suma(number_1, number_2)}")
    print(f"La resta de {number_1} y {number_2} es: {sustraction(number_1, number_2)}")
    print(
        f"La multiplicación de {number_1} y {number_2} es: {multiplication(number_1, number_2)}"
    )
    print(f"La división de {number_1} y {number_2} es: {division(number_1, number_2)}")
    print(
        f"La división entera de {number_1} y {number_2} es: {int_division(number_1, number_2)}"
    )
    print(f"El residuo de {number_1} y {number_2} es: {resiudue(number_1, number_2)}")
    print(
        f"La potencia de {number_1} elavado a {number_2} es: {power(number_1, number_2)}"
    )
    print(
        f"El número mayor entre {number_1} , {number_2} y {number_3} es: {greather_than(number_1, number_2, number_3)}"
    )
    print("Un ejemplo de identidad")
    identity()
    print("Un ejemplo de identidad negativa")
    identity_negative()
    print("Un ejemplo de pertenencia")
    belonging()
    print(
        f"Un ejemplo de operadores con bits convirtiendo a binarios el número {number_1} y {number_2}"
    )
    bit_operators(number_1, number_2)
    print("Un ejemplo de estructuras de control")
    control_structures()
    print("El resultado del ejercio extra")
    extra()
