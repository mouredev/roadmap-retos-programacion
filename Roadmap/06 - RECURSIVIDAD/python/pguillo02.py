#Función recursiva para contar hasta 100

def recursiva(n):

    if n == 0:
        print(n,"final de la función recursiva", sep = " " )
    else:
        print(n)
        recursiva(n-1)

recursiva(100)

def factorial(n, x =1):

    if n == 0:
        print("Factorial = ", x)
    else:
        factorial(n-1, x*n)

factorial(4)

def fibonnacci(n):

    if n == 1:
        return 1
    elif n == 2: 
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    
print(fibonnacci(3))

