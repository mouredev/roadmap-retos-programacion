# 01 Operadores y estructuras de control

"""
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
 """

 # Operadores Aritmeticos

suma = 10 + 5  # Suma
resta = 10 - 5  # Resta
multiplicacion = 10 * 5  # Multiplicación
division = 10 / 3  # División
modulo = 10 % 3  # Módulo
exponente = 10 ** 3  # Exponente
division_entera = 10 // 3  # División entera

print("Operadores Aritméticos:")
print(f"Suma 10 + 5: {suma}")
print(f"Resta 10 - 5: {resta}")
print(f"Multiplicación 10 * 5: {multiplicacion}")
print(f"División 10 / 3: {division}")
print(f"Módulo 10 % 3: {modulo}")
print(f"Exponente 10 ** 3: {exponente}")
print(f"División entera 10 // 3: {division_entera}")

# Operadores de Comparación

mayor_que = 10 > 5  # Mayor que
menor_que = 10 < 5  # Menor que
igual_que = 10 == 5  # Igual que
mayor_igual_que = 10 >= 5  # Mayor o igual que
menor_igual_que = 10 <= 5  # Menor o igual que
diferente_que = 10 != 5  # Diferente que 

print("\nOperadores de Comparación:")
print(f"10 > 5: {mayor_que}")
print(f"10 < 5: {menor_que}")
print(f"10 == 5: {igual_que}")
print(f"10 >= 5: {mayor_igual_que}")
print(f"10 <= 5: {menor_igual_que}")
print(f"10 != 5: {diferente_que}")

# Operadores Lógicos

and_condition = True and False  # AND lógico
or_condition = True or False  # OR lógico
not_condition = not True  # NOT lógico
print("\nOperadores Lógicos:")
print(f"True and False: {and_condition}")
print(f"True or False: {or_condition}")
print(f"not True: {not_condition}")

# Operadores de Asignación

asignacion = 10  # Asignación simple
print("\nOperadores de Asignación:")
print(f"Asignación simple: {asignacion}")
asignacion += 5  # Asignación con suma
print(f"Asignación += 5: {asignacion}")
asignacion -= 3  # Asignación con resta
print(f"Asignación -= 3: {asignacion}")
asignacion *= 2  # Asignación con multiplicación
print(f"Asignación *= 2: {asignacion}")
asignacion /= 3  # Asignación con división
print(f"Asignación /= 3: {asignacion}")
asignacion %= 3  # Asignación con módulo
print(f"Asignación %= 3: {asignacion}")
asignacion **= 4  # Asignación con exponente
print(f"Asignación **= 4: {asignacion}")
asignacion //= 5  # Asignación con división entera
print(f"Asignación //= 5: {asignacion}")

# Operadores de Identidad

is_operator = (10 is 10)  # Identidad
is_not_operator = (10 is not 5)  # No identidad
print("\nOperadores de Identidad:")
print(f"10 is 10: {is_operator}")
print(f"10 is not 5: {is_not_operator}")

# Operadores de Pertenencia
in_operator = 10 in [1, 2, 3, 4, 5]  # Pertenencia
not_in_operator = 10 not in [1, 2, 3, 4, 5]  # No pertenencia 
is_true = "e" in "Alejandro"  # Verifica si 'e' está en 'Alejandro'
print("\nOperadores de Pertenencia:")
print(f"10 in [1, 2, 3, 4, 5]: {in_operator}")
print(f"10 not in [1, 2, 3, 4, 5]: {not_in_operator}")
print(f"'e' in 'Alejandro': {is_true}")

# Operadores de Bits

bit_and = 10 & 5  # AND bit a bit 
bit_or = 10 | 5  # OR bit a bit
bit_xor = 10 ^ 5  # XOR bit a bit
bit_not = ~10  # NOT bit a bit
bit_left_shift = 10 << 2  # Desplazamiento a la izquierda
bit_right_shift = 10 >> 2  # Desplazamiento a la derecha
print("\nOperadores de Bits:")
print(f"10 & 5: {bit_and}")
print(f"10 | 5: {bit_or}")
print(f"10 ^ 5: {bit_xor}")
print(f"~10: {bit_not}")
print(f"10 << 2: {bit_left_shift}")
print(f"10 >> 2: {bit_right_shift}")

# Estructuras de Control
print("\nEstructuras de Control:")

# Condicionales
print("\nCondicionales:")

if 10 > 5:
    print("\nCondicional: 10 es mayor que 5")
elif 10 < 5:
    print("\nCondicional: 10 es menor que 5")
else:
    print("\nCondicional: 10 es igual a 5")


# Iterativas

print("\nIterativas:")
for i in range(5):
    print(f"Iterativa: Iteración {i}")
while i < 5:
    print(f"Iterativa: Iteración {i}")
    i += 1

# Excepciones
print("\nExcepciones:")
try:
    print("Resultado de la división 10 / 0:")
    resultado = 10 / 0  # Esto generará una excepción
except ZeroDivisionError:
    print("Excepción: No se puede dividir por cero")
print("\nExtra: Números entre 10 y 55, pares, no 16 ni múltiplos de 3")
print("Dificultad Extra:")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num, end=" ")
print("\n \nFin del reto. ¡Sigue practicando y aprendiendo!")