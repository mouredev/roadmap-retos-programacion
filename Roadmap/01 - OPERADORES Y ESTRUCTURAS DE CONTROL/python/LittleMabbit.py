# * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

## Operadores Aritméticos - Operadores utilizados para llevar acabo operaciones matemáticas
my_sum = 5 + 5 # 10 - Suma de dos numeros positivos
print(my_sum)
my_sub = 5 - 4 # 1 - Resta de dos numeros positivos.
print(my_sub)
my_mult = 2 * 2 # 4 - Multiplicacion de numeros positivos.
print(my_mult)
my_div = 10 / 2 # 5 - División de numeros positivos
print(my_div)
my_floor_div = 10 // 3 # 3 - Divisón cuyo restante redondea.
print(my_floor_div)
my_modulo = 10 % 7 # 3 - Modulo de una operación, es decir, el restante de una operación.
print(my_modulo)
my_power = 2 ** 8 # 256
print(my_power)


## Operadores de Asignación - Operadores utilizados para asignar valores a variables.
a = 1 # Utilizando el '=' asignamos '1' a la variable 'a'.
print(a)
a += 1 # Utilizando el '+=' y asignando el valor de '1' a la variable 'a', tomamos el valor actual de la variable 'a' y le sumamos '1'. Luego actualizamos 'a' con el resultado.
print(a)
a -= 1 # Utilizando el '-=' y asignando el valor de '1' a la variable 'a', tomamos el valor actual de la variable 'a' y le restamos '1'. Luego actualizamos 'a' con el resultado.
print(a)
a *= 6 # Utilizando el '*=' y asignando el valor de '6' a la variable 'a', tomamos el valor actual de 'a' y lo multiplicamos por '6' luego actualizamos 'a' con el resultado.
print(a) # Para que este funcione, toca cambiar el valor inicial de la variable 'a' en la linea 22.
a /= 3 # Utilizando el '/=' y asignando el valor de '6' a la variable 'a', tomamos el valor actual de 'a' y lo dividimos entre '3', luego actualizamos 'a' con el resultado.
print(a) # Para que este funcione, toca cambiar el valor inicial de la variable 'a' en la linea 22.
a %= 6 # Utilizando el '%=' y asignando el valor de '6' a la variable 'a', tomamos el valor actual de 'a' y calculamos el restante de '6', luego actualizamos 'a' con el resultado.
print(a)
a **= 8 # Utilizando el '**=' y asignando el valor de '8' a la variable 'a', tomamos el valor actual de 'a' y elevamos al cuadrado '8' veces, luego actualizamos 'a' con el resultado.
print(a)

b = 5
c = 8
b /= c
print(b)

'''
En el ejemplo de encima, utilizamos la división para tomar el valor de B, y dividirlo entre C y actualizar el resultado de B.
'''

## Operadores de Comparación - Compara los resultados entre dos variables/valores y retorna un booleano True o False.
'''
a = 5
b = 2

print (a > b)    # True - is 'a' greater than 'b'? False
'''

seis = 6
diez = 10

seis == diez # Igual a - Devuelve False, ya que seis es menos que diez, no es igual.
seis != diez # Diferente a - Devuelve True, ya que seis es diferente a diez.
seis > diez # Mayor a - Devuelve False, ya que seis no es mayor a diez.
seis < diez # Menor a - Devuelve True, ya que seis es menor a diez.
seis >= diez # Mayor o igual a - Devuelve False, ya que seis no es mayor ni tampoco es igual a diez.
seis <= diez # Menor o igual a - Devuelve True, ya que seis es menor a diez, mas no igual.

## Operadores lógicos - Operadores utilizados para saber si una operación es True o False.

a = 5
b = 6

print((a > 2) and (b >= 6))    # True - Devuelve true ya que 'a' es mayor a '2', y 'b' es mayor o igual a '6'. Como ambos son True, devuelve True.
print((a > 2) or (b >= 6))    # True - Devuelve true ya que uno de los dos operandos es true.
print(not True)    # False - Es lo contrario a lo que se verifica con el not. En este caso, da False. Si escribiera False, entonces sería True.

## Operadores en bits - Operadores utilizados para calcular en base a bits.
a = 5 # 0101
b = 10 # 1010

# Bitwise AND (&) retornará el valor de '1' cada vez que los bits en su posición correspondiente equivalgan a '1'.
result_and = a & b   # 0101 & 0011 = 0001 (1 en decimal)
print("Bitwise AND:", result_and)

# Bitwise OR (|) retornará el valor de '1' cada vez que uno de los los bits en su posición equivalga a '1', de resto si es 0, entonces devolverá 0.
result_or = a | b    # 0101 | 0011 = 0111 (7 en decimal)
print("Bitwise OR:", result_or)

# Bitwise XOR
result_xor = a ^ b   # 0101 ^ 0011 = 0110 (6 en decimal)
print("Bitwise XOR:", result_xor)

# Bitwise NOT (~) retornará el valor de los bits una vez estos sean flipeados y convertidos a decimales.
result_not_a = ~a   # 0101 -> 1010 -> 11010 -> 2^4 = -16 + 8 + 2 = 6. El 0101 equivale al 5, flipeado queda 1010, mas el sign bit quedaría en 11010, el primer bit se eleva a su posición (cuarta posición) osea 2^4, queda -16 (negativo por su signo) y luego los bits activos (8 y 2 por su valor elevado) se le suman al -16.
print("Bitwise NOT of a:", result_not_a)

# Left Shift
result_left_shift = a << 1   # 0101 << 1 = 1010 (10 in decimal)
print("Left Shift of a:", result_left_shift)

# Right Shift
result_right_shift = a >> 1  # 0101 >> 1 = 0010 (2 in decimal)
print("Right Shift of a:", result_right_shift)


## Operadores de identidad - Operadores utilizados para saber si dos valores estan localizados en el mismo lugar en la memoria física.
a1 = 5
b1 = 5
a2 = 'Hola'
b2 = 'Hola'
a3 = [1,2,3]
b3 = [1,2,3]

print(a1 is not b1)  # prints False - a1 literalmente se almacena en el mismo lugar que b1, así que retorna False, ya que NO está lugares diferentes.

print(a2 is b2)  # prints True - a2 se encuentra en el mismo lugar en memoria que b1, con el mismo valor, así que retorna True ya que bueno, a2 literalmente está en b2.

print(a3 is b3)  # prints False - Esto sucede porque a pesar de que los valores son iguales, no son idénticos en memoria.

## Operadores de membresía/pertenencia - Operadores utilizados para comprobar la validez de un valor en una sequencia.
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

print('H' in message)  # Devuelve True - Revisará si el string con la letra 'H' está en la variable 'mensaje'.
print('hello' not in message)  # prints True - Revisará si el string 'hello' NO esta en mensaje, en este caso devuelve True, osea que realmente NO está en message.
print(1 in dict1)  # prints True - Revisará si la key '1' está presente en 'dict1', y como lo está, entonces devuelve True.
print('a' in dict1)  # prints False - Revisará si el string 'a' está en dict1, y como no lo está, entonces devuelve False.

'''
 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
'''

a = 5
b = 10
#Declaración de 'if's.
if a < b:
    print(f"{a} es menor que {b}")
if b > a:
    print(f"{b} es menor que {a}")

# Declaración de 'else-if'
if a > b:
    print(f"Esta es una declaración else-if. {a} es menor que {b}")
else:
    print(f"Esta es la parte 'else' de un else-if. {a} es mayor que {b}")

# Declaración de elif
if a > b:
    print(f"Esta es una declaración elif. {a} es menor que {b}")
elif a < b:
    print(f"Esta es la parte 'elif' de un else-if. {a} es mayor que {b}")
else:
    print("Está fuera del rango.")
   
# Declaración del for loop
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    print(i)

# Declaración de un while
x = 0

while x < 10:
    x += 1
    print("Esto es un bucle while", x)

# Declaración de una excepción
valores = [10, 8, 5, 0, 2, 6, 7, 'Hi']

for valor in valores:
    try:
        print(10 / valor)
    except ZeroDivisionError as e:
        print(f"Un error ha ocurrido: {e}")
    except TypeError as e:
        print(f"{e}. \nPor favor, no uses texto en este campo.")


def ejercicioExtra():
    # Crear numeros entre 10 y 55
    for i in range(10, 56):
        # Si el módulo de i entre 2 da 0, y el indice i NO es igual a 16, y el módulo de i entre 3 no es igual a 0, entonces haz print.
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)

        
ejercicioExtra()