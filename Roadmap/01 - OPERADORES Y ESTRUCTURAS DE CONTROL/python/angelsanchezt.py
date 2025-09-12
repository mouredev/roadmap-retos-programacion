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

# Operadores
# Aritméticos
resultado_aritmetico = 10 + 5 * 2
print(f'Aritmético: {resultado_aritmetico}')

# Lógicos
valor_logico = True and False
print(f'Lógico: {valor_logico}')

# De comparación
comparacion = 5 > 3
print(f'Comparación: {comparacion}')

# De asignación
variable_asignacion = 42
print(f'Asignación: {variable_asignacion}')

# De identidad
a = [1, 2, 3]
b = [1, 2, 3]
identidad = a is b
print(f'Identidad: {identidad}')

# De pertenencia
lista = [1, 2, 3]
pertenencia = 2 in lista
print(f'Pertenencia: {pertenencia}')

# Bits
operacion_bits = 5 & 3
print(f'Bits: {operacion_bits}')

# Estructuras de control
# Condicionales
if resultado_aritmetico > 20:
    print("El resultado es mayor que 20")
elif resultado_aritmetico == 20:
    print("El resultado es igual a 20")
else:
    print("El resultado es menor que 20")

# Iterativas
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(f'Número válido: {i}')

# Excepciones
try:
    resultado_division = 10 / 0
except ZeroDivisionError:
    print("¡Error! División por cero.")
else:
    print(f'Resultado de la división: {resultado_division}')
finally:
    print("Operación completa.")

