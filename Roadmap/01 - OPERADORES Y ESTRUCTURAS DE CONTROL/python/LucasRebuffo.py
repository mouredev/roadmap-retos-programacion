""" /*
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
 */ """

##Operadores aritmeticos
print(f"Suma 100 + 50 :{100+50}")
print(f"Resta 100 - 50 :{100-50}")
print(f"Multiplicacion 100 * 50 :{100*50}")
print(f"Division 100 / 50 :{100/50}")
print(f"Modulo 100 % 50 :{100 % 50}")
print(f"Potencia 2 ** 50 :{2**50}")
print(f"Division entera 2 // 50 :{6**50}")

## Operadores de comparacion
print(f"Igual 6 == 6 :{6==6}")
print(f"No igual 6 != :{6!=6}")
print(f"Mayor 2 > 50 :{6>50}")
print(f"Menor entera 2 < 50 :{6<50}")
print(f"Menor o igual entera 2 <= 50 :{6<=50}")
print(f"Mayor o igual entera 2 >= 50 :{6>=50}")
print(f"Division entera 2 // 50 :{6**50}")

##Operadores logicos
print(f"AND True and True :{4+4 == 8 and 6 == 5+1}")
print(f"OR True or False :{4+4 == 8 or 6 == 5}")
print(f"NOT False :{not 6 == 9*3}")

## Operadores de asignacion
num = 4
print(num)
num += 1
print(num)
num -= 1
print(num)
num *= 2
print(num)
num /= 3
print(num)
num %= 2
print(num)
num **= 2
print(num)
num //= 4
print(num)

## Operadores de identidad
my_var = 0.0
print(f"my_var is my_other_var {my_var is num}")
print(f"my_var is not my_other_var {my_var is not num}")

## Operadores de pertenencia
print(f"'u' in 'lucas' = {'u' in 'lucas'}")
print(f"'v' not in 'lucas' = {'u' not in 'lucas'}")


## Operadores de bit
a = 8  # 1000
b = 9  # 1001
print(f"AND : 8 & 9: {a & b}")
print(f"OR : 8 | 9: {a | b}")
print(f"XOR : 8 ^ 9: {a ^ b}")
print(f"NOT : ~8: {~a}")
print(f"RShift : 8 >> 2: {a >> 2}")
print(f"LShift : 8 << 2: {a << 2}")

## Estructuras de control

## Condicionales
var = "lucas"
if var == "alberto":
    print("Condicional")
elif var != "lucas":
    print("elif")
else:
    print("else")

##Iterativas
for num in range(11):
    print(num)

numer = 20
while numer > 0:
    print(numer)
    numer -= 1

## Excepciones
try:
    10 / 0
except:
    raise (ZeroDivisionError)
finally:
    print("Finalizado exitosamente")


## Extra
for num in range(10, 56):
    if (not (num == 16 or num % 3 == 0)) and num % 2 == 0:
        print(num)
