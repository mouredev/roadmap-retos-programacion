'''
 *** Ejercicios ***
'''

print('''
 * Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 * Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 * (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
''')

print('\n*** Operadores Aritmeticos ***')
print("------------------------------")
print(f"La suma de 3 + 4 es: {3 + 4}") # Operador de Suma
print(f"La resta de 10 - 4 es: {10 - 4}") # Operardor de Resta
print(f"La multiplicacion de 5 * 4 es: {5 * 4}") # Operador de Multiplicacion
print(f"la division de 20 / 4 es: {20 / 4}") # Operador de Division
print(f"El modulo de 19 % 4 es: {19 / 4}") # Operador de Modulo(Resto de la division)
print(f"La exponenciacion de 5 ** 6 es: {5 ** 6}") # Operador de Exponenciacion
print(f"La division entera de 23 // 4 es: {23 // 4}") # Operador de Division Entera
print("------------------------------\n")


print('\n*** Operadores Comparacion ***')
print("------------------------------")
print(f"34 == 34: {34 == 34}") # Igual a
print(f"36 != 34: {36 != 34}") # Distinto a
print(f"34 > 34: {36 > 34}") # Mayor a
print(f"32 < 34: {32 < 34}") # Menor a
print(f"34 >= 34: {34 == 34}") # Mayor o Igual a
print(f"24 <= 24: {34 == 34}") # Menor o Igual a
print("------------------------------\n")

print('\n*** Operadores Asignacion ***')
print("------------------------------")

a = 4
print(f"a = {a}") # Asignacion simple

a += 1
print(f"a +=1 = {a}") # Suma y asignacion

a -= 1
print(f"a -=1 = {a}") # Resta  y asignacion

a *= 5
print(f"a *=5 = {a}") # Multiplicacion  y asignacion

a /= 3
print(f"a /=3 = {a}") # Division  y asignacion

a %= 5
print(f"a %=5 = {a}") # Multiplicacion  y asignacion

a **= 4
print(f"a **=4 = {a}") # Exponenciacion  y asignacion

a //= 2
print(f"a //=2 = {a}") # Multiplicacion  y asignacion

print("------------------------------\n")

print('\n*** Operadores Logicos ***')
print("------------------------------")

print(f"3 < 5 and 5 > 2 = {3 < 5 and 5 > 2}") # and : Devuelve True si ambas expresiones son verdaderas
print(f"3 < 5 or 2 > 3 ={3 < 5 or 2 > 3}") # or : Devuelve True si al menos una de las expresiones es verdadera
print(f"not 3 > 5 = {not 3 > 5}") # not : Invierte el valor booleano de una expresión (True a False, y viceversa)

print("------------------------------\n")

print('\n*** Operadores de Identidad ***')
print("---------------------------------")

a = 3
b = a
c = 5
print(f"'a' es igual a {3}, 'b' es igual a 'a' y 'c' es igual a {c}")

print(f"a is b = {a is b}")  # is : Devuelve True porque b es el mismo objeto que a
print(f"a is not c = {a is not c}")  # is not : Devuelve True porque c no es el mismo objeto que a
print("---------------------------------\n")

print('\n*** Operadores de Pertenencia ***')
print("----------------------------------")
numeros = [1, 2, 3, 4, 5]
letras = "abcdefg"

print(f"numeros es = {numeros}")
print(f"letras es = {letras}")
print(f"3 in numeros = {3 in numeros}")  # in : Devuelve True porque 3 está en la lista numeros
print(f"z not in letras = {"z" not in letras}")  # not in : Devuelve True porque z está en la lista letras
print("---------------------------------\n")

print('\n*** Operadores de Bits ***')
print("----------------------------------")
a = 5  # En binario: 0101
b = 3  # En binario: 0011

print(f"a es = {a} (binario: {bin(a)})")
print(f"b es = {b} (binario: {bin(b)})")

# Operador AND a nivel de bits
print(f"a & b = {a & b} (binario: {bin(a & b)})")  # & : Devuelve 1 porque 0101 & 0011 es 0001

# Operador OR a nivel de bits
print(f"a | b = {a | b} (binario: {bin(a | b)})")  # | : Devuelve 7 porque 0101 | 0011 es 0111

# Operador XOR a nivel de bits
print(f"a ^ b = {a ^ b} (binario: {bin(a ^ b)})")  # ^ : Devuelve 6 porque 0101 ^ 0011 es 0110

# Operador NOT a nivel de bits
print(f"~a = {~a} (binario: {bin(~a)})")  # ~ : Devuelve -6 porque ~0101 es 1010 (en complemento a dos)

# Desplazamiento de bits a la izquierda
print(f"a << 1 = {a << 1} (binario: {bin(a << 1)})")  # << : Desplaza 0101 una posición a la izquierda, resultado: 1010

# Desplazamiento de bits a la derecha
print(f"a >> 1 = {a >> 1} (binario: {bin(a >> 1)})")  # >> : Desplaza 0101 una posición a la derecha, resultado: 0010

print("---------------------------------\n")

print('''
 * Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 * que representen todos los tipos de estructuras de control que existan
 * en tu lenguaje:
 * Condicionales, iterativas, excepciones...
''')

print('\n*** Condicionales `if`, `elif` y `else` ***')
print("----------------------------------")

a = 18
b = 16
print(f"el valor de 'a' es {a} y el valor de 'b' es {b}")
if a > b:
    print(f"'a' es mayor que 'b'")
elif a == b:
    print(f"'a' es igual a 'b'")
else:
    print(f"'a' es menor que 'b'")

print("---------------------------------\n")

print('\n*** Iterativas `for` ***')
print("----------------------------------")

numeros = [1,2,3,4,5,6]
print(f"Recorriendo la lista Numeros {numeros} e imprimiendo cada elemento")

for i in numeros:
    print(i)

print('\n*** Iterativas `while` ***')
print("----------------------------------")

contador = 5
print(f"Se imprimira una cuenta regresiva desde el numero 5")
while contador >= 0:
    print(contador)
    contador -= 1
print(f"Boooom 💥")

print("---------------------------------\n")

print('\n*** Exepciones ***')
print("----------------------------------")

try:
    print(10 /1)
except: 
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de exepciones")
print("---------------------------------\n")

print('\n*** Dificultad Extra ***')
print("----------------------------------")

print('''
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
''')

for i in range(10,56):
    if i % 2 != 0 and i != 16 and i % 3 != 0:
        print(i)