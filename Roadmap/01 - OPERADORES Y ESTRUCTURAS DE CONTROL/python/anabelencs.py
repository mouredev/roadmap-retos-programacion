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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

''' OPERADORES '''
print("***OPERADORES***")
print("")

# OPERADORES ARITMÉTICOS
print("OPERADORES ARITMÉTICOS")

print(f"Suma 12 + 4 = {12+4}")
# Al colocar la f adelante, se leen las llaves como código, no como cadena de texto. Poner la f se llama interpolar, me parece entender.
# Otra forma de imprimir la suma:
sum = 12+4
print("Suma 12 + 4 =",sum) # Notar que aquí no se necesita la f. Y que se separan los elementos con ,.
#Otra forma, con variables:
a = 12
b = 4
print("Suma de a + b =",a+b)
print(f"Resta 12 - 4 = {12-4}") #1
print(f"Resta 12 - 4 =", {12-4}) #2
print(f"Resta 12 - 4 =", 12-4) #3
#1 Si dejo todo dentro de las comillas de string, tengo la respuesta sin {}.
#2 Si las comillas las aplico hasta antes de la operación, la respuesta va dentro de {}.
#3 Si cierro comillas al acabar la cadena de texto y luego pongo la operación, puedo ponerla sin {}.
print(f"Multiplicación 12 x 4 = {12*4}")
print(f"División 10 / 3 = {10/3}")
print(f"División entera 10 // 3 = {10//3}")
print(f"Módulo (o residuo) 12 % 4 = {12%4}")
print(f"Potenciación (o exponente) 12 ^ 4 = {12**4}")
print(" ")

# OPERADORES DE COMPARACIÓN
print("OPERADORES DE COMPARACIÓN")

print(f"¿Son iguales 10 y 3? {10==3}")
print(f"Igualdad 10==3 : {10==3}")
print(f"¿Diferentes? 10!=3 : {10!=3}")
print(f"¿Es 10 mayor que 3? : {10>3}")
print(f"¿Es 10 menor que 3? : {10<3}")
print(f"¿Es 10 mayor o igual que 3? : {10>=3}")
print(f"¿Es 10 menor o igual que 3? : {10<=3}")
print(" ")

# OPERADORES LÓGICOS
print("OPERADORES LÓGICOS")

print(f"AND (&& en otros lenguajes): 34+1==35 and 4/2==2 : {34+1==35 and 4/2==2}")
print(f"OR (|| en otros lenguajes): 34+1==325 or 4/2==2 : {34+1==325 or 4/2==2}")
print(f"OR (|| en otros lenguajes): 34+1==325 or 4/2==3 : {34+1==325 or 4/2==3}")
print(f"NOT (! en otros lenguajes): not 34+1==38 : {not 34+1==38}")
print(f"NOT (! en otros lenguajes): not 34+1==35 : {not 34+1==35}")
# Se pueden dejar espacios o no en las fórmulas, da igual.
print(" ")

# OPERADORES DE ASIGNACIÓN
print("OPERADORES DE ASIGNACIÓN")

a = 5
print("Asignando:",a)
a += 1
print("Sumando y asignando:",a)
a += 1
print("Sumando y asignando de nuevo:",a)
a -= 2
print("Restando y asignando:",a)
a*=5 #En asignación de variables, también da igual si se dejan espacios o no.
print("Multiplicando y asignando:",a)
a/=3
print("Dividiendo y asignando:",a)
a//=1
print("División entera y asignar:",a)
a%=3
print("Residuo y asignar:",a)
a**=3
print("Exponente y asignar:",a)
print("")

# OPERADORES DE IDENTIDAD
print("OPERADORES DE IDENTIDAD") # El uso de "is" o "is not"

b=8
print(f"a is b es:",{a is b})
# Porque distinto "valor en memoria". Ocupan diferentes dimensiones de memoria (o direcciones?). Posición de memoria.
# Pero si pongo:
a=8
# (de manera que sea la misma posición en memoria)
print(f"a is b es:",{a is b})
print(f"a is not b es:",{a is not b}) # Es un no yes = no
print("")

# OPERADORES DE PERTENENCIA
print("OPERADORES DE PERTENENCIA")
# De estos no hay en todos los lenguajes

print(f"'K' in 'Castillo'?",{'K' in 'Castillo'})
print(f"'c' in 'Castillo'?",{'c' in 'Castillo'})
print(f"'C' in 'Castillo'?",'C' in 'Castillo')
print(f"'C' not in 'Castillo'?",'C' not in 'Castillo') # Es un yes no = no
print("")


# OPERADORES BINARIO O DE BIT
print("OPERADORES BINARIOS O DE BIT")

# Contando en binario desde 0 hasta 15: 00 01 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111
c = 10 # 1010
d = 3 # 11 ó 0011, es lo mismo
# AND: Compara bit a bit... Si los dos son 1: 1. Todas las demás combinaciones: 0.
print("AND: 10 & 3 =", 10 & 3) # La comparación da: 0010, y eso contando en binario es igual a 2.
print(10 & 3)
# OR: si al menos uno de los dos bits es 1: 1. Si no: 0.
print("OR: 10 | 3 =", 10 | 3) # 1011, es decir, 11.
# XOR: si los bits son diferentes: 1. Si son iguales: 0.
print("XOR: 10 ^ 3 =", 10 ^ 3) # 1001, es decir, 9.
# NOT: No lo entendí. Google dice: Invierte todos los bits (los 1 pasan a 0 y los 0 a 1). En Python, equivale a -(x + 1). Ejemplo: ~5 da -6.
print("NOT: ~ 10 =", ~ 10)
# Desplazamiento a la derecha, >>: 
print("Desplazamiento a la derecha: 10 >> 2 =", 10 >> 2) # 1010 si se desplaza una posición a la derecha queda como 0101, si se desplaza otra posición más a la derecha queda como 0010, que es igual a 2.
# Desplazamiento a la izquierda, <<: 
print("Desplazamiento a la izquierda: 10 << 2 =", 10 << 2) # 1010 si se desplaza dos posiciones a la izquierda, se rellena con dos 0 ceros a la derecha, quedando como 101000, y eso es 40.
# Otras pruebas:
print("Desplazamiento a la derecha: 5 >> 1 =", 5 >> 1)
print(5 >> 1)
print("Desplazamiento a la izquierda: 5 << 1 =", 5 << 1)
print(5 << 1)
print("")

''' ESTRUCTURAS DE CONTROL '''
print("***ESTRUCTURAS DE CONTROL***")
print("")

# ESTRUCTURAS DE CONTROL CONDICIONALES
print("ESTRUCTURAS DE CONTROL CONDICIONALES")

nombre = "Anaa"
if nombre == "Ana Belén":
    print("Sí, mi nombre es Ana Belén")
elif nombre == "Ana":
    print("Sí, Ana es mi nombre de pila")
elif nombre == "Belén":
    print("Sí, Belén es mi segundo nombre")
else:
    print("Ese no es mi nombre.")
print("")

# ESTRUCTURAS DE CONTROL ITERATIVAS
print("ESTRUCTURAS DE CONTROL ITERATIVAS")

for i in range(5):
# Ejecuta en ese rango desde el 0, el 5 que se colocó como tope: no
    print (i)
print("")

i = 0
while i <= 4:
    print (i)
    i += 1
# Resulta lo mismo que el for de arriba
print("")

i = 0
while i <= 5:
    print (i)
    i += 2
# Si le doy un valor a i, se genera un bucle infinito... así que debo ponerle un fin, después de imprimir, reasignando el valor.
print("")

# ESTRUCTURAS DE CONTROL DE MANEJO DE EXCEPCIONES
print("ESTRUCTURAS DE CONTROL DE MANEJO DE EXCEPCIONES")

try:
    print(10/0)
except:
    print("Se ha producido un error.")
finally:
    print("Ha finalizado el manejo de excepciones.")
print("")

''' PROGRAMA EXTRA '''
print("***PROGRAMA EXTRA***")
print("")

print("Manera 1")
i = 10
while i <= 55:
    if (i % 2 == 1):
        pass
    elif (i % 3 == 0):
        pass
    elif (i == 16):
        pass
    else:   
        print (i)
    i += 1
print("")

print("Manera 2")
i = 10
while i <= 55:
    if (i % 2 == 1 or i % 3 == 0 or i == 16):
        pass
    else:   
        print (i)
    i += 1
print("")

print("Manera 3")
for n in range (10,56):
    if n % 2 == 0 and n != 16 and n % 3 != 0:
        print(n)
print("")