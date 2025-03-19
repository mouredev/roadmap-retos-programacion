# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝

# -------------
# Recursividad:
# -------------
# - La recursividad es la capacidad de una función para llamarse a sí misma,ya sea 
#   de forma directa o indirecta, con el propósito de resolver un problema.
# _________________________________
# imprimiendo números del 100 al 0.
# Ejemplo con recursividad directa:
# ocurre cuando una función se llama a sí misma.
def num(n: int):
    print(n)
    # caso base
    if n > 0: # evitar que la función se llame indefinidamente.
        num(n - 1)
num(100)

# Ejemplo con recursividad indirecta:
# implica que varias funciones se llamen entre sí.
def resta(n: int):
    write(n - 1)

def write(n: int):
    print(n)
    # caso base
    if n > 0:
        resta(n)

write(100)

# -----------
# Ejercicios:
# -----------
# Calcular el factorial de un número concreto (la función recibe ese número).
# 4! = 4 * 3 * 2 * 1 = 24
def factorial(n: int) -> int:
    if n != 0: 
        return n * factorial(n - 1)
    else: 
        return 1
    # explicación
    '''
    fac(4)
        | = 24 
     return 4 * fac(3) ->(4 * 6)
                  | = 6 
         return 3 * fac(2) ->(3 * 2)
                      | = 2 
             return 2 * fac(1) ->(2 * 1)
                          | = 1 
                 return 1 * fac(0) ->(1 * 1)
                              | = return 1 -> caso base
    '''

# -Calcular el valor de un elemento concreto (según su posición) en la 
#  sucesión de Fibonacci (la función recibe la posición).
# n : |0|1|2|3|4|5|6|..
# fb: |0|1|1|2|3|5|8|..
#      |+|=^   |+|=^ ..
def fibonacci(n: int) -> int:
    if n <= 1: 
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        # explicación
        '''
                            return 3
                  fib(3)      / \    fib(2)
                   / \ =2      +      / \ =1
             fib(2) + fib(1)    fib(1) + fib(0) -> caso base
              / \ =1
        fib(1) + fib(0) -> caso base
        '''
# NOTE: Este enfoque recursivo puede ser ineficiente para valores grandes de "n".
#___________________________________
print(f"""
Factorial de 4: 
{factorial(4)}
Valor según posición 4 en Fibonacci:
{fibonacci(4)}
""")
