
"""

# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
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

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

"""

"""
OPERADORES
"""

#Operadores aritmeticos 
print(f"Suma: 24 + 6 = {24 + 6}")
print(f"Resta: 24 - 6 = {24 - 6}")
print(f"Multiplicacion: 24 * 6 = {24 * 6}")
print(f"Division: 24 / 6 = {24 / 6}")
print(f"Division Entera: 24 // 6 = {24 // 6}")
print(f"Resto: 24 % 6 = {24 % 6}")
print(f"Exponente: 24 ** 6 = {24 ** 6}")

#Operadores de comparacion
print(f"Mayor: 24 > 6 = {24 > 6}")
print(f"Menor: 24 < 6 = {24 < 6}")
print(f"Mayor o igual: 24 >= 6 = {24 >= 6}")
print(f"Menor o igual: 24 <= 6 = {24 <= 6}")
print(f"Igual: 24 == 6 = {24 == 6}")
print(f"Diferente: 24 != 6 = {24 != 6}")

#Operadores logicos     
print(f"AND: 10 + 3 == 13 and 3 + 2 == 5 = {10 + 3 == 13 and 3 + 2 == 5}") #Si ambos true, devuelve true
print(f"OR: 10 + 3 == 13 or 3 + 2 == 5 = {10 + 3 == 14 or 3 + 2 == 6}") #Si alguno true, devuelve true
print(f"NOT: not 10 + 3 == 14 = {not 10 + 3 == 13}") #Si alguno true, devuelve false

#Operadores de asignacion

my_number = 10 #asignacion
print(f"my_number = 10 = {my_number}")
my_number += 10 #suma y asignacion
print(f"my_number += 10 = {my_number}")
my_number -= 10 #resta y asignacion
print(f"my_number -= 10 = {my_number}")
my_number *= 10 #multiplicacion y asignacion
print(f"my_number *= 10 = {my_number}")
my_number /= 10 #division y asignacion
print(f"my_number /= 10 = {my_number}")
my_number %= 10 #modulo y asignacion
print(f"my_number %= 10 = {my_number}")

#Operadores de identidad: is y is not es un operador de comparacion que se utiliza para comprobar si dos variables son la misma o no
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia: in y not in es un operador de comparacion que se utiliza para comprobar si un elemento esta en una secuencia
print(f"'m' in 'martin' = {'m' in 'martin'}")
print(f"'m' not in 'martin' = {'m' not in 'martin'}")

#Operadores de bit 
a = 10 # 1010
b = 3 # 0011

print(f"AND: a & b = {a & b}") # 0010
print(f"OR: a | b = {a | b}") # 1011 
print(f"XOR: a ^ b = {a ^ b}") # 1001 
print(f"NOT: ~a = {~a}") # -11
print(f"DESPLAZAMIENTO A LA IZQUIERDA: a << 2 = {a << 2}") # 40
print(f"DESPLAZAMIENTO A LA DERECHA: a >> 2 = {a >> 2}") # 2


"""
ESTRUCTURAS DE CONTROL
"""

#Condicionales
my_string = "Zeta"

if my_string == "Martin":
    print("my_string es 'Martin'")
elif my_string == "Zeta":
    print("my_string es 'Zeta'")
else:
    print("my_string no es 'Martin' ni 'Zeta'")
    
#Iterativas o bucles

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1
    
#Manejo de excepciones
try:
    # Código que podría causar una excepción
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    
    
"""
EXTRAS
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)