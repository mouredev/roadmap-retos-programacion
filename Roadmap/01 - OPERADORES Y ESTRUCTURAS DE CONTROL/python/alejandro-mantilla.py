"""
OPERADORES 
"""

# Operadores Aritméticos
"""
Operadores en interpolación
"""
print(f"Suma: 20 + 3 = {20 + 3}")
print(f"Resta: 33 - 10 = {33 - 10}")
print(f"Multiplicacion 20 * 3 = {20 * 3}")
print(f"División: 20 / 3 = {20 / 3}")
print(f"Módulo: 20 % 3 = {20 % 3}")
print(f"Exponente: 20 ** 3 = {20 ** 3}")
print(f"División entera: 20 // 3 = {20 // 3}")

# Operadores de comparación
print(f"Igualdad: 20 == 3 es {20 == 3}")
print(f"Desigualdad: 20 != 3 es {20 != 3}")
print(f"Mayor que: 20 > 3 es {20 > 3}")
print(f"Menor que: 20 < 3 es {20 < 3}")
print(f"Mayor o igual que: 20 >= 3 es {20 >= 3}")
print(f"Menor o igual que: 20 <= 3 es {20 <= 3}")

#Operadores lógicos
print(f"AND &&: 20 + 3 == 23 and 5 - 1 == 4 es: {20 + 3 == 23 and 5 - 1 == 4}") # Si ambos es verdadero la respuesta es Verdadero(True), si uno es falso la respuest es Falso(False)
print(f"OR ||: 20 + 3 == 23 and 5 - 1 == 4 es: {20 + 3 == 22 or 5 - 1 == 4}") # Si uno u otro es verdadero la respuesta es Verdadero(True)
print(f"NOT !: not 20 + 3 = 24 es: {not 20 + 3 == 24}")

#Operadores de asignación
my_number = 11 # = <-asignación
print(my_number)
my_number += 1 # suma y asignación += <-asignación
print(my_number)
my_number -+ # resta y asignación -= <-asignación
print(my_number)
my_number *= 2 # multiplicación y asignación *= <-asignación
print(my_number)
my_number /= 2 # división y asignación /= <-asignación
print(my_number)
my_number %= 2 # modulo y asignación %= <-asignación
print(my_number)
my_number **= 1 # exponente y asignación **= <-asignación
print(my_number)
my_number // = 1 # división entera y asignación //= <-asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'o' in 'Alejandro' =  {'o' in 'Alejandro'}")
print(f"'b' not in 'Alejandro' =  {'o' not in 'Alejandro'}")

# Operadores de bit
a = 10 # 1010 <- num 10 respresntado en Binario
b = 3 # 0011 <- num 3 representado en Binario
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 & 3 = {10 | 3}") # 1011
print(f"XOR: 10 & 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 >> 2 = {10 >> 2}") # 101000

"""
Estructura de control
"""

# Condicionales

my_string = "ManCar"
if my_string == "Alejandro"
  print("my_string es 'Alejandro'")
elif my_string = "ManCar":
  print("my_string es 'ManCar'")
else: 
  print("my_string no es 'Alejandro' ni 'ManCar'")

# Iterativas

for i in range(11):
  print(i)
  
i = 0

while i <= 10:
  print(i)
  i += 1

# Manejo de excepciones
try:
  print(10 / 0)
except: 
  print("Se ha producido un error")
finally:
  print("Ha finalzado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56)
  if number %2 == 0 and number != 16 and number % 3 != 0:
    print(number)
