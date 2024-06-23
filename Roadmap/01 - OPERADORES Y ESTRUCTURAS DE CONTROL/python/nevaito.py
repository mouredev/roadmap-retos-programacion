"""
/*
 * EJERCICIO:
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
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
""" 
Operadores
 """
# Operadores aritmeticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}") # modulo es el resto de la division
print(f"Exponente: 10 ** 3 = {10 ** 3}") # elevar un numero
print(f"Division entera: 10 // 3 = {10 // 3}") # resultado numero entero

# Operadores de comparacion
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor Que: 10 > 3 es {10 > 3}")
print(f"Menor Que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") # se tienen q cumplir las dos condiciones para que sea true
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") # se tiene que cumplir al menos una de las condiones para que sea true
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignacion
my_number = 11  #asignacion
print(my_number)
my_number += 1  #suma y asignacion
print(my_number)
my_number -= 1   #resta y asignacion
print(my_number)
my_number *= 2  #multiplicacion y asignacion
print(my_number)
my_number /= 2  #division y asignacion
print(my_number)
my_number %= 2  #modulo y asignacion
print(my_number)
my_number **= 1  #exponente y asignacion
print(my_number)
my_number //= 1  # Div entera y asignacion
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'d' in 'David' = {'d' in 'David'}")
print(f"'b' not in 'David' = {'b' not in 'David'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000


"""
Estructuras de control
"""
# Condicionales

my_string = "Daviddd"

if my_string == "David":
    print("my_string es 'David'")
elif my_string == "Hoyos":
    print(" my string es 'Hoyos'")
else:
    print("my_string no es 'David'ni 'Hoyos'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizo el manejo de excepciones")

"""
Extra
"""
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
