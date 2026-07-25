# Operadores aritméticos

print(10+3)#Suma
print(10-3)#Resta
print(10*3)#Multiplicación
print(10/3)#División
print(10//3)#División entera
print(10%3)#Módulo
print(10**3)#Exponente

# Operadores de comparación

print(10==3)#Igualdad
print(10!=3)#Desigualdad
print(10>3)#Mayor que
print(10<3)#Menor que
print(10>=3)#Mayor o igual que
print(10<=3)#Menor o igual que

#Operadores logicos

print(10>3 and 5<2)#AND
print(10>3 or 5<2)#OR
print(not(10>3))#NOT

#Operadores de asignación

num = 10 #asignación
print(num)
num += 5 #asignación con suma
print(num)
num -= 3 #asignación con resta
print(num)
num *= 2 #asignación con multiplicación
print(num)
num /= 4 #asignación con división
print(num)
num //= 2 #asignación con división entera
print(num)
num **= 2 #asignación con exponente
print(num)
num %= 3 #asignación con módulo
print(num)

# Operadores de identidad 

num2 = 10
print(num is num2) # Identidad
print(num is not num2) # No identidad

# Operadores de pertenencia

print(num in [1, 2, 3, 4, 5]) # Pertenece
print(num not in [1, 2, 3, 4, 5]) # No pertenece

# Operadores bit a bit
print(10 & 3) # AND bit a bit
print(10 | 3) # OR bit a bit
print(10 ^ 3) # XOR bit a bit
print(~10)    # NOT bit a bit
print(10 << 2) # Desplazamiento a la izquierda
print(10 >> 2) # Desplazamiento a la derecha

#Estructuras de control

#Condicionales

num3 = 11
if num3 > 10:
    print("El numero es mayor que 10")
elif num3 == 10:
    print("El numero es igual a 10")
else:
    print("El numero es menor que 10")
    
# Iterativas

for i in range(5):
    print("Iteracion:", i)
    
valor = 0

while valor < 5:
    print(valor)
    valor += 1

# Manejo de excepciones
try:
    print(10/0)
except ZeroDivisionError:
    print("Error: Division por cero no permitida.")
    
#Extra
for number in range(10,56):
    if number % 2 ==0 and number != 16 and number % 3 == 0:
        print(number)