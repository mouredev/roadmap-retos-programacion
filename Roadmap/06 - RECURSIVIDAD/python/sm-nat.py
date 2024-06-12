def funcion_recursiva(n):
    if n < 0:
        return
    else:
        print(n)
        funcion_recursiva(n-1)
funcion_recursiva(100)