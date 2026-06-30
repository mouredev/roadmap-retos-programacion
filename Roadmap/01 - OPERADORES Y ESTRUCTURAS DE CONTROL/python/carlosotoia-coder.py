"""
Operadores
"""
# Operadores aritméticos
print(f"Suma: {5 + 3}")  # Suma
print(f"Resta: {5 - 3}")  # Resta
print(f"Multiplicación: {5 * 3}")  # Multiplicación
print(f"División: {5 / 3}")  # División
print(f"División entera: {5 // 3}")  # División entera
print(f"Residuo: {5 % 3}")  # Residuo
print(f"Potencia: {5 ** 3}")  # Potencia

#Operadores de comparación
print(f"Es igual: {5 == 3}")  # Es igual
print(f"Es diferente: {5 != 3}")  # Es diferente
print(f"Es mayor: {5 > 3}")  # Es mayor
print(f"Es menor: {5 < 3}")  # Es menor
print(f"Es mayor o igual: {5 >= 3}")  # Es mayor o igual
print(f"Es menor o igual: {5 <= 3}")  # Es menor o igual

#Operadores lógicos
print(f"Y lógico: {True and False}")  # Y lógico
print(f"O lógico: {True or False}")  # O lógico 
print(f"No lógico: {not True}")  # No lógico

#operadores de asignación
x = 5
print(f"x = {x}")  # Asignación
x += 2
print(f"x += 2: {x}")  # Asignación con suma
x -= 2
print(f"x -= 2: {x}")  # Asignación con resta
x *= 2
print(f"x *= 2: {x}")  # Asignación con multiplicación
x /= 2
print(f"x /= 2: {x}")  # Asignación con división
x //= 2
print(f"x //= 2: {x}")  # Asignación con división entera
x %= 2
print(f"x %= 2: {x}")  # Asignación con residuo
x **= 2
print(f"x **= 2: {x}")  # Asignación con potencia

#Operadores de identidad
a = [1, 2, 3] 
b = a
print(f"a is b: {a is b}")  # Identidad
c = [1, 2, 3]
print(f"a is c: {a is c}")  # No identidad  


#operadores de pertenencia
lista = [1, 2, 3, 4, 5]
print(f"3 in lista: {3 in lista}")  # Pertenencia
print(f"6 not in lista: {6 not in lista}")  # No pertenencia

#operadores bit a bit
x = 5  # 0101 en binario
y = 3  # 0011 en binario
print(f"x & y: {x & y}")  # AND bit a bit
print(f"x | y: {x | y}")  # OR bit a bit
print(f"x ^ y: {x ^ y}")  # XOR bit a bit

"""
Estructuras de control
"""
# Condicionales
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

# Iteraciones

for i in range(5):
    print(f"Iteración: {i}")

# Bucle while   

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1 

#manejo de excepciones
try:
    numero = int(input("Ingresa un número: "))
    print(f"El número ingresado es: {numero}")  
except ValueError:
    print("Por favor, ingresa un número válido.")


# extra

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(f"{i}")

