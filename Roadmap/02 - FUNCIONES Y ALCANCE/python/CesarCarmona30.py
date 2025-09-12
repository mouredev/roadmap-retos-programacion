'''
  FUNCIONES
'''

# Función sin parámetros ni retorno
def greet():
  print('Hi!')

greet()

# Función con parámetros sin retorno
def greetPerson(name):
  print(f'¡Hello {name}!')

greetPerson('César')

# Función con varios parámetros sin retorno
def add(number1, number2):
  print(f'{number1} + {number2} = {number1 + number2}')

add(5, 8)

# Función con varios parámetros con retorno
def subtract(number1, number2):
  return number1 - number2

result = subtract(175, 123)
print(f'175 - 123 = {result}')

# Función con parámetros variables
def average(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum/len(args)

result = average(9, 8, 7, 9, 9, 8, 10, 10)
print(result)

# Función con parámetros variables con identificador
def capitals(**kwargs):
  for country, city in kwargs.items():
    print(f"{country} - {city}")
  return

countries = {
  'Mexico': 'Mexico City',
  'Argentina': 'Buenos Aires',
  'Spain': 'Madrid',
  'Chile': 'Santiago'
  }

capitals(**countries)  

# Funciones anónimas o lambda
exponentiate = lambda number, exponent: number ** exponent
result = exponentiate(2, 8)

print(f'2 ** 8 = {result}')

# Funciones dentro de funciones
def exterior_function(x):
    def interior_function(y):
        return y * 2
    
    result = x + interior_function(x)
    return result

operation = exterior_function(5)
print(operation)

# Funciones nativas
my_list = [5, 6, 7, 3, 6, 7, 9, 3, 5, 8]
print(f'Esta es la función nativa: print()\nMi lista: {my_list}')
print(f'Tipo de dato: {type(my_list)}')
print(f'Longitud de mi lista: {len(my_list)}')
print(f'Máximo de mi lista: {max(my_list)}')
print(f'Mínimo de mi lista: {min(my_list)}')
print(f'Suma de mi lista: {sum(my_list)}')
input('Esta es la función input, \n para continuar escribe un número: ')

'''
  VARIABLE LOCAL Y GLOBAL
'''
global global_var

global_var = "Soy global"

def myFunction():
    local_var = "Soy local"
    print(f'Accediendo a la variable global dentro de la función: {global_var}')
    print(f'Accediendo a la variable local dentro de la función: {local_var}')

myFunction()

print(f'Accediendo a la variable global fuera de la función: {global_var}')
try:
  print(f'Accediendo a la variable loca fuera de la función: {local_var}')
except NameError as err:
  print(f'Error: {type(err).__name__}')
  print(f'No se puede acceder a la variable local desde afuera de su bloque')

'''
  EXTRA
'''

def printNumbers(text1, text2):
  printed_numbers = 0
  for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
      print(f"{text1} y {text2}")
    elif number % 3 == 0:
      print(text1)
    elif number % 5 == 0:
      print(text2)
    else:
      print(f"{number}")
      printed_numbers += 1
  return printed_numbers  

prints = printNumbers(text2 = 'Múltiplo de 5', text1 = 'Múltiplo de 3')
print(prints)