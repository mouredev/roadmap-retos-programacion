'''
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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.'''
 
# Operadores aritméticos basicos:
# Ejemplo de suma de dos numeros enteros

print("operadores aritmeticos:")
num1_int, num2_int = 10, 10
suma = num1_int + num2_int
print("la suma de los dos numeros es: ", suma)

# Ejemplo de resta de dos numero decimales

n1_float, n2_float = 6.55, 1.32
resta = n1_float - n2_float
resultado_resta = round(resta, 2) # La funcion round redondea a N decimales la operacion
print("la resta de los dos numeros es: ", resultado_resta)

# Ejemplo del operador de division 

n1_division, n2_division = 5, 3
division = n1_division / n2_division
division = round(division, 2) # La funcion round redondea a N decimales la operacion
print("la division de los dos numeros es: ", division)

# Ejemplo del operador de multiplicacion

n1_multiplicacion, n2_multiplicacion = 3, 6
multiplicacion = n1_multiplicacion * n2_multiplicacion
print("la multiplicacion de los dos numeros es: ", multiplicacion)

# Operadores logicos

print("operadores logicos:")
print(True and True) # El operador AND devuelve verdad solo cuando ambos son verdad, es decir; true and true is true, false and false is true 
print(True or False) # El operador OR devuelve verdad cuando uno de los dos es verdad, si ambos son falso devolvera false
print(not True) # El operador NOT niega una condicion, es decir; si negamos false devolvera verdadero, si negamos true devolvera false

# Operadores de comparacion

print("operadores de comparacion:")
print(10 > 5) # El simbolo (>) reprensenta si es mayor, es decir; ¿10 es > (mayor) a 5?, si es mayor por lo que devolvera true
print(10 < 5) # El simbolo (<) reprensenta si es menor, es decir; ¿10 es < (menor) a 5?, si es menor por lo que devolvera false
print("mono" == "mono") # El simbolo (==) reprensenta una comparacion, es decir; ¿mono es (==) igual a mono?, como es verdad devolvera true, hay que tener en cuenta que diferencia mayusculas y minusculas
print(10 != 10) # El simbolo (!=) reprensenta una diferencia, es decir; ¿10 es (!=) diferente de 10?, no es diferente por lo que devolvera false
print(10 >= 11) # El simbolo (>=) reprensenta si es mayor o igual, es decir; ¿10 es (>=) mayor o igual a 11?, no es mayor ni igual, por lo que devolveria false
print(15 <= 15) # El simbolo (<=) reprensenta si es menor o igual, es decir; ¿10 es (<=) menor o igual a 15?, no es menor, pero si es igual, por lo que retorna true

# Operadores condicionales
# Devuelve uno de dos valores en función de una condición, ejemplo:

print("operadores condicionales:") 
if 20 > 10:                   # (IF) si 20 es (>) mayor a 10 entonces realiza...
    print("si es mayor :D ")  # este bloque de codigo
else:                         # (ELSE) en caso contrario de que no se cumpla
    print("no es mayor :( ")  # ejecuta este bloque de codigo

# Operadores de asignación
# se utilizan para asignar un valor a una variable, ejemplo:

x = 7 # Asigna un valor a una variable
x += 2 # Equivalente a x = x + 2, Incrementa el valor de la variable
x -= 2 # Equivalente a x = x - 2, Decrementa el valor de la variable
x *= 2  # Equivalente a x = x * 2, Multiplica el valor de la variable
x /= 2  # Equivalente a x = x / 2, Divide el valor de la variable

# Operadores índex y slicing
# Lista
nombres = ['riuck', 'fermando', 'jesus'] # Esto es una lista

# Ejemplos que representen los tipos de estructuras de control
# condicionales

print("ingrese dos numeros para comparlos")
a = int(input("ingrese el primer numero: ")) # Solicitamos al usuario que ingrese el primer numero, y lo guardamos en la variable (a)
b = int(input("ingrese el segundo numero: ")) # Solicitamos al usuario que ingrese el segundo numero, y lo guardamos en la variable (b)
if a == b: # Utilizamos la condicional (if) y aplicamos la comparacion 
    print("son iguales :D ") # si la condicion se cumple se imprime este bloque de codigo
else:
    print("no son iguales :( ") # si no se cumple la condicion se imprime este bloque de codigo 

# Bucles
# For: Itera sobre una secuencia (lista, tupla, cadena, etc.)
nombres = ['riuck', 'fernando', 'jesus'] # creamos una variable tipo lista
for k in nombres:
    print(k)

# While: Ejecuta un bloque de código mientras se cumpla una condición
i = 10 # Declaro una variable, y le asigno un valor de 10
while i > 0: # (WHILE) mientras i (>) sea mayor a 0 (:) entonces, ejecuta el siguiente bloque de codigo  
    print(i)
    i -= 1 # Aqui discrementamos el valor de i en 1, cuando i sea menor a 0 se saldra de bucle, sin una condicion de salida tendriamos un bulce infinito.

''' Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3'''

# Aplicamos un ciclo for para solventar este problema, utilizamos un rango para las interaciones se la variable n
# gracias a la funcion range (min, max, step) ademas de usar step que es un incremento, es este caso de 2 en 2
for n in range(10, 55, 2):
    if n != 16 and n % 3 != 0: # utilizamos la condicional if, y decimos que la codicion es que n sea diferente de 16, y que n no sea multiplo de 3
        print(n) # hacemos un print para pintar los numeros pares, y cumplir las exepciones 
print(55) # agrego el 55
