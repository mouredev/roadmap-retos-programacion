'''
  EJERCICIO: Entiende el concepto de recursividad creando una función recursiva que imprima
  números del 100 al 0.
'''

def numbers(number = 0):
  if number == 100:
    print(number)
  else:
    print(number)
    numbers(number + 1)
  return  

print('Números: del 0 al 100 mediante recursividad')
numbers()

'''
  EXTRA
'''

# Factorial de un número concreto:

def factorial(number):
  if number == 0:
    return 1
  else:
    return number * factorial(number - 1)

while True:
  user_number = input("Introduce un número entero para calcular su factorial: ")
  if user_number.isnumeric():
    user_number = int(user_number)
    result = factorial(user_number)
    print(f'!{user_number} = {result}')
    break
  else:
    print("Por favor, introduce un número entero válido.")

# Serie de Fibonacci dada una posición como parámetro:

def fibonacci(number):
  if number == 0:
    return 0
  elif number == 1 or number == 2:
    return 1
  else:
    return fibonacci(number - 2) + fibonacci(number - 1)

while True:
  position = input("Introduce un número para calcular el valor de la serie de Fibonacci en esa posición: ")
  if position.isnumeric():
    position = int(position)
    value = fibonacci(position)
    print(f'Valor de la serie de Fibonacci en la posción {position} = {value}')
    break
  else:
    print("Por favor, introduce una posición válida.")