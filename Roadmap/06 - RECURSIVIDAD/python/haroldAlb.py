### 06 - RECURSIVIDAD ###

# Entiende el concepto de recursividad creando una función
# recursiva que imprima números del 100 al 0. #

def cuenta_atras(n):
    print(n)
    if n > 0:
        n -= 1
        cuenta_atras(n)
    else:
        print("Fin de la cuenta atras.")

cuenta_atras(100)

### EXTRA ###

# Calcular el factorial de un número concreto (la función recibe ese número) #

def factorial(n):
    if n > 1:
        aux = factorial(n-1)
    else:
        return 1
    return aux * n

resultado = factorial(6)

print(resultado)

# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición) #

def fibonacci(n): # No me salió bien!!!
    if n > 1:
        fib_list = fibonacci(n-1)
        fib_list.append(fib_list[n-1] + fib_list[n-2])
        return fib_list
		
    else:
        fib_list = []
        fib_list.append(0)
        fib_list.append(1)
        return fib_list

posicion = fibonacci(5)	
print(posicion[-1])

# Solución de Brais

def fibo_Brais(number):
    if number <= 0:
        print("La posición tiene que ser mayor de cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibo_Brais(number - 1) + fibo_Brais(number - 2)
    
print(fibo_Brais(5))