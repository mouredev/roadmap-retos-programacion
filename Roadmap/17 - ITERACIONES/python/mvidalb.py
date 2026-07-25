'''
Ejercicio
'''

# For
for i in range(1,11):
    print(i)

# Wjoñe
i = 1
while i <= 10:
    print(i)
    i += 1

# Recursividad
def count(i):
    if i <= 10:
        print(i)
        count(i+1)

count(1)


'''
Ejercicio extra
'''
for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.keys():
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1,11)], sep="\n")

for c in "python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["v", "i", "d", "a", "l"]):
    print(e)

for i, e in enumerate(sorted(["v", "i", "d", "a", "l"])):
    print(f"Índice: {i}, Value: {e}")

    