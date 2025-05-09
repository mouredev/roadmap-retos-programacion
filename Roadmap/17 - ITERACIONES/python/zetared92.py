# RETO 17 ITERACIONES

"""
EMPLEA 3 MECANISMOS DIFERENTES PARA 
IMPRIMIR NÚMEROS DEL 1-10 MEDIANTE ITEACIÓN
"""

# FOR
for i in range(1,11):
    print(i)

# WHILE
i = 1
while i <= 10:
    print(i)
    i += 1

# RECURSIVIDAD
def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

count_ten()

# Extra

print("🧩 DIFICULTAD EXTRA - MECANISMOS PARA ITERAR VALORES 🧩")

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["z", "e", "t", "a"]):
    print(e)

for i, e in enumerate(sorted(["z", "e", "t", "a"])):
    print(f"Index: {i}, value: {e}")