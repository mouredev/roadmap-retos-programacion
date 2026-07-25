# EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


# Operadores Aritméticos
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
exponente = a ** b
division_entera = a // b

print("Operadores Aritméticos:\n---------------------------")
print("Suma:", suma)    
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Exponente:", exponente)
print("División Entera:", division_entera)


# Operadores de asignación
x = 5 

print("\nOperadores de Asignación:\n---------------------------")
x += 2 
print("Después de x += 2:", x)
x -= 1
print("Después de x -= 1:", x)
x *= 3 
print("Después de x *= 3:", x)
x /= 2 
print("Después de x /= 2:", x)
x %= 2 
print("Después de x %= 2:", x)
x //= 2 
print("Después de x //= 2:", x)
x **= 2
print("Después de x **= 2:", x)
x = int(x)  # Asegurar que x es entero antes de operaciones bit a bit
x &= 1 
print("Después de x &= 1:", x)
x |= 2 
print("Después de x |= 2:", x)
x ^= 1 
print("Después de x ^= 1:", x)
x >>= 1 
print("Después de x >>= 1:", x)
x <<= 1
print(x := 3)


# Operadores de comparación
a = 7
b = 10

igual = a == b
diferente = a != b
mayor_que = a > b
menor_que = a < b
mayor_o_igual = a >= b
menor_o_igual = a <= b

print("\nOperadores de Comparación:\n---------------------------")
print("Igual:", igual)
print("Diferente:", diferente)  
print("Mayor que:", mayor_que)
print("Menor que:", menor_que)
print("Mayor o igual:", mayor_o_igual)  
print("Menor o igual:", menor_o_igual)

# Operadores lógicos
x = 10
y = 5

and_result = (x > 5) and (y < 10)
or_result = (x < 5) or (y < 10)
not_result = not (x > 5)

print("\nOperadores Lógicos:\n---------------------------")
print("AND:", and_result)
print("OR:", or_result)
print("NOT:", not_result)


# Operadores de identidad
list1 = [1, 2, 3]
list2 = list1
is_result = list1 is list2
is_not_result = list1 is not [1, 2, 3]

print("\nOperadores de Identidad:\n---------------------------")
print("is:", is_result)
print("is not:", is_not_result)


# Operadores de pertenencia
frutas = ['manzana', 'banana', 'cereza']
in_result = 'banana' in frutas
not_in_result = 'pera' not in frutas

print("\nOperadores de Pertenencia:\n---------------------------")
print("in:", in_result)
print("not in:", not_in_result)


# Operadores a nivel de bits
p = 5
q = 3
and_bit = p & q
or_bit = p | q
xor_bit = p ^ q
not_bit = ~p
left_shift = p << 1
right_shift = p >> 1

print("\nOperadores a Nivel de Bits:\n---------------------------")
print("AND a nivel de bits:", and_bit)
print("OR a nivel de bits:", or_bit)
print("XOR a nivel de bits:", xor_bit)
print("NOT a nivel de bits:", not_bit)
print("Desplazamiento a la izquierda:", left_shift)
print("Desplazamiento a la derecha:", right_shift)



# Estructuras de control
print("\nEstructuras de Control:\n---------------------------")

# Estructura condicional
print("Estructura Condicional\n---------------------------")

num = 15

if num > 10:
    print("El número es mayor que 10")
elif num == 10:
    print("El número es igual a 10")
else:
    print("El número es menor que 10")


my_string = "Hola Mundo"
if 'Mundo' in my_string:
    print("La cadena contiene 'Mundo'")
else:
    print("La cadena no contiene 'Mundo'")


day = "Sábado"
match day:
    case "Lunes":
        print("Hoy es Lunes")
    case "Martes":
        print("Hoy es Martes")
    case "Miércoles":   
        print("Hoy es Miércoles")
    case "Jueves":
        print("Hoy es Jueves")
    case "Viernes":
        print("Hoy es Viernes")
    case "Sábado" | "Domingo":
        print("Es fin de semana")
    case _:
        print("Día no válido")


# Estructura iterativa
print("\nEstructura Iterativa\n---------------------------")

for i in range(16):
    print("Iteración:", i)

num = 0
while num <= 15:
    print("Iteración:", num)
    num += 1


# Estructura de manejo de excepciones
print("\nEstructura de Manejo de Excepciones\n---------------------------")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
finally:
    print("Bloque finally ejecutado.")



# DIFICULTAD EXTRA
print("\nNúmeros entre 10 y 55, pares, que no son ni el 16 ni múltiplos de 3:\n---------------------------")

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)