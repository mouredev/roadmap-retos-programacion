def serie(numero):
    if numero >= 0:
        print(numero)
        return serie(numero -1) + 1
    else:
        return 0
serie(100)

# ---- DIFICULTAD EXTRA ----

def factorial(numero):
    if numero < 1:
        return 1
    else:
        return factorial(numero -1) * numero
print(factorial(5))


def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index -1) + fibonacci(index -2)
print(fibonacci(10))