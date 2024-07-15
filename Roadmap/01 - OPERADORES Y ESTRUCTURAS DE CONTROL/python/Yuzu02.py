""" 
/*
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA(opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
# Para las type annotations
from typing import List


def aritmeticos(a: int, b: int) -> None:
    """Operadores aritméticos"""
    print("\nAritméticos:")
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"División entera: {a} // {b} = {a // b}")
    print(f"Módulo: {a} % {b} = {a % b}")
    print(f"Exponenciación: {a} ** {b} = {a ** b}")


def comparacion(a: int, b: int) -> None:
    """Operadores de comparación"""
    print("\nComparación:")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")


def logicos(a: bool, b: bool) -> None:
    """Operadores lógicos"""
    print("\nLógicos:")
    print(f"{a} and {b}: {a and b}")
    print(f"{a} or {b}: {a or b}")
    print(f"not {a}: {not a}")


def asignacion(a: int | float, b: int | float) -> None:
    """Operadores de asignación"""
    print("\nAsignación:")
    a += b
    print(f"a += b: {a}")
    a -= b
    print(f"a -= b: {a}")
    a *= b
    print(f"a *= b: {a}")
    a /= b
    print(f"a /= b: {a}")
    a //= b
    print(f"a //= b: {a}")
    a %= b
    print(f"a %= b: {a}")
    a **= b
    print(f"a **= b: {a}")


def identidad(a: int, b: int) -> None:
    """Operadores de identidad"""
    print("\nIdentidad:")
    print(f"a is b: {a is b}")
    print(f"a is not b: {a is not b}")


def pertenencia(element: int, lista: List[int]) -> None:
    """Operadores de pertenencia"""
    print("\nPertenencia:")
    print(f"{element} in {lista}: {element in lista}")
    print(f"{element} not in {lista}: {element not in lista}")


def bits(a: int, b: int) -> None:
    """Operadores de bits"""
    print("\nBits:")
    print(f"a & b: {a & b}")
    print(f"a | b: {a | b}")
    print(f"a ^ b: {a ^ b}")
    print(f"a << 1: {a << 1}")
    print(f"a >> 1: {a >> 1}")


def estructuras_de_control(lista: List[int]) -> None:
    """Ejemplo con estructuras de control"""
    print("\nEstructuras de control:")

    # Condicional
    for numero in lista:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

    # Iterativa
    for i in range(5):
        print(f"\nIteración {i}")

    # Excepciones
    try:
        print(lista[10])
    except IndexError as e:
        print(f"\nError: {e}")


def imprimir_numeros_especiales() -> None:
    """Programa extra: imprimir números entre 10 y 55 que son pares y no son ni 16 ni múltiplos de 3"""
    print("\nNúmeros especiales:")
    for num in range(10, 56):
        if num % 2 == 0 and num != 16 and num % 3 != 0:
            print(num)


# Ejecución de funciones
aritmeticos(5, 3)
comparacion(5, 3)
logicos(True, False)
asignacion(5, 3)
identidad(5, 3)
pertenencia(3, [1, 2, 3, 4, 5])
bits(5, 3)
estructuras_de_control([1, 2, 3, 4, 5])
imprimir_numeros_especiales()
