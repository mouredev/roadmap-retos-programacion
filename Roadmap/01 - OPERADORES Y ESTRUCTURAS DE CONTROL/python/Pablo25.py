'''* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, 
asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)'''
    # Operadores: En Python, existen varios tipos de operadores que permiten realizar diferentes operaciones sobre datos.
# 1) Operadores Aritméticos: Se usan para realizar operaciones matemáticas.
 # Ejemplo: para los valores:
a = 8; b = 5
print ("Operadores Aritmeticos")
print ("Suma =", a + b)
print ("Resta =", a - b)
print ("Multiplicación =", a * b)
print ("División =", a / b)
print ("Modulo =", a % b)
print ("Exponente =", a ** b)
print ("Cociente =", a // b)
# Orden de Aplicación
'''El orden de prioridad para su ejecución sería el siguiente, siendo el primero el de mayor prioridad. 
1.	() paréntesis.
2.	** exponente
3.	* / // %multiplicación, división, cociente, modulo
4.	+ - suma, resta.'''
# Ejemplo de lo antes descrito.
print (10*(5+3)) # 80 con paréntesis se realiza la suma primero.
print (10*5+3) # 53 sin paréntesis se realiza primero la multiplicación.
# 2) Operadores de Asignación: Permite realizar una operación aritmética y asignar ese valor a una variable.
# Ejemplo para los valores:
a = 10; b = 5
print ("Operadores de Asignación")
x = a; x += b; print ("x +=", x)
x = a; x -= b; print ("x -=", x)
x = a; x *= b; print ("x *=", x)
x = a; x /= b; print ("x /=", x)
x = a; x **= b; print ("x **=", x)
x = a; x %= b; print ("x %=", x)
x = a; x //= b; print ("x //=", x)
# Se coloca x = a, para reiniciar el valor de x, al valor inicial de a, para que no afecte los resultados.
# 3) Operadores de Comparación: Permite comparar dos valores y devuelve un valor booleano (True o False).
# Ejemplo para los valores:
a = 10; b = 5
print ("Operadores de Comparación")
print ("Igualdad (==)", a == b)
print ("Diferente (!=)", a != b)
print ("Menor que (<)", a < b)
print ("Mayor que (>)", a > b)
print ("Menor o Igual que (<=)", a <= b)
print ("Mayor o Igual que (>=)", a >= b)
# 4) Operadores Lógicos: AND, OR, NOT. Permite combinar expresiones booleanas y devuelve un valor booleano.
# Ejemplo para los valores:
a = True; b = False
print ("Operadores Lógicos")
print ("Operador (and)", a and b)
print ("Operador (or)", a or b)
print ("Operador (not)", not a)
print (not not not not True) # PyTip si el número de condiciones es Par, el valor permanece, si es impar el valor cambia.
# 5) Operadores de Identidad: Permite comparar si dos variables apuntan al mismo objeto en memoria. Operadores IS y IS NOT.
# Ejemplo para los valores:
a = 10; b = a
print ("Operadores de Identidad")
print ("Operador (is)", a is b)
print ("Operador (is not)", a is not b)
# Para Python, las listas son mutables, por lo tanto crea objetos diferentes para cada lista.
# Ejemplo.
a = [1,2,3]; b = a
print (a is not b)
# 6) Operadores de Pertenencia: Permite comprobar si un valor pertenece a una secuencia (como una lista, tupla o cadena).
# Ejemplo para los valores:
a = [1,2,3]
print ("Operadores de Pertenencia")
print ("Operador (in)", 2 in a)
print ("Operador (not in)", 4 not in a)
# 7) Operadores Bit a Bit: Permite realizar operaciones a nivel de bits.
'''Los operadores más comunes son:
1.	Operador AND (&) Realiza una operación AND a nivel de bits.
2.	Operador OR (|) Realiza una operación OR a nivel de bits.
3.	Operador XOR (^) Realiza una operación XOR a nivel de bits.
4.	Operador NOT (~) Realiza una operación NOT a nivel de bits.
5.	Operador de Desplazamiento Izquierdo (<<) Desplaza los bits a la izquierda.
6.	Operador de Desplazamiento Derecho (>>) Desplaza los bits a la derecha.'''
# Ejemplo para los valores:
a = 10; b = 4
print ("Operadores Bit a Bit")
print ("Operador AND (&)", a & b)
print ("Operador OR (|)", a | b)
print ("Operador XOR (^)", a ^ b)
print ("Operador NOT (~)", ~a)
print ("Operador de Desplazamiento Izquierdo (<<)", a << 1)
print ("Operador de Desplazamiento Derecho (>>)", a >> 1)
'''* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos 
de estructuras de control que existan, en tu lenguaje: Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos.'''
    # Estructuras de control en Python, permiten dirigir el flujo de ejecución de un programa.
# 1) Estructuras condicionales: Es una estructura de control de selección que sirve para tomar decisiones, IF, ELIF, ELSE.
# Ejemplo para los valores:
a = 10; b = 5
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")
# 2) Estructuras de Bucles: Permite repetir un bloque de código varias veces, mientras se cumpla una condición. FOR, WHILE.
# Ejemplo para los valores:
# Bucle For:
for i in range(5):
    print("Bucle for:", i)
# Bucle While:
j = 0
while j < 5:
    print("Bucle while:", j)
    j += 1
# 3) Gestion de Excepciones: Permite manejar errores y excepciones que pueden ocurrir durante la ejecución del programa. 
# TRY-EXCEPT.
# Ejemplo para el valor:
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
try:
    c = a / b 
    print("Resultado de la división:", c)
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
# 4) Otros elementos importantes.
# Ejemplo para el valor:
# Operador break
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)
# Operador continue
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)
# Operador pass
for i in range(10):
      if i == 5:
          pass # Se omite la acción en la iteración 5
      else:
          print(i)
#Operador range
for i in range(6):
    print(i) #0, 1, 2, 3, 4, 5
'''* DIFICULTAD EXTRA (opcional): Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 
(incluidos), pares, y que no son ni el 16,ni múltiplos de 3. 
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.'''
# Respuesta en bruto
lista_0 = list(range(10, 56)) # crear lista de 10 a 55
print(lista_0)
lista_1 = [] # lista de números pares
for i in (lista_0):
    if ((-1)**i) > 0: lista_1.append(i)
print(lista_1)
for i in (lista_1): # eliminar múltiplos de 3
    if i % 3 == 0:
        lista_1.remove(i)
print(lista_1)
for i in (lista_1): # eliminar 16
    if i == 16:
        lista_1.remove(i)
print(lista_1)
# Respuesta un poco más elegante.
lista_0 = list(range(10, 56)) # crear lista de 10 a 55
lista_1 = [] # lista de números pares
for i in (lista_0): # agrega números pares
    if ((-1)**i) > 0: lista_1.append(i)
for i in (lista_1): # eliminar múltiplos de 3
    if i % 3 == 0: lista_1.remove(i)
for i in (lista_1): # eliminar numero 16
    if i == 16: lista_1.remove(i)
print(lista_1)
# Respuesta más elegante y eficiente, por Mouredev.!!! Me falta calle :-)!!!
for number in range(10, 56): # imprimir números pares, no 16, no múltiplos de 3
    if ((-1)**number) > 0 and number != 16 and number % 3 != 0:
        print(number)