# @RoniPG

"""
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.
"""
count=100
def imprimirNumeros():
    global count
    if (count > -1) and (count<101):
        print(f"{count},")
        count-=1
        imprimirNumeros()
    else:
        count=0

imprimirNumeros()

"""
DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
"""
result =1
def factorial(a:int):
    global count
    global result
    if count < a -1:
        result=result*(2)
        count +=1
        factorial(a)
    else:
        print(f"{a}! = {result}")
        count=0
        return result
    return 0

factorial(6)
"""
- Calcular el valor de un elemento concreto (según su posición) en la 
  sucesión de Fibonacci (la funciún recibe la posición).
"""
resultado=0
resultado2=1
def fibonacci(a:int):
    global count
    global resultado
    global resultado2
    if a==1:
        print(0)
        return 0
    elif a==2 and a==3:
        print(1)
        return 0
    elif count+2<a:
        x=resultado2+resultado
        resultado=resultado2
        resultado2=x
        count+=1
        fibonacci(a)
    elif count+2>=a:
        print(resultado2)
        count=0
        return 0
    return 0

fibonacci(6)
