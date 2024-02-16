# #06 RECURSIVIDAD


def imprimir_numeros(contador):
    if contador < 0:
        return
    else:
        print(contador)
        contador -= 1
        imprimir_numeros(contador)


imprimir_numeros(100)

# Dificultad Extra


def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


print(factorial(5))  # 120


def fibonacci(numero):
    if numero < 1:
        print("El número debe ser mayor o igual a 1")
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


print(fibonacci(8))  # 13
