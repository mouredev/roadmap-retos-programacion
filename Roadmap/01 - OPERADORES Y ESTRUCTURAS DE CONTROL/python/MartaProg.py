a = 666
b = 66

#Operadores Aritméticos. 
print("----- Operadores Aritméticos -----")

print(f"Suma: 666 + 66 = {a + b}")
print(f"Resta: 666 - 66 = {a - b}")
print(f"Multiplicacíon: 666 * 66 = {a * b}")
print(f"División: 666 / 66 = {a / b}")
print(f"Módulo: 666 % 66 = {a % b}")
print(f"Potencia: 666 ** 66 = {a ** b}")
print(f"División entera: 666 // 66 = {a // b}")

#Operadores de comparación.
print("----- Operadores de comparación -----")
print(f"Mayor que: 666 > 66 --> {a > b}")
print(f"Menor que: 666 < 66 --> {a < b}")
print(f"Igual a: 666 == 66 --> {a ==b}")
print(f"Mayor o igual: 666 >= 66 --> {a >= b}")
print(f"Menor o igual: 666 <= 66 --> {a <= b}")
print(f"Diferente a: 666 != 66 --> {a != b}")

#Operadores Bit a Bit

print("----- Operadores Bit a Bit -----")
print(f"AND: 666 & 66 --> {a & b}")
print(f"OR: 666 | 66 --> {a | b}")
print(f"XOR: 666 ^ 66 --> {a ^ b}")
print(f"NOT: ~666 --> {~a}")
print(f"Desplazamiento izquierda: 666 << 2 --> {a << 2}")
print(f"Desplazamiento derecha: 666 >> 2 --> {a >> 2}")

#Operadores de asignación
print("----- Operadores de asignación -----")

x = a
x += b
print(f"{a} += {b} = {x}")

x = a
x -= b
print(f"{a} -= {b} = {x}")

x = a
x *= b
print(f"{a} *= {b} = {x}")

x = a
x /= b
print(f"{a} /= {b} = {x}")

x = a
x %= b
print(f"{a} %= {b} = {x}")

x = a
x //= b
print(f"{a} //= {b} = {x}")

x = a
x **= b
print(f"{a} **= {b} = {x}")

#Operadores Logicos
print("----- Operadores Lógicos -----")

print(f"({a} > {b}) and ({b} < 100) = {(a > b) and (b < 100)}")
print(f"({a} < {b}) or ({b} == 66) = {(a < b) or (b == 66)}")
print(f"not ({a} == {b}) = {not (a == b)}")


#Tipos de estructuras de control
#Condicionales
if a > b: 
    print(f"{a} es mayor a {b}")
elif a == b:
    print(f"{a} es igual a {b}")
else:
    print(f"{a} es menor a {b}")

#Iteratividad
#While
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    
#For
for n in range(1,6):
    print(n)
    
#Control de flujo
#Break
for i in range(10):
    if i == 5:
        break
    print(i)

#Continue
for i in range(b): 
    if i == 1: 
        continue
    print(f"i = {i}")
    
#Pass
for i in range(5): 
    if i == 3:
        pass
    print(f"i = {i}")
    
#Control de excepciones
try:
    x = int("abc")
except ValueError:
    print("¡Eso no es un número!")

#Opcional 
for i in range(10,56): 
    if i % 2 == 0 and i != 16 and i % 3 == 0:   #Tabla del  6?
        print(i)