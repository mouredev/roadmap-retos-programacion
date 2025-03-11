"""
Operadores y estructuras de control
"""

# Operadores aritméticos
print(f"suma = 1 + 2: {1 + 2}")
print(f"resta = 7 - 8: {7 - 8}")
print(f"multiplicacion = 2 * 2: {2 * 2}")
print(f"division = 10 / 2: {10 / 2}")
print(f"divisionEntero = 13 // 4: {13 // 4}")
print(f"modulo = 9 % 2: {9 % 2}")
print(f"exponente = 3 ** 3: {3 ** 3}")

# operadores de comparación

print(f"igualdad = 1 == 1: {1 == 1}")
print(f"desigualdad = 1 != 2: {1 != 2}")
print(f"mayor Que = 1 > 2: {1 > 2}") 
print(f"menor Que = 1 < 2: {1 < 2}") 
print(f"mayor o igua = 1 >= 2: {1 >= 2}") 
print(f"menor o igual = 1 <= 2: {1 <=2}") 

# operadores lógicos

print(f"and &&= 10 + 3 == 13 and 5 - 1 == 4: { 10 + 3 == 13 and 5 - 1 == 4}")
print(f"or || = 10 + 3 == 13 or 5 - 1 == 5: { 10 + 3 == 13 or 5 - 1 == 4}")
print(f"not ! = not 10 + 3 == 13: {not 10 + 3 == 13}")

# operadores de asignación

my_number = 10 #asignación
print(my_number)
my_number += 5 #suma  
print(my_number)
my_number -= 5 #resta
print(my_number)
my_number *= 5 #multiplicación
print(my_number)
my_number /= 5 #división
print(my_number)
my_number %= 5 #modulo
print(my_number)
my_number **= 5 #exponente
print(my_number)
my_number //= 5 #división entera
print(my_number)

# operadores de identidad 
# // se usa para saber si una variable tiene el mismo espacio de memoria que otra
# my_number = 1.0
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")
# print(my_new_number, my_number)

# operadores de pertenencia

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(f"1 in my_list es {1 in my_list}")
print(f"6 not is my_list es {6 not in my_list}")

#operadores de bits

a = 10 # 1010
b= 3 # 0011

print(f"AND: 10 & 3= {a & b}") # 0010
print(f"OR: 10 | 3= {a | b}") # 1011 
print(f"XOR: 10 ^ 3= {a ^ b}") # 1001
print(f"NOT: ~10= {~a}") # 0101
print(f"Desplazamiento a la derecha: 10 >> 1= {a >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 1= {a << 2}") # 101000


"""
Estructuras de control
"""
# condicionales
my_sring = "hola3"
if my_sring == "hola":
    print("my_sring es igual a hola")
elif my_sring == "hola2":
    print("my_sring es igual a hola2")
else:
    print("my_sring no es igual a 'hola' ni 'hola2'")


# bucles
# for
for i in range(0, 11):
    print(i)

i = 0
# while
while i < 11:
    print(i)
    i += 1

#manejo de excepciones
try:
    print(10/1)
except:
    print("No se puede dividir por cero")
finally:
    print("Se termino el proceso")


# Ejercicio EXTRA
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)