""" /*
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
 */ """
 
"""Operadores Aritméticos:"""
 # Suma
resultado_suma = 5 + 3
print("Suma:", resultado_suma)

# Resta
resultado_resta = 10 - 4
print("Resta:", resultado_resta)

# Multiplicación
resultado_multiplicacion = 3 * 6
print("Multiplicación:", resultado_multiplicacion)

# División
resultado_division = 15 / 3
print("División:", resultado_division)

# Módulo
resultado_modulo = 17 % 4
print("Módulo:", resultado_modulo)

# Potencia
resultado_potencia = 2 ** 4
print("Potencia:", resultado_potencia)

"""Operadores de Comparación:"""
# Igualdad
es_igual = (5 == 5)
print("Igualdad:", es_igual)

# Desigualdad
no_es_igual = (7 != 3)
print("Desigualdad:", no_es_igual)

# Mayor que
mayor_que = (10 > 5)
print("Mayor que:", mayor_que)

# Menor que
menor_que = (8 < 12)
print("Menor que:", menor_que)

# Mayor o igual que
mayor_o_igual_que = (6 >= 6)
print("Mayor o igual que:", mayor_o_igual_que)

# Menor o igual que
menor_o_igual_que = (9 <= 10)
print("Menor o igual que:", menor_o_igual_que)

"""Operadores Lógicos:"""
# AND lógico
and_logico = True and False
print("AND lógico:", and_logico)

# OR lógico
or_logico = True or False
print("OR lógico:", or_logico)

# NOT lógico
not_logico = not True
print("NOT lógico:", not_logico)

"""Operadores de Asignación:"""
# Asignación simple
variable_asignada = 42
print("Variable asignada:", variable_asignada)

# Asignación con suma
variable_asignada += 8
print("Variable asignada con suma:", variable_asignada)

# Asignación con multiplicación
variable_asignada *= 2
print("Variable asignada con multiplicación:", variable_asignada)

"""Operadores de Identidad:"""
# Identidad
x = [1, 2, 3]
y = [1, 2, 3]

es_misma_identidad = x is y
print("Misma identidad:", es_misma_identidad)

# No es la misma identidad
no_es_misma_identidad = x is not y
print("No es la misma identidad:", no_es_misma_identidad)

"""Operadores de Pertenencia:"""
# Pertenencia a una lista
lista = [1, 2, 3, 4]
pertenece_a_lista = 3 in lista
print("Pertenece a lista:", pertenece_a_lista)

# No pertenece a una lista
no_pertenece_a_lista = 5 not in lista
print("No pertenece a lista:", no_pertenece_a_lista)

"""Operadores a Nivel de Bits:"""
# AND a nivel de bits
resultado_and_bits = 5 & 3
print("AND a nivel de bits:", resultado_and_bits)

# OR a nivel de bits
resultado_or_bits = 5 | 3
print("OR a nivel de bits:", resultado_or_bits)

# XOR a nivel de bits
resultado_xor_bits = 5 ^ 3
print("XOR a nivel de bits:", resultado_xor_bits)

# Desplazamiento a la izquierda
resultado_desplazamiento_izquierda = 8 << 2
print("Desplazamiento a la izquierda:", resultado_desplazamiento_izquierda)

"""Estructuras Condicionales (if-elif-else):"""
# Condicional simple
numero = 10
if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.")

# Condicional con operador ternario
resultado = "Éxito" if numero > 0 else "Fracaso"
print("Resultado:", resultado)

"""Bucle For:"""
# Bucle for para imprimir los números del 1 al 5
for i in range(1, 6):
    print(i)

"""Bucle While:"""
# Bucle while para imprimir los números del 1 al 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

"""Manejo de Excepciones:"""
# Manejo de excepciones para dividir dos números
try:
    numerador = 10
    denominador = 0
    resultado_division = numerador / denominador
    print("Resultado de la división:", resultado_division)
except ZeroDivisionError:
    print("Error: División por cero.")
except Exception as e:
    print(f"Otro error: {e}")
finally:
    print("Este bloque siempre se ejecuta.")

#Programa pedido
for i in range(10,55):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i);
