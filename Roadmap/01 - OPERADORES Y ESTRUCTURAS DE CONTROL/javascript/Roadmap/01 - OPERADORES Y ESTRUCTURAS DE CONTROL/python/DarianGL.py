"""TIPOS DE OPERADORES"""

# La interpolacion permite agregar codigo a una cadena de texto (f,{})

# OPERADORES ARITMETICOS
print(f"Suma: 7 + 8 = {7 + 8}") # Operador de Suma (+)
print(f"Resta: 20 - 5 = {20 - 5}") # Operador de Resta (-)
print(f"Multiplicación: 3 * 5 = {3 * 5}") # Operador de Multiplicación (*)
print(f"División: 10 / 3 = {10 / 3}") # Con este operador se pueden realizar divisiones con decimales (/)
print(f"Módulo: 14 % 10 = {14 % 10}") # Este operador sirve para calcular el residuo de una división (%)
print(f"Exponente: 10 ** 3 = {10 ** 3}") # Este operador sirve para realizar operaciones exponenciales (**)
print(f"División entera: 10 // 3 = {10 // 3}") # Con este operador se realizan divisiones sin decimal (//)

# OPERADORES DE COMPARACIÓN
variable_1 = "Hola"
variable_2 = "Adios"
print(f"Igualdad: variable_1 == variable_2 {variable_1 == variable_2}") # Operador de Igualdad (==)
print(f"Desigualdad: variable_1 != variable_2 {variable_1 != variable_2}") # Operador de Desigualdad (!=)
print(f"Mayor o igual que: 15 >= 8 {15 >= 8}") # Operador de Mayor o igual que (>=) (alt + 62)
print(f"Menor o igual que: 8 <= 15 {8 <= 15}") # Operador de Menor que (<=) (alt + 60)

# OPERADORES LÓGICOS
print(f"And &&: 7 + 8 == 15 and 10 - 2 == 8 {7 + 8 == 15 and 10 - 2 == 8}") # Operador and (And, &&)
print(f"Or ||: 7 + 8 == 16 or 10 - 2 == 8 {7 + 8 == 16 or 10 - 2 == 8}") # Operador Or (Or, ||)
print(f"Not !: Not 7 + 8 == 16 {not 7 + 8 == 16}") # Operador de negación (Not, !)

# OPERADORES DE ASIGNACIÓN
number = 10
print(f"Asignación: {number}") # Operador de Asignación (=)
number += 10
print(f"Suma y asignación: {number}") # Operador de Suma y Asignacion (+=)
number -= 5
print(f"Resta y Asignación: {number}") # Operador de Resta y Asignacion (-=)
number *= 2
print(f"Multiplicación y Asignación: {number}") # Operador de Multiplicación y Asignacion (*=)
number /= 2
print(f"División y Asignación: {number}") # Operador de División y Asignación (/=)
number %= 2
print(f"Módulo y Asignación: {number}") # Operador de Módulo y Asignación (%=)
number **= 2
print(f"Exponente y Asignación: {number}") # Operador de Exponente y Asignación (**=)
number //= 1
print(f"División entera y Asignación: {number}") # Operador de División entera y Asignación (//=)

# OPERADORES DE IDENTIDAD (sirve para comparar la identidad de las variables)
new_number = 1.0
print(f"number is new_number {number is new_number}") # Operador de identidad (is)
print(f"number is not new_number {number is not new_number}") # Operador de identidad (is not)

# OPERADORES DE PERTENENCIA
print(f"'Y' in 'Python' = {'y' in 'python'}") # Operador de Pertenencia (in)
print(f"'X' not in 'Python' = {'x' not in 'python'}") # Operador de Pertenencia (not in)
print(f"'5' in '888' = {'5' in '888'}")

# OPERADORES DE BIT (Comparan bit pot bit y hacen operaciones en binario)
a = 8 # 1000
b = 10 # 1010
print(f"AND: 8 & 10 = 1000 = {a & b}") # Operador de bit And (&) (si dos bits son igual a 1 el resultado es 1)
print(f"OR: 8 | 10 = 1010 = {a | b}") # Operador de bit Or (|) (si al menos uno de los dos bits es uno el resultado es 1)
print(f"XOR: 8 ^ 10 = 0010 = {a ^ b}") # Operador de bit Xor (^, alt + 94) (Si los dos bits son diferentes el resultado es 1 y si son iguales es 0)
print(f"NOT: ~8 = {~a}") # Operador de bit NOT (~, alt + 126) (invierte el valor del numero bit a bit)
print(f"Desplazamiento derecha: 10 >> 3 = {b >> 3}") # Desplaza a la derecha los bits el numero de veces indicado (>>)
print(f"Desplazamiento izquierda: 10 << 1 = {b << 1}") # Desplaza a la izquierda los bits el numero de veces indicado (<<)

"""ESTRUCTURAS DE CONTROL"""

# ESTRUCTURAS CONDICIONALES
string = "Xion"
if string == "Roxas":
    print("string es 'Roxas'")
elif string == "Axel":
    print("string es 'Axel'")
else:
    print("String es 'Xion'")

# ESTRUCTURAS ITERATIVAS
for i in range(11): # Sirve para crear rangos
    print(i)
i = 0
while i <= 10: # Sirve para crear bucles
    print(i)
    i += 2

# Estructuras de Excepción
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Finalizado el manejo de excepciones")


"""EXTRA"""
for my_number in range(10, 56):
    if my_number % 2 == 0 and my_number % 3 != 0 and my_number != 16:
        print(my_number)
