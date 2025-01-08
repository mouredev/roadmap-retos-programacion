# Invocar una funcion
def saludar():
  print("Hola!") # Uso de funcion print() ya existente en Python

saludar()

# Retornar un valor
def returnValue():
  return 10

returnValue()

# Retornar multiples valores
def returnMultiple():
  return 0, 1

returnMultiple()

# Funciones con parametros
def raiz(value):
  return value ** (1/2)

raiz(9)

def minMax(a, b):
  return a < b

minMax(6, 4)

# Funciones con parametros con valores por default
def byDefault(a, b = 2):
  return a + b

byDefault(3, 2)
byDefault(9) 


# DIFICULTAD EXTRA
def fizzBuzz(text1, text2):
  numbers = 0
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print(text1 + text2)
    elif i % 3 == 0:
      print(text1)
    elif i % 5 == 0:
      print(text2)
    else:
      numbers += 1
      print(i)
  print('Cantidad de numeros donde no hay texto: ', numbers)
  return numbers

fizzBuzz('fizz', 'buzz')





