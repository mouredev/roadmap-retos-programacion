# #06 Recursividad
# EJERCICIO
'''
Crea una funcion recursiva que imprima numeros del 100 al 0
'''
def numbers(number):
    if number < 0:
        return
    else:
        print(number)
        numbers(number - 1)

numbers(100)

print("\n----------------------------------------------------")
print("EXTRA DIFFICULT")
'''
Utiliza el concepto de recursividad para:
- Calcular el factorial de un numero concreto (la funcion recibe ese numero)
- Calcular el valor de un elemento concreto (segun su posicion) en la
  sucesion de Fibonacci (la funcion recibe la posicion).
'''

def factorial(number):
    if number < 0:
        print("Invalid input")
        return 0
    elif number == 0:
        return 1
    else:
        return number*factorial(number - 1)

def fibonacci(number):
    if number <= 0:
        print("Input must be greather than 0")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(f"!0 = {factorial(0)}")
print(f"!5 = {factorial(5)}")

print(f"1st Fibonacci value is {fibonacci(1)}")
print(f"2nd Fibonacci value is {fibonacci(2)}")
print(f"4th Fibonacci value is {fibonacci(4)}")
print(f"10th Fibonacci value is {fibonacci(10)}")
