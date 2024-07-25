


# función recursiva que imprime número del 100 al 0


def func_recursiva(num: int):
    if num > 0: 
        minus = num - 1
        print(minus)
        func_recursiva(minus)
    else:
        print("Fin de la recursividad")

func_recursiva(100)



def factorial(num: int):
    if num < 0:
        print("Los números negativos no son válidos")
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))


def fibonacci(pos: int):
    if pos <= 0: 
        return 0
    elif pos == 1:
        return 0
    elif pos == 2:
        return 1
    else: 
        return fibonacci(pos - 1) + fibonacci(pos -2)

print(fibonacci(10))