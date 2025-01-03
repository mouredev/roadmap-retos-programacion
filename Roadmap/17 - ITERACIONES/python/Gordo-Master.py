# 17 - Iteraciones

for i in range(10):
    print(i+1)

contador = 0
while contador < 10:
    contador += 1
    print(contador)


iterador = iter([i+1 for i in range(10)])

for i in iterador:
    print(i)

"""
Ejercicio extra
"""
contador = 0
def generador():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10

for i in generador():
    print(i)

def count_from_1_to(num):
    if not num == 1:
        count_from_1_to(num-1)
        print(num)
    else:
        print(num)

count_from_1_to(10)

for e in [1,2,3,4]:
    print(e)

for e in {1,2,3,4}:
    print(e)

for e in (1,2,3,4):
    print(e)

for e in {1:"a",2:"b",3:"c",4:"d"}:
    print(e)

for e in {1:"a",2:"b",3:"c",4:"d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep = "\n")

for c in "Python":
    print(c)

for e in reversed([1,2,3,4]):
    print(e)

for e in sorted(["G","O","R","D","O"]):
    print(e)

for n, e in enumerate(sorted(["G","O","R","D","O"])):
    print(f"{n}:{e}")
