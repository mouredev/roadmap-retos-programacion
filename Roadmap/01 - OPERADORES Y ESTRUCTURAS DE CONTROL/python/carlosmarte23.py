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

# Ejemplos de operadores en Python:

# OPERADORES ARITMETICOS:
numero_1 = 5;
numero_2 = 10;

print("Operadores aritmeticos:")
print(f"Suma: {numero_1 + numero_2}");
print(f"Resta: {numero_1 - numero_2}");
print(f"Multiplicacion: {numero_1 * numero_2}");
print(f"Potencia: {numero_1 ** numero_2}");
print(f"Division: {numero_1 / numero_2}");
print(f"Division entera: {numero_1 // numero_2}");
print(f"Modulo: {numero_1 % numero_2}");
print("##########################################")

# OPERADORES DE COMPARACION:
print("Operadores de comparacion:")
print(f"Mayor que: {numero_1 > numero_2}");
print(f"Menor que: {numero_1 < numero_2}");
print(f"Mayor o igual que: {numero_1 >= numero_2}");
print(f"Menor o igual que: {numero_1 <= numero_2}");
print(f"Igualdad: {numero_1 == numero_2}");
print(f"Desigualdad: {numero_1!= numero_2}");
print("##########################################")

# OPERADORES DE ASIGNACION:
print("Operadores de asignacion:")
numero_1 = 5;
numero_2 = 10;

resultado = 0;
# Asignacion de suma:
resultado += numero_1;
print(f"Asignacion de suma: {resultado}");

# Asignacion de resta:
resultado -= numero_2;
print(f"Asignacion de resta: {resultado}");

# Asignacion de multiplicacion:
resultado *= numero_1;
print(f"Asignacion de multiplicacion: {resultado}");

# Asignacion de division:
resultado /= numero_2;
print(f"Asignacion de division: {resultado}");

# Asignacion de modulo:
resultado %= numero_1;
print(f"Asignacion de modulo: {resultado}");
print("##########################################")

# OPERADORES LOGICOS:
print("Operadores logicos:")
verdadero = True;
falso = False;

print(f"Condicional AND: {verdadero and verdadero}");
print(f"Condicional OR: {verdadero or falso}");
print(f"Negacion: {not verdadero}");
print("##########################################")

# OPERADORES DE IDENTIDAD:
print("Operadores de identidad:")
print(f"Identidad 'is': {numero_1 is numero_1}");
print(f"Identidad con negacion 'is not': {numero_1 is not numero_2}");
print("##########################################")

# OPERADORES DE PERTENENCIA:
print("Operadores de pertenencia:")
print("Ejemplo de pertenencia in:")
lista = [1, 2, 3, 4, 5];
print(f"1 in lista: {1 in lista}");

print("Ejemplo de pertenencia not in:")
texto = "Python";
print(f"Z not in texto: { 'Z' not in texto}");
print("##########################################")

# OPERADORES DE BIT:
print("Operadores de bits:")
byte_1 = 0b00010101;
byte_2 = 0b00011011;

print(f"Byte 1: {bin(byte_1)}, Byte 2: {bin(byte_2)}");
print("Ejemplo de operador AND bit a bit:")
print(f"Resultado AND bit a bit: {bin(byte_1 & byte_2)}");

print("Ejemplo de operador OR bit a bit:")
print(f"Resultado OR bit a bit: {bin(byte_1 | byte_2)}");

print("Ejemplo de operador XOR bit a bit:")
print(f"Resultado XOR bit a bit: {bin(byte_1 ^ byte_2)}");

print("Ejemplo de operador NOT bit a bit:")
print(f"Resultado NOT bit a bit: {bin(~byte_1)}");

print("Ejemplo de operador RIGHT SHIFT bit a bit:")
print(f"Resultado RIGHT SHIFT bit a bit: {bin(byte_1 >> 1)}");

print("Ejemplo de operador LEFT SHIFT bit a bit:")
print(f"Resultado LEFT SHIFT bit a bit: {bin(byte_1 << 1)}");
print("##########################################")

# OPERADORES DE ITERACION:
print("Operadores de iteracion:")
print("Ejemplo de iteracion for:")
for i in range(1, 10):
  print(f"Iteracion for: {i}");

print("Ejemplo de iteracion while:")
i = 1;
while i <= 10:
  print(f"Iteracion while: {i}");
  i += 1;

print("Ejemplo de iteracion for-else:")
for i in range(1, 10):
  print(f"Iteracion for-else: {i}");
else:
  print("Fin del for-else");

print("Ejemplo de iteracion while-else:")
i = 1;
while i <= 10:
  print(f"Iteracion while-else: {i}");
  i += 1;
else:
  print("Fin del while-else");
print("##########################################")

# OPERADORES DE EXCEPCIONES:
print("Operadores de excepciones:")
try:
  print("Ejemplo de try:")
  print(numero_1 / 0);
except ZeroDivisionError:
  print("Error de division por cero");

try:
  print("Ejemplo de try-except-else:")
  print(numero_1 / 0);
except ZeroDivisionError:
  print("Error de division por cero");
else:
  print("No hubo error de division por cero");

try:
  print("Ejemplo de try-except-finally:")
  print(numero_1 / 0);
except ZeroDivisionError:
  print("Error de division por cero");
finally:
  print("Se ejecuta siempre");
print("##########################################")

# Ejercicio Extra:
print("Ejercicio Extra:")
for i in range(10, 55):
  if i % 2 == 0 and i!= 16 and i % 3!= 0:
    print(i)

