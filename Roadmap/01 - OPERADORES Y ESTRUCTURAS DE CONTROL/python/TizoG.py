# Ejemplos de Operadores

print(1 + 1) # Suma
print(1 - 1) # Resta
print(2 * 2) # Multiplicacion
print(2 / 2) # Division
print(5 % 2) # Modulo
print(10 // 3) # Division con resultado entero forzado
print(2 ** 2) # Potenciacion

# Operaciones con enteros
print(3 < 2) # Menor
print(3 > 2) # Mayor
print(3 <= 2) # Menor o Igual
print(3 >= 2) # Mayor o Igual 
print(3 == 2) # Igualdad
print(3 != 2) # Desigualdad

# Operadores Logicos
print(3 < 2 and "hola" < "mundo") # Retorna verdadero si ambos son verdadero
print(3 < 2 or "hola" < "mundo") # Retorna verdad si uno de los dos es verdadero
print(3 > 2 and "hola" > "mundo")
print(3 > 2 or "hola" > "mundo")
print(not(3 > 4)) # Da el valor contrario

# Operadores de asignación 
my_number = 1
print(my_number)
my_number += 1 # suma y asignación 
print(my_number)
my_number -= 1
print(my_number)
my_number *= 2
print(my_number)
my_number /= 2
print(my_number)
my_number %= 2
print(my_number)
my_number **= 2
print(my_number)
my_number //= 1
print(my_number)



# Operadores de identidad
my_nuevo_numero = my_number
print(f"my_number is my_nuevo_numero es {my_number is my_nuevo_numero}")
print(f"my_numer is not my_nuevo_numero {my_number is not my_nuevo_numero}")

# Operadores de pertenencia
print(f"'i' in 'TizoG' = {'i' in 'TizoG'}")
print(f"'a' in 'TizoG' = {'a' in 'TizoG'}")

# Operadores de bit
a = 5
b = 2
print(f"AND : 5 & 2 = {5 & 2}")
print(f"OR: 5 | 2 = {5| 2}")
print(f"XOR: 5 ^ 2 = {5 ^ 2}")
print(f"Desplazamiento a la derecha: 5 >> 2 = {5 >> 2}")
print(f"Desplazamiento a la izquierda: 5 << 2 = {5 << 2}")

"""
Estructuras de control
"""

# Condicionales
my_name = "TizoG"
if my_name == "TizoG":
    print("my_name is 'TizoG'")
elif my_name == "tizog":
    print("my_name is 'tizog'")
else:
    print("my_name no es 'TizoG' ni 'tizog'")

# Iterativas
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try: 
    print(10 /0)
except:
    print("Se ha produicido un error")
finally:
    print("ha finalizado el manejo de excepciones")


"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)