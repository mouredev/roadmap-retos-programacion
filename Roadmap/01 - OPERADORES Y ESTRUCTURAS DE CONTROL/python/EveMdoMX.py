#Operadores en Python
"""
#Operadores aritméticos

#Operadores Relacionales

#Operadores Bit a Bit

#Operadores de Asignación

#operadores logicos

#operador de identidad
"""

#Operadores aritméticos

var_1 = 4
var_2 = 5


print("Suma: ", var_1 + var_2, "\n" "Resta: ", var_1 - var_2)
print("Multiplicación: ", var_1 * var_2, "\n" "División: ", var_1 / var_2 , "\n" "División con resultado entero: ", var_1 // var_2)
print("Módulo: ", var_1 % var_2, "\n" "Potencia: ", var_1 ** var_2)
print("\n")

#Operadores Relacionales

print("¿Es var_1 mayor que var_2?: ", var_1 > var_2)
print("¿Es var_1 menor que var_2?: ", var_1 < var_2)
print("¿Es var_1 igual a var_2?: ", var_1 == var_2)
print("¿Es var_1 diferente de var_2?: ", var_1 != var_2)
print("¿Es var_1 mayor o igual var_2?: ", var_1 >= var_2)
print("¿Es var_1 menor o igual var_2?: ", var_1 <= var_2)
print("\n")

#Operadores Bit a Bit
print(bin(var_1) + " AND " + bin(var_2) + ":", bin(var_1 & var_2))
print(bin(var_1) + " OR: " + bin(var_2) + ":", bin(var_1 | var_2))
print(bin(var_1) + " XOR: " + bin(var_2) + ":", bin(var_1 ^ var_2))
print(bin(var_1) + " NOT: " + bin(~var_1) + ":", bin(~var_1))
print(bin(var_1) + "Desplazamiento a la izquierda: " + bin(var_1 << 2) + ":", bin(var_1 << 2))
print(bin(var_1) + "Desplazamiento a la derecha: " + bin(var_1 >> 2) + ":", bin(var_1 >> 2))
print("\n")

#Operadores de Asignación

print("Asignación: ", var_1)
var_1 += 1
print("Asignación de suma + 1 : ", var_1)

var_1 -= 1
print("Asignación de resta - 1 : ", var_1)

var_1 *= 1
print("Asignación de multiplicación * 1 : ", var_1)

var_1 /= 1
print("Asignación de división / 1 : ", var_1)

var_1 %= 1
print("Asignación de módulo % 1 : ", var_1)

var_1 **= 1
print("Asignación de potencia ** 1 : ", var_1)

var_1 //= 1
print("Asignación de división entera // 1 : ", var_1)

var_2 = 0b111

var_2 &= 1
print("Asignación de AND & 1 : ", var_2)

var_2 |= 1
print("Asignación de OR | 1 : ", var_2)

var_2 ^= 1
print("Asignación de XOR ^ 1 : ", var_2)

var_2 >>= 1
print("Asignación de desplazamiento a la derecha >> 1 : ", var_2)

var_2 <<= 1
print("Asignación de desplazamiento a la izquierda << 1 : ", var_2)

#operador de identidad

a = 10
b = 10

print(a is b) #true

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True
print(a is b) # False


a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b) # True

a = 5
b = 5

print(a is not b)

#operadores logicos

var_true = True
var_false = False #false

print("var_true and var_false: ", var_true and var_false)
print("var_true or var_false: ", var_true or var_false)
print("not var_true: ", not var_true)


#tipos de estructuras

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [5, 6, 7, 8, 9]
tupla_1 = (1, 2, 3, 4, 5)
tupla_2 = (5, 6, 7, 8, 9)
set_1 = {1, 1, 5, 4, 5}
set_2 = {5, 6, 9, 8, 9}


print("¿lista_1 esta en lista_2?: ", lista_1 in lista_2)
print("¿tupla_1 no esta en tupla_2?: ", tupla_1 not in tupla_2) 
print("¿set_1 esta en set_2?: ", set_1 in set_2)


"""
#Estructuras condicionales
    IF
    ELIF
    ELSE
    MATCH

#Estructuras bucle/iterativas
    FOR
    WHILE
    DO/WHILE
    BREAK
    CONTINUE

#Estructuras espreciones
    TRY
    EXCEPT
    FINALLY

"""

#Estructuras condicionales

var_5 = 10
var_6 = 20


if var_5 != var_6:
    print("Las variables son diferentes")
elif var_5 == var_6:
    print("Las variables son iguales")
else:
    print("aqui solo improme la sentencia else")


"""status = 404

match status:
    case 400 | 404:
        print("Error del cliente (solicitud mala o no encontrada)")
    case 500 | 502:
        print("Error del servidor")
    case _:
        print("Otro código")
"""


#Estructuras bucle/iterativas
    
    #for

frutas = ["manzana", "pera", "uva"]
for f in frutas:
    print(f)

for i in range(10):
    print(i)  # Muestra del 0 al 9


for i in range(10):
    if i == 5:
        break
    print(i)

for letra in "hola":
    print(letra)


for numero in range(1, 6):
    if numero == 3:
        continue  # Salta el número 3
    print(numero)


    #while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

    #WHILE true
while True:
    texto = input("Escribe 'salir' para terminar: ")
    
    if texto.lower() == "salir":
        break


#Estructuras espreciones
    #TRY
    #EXCEPT
    #FINALLY

try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Debes ingresar un número válido.")
else:
    print(f"El resultado es {resultado}.")
finally:
    print("Fin del proceso.")

"""
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

contador= 1

while contador <= 55:
    if contador %2 == 0 and contador != 16 and contador %3 != 0 and contador >10:
        print (contador)
    contador += 1


for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
        