""" # #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

```
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
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**. """

#OPERADORES DE ASIGNACIÓN

x = 4       #x = 2
x += 2      #x = x + 2
x -= 2      #x = x - 2
x *= 2      #x = x * 2
x /= 2      #x = x / 2
x %= 2      #x = x / 2
x **= 2     #x = x ** 2

#OPERADORES ARITMÉTICOS

2 + 2       #4
2 - 2       #0
2 * 2       #4
2 / 2       #1
8 // 4      #2
8 % 4       #0
2 ** 3      #8

#OPERADORES DE COMPARACIÓN

x == "y"
x != "y"
x > "y"
x < "y"
x >= "y"
x<= "y"

#OPERADORES LÓGICOS

True and False = False
True and True = True

True or False = True
True or True = True

not True = False

#OPERADORES BIT

print(bin(27)) = "0b11011"

a = "0b1101"
b = "0b1011"
print(bin(a & b)) = "0b1001" #Si ambas posiciones de números coinciden es 1, si no es 0 (equivalente a AND)

a = "0b1101"
b = "0b1011"
print(bin(a | b)) = "0b1111" #Equivalente a OR

a = 40 
print(bin(a)) = "0b101000"
print(bin(~a)) = "-0b101000" #Equivalente a NOT

x = 0b0110 ^ 0b1010 #0b1100
print(bin(x)) 
#0 xor 1 = 1
#1 xor 0 = 1
#1 xor 1 = 0
#0 xor 0 = 0

a = 0b1000 #0b10
print(bin(a>>2)) #Las unidades se desplazan a la derecha el número de veces que marcamos en el bin, rellenándo los puestos de la izquierda con ceros

a = 0b001 #0b1000
print(bin(a<<3)) #Al contrario que el anterior

#OPERADORES DE IDENTIDAD

a = 10
b = 10
print(a is b) #True

a = 10
b = 10
print(a is not b) #False

#OPERADORES DE MEMBRESÍA

print(3 in[1, 2, 3]) #True

print(3 not in[1, 2, 3]) #False

"""----------------------------------------------------------------------"""

#CONDICIONALES

x = input(int())

if x >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#BUCLES

while x >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

edad = input(int())
for x in edad:
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

"""----------------------------------------------------------------------"""

#DIFICULTAD EXTRA

numeros = list(range(10, 56))

for numeros in numeros:
    if numeros % 2 == 0 and numeros != 16 and numeros % 3 != 0:
        print(numeros)
for numeros in numeros:
    if numeros % 2 == 0:
        print(numeros)