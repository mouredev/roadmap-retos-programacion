#17 { Retos para Programadores } ITERACIONES

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

"""
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

"""

import time

# Short for print
log = print

log('Retosparaprogramadores #17')

# For loop
for i in range(1, 11):
    log(i) # logs nums from 1 to 10

# While loop
count = 0
while count < 10:
    count += 1
    log(count) # logs nums from 1 to 10

# forEach equivalent using a for loop
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    log(n) # logs nums from 1 to 10 

# Extra Difficulty Exercise

# do while equivalent using a while loop
i = 0
while True:
    log(i) # will log nums form 0 to 4
    i += 1
    if i >= 5:
        break

# map equivalent using list comprehension
arr = [1, 2, 3, 4, 5]
doubled = [value * 2 for value in arr]
log(doubled)  # [2, 4, 6, 8, 10]

# filter equivalent using list comprehension
arr1 = [1, 2, 3, 4, 5]
even_numbers = [value for value in arr1 if value % 2 == 0]
log(even_numbers)  # [2, 4]

# reduce equivalent using functools.reduce
from functools import reduce
arr2 = [1, 2, 3, 4, 5]
sum_result = reduce(lambda total, current: total + current, arr2, 0)
log(sum_result)  # 15

# some equivalent using any()
arr3 = [1, 2, 3, 4, 5]
has_even = any(value % 2 == 0 for value in arr3)
log(has_even)  # True

# every equivalent using all()
arr4 = [1, 2, 3, 4, 5]
all_even = all(value % 2 == 0 for value in arr4)
log(all_even)  # False

# For of equivalent using a for loop
arr5 = [1, 2, 3, 4, 5]
for value in arr5:
    log(value)  # Logs: 1 2 3 4 5

# Iteration with enumerate (similar to entries)
arr6 = ['a', 'b', 'c']
for index, value in enumerate(arr6):
    log(index, value)  # 0 a 1 b 2 c 3

# Iteration with items (similar to Object.entries)
obj1 = {'a': 1, 'b': 2, 'c': 3}
for key, value in obj1.items():
    log(key, value)  # a 1 b 2 c 3

# Iteration with keys
arr7 = ['a', 'b', 'c']
for index in range(len(arr7)):
    log(index)  # 0 1 2

# Iteration with keys of a dictionary
obj2 = {'a': 1, 'b': 2, 'c': 3}
for key in obj2.keys():
    log(key)  # a b c

# Iteration with values
arr8 = ['a', 'b', 'c']
for value in arr8:
    log(value)  # a b c

# Iteration with values of a dictionary
obj3 = {'a': 1, 'b': 2, 'c': 3}
for value in obj3.values():
    log(value)  # 1 2 3

# For in equivalent using a for loop
obj = {'a': 1, 'b': 2, 'c': 3}
for key in obj:
    log(f"{key}: {obj[key]}")  #  a: 1 b: 2 c: 3

