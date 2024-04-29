"""
Ejercicio
"""
# For
for i in range(1, 11):
    print(i)

# While
i = 1
while i <= 10:
    print(i)
    i += 1

# Recursividad


def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)


count_ten()

"""
Extra
"""

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

for e in sorted(["m", "o", "u", "r", "e"]):
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Índice: {i}, valor: {e}")
