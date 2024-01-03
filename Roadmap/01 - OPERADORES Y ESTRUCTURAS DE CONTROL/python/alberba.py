print("4 + 3 =", 4 + 3)
print("4 == 3 or 10==10.0 = ", 4 == 3 or 10 == 10.0)
a = 5
b = 2
print("a es b?: ", a is b)
lista = [4, a, "a"]
print("'a' in lista: ", "a" in lista)
print(" a & b : ", a | b)

if (a in lista): 
    print("La variable A esta en la lista")

while (b < 5):
    b += 1
    print("B es igual a ", b)

# Excepciones 
try:
    print("a / 0 = ", a / 0)
except ZeroDivisionError:
    print("No se puede dividir por 0")

# Dificultad extra

for i in range (10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)