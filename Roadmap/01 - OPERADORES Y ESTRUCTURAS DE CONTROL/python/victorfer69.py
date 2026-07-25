#OPERADORES

#Operadores artméticos
print(f"Suma: 2 + 3 = {2+3}")
print(f"Resta: 2 - 3 = {2-3}")
print(f"Multiplicación: 2 * 3 = {2*3}")
print(f"Exponente: 2 ** 3 = {2**3}")
print(f"División: 2 / 3 = {2/3}")
print(f"División entera: 2 // 3 = {2//3}")
print(f"Módulo o resto de la división: 2 % 3 = {2&3}")
print("==================================================")

#Operadores de comparación
print(f"Igualdad: 2 == 3 es {2 == 3}")
print(f"Desigualdad: 2 != 3 es {2 != 3}")
print(f"Mayor que: 2 > 3 es {2 > 3}")
print(f"Mayor o igual que: 2 >= 3 es {2 >= 3}")
print(f"Menor que: 2 < 3 es {2 < 3}")
print(f"Menor o igual que: 2 <= 3 es {2 <= 3}")
print("==================================================")

#Operadores lógicos
print(f"AND &&: 2 + 1 = 3 and 10 - 1 = 9 es {2 + 1 == 3 and 10 - 1 == 9}")
print(f"OR ||: 2 + 1 = 3 and 10 - 1 = 8 es {2 + 1 == 3 or 10 - 1 == 8}")
print(f"NOT !: not 2 + 1 = 4 es {not 2 + 1 == 4}")
print("==================================================")

#Operadores de asignación
a = 11
print(a)
a += 1      #suma y asignacion
print(a)
a -= 1      #resta y asignacion
print(a)
a *= 2      #multiplicacion y asignacion
print(a)
a /= 2      #division y asignacion
print(a)
a %= 2      #modulo y asignacion
print(a)
a **= 1      #exponente y asignacion
print(a)
a //= 1      #division entera y asignacion
print(a)
print("==================================================")

#Operadores de identidad
b = 1.0
print(f"a is b es {a is b}")
b = a
print(f"a is b es {a is b}")
b = 1.0
print(f"a is not b es {a is not b}")
b = a
print(f"a is not b es {a is not b}")
print("==================================================")

# Operadores de pertenencia
print(f"'o' in 'victor' = {'o' in 'victor'}")
print(f"'a' in 'victor' = {'a' in 'victor'}")
print(f"'o' not in 'victor' = {'o' not in 'victor'}")
print(f"'a' not in 'victor' = {'a' not in 'victor'}")
print("==================================================")

# Operadores de bit (en binario)
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000
print("==================================================")


#Estructuras de control

# Condicionales
a = "victor"

if a == "victor":
    print("a es 'victor'")
elif a == "no":
    print("a es 'no'")
else:
    print("a no es 'victor' ni 'no'")

print("==================================================")

# Bucle for
for i in range(3):
    print(i)

print("==================================================")

#Bucle while
i = 0
while i <= 10:
    print(i)
    i += 1

print("==================================================")

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

print("==================================================")



#DIFICULTAD EXTRA

#Recorremos numeros del 10 al 55
for i in range(10, 56):
    #Numero par && no 16 && no multiplo de 3
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)