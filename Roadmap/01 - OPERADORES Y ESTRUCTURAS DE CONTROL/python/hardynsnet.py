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

# Aritmeticos
suma = 1 + 2
resta =  9 - 5 
multiplicacion = 10 * 3
division = 6 / 3
exponente = 4 ** 2
modulo = 10 % 5

# De comparación
mayor = 10 > 3
menor= 10 < 20
mayor_igual_que= 18 >= 10
menor_igual_que= 90 <= 100
igual_que = 40 == 40

# Lógicos
_and = (5>3) and (2<4)
_or =  (7<9) or (2 > 3)
_not = (5>3)

# Asignación
x = 10 # Asignación simple
x += 3 # Suma y asignación (x = 13)
x -= 2 # Resta y asignación (x ahora es 11)
x *= 2 # Multiplicación y asignación (x ahora es 22)
x /= 2 # División y asignación (x ahora es 11.0)

# Identidad
# Verifican si dos variables apuntan al mismo objeto en memoria
lista1 = [1,2]
lista2 = [1,2]
lista3 = lista1

es_el_mismo = lista1 is lista3 # True 
no_es_el_mismo = lista1 is not lista2 # True (tienen el mismo contenido, pero son objetos distintos)

# Pertenencia
texto = "Python"
en_lista = "y" in texto # True 
no_en_lista = "z" not in texto # True

# Bits (Bitwise)
bit_and = 5 & 3 # 1 (0101 AND 0011 = 0001)
bit_or = 5 | 3 # 7 (0101 OR 0011 = 0111)
bit_xor = 5 ^ 3 # 6 (0101 XOR 0011 = 0110)
bit_not = ~5 # -6 (Invierte los bits)
desplazar_derecha = 5 >> 1 # 2 (Desplaza bits a la derecha)
desplazar_izquierda = 5 << 1 # 10 (Desplaza bits a la izquierda)

# Estructuras de control
#Condicionales
edad = 20
if edad >= 18 and edad < 65:
    print("Es un adulto")
elif edad >= 65:
    print("Es un adulto mayor")
else:
    print("Es menor de edad")

# Iterativas
print("BUCLE FOR:")
for i in range(1,4):
    print(f"Iteración {i}")

# Bucle WHILE
print("Bucle WHILE:")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1 

# Excepciones
# Manejo de errores en tiempo de ejecución
try:
    numero = 10
    divisor = 0
    resultado = numero / divisor # Causa un error ZeroDivisionError
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
finally:
    print("Fin del bloque de excepciones")

# Prints
print(" --- RESULTADOS OPERADORES ---")
print(f"Suma: {suma}")
print(f"Mayor que {mayor}")
print(f"AND Lógico {_and}")
print(f"Identidad (is) {es_el_mismo}")
print(f"Pertenencia (in) {en_lista}")
print(f"Bitwise AND: {bit_and}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

for i in range (10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
