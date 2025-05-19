# Ejercicio 06
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.

Numero = 100


def Conteo_Numero(valor):
    if valor < 0 or valor == 0:
        print("Termina la recursividad en ", valor)
    else:
        print(valor)
        Conteo_Numero(valor - 1)


Conteo_Numero(Numero)

# Extra

# Factorial de un numero concreto


def Factorial(valor: int) -> int:
    if valor == 0:
        return 1
    else:
        return valor * Factorial(valor - 1)

# Variables


Num_factorial = 4

print(Factorial(Num_factorial))


def fobanacci(num: int) -> int:
    if num < 0:
        print("La posicion tiene que ser mayor a cero")
        return 0
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fobanacci(num - 1) + fobanacci(num - 2)


print("Foba", fobanacci(10))
