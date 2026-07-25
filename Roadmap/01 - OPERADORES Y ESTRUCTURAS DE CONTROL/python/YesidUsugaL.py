
# Operadores Aritmeticos
a = 10
b = 3

print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicacion
print(a / b) # Division
print(a % b) # Modulo
print(a ** b) # Exponencia
print(a // b) # Division Entera

# Operadores de comparacion
print("-------------------")

print(a == b) # Igual
print(a != b) # No igual
print(a > b) # Mayor que
print(a < b) # Menor que
print(a >= b) # Mayor o igual que
print(a <= b) # Menor o igual que

# Operadores Logicos
print("-------------------")

x = True
y = False

print(x and y) # Devuelve True si ambas declaraciones son True
print(x or y) # Devuelve True si solo 1 de las declaraciones es True
print(not x) # Revierte el resultado, si es False el resultado es True
print(not y) # Revierte el resultado, si es False el resultado es True

# Operadores de Asignacion
print("-------------------")
a = 10 # Asigna el valor de la derecha al de la izquierda
print(a)

a += 5 #Hace una suma y le añade el valor ==  a = a + 5
print(a)

a = 10
a -= 3 #Hace una resta y le añade el valor ==  a = a - 3
print(a)

a = 10
a *= 3 #Hace una multiplicacion y le añade el valor ==  a = a * 3
print(a)

a = 10
a /= 3 #Hace una division y le añade el valor ==  a = a / 3
print(a)

a = 10
a //= 3 #Hace una division entera y le añade el valor ==  a = a // 3
print(a)

a = 10
a %= 3 #Hace un modulo y le añade el valor ==  a = a % 3
print(a)

a = 10
a **= 3 #Hace una exponencia y le añade el valor ==  a = a ** 3
print(a)

# Operadores de identidad
print("-------------------")
a = [1, 2]
b = a
c = [1, 2]
 
print(a is b) # Retorna True si ambas variables son el mismo objeto
print(a is c) # Retorna True si ambas variables son el mismo objeto
print(a is not c) # Retorna True si ambas variables NO son el mismo objeto

# Operadores de membresia
print("-------------------")
number_list = [1, 2, 3, 4]

print(2 in number_list) # Retorna True si una secuencia con el valor exacto se encuentra en el objeto
print(5 not in number_list) # Retorna True si una secuencia con el valor exacto NO se encuentra en el objeto

# Operadores Bitwise
print("-------------------")
a = 5   # 0101
b = 3   # 0011

print(a & b)   # Coloca cada bit a 1 si ambos bits son 1 AND (1 = 0001)
print(a | b)   # Coloca cada bit a 1 si uno de los 2 bits es 1 OR (7 = 0111)
print(a ^ b)   # Coloca cada bit a 1 si solo uno de 2 bits es 1 XOR(6 = 0110)
print(~a)      # Invierte todos los bits NOT 5 → -6
print(a << 1)  # Mueve a la izquiera empujando ceros de derecha a izquierda Left shift → 10 (1010)
print(a >> 1)  # Mueve a la derecha empujando copias del bit más a la izquierda Right shift → 2 (0010)

# Estructuras de control
# Condicionales
print("-------------------")
x = 10
if x >= 11:
    print("Mayor que 10")
elif x == 10:
    print("Es 10")
else:
    print("Menor que 10")

print("-------------------")
# Iterativa / Bucle
i = 0
while i < 6:
    print(i)
    i += 1

print("-------------------")
number_list = [1, 2, 3, 4]
for n in number_list:
    print(n)
    n =+ 1

print("-------------------")
# Excepciones
try:
    a = 10
    b = 5
    result = a / b
    print(result)

except ZeroDivisionError:
    print("No puedes dividir por 0")
finally:
    print("Ejecucion finalizada")


# EXTRA
print("-------------------")
for i in range(10 ,56):

    x = i % 2
    y = i % 3

    if x == 0 and y != 0 and i != 16:
        print(i)
    i += 1