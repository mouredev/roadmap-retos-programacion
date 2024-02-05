#Función recursiva para contar hasta 100

def recursiva(n):

    if n == 0:
        print(n,"final de la función recursiva", sep = " " )
    else:
        print(n)
        recursiva(n-1)

recursiva(100)