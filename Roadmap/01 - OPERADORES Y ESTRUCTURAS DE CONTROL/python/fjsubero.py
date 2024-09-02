"""
  EJERCICIO:
  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.
 
 *DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
 *entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

### Tipos de operadores en Python ###

# 1. Operadores Aritméticos
# Se utilizan para realizar operaciones matemáticas básicas.

suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
division_entera = 5 // 3
modulo_resto = 1 % 3
potencia = 5 ** 2

print("Suma:", suma, "Tipo de dato:", type(suma))
print("Resta:", resta, "Tipo de dato:", type(resta))
print("Multiplicación:", multiplicacion, "Tipo de dato:", type(multiplicacion))
print("División:", division, "Tipo de dato:", type(division))
print("División entera:", division_entera, "Tipo de dato:", type(division_entera))
print("Módulo (resto):", modulo_resto, "Tipo de dato:", type(modulo_resto))
print("Potencia:", potencia, "Tipo de dato:", type(potencia))

## 2. Operadores de Asignación
"""
Asignación simple: = (Ej: x = 5)
Asignación con operación: +=, -=, *=, /=, //= (Ej: x += 3 es equivalente a x = x + 3)
"""
# Se utilizan para asignar valores a variables.

# Operadores de Asignación

# Asignación simple (=)
x = 5
print("x =", x)

# Asignación con operación:

#  Suma y asigna (+=)
x += 3  # Equivalente a x = x + 3
print("x =", x)

# Resta y asigna (-=)
x -= 2  # Equivalente a x = x - 2
print("x =", x)

# Multiplica y asigna (*=)
x *= 4  # Equivalente a x = x * 4
print("x =", x)

# Divide y asigna (/=)
x /= 2  # Equivalente a x = x / 2
print("x =", x)

# Divide a entero y asigna (//=)
x //= 2  # Equivalente a x = x // 2 (división entera)
print("x =", x)

# Módulo(resto) y asigna (%=)
x %= 3  # Equivalente a x = x % 3 (módulo)
print("x =", x)

# Potencia y asigna (**=)
x **= 2  # Equivalente a x = x ** 2 (potencia)
print("x =", x)


## 3. Operadores de Comparación
"""
Igual: ==
Diferente: !=
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=
"""
# Se utilizan para comparar valores y devolver un valor booleano (True o False).

# Nuestras variables para ejemplificar
valor_uno = 5
valor_dos = 3
texto_uno = "Juan"
texto_dos = "Perez"

# Igualdad (==)
print(valor_uno == valor_dos)  # False
print(texto_uno == texto_dos)   # False

# Desigualdad (!=)
print(valor_uno != valor_dos)  # True
print(texto_uno != texto_dos)   # True

# Mayor que (>)
print(valor_uno > valor_dos)  # True
# No se puede comparar directamente un número con un texto

# Menor que (<)
print(valor_uno < valor_dos)  # False
# No se puede comparar directamente un número con un texto

# Mayor o igual que (>=)
print(valor_uno >= valor_dos)  # True
print(valor_uno >= valor_uno)  # True

# Menor o igual que (<=)
print(valor_uno <= valor_dos)  # False
print(valor_uno <= valor_uno)  # True

# Comparación de cadenas
print("apple" < "banana")  # True (porque 'a' viene antes que 'b')

# Comparación de números flotantes
print(3.14 > 3)  # True

# Comparación de valores booleanos
print(True == True)  # True
print(False != True)  # True


## 4. Operadores Lógicos
"""
Y: and (Ambas expresiones deben ser True para que el resultado sea True)
O: or (Al menos una expresión debe ser True para que el resultado sea True)
No: not (Invierte el valor booleano)
"""
# Se utilizan para combinar expresiones booleanas.

# Operadores Lógicos

# Definimos algunas variables booleanas
a = True
b = False

# Operador AND (y)
print(a and b)  # False (ambas deben ser True)
print(a and a)  # True (ambas son True)

# Operador OR (o)
print(a or b)  # True (al menos una debe ser True)
print(b or b)  # False (ninguna es True)

# Operador NOT (no)
print(not a)  # False (invierte el valor de a)
print(not b)  # True (invierte el valor de b)

# Combinando operadores
print(a and (not b))  # True (a es True y b es False)
print((not a) or b)  # False (ninguna es True)

## 5. Operadores de Identidad
"""
Es: is
No es: is not
"""
# Comprueban si dos objetos son exactamente el mismo objeto en memoria.

# Nuestras variables
a = 3
b = 3
c = 4

# Impresión de resultados
print(a is b)               # True
print(a is not b)           # False
print( a is c)              # False
print( a is not c)          # True


# 6. Operadores de Pertenencia 
"""
En: in
No en: not in
"""
# Comprueban si un valor está presente en una secuencia (como una lista, tupla o cadena)

lista = [1, 2, 3, 4, 5]
print(3 in lista)           # True
print(15 not in lista)      # True

string = 'Hola, que tal'
print('que' in string)      # True
print('de' in string)       # False
print('Ho' in string)       # True
print('ho' in string)       # False, ya que distingue entre mayusc y minusc

## 7. Operadores Bit a Bit
# Realizan operaciones a nivel de bits sobre números enteros.
"""
Operadores bit a bit:
&: Realiza una operación AND bit a bit, donde cada bit correspondiente se compara. 
Si ambos bits son 1, el resultado es 1; de lo contrario, es 0.

|: Realiza una operación OR bit a bit. Si al menos uno de los bits correspondientes es 1, 
el resultado es 1.

^: Realiza una operación XOR bit a bit. Si los bits correspondientes son diferentes, 
el resultado es 1; de lo contrario, es 0.

~: Invierte todos los bits de un número.

<<: Desplaza los bits hacia la izquierda, multiplicando el número por una potencia de 2.

>>: Desplaza los bits hacia la derecha, dividiendo el número por una potencia de 2 (división entera).
"""

# variables de ejemplo
a = 5  # En binario: 0101
b = 3  # En binario: 0011

# AND bit a bit (&)
c = a & b
print(c)  # Resultado: 1 (en binario: 0001)

# OR bit a bit (|)
d = a | b
print(d)  # Resultado: 7 (en binario: 0111)

# XOR bit a bit (^)
e = a ^ b
print(e)  # Resultado: 6 (en binario: 0110)

# Complemento a dos (~)
f = ~a
print(f)  # Resultado: -6 (el complemento a dos puede variar según la implementación)

# Desplazamiento a la izquierda (<<)
g = a << 2
print(g)  # Resultado: 20 (5 * 2^2)

# Desplazamiento a la derecha (>>)
h = a >> 1
print(h)  # Resultado: 2 (5 / 2^1, división entera)

## 8. Operador de Concatenación:
"""
+: Une dos cadenas de texto para formar una cadena más larga.
"""
# Ejemplos

mensaje = "Hola, " + "mundo!"
print(mensaje)  # Imprime: Hola, mundo!

nombre = "Juan"
saludo = "Bienvenido, " + nombre + "!"
print(saludo)  # Imprime: Bienvenido, Juan!

### Estructuras de Control ###
"""
permiten alterar el flujo normal de ejecución de un programa, 
tomando decisiones o repitiendo bloques de código
"""

## 1. Condicionales (if, elif, else)
"""
if: Se ejecuta un bloque de código si una condición es verdadera.
elif: Se ejecuta si la condición anterior era falsa y esta nueva condición es verdadera.
else: Se ejecuta si ninguna de las condiciones anteriores era verdadera.
"""

edad = 18

if edad < 18:
  print("Eres menor de edad.")
elif edad == 18:
  print("Acabas de cumplir la mayoría de edad.")
else:
  print("Eres mayor de edad.")

## 2. Iterativas
"""
for: Se utiliza para iterar sobre una secuencia (lista, tupla, cadena, etc.).
while: Se ejecuta un bloque de código mientras una condición sea verdadera.
"""
# Bucle for
lista_de_frutas = ["manzana", "banana", "cereza"]
for fruta in lista_de_frutas:
  print(fruta)

# Bucle while
contador = 0
while contador <= 5:
  print(contador)
  contador += 1


## 3. Sentencia try-except
"""
try: Intenta ejecutar un bloque de código.
except: Captura y maneja excepciones (errores) que puedan ocurrir.
"""
try:
  numero = int(input("Ingrese un número: "))
  resultado = 10 / numero
  print(resultado)
except ZeroDivisionError:
  print("No puedes dividir por cero.")
except ValueError:
  print("Debes ingresar un número entero.")

## 4. Otras estructuras de control (opcional)
"""
break: Sale de un bucle.
continue: Salta a la siguiente iteración de un bucle.
pass: Sirve como un marcador de posición para una sentencia que aún no se ha implementado.
"""

# break
for i in range(10):
  if i == 5:
    break
  print(i)

# continue
for i in range(10):
  if i % 2 == 0:
    continue
  print(i)

### DIFICULTAD EXTRA ###
"""
Creación de programa de python que imprime por consola todos los números 
comprendidos entre 10 y 55 (incluidos estos), que sean solo pares, 
y que no son ni el 16 ni múltiplos de 3.
"""
for numero in range(10, 56):  # Iteramos desde 10 hasta 55
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)

"""
Explicación del código:
for numero in range(10, 56): Este bucle for itera sobre todos los números desde 
10 hasta 55 (56 no se incluye, así que llega hasta 55).

if numero % 2 == 0 and numero != 16 and numero % 3 != 0: Esta condición verifica 
tres cosas en cada iteración:
  numero % 2 == 0: Comprueba si el número es par (el resto de la división entre 2 es 0).
  numero != 16: Verifica si el número es diferente de 16.
  numero % 3 != 0: Comprueba si el número no es múltiplo de 3 
  (el resto de la división entre 3 es diferente de 0).

print(numero): Si todas las condiciones se cumplen, se imprime el número.
"""