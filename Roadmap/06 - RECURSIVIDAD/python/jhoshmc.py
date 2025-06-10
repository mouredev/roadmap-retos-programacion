"""
! EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
"""

def ejercicio():
  numero=100
  conteoRecursivo(numero)

def conteoRecursivo(numero):
  if numero == 0:
    print(f"numero: {numero}")
    return
  if numero >0:
    print(f"numero: {numero}")
    return conteoRecursivo(numero-1)
  
ejercicio()

"""
! DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def extra():
  numeroFactorial= int(input("ingrese el numero factorial: "))
  resultadoFactorial= factorialRecursivo(numeroFactorial)
  print("\n\t numero factorial \n")
  print(f"el factorial del numero {numeroFactorial}! es: {resultadoFactorial}")
  print("\n\t numero fibonacci \n")
  posicionFibonacci=int(input("ingrese la posicion fibonacci: "))
  resultadoFibonacci = fibonacciRecursivo(posicionFibonacci)
  print(f"el numero fibonacci en la posicion {posicionFibonacci} es: {resultadoFibonacci}")

def factorialRecursivo(numero)->int:
  if numero == 1:
    return 1
  if numero > 1:
    return numero * factorialRecursivo(numero-1)
  
def fibonacciRecursivo(numero)->int:
  if numero == 0:return 0
  if numero == 1: return 1
  return fibonacciRecursivo(numero-1)+fibonacciRecursivo(numero-2)

extra()