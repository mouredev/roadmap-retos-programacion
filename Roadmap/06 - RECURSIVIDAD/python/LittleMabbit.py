'''
def num(x):
  if x > -1:
    print(x)
    num(x-1)
  else:
    pass

num(100)
'''
## -- EXTRA --

def factorial(x):
  if x == 0 or x == 1:
    return 1
  else:
    return x * factorial(x - 1)

numero = 7
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

def fibonacci_recursivo(n):
    if n <= 1: # Retornamos el valor que se introduce si es igual o menor a 1.
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) # Utilizamos la formula, en donde tomamos 'n' y le restamos uno, a eso le sumamos el valor de 'n' con dos dígitos restados, y así nos queda la formula.

for i in range(12): # Creamos 12 veces el número que recibe la función fibonacci y así podemos calcular mejor.
  print(fibonacci_recursivo(i), end="-")
