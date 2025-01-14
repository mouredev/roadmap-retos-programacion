# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits

a = 10
b = 3

# Operadores aritméticos
print("*************OPERADORES ARITMÉTICOS*************")
print(f"Suma: 10 + 3 = {a + b}")
print(f"Resta: 10 - 3 = {a - b}")
print(f"Mulplicación: 10 * 3 = {a * b}")
print(f"División: 10 / 3= {a / b}")
print(f"Módulo: 10 % 3= {a % b}")
print(f"Exponente: 10 ** 3 = {a ** b}")
print(f"División entera: 10 // 3 = {a // b}")

# Operadores lógicos
print("*************OPERADORES LÓGICOS*************")
print(f"AND: 20 + 5 == 25 and 30 - 15 == 15 es {20 + 5 == 25 and 30 - 15 == 15}")
print(f"OR: 20 + 5 == 25 or 30 - 15 != 15 es {20 + 5 == 25 or 30 - 15 != 15}")
print(f"NOT: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de comparación
print("*************OPERADORES DE COMPARACIÓN*************")
print(f"Igualdad: 10 == 3 es {a == b}" )
print(f"Desigualdad: 10 != 3 es {a != b}" )
print(f"Mayor que: 10 > 3 es {a > b}" )
print(f"Menor que: 10 < 3 es {a < b}" )
print(f"Mayor o igual que: 10 >= 3 es {a >= b}" )
print(f"Menor o igual que: 10 <= 3 es {a <= b}" )

# Operadores de asignación
print("*************OPERADORES DE ASIGNACIÓN*************")
my_number = 11 # asignación
print(my_number)

my_number += 1 # suma y asignacion
print(my_number)

my_number -= 1 # resta y asignacion
print(my_number)

my_number *= 3 # multiplicación y asignacion
print(my_number)

my_number /= 3 # división y asignacion
print(my_number)

my_number %= 3 # modulo y asignacion
print(my_number)

my_number **= 1 # potenciación y asignacion
print(my_number)

my_number //= 1 # devisión entera y asignacion
print(my_number)

# Operadores de identidad comparan la dirección de memoria con is
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}") # igualdad
print(f"my_number is my_new_number es {my_number is not my_new_number}") # desigualdad

# Operadores de pertenencia
print(f" a in 'marcos' = {'a' in 'marcos'}") # verifica si a pertenece o esta incluido en marcos

# Operadores de bits
c = 10 # 1010
d = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010 Compara bit a bit solo si los bit son 1-1 es 1
print(f"OR: 10 | 3 = {10 | 3}") # 1011 Compara bit a bit si al menos uno de los bit es 1 el resultado es 1 
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001 Compara bit a bit si los bit son diferentes el resultado es 1 caso contrario es 0
print(f"NOT: ~10 = {~10}") # Intercambia el valor bit a bit de cualquiera de los elementos

# Desplazamiento
print(f"Desplazamientoa la derecha: 10 >> 2 = {10 >> 2}") # 1010 -> 0010
print(f"Desplazamientoa la izquierdad: 10 << 2 = {10 << 2}") # 1010 -> 101000

"""
Estructuras de control
"""
# Condicionales
my_age = 25

if(my_age < 0):
    print("La edad tiene que ser mayor o igual a 0")
elif(my_age >= 18):
    print("Es mayor de edad")
else:
    print("Es menor edad")

# Iterativas
print("-----for-----")
for i in range(0, 11):
    print(i)

print("-----while-----")
contador = 0
while(contador <= 10):
    print(contador)
    contador += 1

# Manejo de excepciones
print("-----Manejo de errores-----")

try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha terminado el manejo de errores o excepciones")

"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

print("****EJERCICIO OPCIONAL****")
for i in range(10, 56):
    if(i % 2 == 0 and i != 16 and i % 3 != 0):
        print(i)
        