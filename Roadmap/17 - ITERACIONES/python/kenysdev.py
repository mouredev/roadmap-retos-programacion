# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * ITERACIONES
# -----------------------------------

"""
 * EJERCICIO #1:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
"""
#_______________________
print("Bucle for")
for n in range(1, 11):
    print(n)

#_______________________
print("\nBucle while")
n = 1
while n <= 10:
    print(n)
    n += 1

#_______________________
print("\nfunción map()")
list(map(print, range(1, 11)))

"""
* EJERCICIO #2:
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

#_______________________
print("\nFunción filter()")
def is_even(n):
    return n % 2 == 0

filtered = list(filter(is_even, range(1, 21)))
print(filtered)

#_______________________
print("\ncon reversed()")
nums = [1, 2, 3, 4]

nums_reversed = list(reversed(nums))
print(nums_reversed)

#_______________________
print("\nIteradores personalizados")
class NumbersEvens:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 2
        return self.number

evens_iterator = NumbersEvens()
for _ in range(4):
    print(next(evens_iterator))

#_______________________
print("\ncon enumerate()")
names = ["Zoe", "Bob", "Ben"]

enumeration = list(enumerate(names, start=1))
print(enumeration)

#_______________________
print("\nFunción zip()")
names = ["Zoe", "Bob", "Ben"]
ages = [21, 22, 23]

# No es un mecanismo de iteración en el sentido tradicional.
users = list(zip(names, ages))
print(users)

#_______________________
print("\nCon recursividad")
# No es un mecanismo de iteración en el sentido tradicional.

def num(n: int):
    print(n)
    if n > 0:
        num(n - 1)
num(10)

