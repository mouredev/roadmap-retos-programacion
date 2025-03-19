a = 3
b = 4
x = [5]
y = [6]

def program1(a, b):
    aux = a
    a = b
    b = aux

    return [a, b]

def program2(x, y):
    aux = x[0]
    x[0] = y[0]
    y[0] = aux

newAB = program1(a, b)
program2(x, y)

print(f"A value: {a}")
print(f"New A value: {newAB[0]}")
print(f"B value: {b}")
print(f"New B value: {newAB[1]}")
print(f"X value: {x[0]}")
print(f"New X value: {x[0]}")
print(f"Y value: {y[0]}")
print(f"New Y value: {y[0]}")
