"""/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
"""

# Métodos Básicos

# 1. For:
print("1. For")
for num in range(10):
    print(num + 1)

# 2. While
print("\n2. While")
number = 0

while number < 10:
    number += 1
    print(number)

# 3. List Comprehension
print("\n3. List Comprehension")
[print(n) for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""

# 4. Map y lambda
print("\n4. Map y Lambda")
numbers = list(map(lambda x: x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
for n in numbers:
    print(n)

# 5. Generator Expression
print("\n5. Generator Expression")
gen = (i for i in range(1, 11))
print(gen) # <generator object <genexpr> at 0x7a17b4734a00>
for num in gen:
    print(num)

# 6. Generator Function

print("\n6. Generator Function")

def generator_function(limit):
    num = 0
    while num < limit:
        num += 1
        yield num


for num in generator_function(10):
    print(num)


# 7. Recursion
print("\n7. Recursion")

def print_number(n=1):
    if n > 10:
        return
    print(n)
    print_number(n+1)

print_number(1)

# 8. Next and Iter
"""Creamos un objeto iter y lo iteramos manualmente"""

print("\n8. Next and Iter")

def next_and_iter():
    numbers_iter= iter(range(1,11))
    while True:
        try:
            print(next(numbers_iter))
        except StopIteration:
            print("Iteración finalizada")
            return
    

next_and_iter()

# 9. Iterator Class
print("\n9.Iterator Class")

class CounterClass:
    def __init__(self, current, limit) -> None:
        self.current = current
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        current = self.current
        self.current += 1
        return current
    

numbers = [num for num in CounterClass(1, 10)]
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("No me alcanzo para llegar al num 10. Lo siento :(")