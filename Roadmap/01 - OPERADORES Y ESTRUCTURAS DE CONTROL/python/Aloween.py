'''Operadores
    - Aritméticos
    - De asignación
    - De comparación
    - Lógicos
    Estructuras de control
    - Condicionales
    - Bucles
    - Funciones'''

# Operadores aritméticos
print (f"Suma 10 + 3 = { 10 + 3}")
print (f"Resta 10 - 3 = { 10 - 3}")
print (f"Multiplicación 10 * 3 = { 10 * 3}")
print (f"División 10 / 3 = { 10 / 3}")
print (f"Modulo 10 % 3 = { 10 % 3}")  # Se usa para obtener el residuo de una división y se hace con el símbolo %.
print (f"Exponente 10 ** 3 = { 10 ** 3}") # Eleva un número a la potencia de otro.
print (f"División entera 10 // 3 = { 10 // 3}") # Devuelve el cociente de una división redondeado hacia abajo al entero más cercano.

# Operadores de comparación podemos usarlos para comparar valores de variables, strings y devuelven un valor booleano (True o False)

print(f"10 > 3 = { 10 > 3 }")   # Mayor que
print(f"10 < 3 = { 10 < 3 }")   # Menor que
print(f"10 >= 3 = { 10 >= 3 }") # Mayor o igual que
print(f"10 <= 3 = { 10 <= 3 }") # Menor o igual que
print(f"10 == 3 = { 10 == 3 }") # Igual que (Compara valores)
print(f"10 != 3 = { 10 != 3 }") # Diferente que (Compara valores)
print(f"10 is 3 = { 10 is 3 }") # Identidad (Compara referencias en memoria)
print(f"10 is not 3 = { 10 is not 3 }") # No identidad (Compara referencias en memoria)
print(f"[1, 2, 3] is [1, 2, 3] = { [1, 2, 3] is [1, 2, 3] }") # False porque son dos listas diferentes en memoria
print(f"[1, 2, 3] == [1, 2, 3] = { [1, 2, 3] == [1, 2, 3] }") # True porque tienen el mismo contenido

#Operadores lógicos
print(f"AND: 10 + 3 == 13  and 5 - 1 == 4  es {10 + 3 == 13  and 5 - 1 == 4 }") # Devuelve True si ambos operandos son True, en otros lenguajes se puede representar con &&
print(f"OR: 10 + 3 == 13  or 5 - 1 == 4  es {10 + 3 == 20  or 5 - 1 == 4 }")   # Devuelve True si al menos uno de lass operaciones es True en otros lenguajes se puede representar con ||
print(f"NOT:! not 10 + 3 ==14 { not 10 + 3 ==14 }")# Invierte el valor booleano es decir si es True lo convierte en False y viceversa.


#Operadores de asignación
my_var = 10 # Asignación simple
print( my_var)
print( f"my_var += 5  es { my_var + 5 }") # Suma y asigna
print( f"my_var -= 3  es { my_var - 3 }") # Resta y asigna
print( f"my_var *= 2  es { my_var * 2 }") # Multiplica y asigna
print( f"my_var /= 4  es { my_var / 4 }") # Divide y asigna
print( f"my_var %= 3  es { my_var % 3 }") # Modulo y asigna
print( f"my_var **= 2 es { my_var ** 2 }") # Exponente y asigna
print( f"my_var //= 2 es { my_var // 2 }") # División entera y asigna

"""Operadores de identenidad nos permiten comparar el valor en memoria de dos variables, es decir si apuntan al mismo objeto en memoria las variables pueden tener el mismo valor pero estar en diferente espacio en memoria ( direcciones de memoria) para ello utilizamos is (identidad) y is not (no identidad)"""

my_new_var = 5 
print(f"my_var es igual a my_new_var? { my_var is my_new_var }") # False porque son diferentes en memoria
my_new_var = my_var
print(f"my_var es igual a my_new_var?  { my_var is my_new_var }") # True porque ahora apuntan al mismo objeto en memoria

#is not es lo contrario de is
print(f"my_var es diferente a my_new_var? { my_var is not my_new_var }") # False porque ahora apuntan al mismo objeto en memoria

# Operadores de pertenencia
"""nos permiten verificar si un valor o variable está presente en una secuencia (como una lista, tupla, conjunto o cadena de texto) ¿algo esta presente dentro de algo ?"""

print(f"10 in [1, 2, 3, 4, 5] es { 10 in [1, 2, 3, 4, 5] }") # False porque no esta presente.
print(f"10 not in [1, 2, 3, 4, 5] es { 10 not in [1, 2, 3, 4, 5] }") # True porque no esta presente.

#Operadores de bit a bit  ( nivel de bits) se utilizan para manipular datos a nivel de bits, es decir, trabajan directamente con la representación binaria de los números.
a =10 # En binario: 1010
b = 3 # En binario: 0011
print(f" ADD: a & b = { a & b }") # AND: 0010 (2 en decimal) es decir el lenguaje compara bit a bit y si ambos son 1 devuelve 1, si alguno es 0 devuelve 0.
print (f"OR: a | b = {a | b }") # OR: 0011 ( 11 en decimal) es decir el lenguaje compara bit a bit y si alguno es 1 devuelve 1, si ambos son 0 devuelve 0.
print(f"XOR: a ^ b = { a ^ b }") #XOR: 1001 (9 en decimal) es decir  el lenguaje compara bit a bit y si los bits son diferentes devuelve 1, si son iguales devuelve 0.
print(f"NOT: ~a = { ~a }") #NOT: 0101 (5 en decimal) es decir invierte los bits, los 0s los convierte en 1s y los 1s los convierte en 0s.
print(f"left shift: a << 1 = { a << 1 }") # Desplazamiento a la izquierda: 10100 (20 en decimal) es decir desplaza todo los bits a la izquierda y completa con los ceros a la derecha.
print(f"right shift: a >> 1 = { a >> 1 }")  #Desplazamiento a la derecha: 0101 ( 5 en decimal) es decir desplaza todos los bits a la derecha y elimina el bit menos significativo.

'''Estructuras de control condicionales:
if, elif, else
ciclos:
for, while
funciones:'''
my_string = " Alonso en Barcelona "
if "Alonso" in my_string: #Si Alonso está presente en my_string
    print(f"Alonso está presente en { my_string }")
else: #si no está presente
    print("Alonso no está presente en my_string")

my_string= " Aloween "
if my_string == " Halloween": #Si my_string es igual a " Halloween"
    print("Feliz Halloween")
elif my_string == " Aloween ": #elif se utilza para que haga comprabaciones intermedias.
    print("Hola Aloween")
else:
    print("my_string no es ni Halloween ni Aloween")

#While es un ciclo que se repite mientras una condicion sea verdadera.
my_string = " Aloween "
while my_string != " Aloween ": #Mientras my_string sea diferente a "Aloween"
    print("my_string no es ni Halloween ni Aloween")
    my_string = input("Ingrese Aloween: ") #Pide al usuario que ingrese "Aloween"

i = 1
while i <= 10:
    print(i)
    i +=1  
#Ciclo for se utiliza para iterar sobre una secuencia ( lista, tupla, diccionario, conjunto o de cadena de texto). Es decir, nos vale para recorrer una estructura de datos o ejecutar una accion un numero determinado de veces.
for i in range(5): #Rango recorre toda la secuendia que le indiquemos, en este caso del 0 al 4
    print(i) #Imprime el valor de i en cada iteracion

#Manejo de Excepciones ( son estructuras de control que nos permiten manejar errores en tiempo de ejecucion para evitar que el programa se detenga abruptamente)
try:
    print(10 / 0) #Intentamos dividir por cero
except:
    print("Error: No se puede dividir por cero") #Imprimimos un mensaje de error
finally:
    print("Fin del programa") #Se ejecuta siempre al final del bloque try-except


'''Extra'''

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 == 0:
        print(number)
   