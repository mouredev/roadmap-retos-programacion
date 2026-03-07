"""
Los operadores pueden ser de varios tipos:
1. Operadores aritmeticos: Para operaciones matematicas.
2. Operadores de comparacion: Para comparar 2 valores retornando un valor logico (Booleano).
3. Operadores logicos: Para combinar declaraciones condicionales.
4. Operadores bit a bit: Operan a nivel de bit: Para comparar valores de variable a nivel de bit a bit y asignar 
   nuevos valores (Muy utiles para la optimizacion, escritura a nivel bajo de codigo y programacion, cifrado/encriptado, 
   procesamiento de imagen, etc.).
5. Operadores de asignacion: Para asignar valores a variables.
6. Operadores de membresia: Para validar una membresia en secuencias como listas, tuplas y strings.
7. Operadores de indentidad: Para comparar identidades de objetos.
"""

#1.1. Operadores aritmeticos:
print("\n1.1. Operadores aritmeticos:")
a = 10
b = 3
print(f"Suma: {a} + {b} = {a + b}") #Adicion +
print(f"Resta: {a} - {b} = {a - b}") #Sustracion/Resta -
print(f"Multiplicacion: {a} * {b} = {a * b}") #Multiplicacion *
print(f"Division: {a} / {b} = {a / b}") #Division / (Resultado float)
print(f"Division piso: {a} // {b} = {a // b}") #Division de piso // (devuelve el numero entero menor o igual al resultado de la divison).
print(f"Modulo: {a} % {b} = {a % b}") #Residuo/modulo % Devuelve el residuo de una division
print(f"Exponente: {a} ** {b} = {a ** b}") #Exponenciacion ** Realiza una operacion de potenciacion/exponenciacion
'''
Parentesis, para hacer la operacion opuesta a division de piso (floor division), se debe importar el modulo de
matematicas(math) adicionales que permitan una division de techo(ceil division), devolviendo el entero mas proximo
pero redondeando al superior, es decir, si el resultado es:
1.01 = 2
1.35 = 2
1.99 = 2
2.01 = 3
'''

#1.2. Operadores de comparacion (Retorna un valor logico (boolean: True / False)):
print("\n1.2. Operadores de comparacion")
print(f"Igualdad: {a} == {b} => {a == b}") #Igualdad = 
print(f"Desgualdad: {a} != {b} => {a != b}") #No igual a !=
print(f"Mayor que: {a} > {b} => {a > b}") #Mayor que >, a > b 3 no es mayor que 10.
print(f"Menor que: {a} < {b} => {a < b}") #Menor que <, a > b 3 es menor que 10.
print(f"Mayor que: {a} >= {b} => {a >= b}") #Mayor o igual que >=, a >= b 3 no es MAYOR o igual que 10.
print(f"Menor que: {a} <= {b} => {a <= b}") #Menor o igual que <=, a <= b 3 es MENOR o igual que 10.

#1.3. Operadores logicos
print("\n1.3. Operadores logicos")
c = True
d = False
print(f"Son iguales? {c} AND {d} = {c and d}") #AND Combinandolos solo sera True si ambos lo son.
print(f"Son diferentes? {c} OR {d} = {c or d}") #OR Combinandolos sera True si por lo menos uno lo es.
print(f"No es! \"NOT {d}\" = {not d}") #NOT Niega un valor bool, sea True o False.

#1.4. Operadores Bit a Bit
print("\n1.4. Operadores Bit a Bit")
e = 5 #En binario: (0101)
f = 3 #En binario: (0011)

print(f"BitAND: Son iguales? {e} y {f} => {e & f}") #AND: & establece cada bit como "1" si ambos son 1: e & f = 1 (0001).
print(f"BitAND: Son iguales? {e} y {f} => {e | f}") #OR: | compara cada bit de "e" y "f", si al menos hay un "1", el resultado es 1,e | f = 7(0111).
print(f"BitAND: Son iguales? {e} y {f} => {e ^ f}") #XOR: ^ compara cada bit de "e" y "f", si los bits son diferentes, el resultado es 1,e ^ f = 6(0110).
print(f"BitAND: Son iguales? {e} y {f} => {(~ e)}") #NOT: ~ Invierte todos los bits de "e" tomando 8 bits e=5(00000101)=>-6(11111010) y cambia el signo
                                                    #por la representacion de numeros negativos en binario.
print(f"BitAND: Son iguales? {e} y {f} => {(e << 1)}") #Left Shift: << mueve los bits de "e" a la izquierda e=5(0101)=>10(1010), y llena los espacios con ceros "0".
print(f"BitAND: Son iguales? {e} y {f} => {(e >> 1)}") #Right Shift: >> mueve los bits de "e" a la derecha e=5(0101)=>2(0010), y llena los espacios con ceros "0".

#1.5. Operadores de asignacion:
print("\n1.5. Operadores de asignacion")
g = 5
print (f"Asginacion: g es {g}") #Asignacion = asigna el valor de la derecha a la variable de la izquierda.
g += 3
print(f"Añade y asigna: g += 3 => {g}") #Como g=g+3 //Añade y asigna += añade el valor indicado y lo asigna a la variable (g +=3 ==> g = 8).
g -= 3
print(f"Resta y asigna: g -= 2 => {g}") #Como g=g-2 //Sustrae y asigna el valor indicado y lo asigna a la variable (g +=2 ==> g = 3).
g *= 4
print(f"Multiplicacion y asignacion: g *= 4 => {g}") #Como g=g*4 //Multiplica por el valor y asigna el resultado a la variable (g *=4 ==> g = 20).
g = 5
g /= 3
print(f"Division y asignacion: g /= 3 => {g}") #Como g=g/3 //Divide por el valor y asigna el resultado a la variable (g *=3 ==> g = 1.667).
g = 5
g //= 2
print(f"Division de piso y asignaacion: g //= 2 => {g}") #Como g=g//2 //Division de piso por el valor y asigna el resultado a la variable (g //=2 ==> g = 2).
g = 5
g %= 2
print(f"Modulo y asignacion: g %= 2 => {g}") #Como g=g%2 //Devuelve el residuo de la division por el valor y asigna el resultado a la variable (g //=2 ==> g = 1).
g = 5
g **= 3
print(f"Exponenciacion y asignacion: g **= 3 => {g}") #Como g=g**3 //Potencia/Exponente: El valor de la variable toma el exponente y asigna el resultado a la variable (g **=3 ==>g = 125).
g = 5
g &= 3
print(f"Bit AND y asignacion: g &= 3 => {g}") #Bitwise AND //Compara ambos valores (el dado (3(0011)) y el valor de la variable (5(0101))) y establece lo antes mencionado g &= 3 ==>g =1(0001).
g = 5
g |= 3
print(f"Bitwise OR y asignacion: g |= 3 => {g}") #Bitwise OR //Compara ambos valores (el dado (3(0011)) y el valor de la variable 5(0101))) y establece lo antes mencionado g &= 3 ==>g =7(0111).
g = 5
g ^= 3
print(f"Bitwise XOR y asignacion: g ^= 3 => {g}") #Bitwise XOR //Compara ambos valores (el dado (3(0011)) y el valor de la variable 5(0101))) y establece lo antes mencionado g &= 3 ==>g =6(0110).
g = 5
g <<= 1
print(f"Left Shift y asignacion: g <<= 1 => {g}") #Left Shift //Mueve los bit a la izquierdad 5(0101) g <<=1 ==>g = 10(1010).
g = 5
g >>= 1
print(f"Right Shift y asignacion: g >>= 1 => {g}") #Right Shift //Mueve los bits a la derecha 5(0101) g >>=1 ==>g = 2(0010).
"""
Conceptos clave para los operadores compuestos.
1. Los operadores compuestos reducen el tiempo al escribir codigo al combinar operaciones con asignaciones.
2. Estos operadores trabajan aritmeticamente, bit a bit y operaciones de potencia.
3. Estos modifican la variable directamente, asi que son especialmente utiles in loops o tareas repetitivas.
"""
#1.6. Operadores de membresia:
print("\n1.6. Operadores de membresia")
m =[1, 2, 3]

print(f"IN, esta el 2 EN m?: {2 in m}") #"in" True si el valor esta en la secuencia (lista en este caso).
print(f"NOT IN, NO ESTA el 4 en m: {4 not in m}") #"not in" True si el valor no se encuentra en la secuencia.

#1.7. Operadores de identidad
print("\n1.7. Operadores de identidad")
k = 6
l = 6

print(f"IS, k ES l? => {k is l}") #"is" True si ambos refieren(hacen referencia) al mismo objeto.
print(f"IS NOT, K NO ES l => {k is not l}") #"is not" True si no son el mismo objeto.

### Estructuras de control ###
#1. Condicional
print("\n\n2.1. Condicional")
x = 2
y = 6
z = 3

print("\nif, else")
if x > y:
    print (f"Condicional if x={x} es mayor que y={y}")
else:
    print(f"Condicional if x={x} es menor que y={y}")

print("\nif, elif, else")
if x > y and y > z:
    print(f"x={x} es mayor que y={y}, z={z}.")
elif y > x and y > z:
    print(f"y={y} es mayor que x={x}, z={z}.")
elif z > x and z > y:
    print(f"z={z} es mayor que x={x}, y={y}.")
elif x == y and x > z:
    print(f"x,y={x} son mayores que z={z}")
elif x == z and x > y:
    print(f"x,z={x} son mayores que y={y}")
elif y == z and y > x:
    print(f"y,z={y} son mayores que x={x}")
else:
    print(f"Los numeros x={x}, y={y}, z={z}, son iguales.")

#2. Estructuras de control iterativas.
#Contar numeros del 1 hasta el 15
print("\n2.2. Estructuras de control iterativas")
contar = 1

print("\nLoop While:")
while contar <= 15:
    print(contar)
    contar += 1
print("Ya termino")

#Loop for:
print("\nLoop for:")

for char in "Hola,mundo":
    print(char)

#2.2.1. Control de flujo dentro de bucles.
#break: Detiene el bucle inmediatamente.
print("\n2.2.1. Control de flujo dentro de bucles")
print("Break")
for numero in range (1 , 11):
    if numero == 8:
        break
    print(numero)
#Continue: Salta a la siguiente iteracion:
print("Continue")
for numero in range (1 , 11):
    if numero == 8:
        continue
    print(numero)

#Pass: No hace nada, solo mantiene la sintaxis
print("Pass")
for numero in range (1 , 11):
    if numero == 8:
        pass    #Podria ser un bloque de codigo que se generara mas adelante
    print(numero)

#Return: Termina una funcion y devuelve un valor:
print("Return")
def mult(a, b):
    return a * b
resultado = mult(2, 7)
print(resultado)


#2.3. Excepciones:
print("\n2.3. Excepciones")
#Try, except, else, Finally:
import random
try:
    #num_2_3 = float(input("Introduzca un numero: "))
    num_2_3 = random.randint(1, 15)
    division = 350 / num_2_3
    print(f"La division es: {division}")
except ValueError:
    print("No se introdujo un numero")
except ZeroDivisionError:
    print("El numero no puede ser cero")
finally:
    print("Siempre se ejecuta\n")

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos 
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
print("\nEjercicio numeros")

for i in range(10, 56):
    if i == 16:
        continue
    elif i % 2 == 0:
        continue
    elif i % 3 == 0:
        continue
    else:
        print(i)

