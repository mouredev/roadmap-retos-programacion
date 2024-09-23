# Operadores
print("OPERADORES ARITMETICOS\n")

print(f"Suma 2+2 = {2+2}")
print(f"Resta 2-2 = {2-2}")
print(f"Multiplicacion 2*2 = {2*2}")
print(f"Exponente 2**2 = {2**2}")
print(f"Division 2/2 = {2/2}")
print(f"Division entera 2//2 = {2//2}")
print(f"Resto 2%2 = {2%2}")

print("\nOPERADORES DE COMPARACION\n")

print(f"Igualdad 5 == 5 es {5==5}")  # true
print(f"Igualdad 2 < 5 es {5==5}")  # true
print(f"Igualdad 5 > 3 es {5==5}")  # true
print(f"Igualdad 5 >= 5 es {5==5}")  # true
print(f"Igualdad 5 <= 5 es {5==5}")  # true

print("\nOPERADORES LOGICOS\n ")

print(f"AND 4 <= 5 and 5 > 1 es = {4<=5 & 5 > 1}")
print(f"OR 6 <= 5 or 0 > 1 es = {6<=5 | 0 > 1}")
print(f"NOT 6 <= 5 es = {not 6<=5}")  # true
print(f"NOT 5 <= 5 es = {not 5<=5}")  # false

print("\nOPERADORES DE ASIGNACION\n ")

number = 5
number += 2  # 7

number2 = 4
number2 -= 2  # 2

number3 = 6
number3 *= 2  # 12

number4 = 8
number4 //= 2

print(
    f"Suma = {number}\nResta = {number2}\nMultplicacion = {number3}\nDivision = {number4}"
)

print("\nOPERADORES DE PERTENENCIA\n ")

print(f"'P' in Password? = {'P' in 'Password'}")
print(f"'P' in Password? = {'P' not in 'Password'}")

print("\nCONDICIONALES\n ")

name = "Andres"

if len(name) >= 5:
    print("Tu nombre tiene mas de 5 caracteres")
elif len(name) < 5 and len(name) >= 1:
    print("Nombre corto")
else:
    print("No hay nombre")


print("\nITERADORES\n")

index = 0

print("\nFor:\n")
for item in range(5):
    print(f"Numero [{item + 1}]")

print("\nWhile:\n")
while index < 5:
    print(f"Numero [{index + 1}]")
    index += 1

print("\nEXCEPCIONES\n")

try:
    print(2 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Fin del programa")

print("\nEXTRA\n")

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
