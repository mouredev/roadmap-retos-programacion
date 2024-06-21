#Operadores

#Operadores artimeticos
print("*****Operadores Aritmeticos*****")
a = 8
b=8
print(f"Suma: 8 + 8 = {a + b}")
print(f"Resta: 8 - 8 = {a - b}")
print(f"Multiplicacion: 8 * 8 = {a * b}")
print(f"Division: 8 / 8 = {a / b}")
print(f"Modulo: 8 % 8 = {a % b}")
print(f"Potencia: 8 ** 8 = {a ** 2}")
print(f"Division Entera: 8 // 8 = {a // b}\n")

#Operadores de asignacion
print("*****Operadores de asignacion*****")
num = 11
print(f"Asignacion simple: {num}")
num += 1
print(f"Suma y asigna: {num}")
num -= 11
print(f"Resta y asigna: {num}")
num *= 2
print(f"Multiplica y asigna: {num}")
num /= 2
print(f"Divide y asigna: {num}")
num %= 2
print(f"Modulo y asigna: {num}")
num **= 1
print(f"Exponenciacion y asigna: {num}")
num //= 1
print(f"Division entera y asigna: {num}\n")

#Operadores de Comparacion
print("*****Operadores de comparacion*****")
print(f"Igualdad: 8 == 8 = {8 == 8}")
print(f"Distinto de: 8 != 8 = {8 != 8}")
print(f"Mayor que: 8 > 6 = {8 > 6}")
print(f"Menor que: 8 < 6 = {8 < 6}")
print(f"Mayor o igual que: 16 >= 8 = {16 >= 8}")
print(f"Menor o igual que: 8 <= 4 = {8 <= 4}\n")

#Operadores logicos
print("*****Operadores Logicos*****")
print(f"AND &&: 2 + 2 = 4 and 3 - 1 = 2 = {2 + 2 == 4 and 3 - 1 == 2}")
print(f"OR ||: 2 + 2 = 4 or 3 - 1 = 2 = {2 + 2 == 4 or 3 - 1 == 2}")
print(f"NOT !: not 2 + 2 == 5 = {not 2 + 2 == 5}\n")

#Operadores de Identidad
print("*****Operadores de Identidad*****")
other_num = num
print(f"other_num is num = {other_num is num}")
print(f"other_num is not num = {other_num is not num}\n")

#Operadores de Pertenencia
print("*****Operadores de pertenencia*****")
print(f"'v' in 'victore16' = {'v' in 'victore16'}")
print(f"'j' not in 'victore16' = {'j' not in 'victore16'}\n")

#Operadores de bit
a = 10 # 1010
b = 3 # 0011

print("*****Operadores de bit*****")
print(f"AND: 10 & 3 = {10 & 3}") #0010
print(f"OR: 10 | 3 = {10 | 3}") #1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001
print(f"NOT: ~10 = {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}\n") #10100

# -----------Estructuras de control --------------
print("*****ESTRUCTURAS DE CONTROL*****\n")
#Estructuras condicionales
print("*****Estructuras condicionales*****\n")
condition = 11

if condition == 11:
    print("Mi condicion se cumplio\n")
elif condition > 11:
    print("Mi segunda condicion se cumplio")
else:
    print("Ninguna de las condiciones se cumplio")

#Estructuras de bucle
print("*****Estructuras de bucle*****")
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

#Control de excepciones
print("*****Control de excepciones*****")
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones\n")

#Extra
print("*****Ejercicio Extra*****")

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)