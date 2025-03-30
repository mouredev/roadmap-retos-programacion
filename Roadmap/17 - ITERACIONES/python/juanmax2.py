"""
Iteraciones
"""
# For
for i in range(1,11):
    print(i)

# Recursividad
def contador(num = 1):
    
    if num <= 10:
        print(num)
        contador(num + 1)
    
contador()

# While
num = 1
while num <= 10:
    print(num)
    num += 1 

"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""

# For in lista
for e in [1, 2, 3, 4]:
    print(e)
    
# For in set
for e in {1, 2, 3, 4}:
    print(e)

# For in dict
for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

# For cadena de texto
for w in "Python":
    print(w)

# For en lista revertida
for e in reversed([1, 2, 3, 4]):
    print(e)

# For en una cadena de texto ordenada
for e in sorted(["j", "u", "a", "n", "m", "a"]):
    print(e)

# For con enumerate 
for i, e in enumerate(["j", "u", "a", "n", "m", "a"]):
    print(i, e)