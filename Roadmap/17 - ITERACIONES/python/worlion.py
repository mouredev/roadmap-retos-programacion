"""
* EJERCICIO: Iteradores
"""

# While
x = 1
print("\nIterando con el while...")
while x <= 10: print(x); x+=1

# For range
print("\nIterando con el for...")
for x in range(1,11):  print(x)

# Iterate list with map O_O
print("\nIterando con el list(map)...")
list(map(print, range(1, 11)))

"""
* DIFICULTAD EXTRA (opcional):
"""

# Recursividad (No es iteración)

def print_to(x: int):
    if(x > 0):
        print_to(x-1)
        print(x)
        
print("\nCon recursividad:")
print_to(10)