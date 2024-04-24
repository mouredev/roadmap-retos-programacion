from itertools import count, islice
from functools import reduce
import numpy as np
'''
  EJERCICIO
'''
print('\nEJERCICIO')

print('a. For in range:')
for number in range(1, 11):
 print(number, end=' ')

number = 1
print('\nb. While:')
while number <= 10:
 print(number, end= ' ', )
 number += 1

print('\nc. Diccionario:')
dict_numbers = {'1': 2, '3': 4, '5': 6, '7': 8, '9': 10}
for key, value in dict_numbers.items():
 print(key, value, sep=' ', end=' ')

'''
  EXTRA
'''

print('\n\nEXTRA')

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]
print('\n- 1. For in con zip:')
for odd, even in zip(odds, evens):
 print(odd, even, sep=' ', end=' ')

print('\n- 2. For in enumerate:')
ten_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for index, value in enumerate(ten_letters):
  print(index + 1, end=' ')

print('\n- 3. For in slicing:')
numbers = list(range(1, 101))  # Crear una lista del 1 al 100
numbers = numbers[0:10:1] # Selecciono del 1 al 10
for number in numbers:
 print(number, end=' ')

print('\n- 4. Funcion con yield:')
def mi_generador():
  yield 1, 2, 3, 4 ,5 ,6, 7, 8, 9, 10
gen = mi_generador()
print(next(gen))

print("- 5. For in con list comprehensions:")
list_nubers = [i for i in range(1, 11)]
for number in list_nubers:  
  print(number, end=' ')

print("\n- 6. Recursividad:")
def printed(number):
 if number > 1:
  printed(number - 1)
 print(number, end=' ')
printed(10)

print("\n- 7. Map:")
numbers = list(map(lambda x: x, range(1, 11)))
for number in numbers:
    print(number, end=' ')

print("\n- 8. Filter:")
filter_numbers = list(filter(lambda x: True if x <= 10 else False, range(1, 101)))
for number in filter_numbers:
    print(number, end=' ')

print("\n- 9. Itertools:")
for number in islice(count(1), 10):
    print(number, end=' ')

print("\n- 10. Utilizando NumPy:")
numbers = np.arange(1, 11)
for number in numbers:
    print(number, end=' ')