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

#operadores aritmeticos
print(f"Esto es una suma 4 + 4 y de solucion {4 + 4}")

#operadores de comparacion
print(f"8 es mayor que 5 por lo que esta comparación va a dar TRUE 8 > 5 = {8 > 5}")

#operadores lógicos
a = True
b = False
print(f"Esto debe de dar False a and b = {a and b} ")

#operadores asignación
numer = 2
numer **= 3
print(f"Resultado de numer **= 3 {numer}")

#operadores identidad
numero_int = 3
numero_int_2 = 3
numero_float = 2.4
print(f"Resultado de numero_int is numero_float {numero_int is numero_float}")
print(f"Pero en cambio Resultado de numero_int is numero_int {numero_int is numero_int_2}")

# Definimos dos listas con los mismos valores
a = [1, 2, 3]
b = [1, 2, 3]

# Comparamos las dos listas con el operador "is"
if a is b:
    print("a y b son el mismo objeto")
else:
    print("a y b no son el mismo objeto")

# Comparamos las dos listas con el operador "is not"
if a is not b:
    print("a y b no son el mismo objeto")
else:
    print("a y b son el mismo objeto")

#Las listas aunque sean iguales son dos objetos diferentes en memoria

#Operadores de pertenencia

secuencia_numero = [1,2,3,4,5,6]
if 2 in secuencia_numero:
    print("El número 2 forma parte de la secuencia")
else:
    print("No forma parte de la secuencia")

#Operadores bit a bit

a = 60    # 60 en binario es 111100
b = 13    # 13 en binario es 1101
c = 3     # 3 en binario es 11

# Operador AND bit a bit
print(a & b)    # 12 (en binario 1100)

# Operador de desplazamiento a la izquierda
print(c << 2)   # 240 (en binario 11110000)

# Operador de desplazamiento a la derecha
print(c >> 2)   # 15 (en binario 1111)

#Dificultad extra:

print(f"Ejercicio dificultad extra\n")
for i in range(56):
    if(i >= 10):
        if(i%2 == 0):
            if(not(i%3==0)):
                if(not(i==16)):
                    print(i)