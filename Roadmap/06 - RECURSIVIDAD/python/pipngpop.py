"""
RECURSIVIDAD -> función que se llama a ella  misma
"""

'''
def hello():
    hello()

hello()
'''
'''
def countdown (number: int):
    if number >= 0:
        print(number)
        countdown(number-1)

countdown(100)
'''
'''
EXTRA
'''
"""
* Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""


#Factorial
def factorial (num: int, fac:  int):
    
    if num > 0:
        num, fac = factorial(num-1, fac*num)
        
    return num, fac

fac=1
while True:
    num1 = int(input("\nIntroduce un número positivo: "))
    if num1 <0:
        print("\nIntroduce un número positivo")
    else:
        break
num, fac = factorial(num1, fac)
print(f"\nEl factorial de {num1} es {fac}")



#Fibonacci
def fibonacci (pos:  int, fib_a: int, fib_b: int, num: int):
    if num < pos:
        pos, fib_a, fib_b, num = fibonacci(pos, fib_b, fib_b+fib_a, num+1)
        
    return pos, fib_a, fib_b, num

while True:
    pos = int(input("\nIntroduce una posición: "))
    if pos < 0:
        print("\nIntroduce un número positivo")
    else:
        break
fib_a = 0
fib_b = 1
num = 0
pos, fib_a,fib_b, num = fibonacci(pos, fib_a, fib_b, num)
print(f"\nEl número {fib_a} corresponde a la posición {pos}\n")

'''
su solución

def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))


def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(5))



'''