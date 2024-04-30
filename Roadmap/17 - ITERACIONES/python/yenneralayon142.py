"""
Iteraciones
"""

# FOR

for i in range(1,11):
    print(i)

#WHILE

i = 1
while i <= 10:
    print(i)
    i += 1

# RECURSIVIDAD
def count_ten(i = 1):
    if i <= 10:
        print(i)
        count_ten(i + 1)
count_ten()


"""
Ejercicio
"""

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

for i in {1,2,3,4,5,6,7,8,9}:
    print(i)

for i in {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"h",8:"i"}:
    print(i)

print(*[i for i in range(1,20)], sep='\n')

for i in "Ubosque":
    print(i)

for i in reversed([1,2,3,4]):
    print(i)

for i in sorted(["y","e","n","n","e","r"]):
    print(i)

for i,e in enumerate(sorted(["y","e","n","n","e","r"])):
    print(f"Indice: {i}, valor: {e}")
