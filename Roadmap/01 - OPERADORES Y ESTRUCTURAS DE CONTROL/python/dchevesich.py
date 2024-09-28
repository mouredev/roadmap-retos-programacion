# Operadores en python

# Aritmeticos

print(1+2)
print(1-2)
print(1*2)
print(1 % 2)

# Logicos comparacion asignacion identidad pertencia
a = "hola"
b = "hola"
c = "ho"

ejemplo_negacion = 7
listanegacion = [1, 2, 3, 4, 5, 6]

if a == b or a == c:
    print("Igualdad")
else:
    print("No es igual")

if a == b and a == c:
    print("Igualdad")
else:
    print("No es igual")

if ejemplo_negacion not in listanegacion:
    print("Negación")

# Extra

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
