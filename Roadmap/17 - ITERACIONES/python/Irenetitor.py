#Exercise
for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1


def count(i=1):
    if i <= 10:
        print(i)
        count(i + 1)

count()

#Extra Exercise

for n in (1, 4, 6 , 8, 9):
    print(n)

for n in {1, 4, 6 , 8, 9}:
    print(n)

for n in [1, 4, 6 , 8, 9]:
    print(n)

for n in [1, 4, 6 , 8, 9]:
    print(n)

for n in {1: "i", 4: "r", 6: "e", 8: "n", 9: "e"}:
    print(n)

for n in {1: "i", 4: "r", 6: "e", 8: "n", 9: "e"}.values():
    print(n)


for n in reversed([1, 4, 6 , 8, 9]):
    print(n)

for c in "iteration":
    print(c)

print(*[i for i in range(1, 11)])

for n in sorted(["i", "t", "e", "r", "a", "t", "i", "o", "n"]):
    print(n)

for i,n in enumerate(["i", "t", "e", "r", "a", "t", "i", "o", "n"]):
    print(f"Index: {i}, value: {n}")
