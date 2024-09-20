"""
EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos. 
 """

# Operadores Aritmeticos
print(f"Suma 37 + 13 = {37 + 13}")
print(f"Resta 76 - 14 = {76 - 14}")
print(f"Multiplica 14 * 14 = {14 * 14}")
print(f"Divide 255 / 4 = {255 / 4}")
print(f"Modulo 23 % 3 = {23 % 3}")  # Nota personal: Modulo es el residuo de una division, en el ejemplo 23/3 es 7 y 7*3 es 21 quedando 2 como resultado del Modulo.
print(f"Exponente 14 ** 3 = {14 ** 3}")
print(f"Division entera 255 // 4 = {255 // 4}")

# Operadores de Comparacion
print(f"Igualdad: 14 == 14 es {14 == 14}")
print(f"Desigualdad: 14 == 27 es {14 != 27}")
print(f"Mayor que: 12 > 13 es {12 > 13}")
print(f"Menor que: 7 < 13 es {7 < 13}")
print(f"Mayor o igual que: 14 >= 13 es {14 >= 13}")
print(f"Menor o igual que: 10 <= 13 es {10 <= 13}")

# Operadores Logicos
print(f"AND &&: 14 + 14 == 28 and 7 + 3 == 10 es {14 + 14 == 28 and 7 + 3 == 10}")
print(f"OR ||: 76 - 40 == 36 or 12 / 4 == 3 es {76 - 40 == 36 or 12 / 4 == 3}")
print(f"NOT !: not 14 - 7 == 6 es {not 14 - 7 == 6}")

# Operadores de Asignacion
# Nota personal: Son operadores que pueden funcionar para asignar valores a variables.
numero = 14
print(numero)
numero += 14
print("+ 14 =", numero)
numero -= 4
print("- 4 =", numero)
numero *= 2
print("* 2 =", numero)
numero /= 2
print("/ 4 =", numero)
numero %= 5
print("% 5 =", numero)
numero **= 2
print("** 2 =", numero)
numero //= 3
print("// 3 =", numero)

# Operadores de Identidad
# Nota personal: Aqui veremos que una identidad es distinto de un valor, las variables valen 5.0, pero no son iguales.
nuevo_numero = 5.0
print(f"Mi nuevo numero es mi numero es {nuevo_numero is numero}")
print(nuevo_numero, "y", numero)
# Aqui cambiaremos el valor de la variable por el de otra y replicaremos el ejercicio.
nuevo_numero = numero
print(f"Mi nuevo numero es mi numero es {nuevo_numero is numero}")
print(nuevo_numero, "y", numero)
print(f"Mi nuevo numero no es mi numero es {nuevo_numero is not numero}")

# Operadores de pertenencia
# Nota personal: para comprobar si algo pertenece a algo.
print(f"'D' in 'Dkp' es {'D' in 'Dkp'}")
print(f"'V' in 'Dkp' es {'V' in 'Dkp'}")
print(f"'D' not in 'Dkp' es {'D' not in 'Dkp'}")
print(f"'V' not in 'Dkp' es {'V' not in 'Dkp'}")

# Operadores de Bit
a = 10  # 1010      # esta es su representacion binaria
b = 3   # 0011      # ocuparemos estos dos para hacer las operaciones manualmente

print(f"AND: 10 & 3 = {10 & 3}")     # 0010     # AND-& va comparar bit a bit y si ambos son 1 dara 1
print(f"OR: 10 | 3 = {10 | 3}")      # 1011     # OR-| va comparar y si un bit es 1 dara 1
print(f"XOR: 10 ^ 3 = {10 ^ 3}")     # 1001     # XOR-^ va comparar y si los bit no son iguales dara 1
print(f"NOT: ~10 = {~10}")                      # va negando bit a bit

print(f"Desplazamiento a la derecha: 10 >> 2 es {10 >> 2}")     # >> sirve para mover bits en ceros, 10 es 1010 pasa a 0010 que es 2
print(f"Desplazamiento a la izquierda: 10 << 2 es {10 << 2}")   # << aqui 10 que es 1010 pasa a 101000 que es 40

"""
Estructura de control
"""

# Condicionales

string = "Condicional 1"

if string == "Condicional 1":
    print("Se imprime primera condicion")
elif string == "Condicional 2":
    print("Se imprime segunda condicion")
else:
    print("No es la condicion")

# Iterativas

for i in range(8):
    print(i)
print("Termina el for")

i = 0
while i <= 10:
    print(i)
    i += 1
print("Termina el while")

# Manejo de excepciones

conejo = 10

try:
    print(conejo / 2)
except: 
    print("Dio error")
finally:
    print("Ha finalizado el sistema de manejo de excepciones")

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

print("Tarea Extra")

for tortuga in range(10,56):
    if tortuga % 2 == 0 and tortuga != 16 and tortuga % 3 != 0:
        print(tortuga)

print("Fin del ejercicio")