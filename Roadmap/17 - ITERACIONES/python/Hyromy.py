# iteracion por for
for i in range(1, 11):
    print(i)

print("\n")

# iteracion por while
x = 1
while x <= 10:
    print(x)
    x += 1

print("\n")

# iteracion por recursividad
def iterar(valor:int, objetivo:int):
    print(valor)

    if valor < objetivo:
        iterar(valor +1, objetivo)

iterar(1, 10)