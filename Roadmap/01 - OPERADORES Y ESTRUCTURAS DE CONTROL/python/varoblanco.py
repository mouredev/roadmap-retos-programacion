#Aritmetica

print(f"Suma 10+15 = {10+15}")
print(f"Resta 10-15 = {10-15}")
print(f"Multiplicación 10*15 = {10*15}")
print(f"Division 10/15 = {10/15}")
print(f"Potencia 10^15 = {10^15}") #INCORRECTO esto hace en XOR de los numeros binarios 10 y 15 y sale el 5 en binario
print(f"Resto de division 240%2 = {240%2}")
print(f"Potencia 10**15 = {10**15}")
print(f"División entera 10//15 = {10//15}") #Recoge la parte entera del cociente

#Operadores de comparación
print(f"Menor que 10<15 = {10<15}")
print(f"Mayor que 10>15 = {10>15}")
print(f"Igual que 10==15 = {10==15}")
print(f"Distinto que 10!=15 = {10!=15}")

#Operadores de logicicos
print(f"AND 10<15 and 5<2 = {10<15 and 5<2}")
print(f"OR 10<15 or 5<2 = {10<15 or 5<2}")
print(f"NOT not 5<2 = {not 5<2}")

#Operadores de asignacion
my_variable = 1
print(my_variable)
my_variable += 1
print(my_variable)
my_variable -= 1
print(my_variable)
my_variable *= 2
print(my_variable)
my_variable /= 2
print(my_variable)
my_variable %= 1
print(my_variable)
my_variable += 2
print(my_variable)
my_variable **= 2
print(my_variable)
my_variable //= 2
print(my_variable)

#Operadores de identidad
my_new_number = my_variable
print(f"Es my_new_number = my_variable -> {my_variable is my_new_number}") #tienen el mismo objeto en memoria, son la misma cosa, aparte de mismo valor misma ubicacion en memoria
print(f"NO es my_new_number = my_variable -> {my_variable is not my_new_number}")

#Operadores de pertenencia
print(f"a in varoblanco -> {"a" in "varoblanco"}")
print(f"@ not in varoblanco -> {"@" not in "varoblanco"}")

#Operadores de bits
a = 10 # 1010
b = 3 # 0011
print(f"AND a & b = { a & b}") #0010
print(f"OR a | b = { a | b}") #1011
print(f"XOR a ^ b = { a ^ b}") #1011
print(f"NOT a ~ b = {~a}")
print(f"Desplazamiento a la derecha 2 pos. a >> 2 = {a >> 2}")
print(f"Desplazamiento a la izq 2 pos. a << 2 = {a << 2}")

"""
Estructuras de control
"""

#Condicionales
email = "varoblanco@gmail.com"
if email == "varoblanco@gmail.com":
    print("Email OK")
elif email == "VAROBLANCO@gmail.com":
    print("Bien pero está en mayus")
else:
    print("Email incorrecto")

#Iteratitas

for i in range(10):
    print(i)

i = 0

while i<=10:
    print(i)
    i+=1

try:
    print(10/2)
except:
    print("Error en codigo")
finally:
    print("Ejecutado sin problema")

"Extra"

for i in range(10,56):
    if i % 2 == 0 and i % 3 != 0 and i != 16:
        print(i)
    