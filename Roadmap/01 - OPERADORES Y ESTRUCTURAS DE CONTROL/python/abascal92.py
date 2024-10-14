'''
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
'''

# Variables
num1, num2 = 23, 10

# Operadores aritméticos
print(f"La suma de {num1} y {num2} es: {num1 + num2}") #Operador aritmético de suma
print(f"La resta de {num1} y {num2} es: {num1 - num2}") #Operador aritmético de resta
print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}") #Operador aritmético de multiplicación
print(f"La división de {num1} y {num2} es: {num1 / num2}") #Operador aritmético de división
print(f"La potencia de {num1} y {num2} es: {num1 ** num2}") #Operador aritmético de potencia
print(f"El módulo de {num1} y {num2} es: {num1 % num2}") #Operador aritmético de módulo
print(f"La división entera de {num1} y {num2} es: {num1 // num2}") #Operador aritmético de división entera

# Operadores lógicos
print(f"¿{num1} es mayor que {num2}?: {num1 > num2}") #Operador lógico de mayor que
print(f"¿{num1} es mayor o igual que {num2}?: {num1 >= num2}") #Operador lógico de mayor o igual que
print(f"¿{num1} es menor que {num2}?: {num1 < num2}") #Operador lógico de menor que
print(f"¿{num1} es menor o igual que {num2}?: {num1 <= num2}") #Operador lógico de menor o igual que
print(f"¿{num1} es igual a {num2}?: {num1 == num2}") #Operador lógico de igualdad
print(f"¿{num1} es diferente de {num2}?: {num1 != num2}") #Operador lógico de diferencia

# Operadores de asignación
print(f"El valor de num1 es: {num1}")
print(f"{num1} += {num2} es igual a: {num1 + num2}") #Operador de asignación de suma
print(f"{num1} -= {num2} es igual a: {num1 - num2}") #Operador de asignación de resta
print(f"{num1} *= {num2} es igual a: {num1 * num2}") #Operador de asignación de multiplicación
print(f"{num1} /= {num2} es igual a: {num1 / num2}") #Operador de asignación de división
print(f"{num1} **= {num2} es igual a: {num1 ** num2}") #Operador de asignación de potencia
print(f"{num1} %= {num2} es igual a: {num1 % num2}") #Operador de asignación de módulo
print(f"{num1} //= {num2} es igual a: {num1 // num2}") #Operador de asignación de división entera

# Operadores de identidad
print(f"¿{num1} es {num2}?: {num1 is num2}") #Operador de identidad de igualdad
print(f"¿{num1} no es {num2}?: {num1 is not num2}") #Operador de identidad de diferencia

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
print(f"¿{num1} está en la lista?: {num1 in lista}") #Operador de pertenencia de existencia
print(f"¿{num1} no está en la lista?: {num1 not in lista}") #Operador de pertenencia de inexistencia

# Operadores de bits
num1 = 23 # 10111
num2 = 10 # 01010
print(f"La operación AND entre {num1} y {num2} es: {num1 & num2}") #Operador de bits AND (00010) (2)
print(f"La operación OR entre {num1} y {num2} es: {num1 | num2}") #Operador de bits OR (11111) (31)
print(f"La operación XOR entre {num1} y {num2} es: {num1 ^ num2}") #Operador de bits XOR (11101) (29)
print(f"La operación NOT de {num1} es: {~num1}") #Operador de bits NOT (11111111111111111111111111101000) (-24)
print(f"La operación de corrimiento a la izquierda de {num1} es: {num1 << num2}") #Operador de bits de desplazamiernto a la izquierda (101110000000000000000) (23552)
print(f"La operación de corrimiento a la derecha de {num1} es: {num1 >> num2}") #Operador de bits de desplazamiernto a la derecha (0) (0)

# Estruturas de control
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:
    print(f"{num1} es igual a {num2}")
else:
    print(f"{num1} es menor que {num2}")

for i in lista:
    print(i)

while num1 > num2:
    print(f"{num1} es mayor que {num2}")
    num1 -= 1

try:
    print(lista[10])
except Exception as e:
    print(f"Error: {e}")
else:  
    print("No hay errores")
finally:
    print("Fin del try")

# DIFICULATAD EXTRA
for i in range(10,55):
    if i % 2 == 0 and (i != 16 and i % 3 != 0):
        print(i)