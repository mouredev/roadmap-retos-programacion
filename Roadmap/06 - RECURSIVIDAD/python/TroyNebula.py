'''
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 '''

# Recursividad -----------------------------------------------
def func_recursive(start:int, end:int):
    if start >= end:
        print(start)
        func_recursive(start -1, end)

func_recursive(100, 0)

print()
# Función sin tener que usar la recursividad -----------------------------------------------
def func_sin():
    for i in range (100,-1,-1):
        print (i)
        i +=1

func_sin()

'''
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
'''
print()

'''El factorial de un número concreto es el producto de todos los enteros positivos desde 1 hasta ese número. 
Se representa con el símbolo "!" y se calcula multiplicando todos los números enteros positivos menores o iguales al número dado. 
Por ejemplo, el factorial de 5 (denotado como 5!) es igual a 5 × 4 × 3 × 2 × 1, que es igual a 120. 
En notación matemática, se expresa como: n! = n × (n-1) × (n-2) × ... × 2 × 1
Es importante mencionar que el factorial de 0 (0!) se define como 1 por convención matemática.'''

'''La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores. 
La secuencia comienza típicamente con los números 0 y 1, y los siguientes números son la suma de los dos números anteriores. 
Así que la secuencia comienza como: 0, 1, 1, 2, 3, 5, 8, 13, 21, y así sucesivamente.
Matemáticamente se representa así: 
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) para n > 1'''

# Factorial  -----------------------------------------------
def factorial(numero):
    if numero < 1:
        return 1
    else:
        return factorial(numero -1) * numero
print(factorial(5))

# Fibonacci  -----------------------------------------------
def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index -1) + fibonacci(index -2)
print(fibonacci(10))

# Me he complicado mucho la vida pero quería practicar otras maneras de llegar a lo mismo y crear listas al mismo tiempo
# Propuesta muy larga para factorial:
lista:list=[]

def num_factorial(f:int):
    if f>=1:
        lista.append(f)
        num_factorial(f-1)

num_factorial (5)  
print (lista)

primero:int = lista[0]
largo:int = len(lista)
ultimo:int = lista[largo - 1]

print (primero) # 5
print (largo) #5
print (ultimo) #1

def calcula_factorial(num1, num2):
    resultado = 1
    for j in range(num1, (num2 + 1)):
        resultado *= j
    return resultado

print (calcula_factorial(ultimo, primero))
