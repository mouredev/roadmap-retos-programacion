# CONCEPTO de recursividad: proceso mediante el que una función se llama a sí misma de forma repetida, hasta satisfacer una determinada condición
# Ejemplo de la funcion recursiva
def impresion_numeros(n):
  if n < 0:
    return
  else:
    print(n)
    impresion_numeros(n - 1)

# llamamos a la función para que imprima los numero del 100 al 0
impresion_numeros(100)

# ---------
#   Extra
# ---------

# Funcion recursiva para calcular el factorial de un número
def calculo_factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * calculo_factorial(n - 1)

# Ejemplo de uso pasandole el número
num = 5
factorial = calculo_factorial(num)
print(f'El factorial del número {num} es: {factorial}')


# Funcion recursiva para calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci
def valor_fibonacci(n):
  if n <= 0:
    print("La posición tiene que ser mayor que cero")
    return 0
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return valor_fibonacci(n-1) + valor_fibonacci(n-2)

numero = 8
fib = valor_fibonacci(numero)
print(f'El valor de fibonacci del número {numero} es: {fib}')
