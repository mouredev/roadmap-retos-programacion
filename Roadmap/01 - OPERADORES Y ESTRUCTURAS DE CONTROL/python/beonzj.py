#   OPERADORES

print("## OPERADORES ##\n")

print("# Aritméticos\n")
print(f"7 + 2 = {7+2}") # Suma
print(f"5 - 2 = {5-2}") # Resta
print(f"5 * 2 = {5*2}") # Multiplicación
print(f"5 / 2 = {5/2}") # División
print(f"5 % 2 = {5%2}") # Resto de división
print(f"5 // 2 = {5//2}") # Cociente de división
print(f"5 ** 2 = {5**2}") # Exponente

print("\n\n# Relacionales\n")
print(f"5 == 2 es {5==2}") # Igual que
print(f"5 != 2 es {5!=2}") # Diferente a
print(f"5 < 2 es {5<2}") # Menor que
print(f"5 > 2 es {5>2}") # Mayor que
print(f"5 <= 2 es {5<=2}") # Menor o igual que
print(f"5 >= 2 es {5>=2}") # Mayor o igual que

print("\n\n# Lógicos\n")
print(f"1 + 2 == 3 or 2 - 1 == 1 {1 + 2 == 3 or 2 - 1 == 1}") # or
print(f"1 + 2 == 3 and 2 - 1 == 1 {1 + 2 == 3 and 2 - 1 == 1}") # and
print(f"not 2 - 1 == 2 {not 2 - 1 == 2}") # not

print("\n\n# Asignación\n")
x = 23 # Asignación
print(x) 
x += 2 # Suma y asignación
print(x)
x -= 2 # Resta y asignación
print(x)
x *= 2 # Multiplicación y asignación
print(x)
x /= 2 # División y asignación
print(x)
x %= 3 # Resto y asignación
print(x)
x //= 1 # Cociente y asignación
print(x)
x **= 2 # Exponente y asignación
print(f"{x}")

print("\n\n# Identidad\n")
y = 2
print(f"y is 2 es {y is 2}") # is
print(f"y is not 2 es {y is not 2}") # is not

print("\n\n# Pertenencia\n")
print(f"'p' in 'palabra' es {'p' in 'palabra'}")
print(f"'o' not in 'palabra' es {'p' in 'palabra'}")

print("\n\n# A nivel de bit\n")
a = 10
b = 3
print(f"a | b = {a | b}")
print(f"a ^ b = {a ^ b}")
print(f"a & b = {a & b}")
print(f"a << 2 = {a << b}")
print(f"a >> 2 = {a >> b}")
print(f"~a = {~a}")

print("\n\n## ESTRUCTURAS DE CONTROL ##\n")

print("# Condicionales\n")
number = 11
print(f"Número= {number}")
if number > 0 and number <= 10:
    print("El número es mayor a 0 e igual o menor que 10")
elif number > 10 and number <= 20:
    print("El número es mayor a 10 e igual o menor que 20")
else:
    print("El número es menor a 0 y mayor que 20")

print("\n\n# Iterativas\n")

print("for")
for i in range(11):
    print(i)

i = 0

print("\nwhile")
while i <= 10:
    print(i)
    i += 1

print("\n\n# Excepciones\n")

try:
    print(c-ac)
except:
    print("Excepción error")
finally:
    print("Fin de la exepción")


print("\n\n## TAREA EXTRA ##\n")

for x in range(10, 56):
    if x % 2 == 0 and x != 16 and x % 3 != 0:
        print(x)

