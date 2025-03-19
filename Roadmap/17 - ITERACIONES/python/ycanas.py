# ------ I. Ejercicio

# 1). for

for i in range(1, 11):
    print(i)

# 2). while

c: int = 1

while c < 11:
    print(c)
    c = c + 1

# 3).

c: list[int] = range(1, 11)

for i in c:
    print(i)


# ------ Extra

# 4). recursive

def recursive(n):
    if n == 10:
        print(n)
        return
    
    print(n)
    recursive(n + 1)


recursive(1)

# 5). iter
numbers = iter(range(1, 11))
print(*numbers)

# 6). iter - next

numbers = iter(range(1, 11))

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

# 7). list comprehension

[print(i) for i in range(1, 11)]
