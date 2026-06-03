#................................................Ejercicios................................................

"""
1 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, 
    lógicos, de comparación, asignación, identidad, pertenencia, bits...
"""
#Aritméticos 
print("Tipo de Operadores")
print("Arimeticos")
print (4 + 2) #Suma
print (4 - 2) #Resta
print (4 * 2) #Multiplicación
print (4 / 2) #División
print (5 // 2) #División Entera
print (5 % 2) #Módulo
print (2 ** 2 ) #Exponente

#Lógicos 
print("\nLógicos")
print (True and False)
print (True or False)
print (not True)

#De Comparación
print("\nComparación")
a = 5
b = 4

print (a == b)#Igual a
print (a != b)#Diferente de
print (a > b)#Mayor que
print (a < b)#Menor que
print (a >= b)#Mayor o igual que
print (a <= b)#Menor o igual que

#Asignación
print("\nAsignación")
Numero = 100
print(Numero) #Asigna un valor

Numero += 100
print(Numero) #Suma y asigna el valor

Numero -= 100
print(Numero)#Resta y asigna.

Numero *= 100
print(Numero)#Multiplica y asigna

Numero /= 100
print(Numero)#Divide y asigna

Numero **= 100
print(Numero)#exponente y asigna

Numero //= 100
print(Numero)#Divide entero y asigna

Numero %= 100
print(Numero)#Módulo y asigna

#Identidad
print("\nIdentidad")
a = 10
b = 10

print(a is b) # Is (comprueba si dos variables hacen referencia a el mismo objeto)

a = 5
b = 6
print(a is not b) # Is Not (Ambas variables no hacen referencia al mismo objeto.)


#Pertenencia
print("\nPertenencia")
x = ["Manzana", "Platano"]

print("Platano" in x) #In

print("Platano" not in x) #Not In

#Bits
print("\nBits")
x = 6 & 3 
print (x) #AND resulta 2 (0110 & 0011 = 0010)

x = 6 | 3 
print (x)#OR resulta 7 (0110 | 0011 = 0111)

x = 6 ^ 3 
print (x)#XOR resulta 5 (0110 ^ 0011 = 0101)

x= ~6
print (x)#NOT invierte los bits

x= 6 >> 1
print (x) #Desplazacmiento a la Derecha, resulta 3 (elimina el último bit y desplaza el resto a la derecha, 0110 pasa a ser 0011).

x= 6 << 1
print(x)# Desplazamiento a la Izquierda resulta 12 (0110 pasa a ser 1100).
#------------------------------------------------------------------------------------------

"""
 2 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
 Debes hacer print por consola del resultado de todos los ejemplos.
"""
print("\nEstructuras de Control")
#Condicionales
print ("Condicionales")
a = 2 + 2

if (a == 4):
    print ("El resultado es correcto") #If

a = 3 + 3
if (a == 6):
    print ("El resultado es correcto") 
else:
    print ("El resultado es incorrecto")#If-Else

a = 4-4
if (a == 0):
    print ("El resultado es correcto") 
elif (a==0.0):    
    print ("Estamos trabajando con enteros")
else:
    print ("El resultado es incorrecto")#If-Elif
    

#Iterativas
print("\nIterativas")
i=0
while i<=10:
    print(i)
    i+=1 #While

i=0

for i in [1,2,3,4]: 
    print(i)#For

#Exepciones
print("\nExepciones")

try:
    # Código que puede generar un error
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre la excepción
    print("¡Error! No se puede dividir entre cero.")
else:
    # Código que se ejecuta solo si NO hubo excepciones
    print("El resultado es:", resultado)
finally:
    # Código que siempre se ejecuta, haya error o no
    print("Fin del bloque try-except.")
#------------------------------------------------------------------------------------------

"""
3- DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
#Primera solución
print("\n1° Forma")
for i in range(10, 56):
    if i %3 == 0 or i == 16:
        i+=1
    elif i%2 == 0: 
        print (i)
        i+=1

print("\n2° Forma")
#Segunda solución
for i in range (10, 56):
    if i%2 == 0 and i%3 != 0 and i !=16:
        print(i)
