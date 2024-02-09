# Reto #01 Roadmap

"""
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
"""

# Operadores Arietméticos 

sum_integer =  10 + 10     # Suma de enteros
sum_float = 10.5 + 10.1    # Suma de flotantes
sub_integer = 10 - 5       # Resta de enteros
sub_float = 10.5 - 10.1    # Resta de flotantes
mult_integer = 5 * 3       # Multiplicación de enteros
mult_float = 5.5 * 3.6     # Multiplicación de flotantes
div_enteros = 10 / 2       # División de enteros (puede retornar un número flotante)
div_float = 10.5 / 2.3     # División de flotantes
mod = 10 % 3               # Módulo, calcula el cociente y devuelve el resto de la operación
pot = 10 ** 3              # Potencia de un número ( en el ejemplo es 10 elevado a 3)
coc = 10 // 3              # Calcula el cociente de la divisón y devuelve la parte entera

## Impresión de los resultados de las operaciones aritméticas

print (f"La suma de los números 10 + 10 es : {sum_integer}")
print (f"La suma de los números 10.5 + 10.1 es : {sum_float}")
print (f"La resta de los números 10 - 5 es : {sub_integer}")
print (f"La resta de los números 10.5 - 10.1 es : {sub_float}")
print (f"La multiplicación de los números 5 * 3 es : {mult_integer}")
print (f"La multiplicacicón de los números 5.5 * 3.6 es : {mult_float}")
print (f"La división entre los números 10 / 2 es : {div_enteros}")
print (f"La división entre los números 10.5 / 2.3 es : {div_float}")
print (f"El módulo entre los números 10 % 3 es : {mod}")
print (f"La potencia entre los números 10 ** 3 es : {pot}")
print (f"La parte entera del cociente entre los números 10 // 3 es : {coc}")

# Operadores Lógicos

"""
Los operadores lógicos nos permiten trabajar con valores de tipo booleano. 
Un valor booleano es un tipo de dato que solo puede tomar valores True o False
"""
## Operador lógico and

"""
Este operador analiza si se cumplen dos condiciones
"""
print(True and True)   # Devuelve el valor True
print(True and False)  # Devuelve el valor False
print(False and True)  # Devuelve el valor False
print(False and False) # Devuelve el valor False

## Operador lógico or

"""
Este operador analiza si se cumplen al menos una de dos condiciones
"""
print(True or True)   # Devuelve el valor True
print(True or False)  # Devuelve el valor True
print(False or True)  # Devuelve el valor True
print(False or False) # Devuelve el valor False

## Operador lógico not

"""
Este operador analaiza la negación de las condiciones
"""

print(not True)      # Devuelve el valor False
print(not False)     # Devuelve el valor True
print( not not True) # Devuelve el valor True

# Operadores de comparación

"""
Estos operadores se utilizan para comparar dos o más datos y devuelven True o False
"""

## Mayor (>)
"""
Compara si el dato de la izquierda es mayor al de la derecha
"""
print ("Comparar si 10 es mayor a 5 (10>5): ",10>5)  # Devuelve True
print ("Comparar si 10 es mayor a 15 (10>15): ",10>15) # Devuelve False

## Mayor o igual (>=)
"""
Compara si el dato de la izquierda es mayor o igual al de la derecha
"""
print ("Comparar si 10 es mayor o igual a 5 (10>=5): ",10>=5)  # Devuelve True
print ("Comparar si 10 es mayor a o igual 15 (10>=15): ",10>=15) # Devuelve False
print ("Comparar si 10 es mayor a o igual 10 (10>=10): ",10>=10) # Devuelve True

## Menor (<)
"""
Compara si el dato de la izquierda es menor al de la derecha
"""

print ("Comparar si 10 es menor a 5 (10<5): ",10<5)  # Devuelve False
print ("Comparar si 10 es menor a 15 (10<15): ",10<15) # Devuelve True

## Menor o igual (<=)
"""
Compara si el dato de la izquierda es menor o igual al de la derecha
"""
print ("Comparar si 10 es menor o igual a 5 (10<=5): ",10<=5)  # Devuelve False
print ("Comparar si 10 es menor a o igual 15 (10<=15): ",10<=15) # Devuelve True
print ("Comparar si 10 es menor a o igual 10 (10<=10): ",10<=10) # Devuelve True

## Igual (==)

"""
Compara si el dato de la izquierda es igual al de la derecha
"""
print ("Comparar si 10 es igual a 10: ", 10==10) # Deluve True
print ("Comparar si 10 es igual a 5: ", 10==5) # Deluve False
print ("Comparar si Maria es igual a Maria: ","Maria"=="Maria") # Deluve True
print ("Comparar si Maria es igual a Pedro: ","Maria"=="Pedro") # Deluve False

## Distinto (!=)

"""
Compara si el dato de la izquierda es distinto al de la derecha
"""
print ("Comparar si 10 es distinto a 10: ", 10!=10) # Deluve False
print ("Comparar si 10 es distinto a 5: ", 10!=5) # Deluve True
print ("Comparar si Maria es distinto a Maria: ","Maria"!="Maria") # Deluve False
print ("Comparar si Maria es distinto a Pedro: ","Maria"!="Pedro") # Deluve True

# Operadores de Asignación

"""
Estos operadores se utilizan para asignar valores a una variable.
"""
## Ejemplos de asignaciones (=)

num = 50               # Asigna el valor 50 a la variable num
str = "Hola Python!"   # Asigna el string "Hola Python!" a la variable str

## Asignaciones compuestas

"""
También se pueden realizar asignaciones que realizan algun tipo de operación
"""

## Ejemplos de asignaciones compuestas

x = 0      # Asignación simple a variable x utilizada después para realidas las asignaciones compuestas
x += 2     # Asigna a x el valor de x más 2
x -= 2     # Asigna a x el valor de x menos 2
x *= 2	   # Asigna a x el valor de x multiplicado por 2
x /= 2	   # Asigna a x el valor de x divido 2
x %= 2	   # Asigna a x el módulo de x divido 2
x //= 2	   # Asigna a x el resto de x divido 2
x **= 2	   # Asigna a x la potencia de x elevado a 2


# Operadores de identidad (is , is not)

"""
Estos operadores se utilizan para comparar si una variable is o no un tipo de dato 
y devuelve True en caso de ser afirmativo o False en caso contrario 
"""
## Operador is

x = "Hola Python!"
y = int (25)

print ("La variable x es un número entero: ", x is int)  # Devlueve False
print ("La variable x es un string: ", x is str)         # Devlueve True
print ("La variable y es un número entero: ", y is 25)   # Devuelve True
print ("La variable y es un string: ", y is str)         # Devlueve False

## Operador is not

print ("La variable x no es un número entero: ", x is not int)  # Devlueve True
print ("La variable x no es un string: ", x is not str)         # Devlueve False
print ("La variable y no es un número entero: ", y is not 25)   # Devuelve False
print ("La variable y no es  un string: ", y is not str)        # Devlueve True


# Operadores de Pertenencia (in, not in)

"""
Estos operadores se utilizan para comprobar si un valor o variable 
 se encuentran dentro de una secuencia y devueven True en caso de pertenecer
o False en caso contrario. Es decir, por ejemplo, si pertenecen
 o están dentro de una lista, arreglo, diccionario, etc.
 
"""
# Ejemplo: dada una lista de números, verificar si un valor está dentro de la misma.

list_num = [1,2,3,4,5,6,7,8,9,10]
print ("El valor 10 se encuentra en la lista?:",10 in list_num ) # Devuelve True
print ("El valor 30 se encuentra en la lista?:",30 in list_num ) # Devuelve False
print ("El valor 10 no se encuentra en la lista?:",10 not in list_num ) # Devuelve False
print ("El valor 30 no se encuentra en la lista?:",30 not in list_num ) # Devuelve True

# Operadores a nivel de bits

"""
Los operadores a nivel de bits actúan sobre los operandos como si fueran 
una cadena de dígitos binarios. Como su nombre indica,
actúan sobre los operandos bit a bit.
"""
# Sin ejemplos porque todavía no estoy interiorizado en el tema 

# x | y	  # or bit a bit de x e y.
# x ^ y	  # or exclusivo bit a bit de x e y.
# x & y	  # and bit a bit de x e y.
# x << 10	  # Desplaza x 10 bits a la izquierda.
# x >> 10	  # Desplaza x 10 bits a la derecha.


# Condicionales (if, elif, else)

"""
Estas sentencias se utilizan para comprobar alguna condición y si se cumple realizar alguna operación,
en caso de no cumplir con la condición no entra en la sentencia y sigue ejecutando el promama con la
siguiente instrucción. Para entender un poco más vease el ejemplo siguiente
"""
"""
 - Comprobar si un elemento pertence a una lista, en caso de que sea así debe imprimir por pantalla
    que la misma ya se encuentra en la lista y en caso contrario debe agregarse a la lista e imprimir la nueva
    lista por pantalla.
"""
list_fruits = ["naranjas","manzanas","bananas","kiwis","peras"] # Creación de una lista de frutas

fruit = input ("Ingrese una fruta:")

if fruit in list_fruits:                                   # Pregunta si la fruta ingresada se encuentra en la lista
    print (f"La fruta {fruit} se encuentra en la lista")   # Imprime indicando que la fruta se encuentra en la lista
elif  fruit not in list_fruits:                            # Si no se encuentra
    list_fruits.append(fruit)                              # Agrega la fruta ingresada a la lsita
    print (list_fruits)                                    # Imrpime la nueva lista
else:
    print ("Ha ocurrido un error en el programa")

# Iterativas for y while

"""
El bucle for se utiliza para recorrer todos los elementos dentro de una estructura o rango dado
y se pueden realizar operaciones por cada elemento dentro de la o del mismo.
"""

print (" El bucle For")

for i in range (11):
    print (i)

"""
El bucle while se utiliza para hacer una iteración mientras se cumpla una condición
"""

print (" El bucle While")

x = 0
while x <= 10 :    
    print (x)
    x+=1

# Excepciones

"""
Para el manejo de excepciones se utilizan las estructuras try y except.
En este tipo de estructuras se realizan las operaciones dentro de try, si ocurre algún tipo
de error entra en la estructura de except. Para ello veremos un ejemplo
"""

try:
    num = int(input("Ingrese un número:"))                     
    print ("La suma del número ingresado más 10 es", num + 10)
except:
    print ("Ha ocurrido un error en la ejeccución del try")  

"""
En el ejemplo anterior se pide al usuario que ingrese un número, si el ingreso no es del tipo dato
con el cual se pueda realizar la operación, la ejecución sigue por el except e imprime que ha ocurrido un error.
Esta es forma más sencilla para controlar error sin que la ejecrción del programa tire un error.

""" 


# Ejercicio de dificultad extra

try:
    print ("Números del rango entre 10 y 56 que son pares, no es el 16 y no son múltiplos de 3")
    
    for i in range (10,56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print (i)

except:
    print ("Error en la ejecución del programa")
