#!/usr/bin/env  python3
"""
 *
 * #01 OPERADORES Y ESTRUCTURAS DE CONTROL
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia,
 *   bits...
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
 * Seguro que al revisar detenidamente las posibilidades has descubierto
 * algo nuevo.
 """

# Operadores Aritméticos

# Suma
print("\n[+]Operadores Aritméticos\n")
a = 5
b = 2
print("Suma:", a, "+", b, "=", a + b)

# Resta
print("Resta: %d - %d =" % (a, b),  a - b)

# Multiplicación
print("Multiplicación:", a, "*", b, "=", a * b)

# División
print("División: %d / %d =" % (a, b),  a / b)

# División entera
print("División entera:", a, "//", b, "=", a // b)

# Módulo (resto)
print("Hallar el resto: %d mod %d =" % (a, b), a % b)

# Exponenciación
print(f"Potencias: {a} elevado a {b} =", a ** b)

# Operadores de comparación
print("\n[+] Operadores de comparación\n")

# Igual a ==
print("%d es igual a %d" % (a, b), a == b)

# Distinto de !=
print(a, "es distinto de", b, a != b)

# Mayor que
print("%d es mayor que %d" % (a, b), a > b)

# Menor que
print(a, "Es menor que", b, a < b)

# Mayor igual que
print(f"{a} es mayor o igual que {b}", a >= b)

# Menor igual que
print(f"{a} es menor o igal que {b}", a <= b)

print("Tambien sirve para strings, Hola es mayor que Python?", "Hola" > "Python")
print("Otro ejemplo: Oceanos es mayor que mar?", "Oceano" > "Mar")
print("Lobo es igual a Lobo?", "Lobo" == "Lobo")
print("Cuidado, no cuenta los caracteres, si no que hace una ordenacion alfabetica, para contar caracteres hay que utilizar la función leb()")
print ("Ejemplo, es Terremoto menor que Gato?", len("Terremoto") < len("Gato"))
# Operadores lógicos

# AND Devuelve True si ambos son True
print("\n[+] Operadores Lógicos\n")

# Operando AND devuelve True si todos los argumentos son True
print("a es igual a", a, "AND(y) b es igual a", b, a == a and b == b)

# Operando OR devuele True si solo uno de los argumentos es True
print(f"{a} es menor que {b} OR(o) {b} es menor que {a}", a < b or b < a)

# Operando NOT invierte el resultado, si es True devuelve False
print(f"{a} es mayor que {b} NOT(no)", not a > b)

# Operadores de Asignación

print("\n[+] Operadores de Asignación\n")
var_a = 7
var_b = 3

# Operador =
print(f"= asigna el valor a una variable var_a = 7 var_a vale: {var_a}")

# Operador Incremento +=
var_a += 3
print("+= suma el valor del operando derecho al operando izquierdo y se asigna al operando izquierdo", var_a)

# Operado decremento -=
var_b -= 3
print ("-= resta el valor del operando derecho al valor del operando izquierdo %d" % var_b)

# Operando Multiplicación *=
var_a *= 7
print ("*= Multiplica el operando derecho con el operando izquierdo y asigna el resultado al operando izquierdo", var_a)

# Operando Division /=
var_b /= 3
print (f"/= Divide el operando izquierdo por el operando derecho y asigna el resultado al operando izquierdo {var_b}")

# División entera //=
var_a //= 5
print("Realiza una división entera entre el operando izquierdo y el operando derecho y asigna el resultado al operando izquierdo %d" % var_a)

# Módulo %=
var_b %= 2
print(f"Calcula el módulo del operando izquierdo por el operando derecho y asigna el resultado al operando izquierdo {var_b}")

# Exponenciación **=
var_a **= 3
print(f"Calcula el módulo del operando izquierdo por el operando derecho y asigna el resultado al operando izquierdo {var_a}")

# Operadores de bits
print("\n[+] Operadores de bits\n")
a = 10
b = 4

# Operador AND
print("& Realiza una operación AND bit a bit a & b =", a & b)

# Operador OR
print("| Realiza una operación OR bit a bit a | b =", a | b)

# Operador XOR
print("^ Realiza una operación XOR bit a bit a ^ b =", a ^ b)

# Operado NOT
print("~ Realiza una operación NOT bit a bit ~ a =", ~ a)

# Operadores de Memebresia

print("\n[+] Operadores de Memebresia\n")

lista = ["Gato", "Perro", "Pajaro", "Pez"]

# Operado in
print(lista)
print("El operador 'in' verifica si un elemento esta presente en una secuencia")
print("¿Esta Perro en la lista?\n", "Perro" in lista)

# Operando not in
print("El operador 'not in' verifica si un elemento no esta en una secuencia")
print("¿NO esta Oso en la lista?\n", "oso" not in lista)

# Operadores de identidad
print("\n[+] Operadores de Identidad\n")
lista = [1, 2, 3]
b = lista
c = lista[:]

print(lista)

print("El operador 'is' verifica son el mismo objeto. ¿a is b?", a is b)
print("Otro ejemplo, ¿a is c?", c is b)

# Estructuras de control
print("\n[+] Estructuras de control\n")
# If
valor_a = 5
valor_b = 8

# If
if valor_b > valor_a:
    print(valor_a, " Es mayor que ", valor_b)

# If else
if valor_a > valor_b:
    print(valor_a, " Es mayor que ", valor_b)
else:
    print(valor_a, " Es menor que ", valor_b)

# if elif
valor_a = 5
valor_b = 5
if valor_a > valor_b:
    print(valor_a, " Es mayor que ", valor_b)
elif valor_a == valor_b:
    print(valor_a, " es igual a ", valor_b)
else:
    print(valor_a, " Es menor que ", valor_b)

# For in
# Iterar sobre una lista sacar el contenido por pantalla mientras se rellena
# una tupla con el contenido de la lista
lista = ["P", "y", "t", "h", "o", "n"]
tupla = ()
for i, x in enumerate(lista):
    print(f"\n Visualizando lista elemento: {i} | Valor: {x}")
    tupla = tupla + (i, x)
print(f"\nVisualizando tupla creada {tupla}\n")

# Rellenan un lista con un for que va del 0 al 10 e imprimir la lista por
# pantalla
lista = []
for i in range(10):
    lista.append(i)
print(lista)

# Rellenar una lista mientras i valga menos de 30.
while i < 30:
    lista.append(i)
    print(lista)
    i += 1

# Control de execepciones con Try Except
try:
    resultado = 10 / 0
except:
    print("Se produjo una excepción")

# Reto opcional
print("\nListar los numero del 16 al 55 incluidos, menos los impares, el 16 y los multiplos de 3")
for i in range(16, 55):
    if i == 16:
        i += 1
    else:
        if i % 2 == 0:
            if i % 3 != 0:
                print(f"{i} Es par y No es multiplo de 3")
