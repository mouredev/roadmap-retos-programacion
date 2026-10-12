"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""

def sum_two_values(value1: int, value2: int) -> int:
    return value1 + value2

def test_sum_two_values() -> None:
    result: int = sum_two_values(15, 35)
    assert result == 50, "La función no suma correctamente."

test_sum_two_values()


def div_two_values(dividend: int, divisor: int) -> float:
    assert divisor != 0, "La división entre cero no está permitida."
    return dividend / divisor

div_two_values(1, 2)
#div_two_values(1, 0)

def get_int() -> None:
    string: int = input(">>> INGRESA UN NÚMERO:\n>>> ")
    assert type(string) == int
    print(string)

#get_int()

import pytest 

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

#### EXTRA ####

datos_personales: dict[str, any] = {
    "name": "rosendocamal",
    "age": "180",
    "birth_date": "2026-02-30",
    "programming_languages": ["Python", "Rust", "Bash", "PowerShell", "Typescript"]
}

def test_revisar_llaves() -> None:
    llaves: any = datos_personales.keys()
    llaves_esperadas: set[str] = {
        "name",
        "age",
        "birth_date",
        "programming_languages"
    }

    assert len(llaves) == len(llaves_esperadas), "Los campos no coinciden."

    for key in llaves:
        assert key in llaves_esperadas, "Este campo no existe."

def test_revisar_valores() -> None:
    valores: any = datos_personales.values()
    valores_esperados: list[any] = [
        "rosendocamal",
        "180",
        "2026-02-30",
        ["Python", "Rust", "Bash", "PowerShell", "Typescript"]
    ]

    assert len(valores) == len(valores_esperados), "La cantidad de datos no coinciden."

    for value in valores:
        assert value in valores_esperados, "Este valor es incorrecto."

test_revisar_llaves()
test_revisar_valores()