'''
/*
 * EJERCICIO 01 - OPERADORES Y ESTRUCTURAS DE CONTROL:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'''

# Operadores aritméticos
print(f"Suma: 10 + 5 = {10 + 5}")
sum = 15 + 5
print(f"Suma con variable: 15 + 5 = {sum}")
print(f"Multiplicacion: 10 * 5 = {10 * 5}")
print(f"Divison: 10 / 5 = {10 / 5}") # La division deja resultado float
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 5 = {10 ** 5}")
print(f"Division entera: 10 // 5 = {10 // 5}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10+3 and 5-1 == 4 es {10+3 and 5-1 == 4}") # Es verdadero
print(f"OR ||: 10+3==14 or 5-1 == 4 es {10+3 == 14 or 5-1 == 4}") #Es verdadero
print(f"NOT !: 10 + 3  == 14 es {not 10+3 == 14}") # True porque no es igual a 14

# Operadores de asignación
my_number = 11 # asigna
print(my_number)
my_number += 1 # suma y asigna
print(my_number)
my_number -= 1 # resta y asigna
print(my_number)
my_number *= 2 # multiplica y asigna
print(my_number)
my_number /= 2 # divide y asigna
print(my_number)
my_number %= 2 # modulo y asigna
print(my_number)
my_number **= 2 # exponente y asigna
print(my_number)
my_number //= 2 # divide entero y asigna
print(my_number)
my_number = 1

# Operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operador de pertenencia
print(f"'u' in 'moure' = {'u' in 'moure'}")
print(f"'z' in 'moure' = {'z' in 'moure'}")
print(f"'b' not in 'moure' = {'b' not in 'moure'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") #  0010 ¿Son los dos 1?
print(f"OR: 10 | 3 = {10 | 3}") #  1011 ¿Al menos uno es 1?
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001 ¿Son diferentes?
print(f"NOT: ~10 = {~10}") # -11 ?? Ni idea
print(f"Desplazamiento a la derecha: 10 >> 2 {10 >> 2}") # 0010 Se desplazan los bits 2 posiciones
print(f"Desplazamiento a la izquierda: 10 << 2 {10 << 2}") # 101000 Se desplazan los bits 2 posiciones

# ESTRUCTURAS DE CONTROL

# Condicionales
my_string = "Jiji"
if my_string == "Luis":
    print("my_string es 'Luis'")
elif my_string == "MdF":
    print("my_string es 'MdF'")
else:
    print("my_string no es ni 'Luis' ni 'MdF")

# Iterativas
print("Bucle for")
for i in range(10): # De 0 a 9
    print(i)

print("Bucle while") 
i=0
while i <= 5: # De 0 a 5
    print(i)
    i += 1 

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado las excepciones")

#########
# EXTRA #
#########
for i in range(10, 56):
    if (i % 2 == 0) and (i != 16) and  (i % 3 != 0):
        print(i)