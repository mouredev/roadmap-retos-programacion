"""
 * EJERCICIO:
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

var_numero1 = 1
var_numero2 = 2
var_numero3 = 4
var_numero4 = 4

"""Operadores Aritméticos"""
#Suma
print (f"suma = {var_numero1 + var_numero2}") 
#Resta
print (f"resta = {var_numero1 - var_numero2}") 
#Multiplicación
print (f"multiplicación = {var_numero1 * var_numero2}") 
#División
print (f"división = {var_numero1 / var_numero2}")
#División entera
print (f"división_entera = {var_numero1 // var_numero2}")
#Modulo
print (f"modulo = {var_numero1 % var_numero2}")
#Potencia
print (f"potencia = {var_numero1 ** var_numero2}")


"""Operadores Lógicos"""
#and o conocido como "y" 
if var_numero1 == var_numero2 and var_numero3 == var_numero4:
    print ("son iguales")
else:
    print ("no son iguales")

#or o conocido como "o"
if var_numero1 == var_numero2 or var_numero3 == var_numero4:
    print ("son iguales")
else:
    print ("no son iguales")

#not o conocido como "no"
operando_no =  not (var_numero1 == var_numero2)
if operando_no == True:
        print ("esta correcto el operando")
else:
        print ("¿se ha equivocado?")


"""Operadores comparación"""

print (f"Mayor que: {var_numero1 > var_numero2}") 
print (f"Menor que: {var_numero1 < var_numero2}")
print (f"Igual que: {var_numero1 == var_numero2}")
print (f"Mayor igual que: {var_numero1 >= var_numero2}")
print (f"Menor igual que: {var_numero1 <= var_numero2}")
print (f"No es igual: {var_numero1 != var_numero2}")

"""Operadores asignación"""
#operador =  el valor 7 es asignado a la variable var_operador1
var_operador1 = 2
var_operador2 = 1
#operador += es equivalente a var_operador1 = var_operador1 + 7
var_operador1 += 7
#operador -= es equivalente a var_operador1 = var_operador1 - 7
var_operador1 -= 7
#operador *= es equivalente a var_operador1 = var_operador1 * 7
var_operador1 *= 7
#operador /= es equivalente a var_operador1 = var_operador1 / 7
var_operador1 /= 7
#operador %= es equivalente a var_operador1 = var_operador1 % 7
var_operador1 %= 7
#operador **= es equivalente a var_operador1 = var_operador1 ** 7
var_operador1 **= 7
#operador //= es equivalente a var_operador1 = var_operador1 // 7
var_operador1 -= 7
#operador &= es un operador bit a bit  es equivalente a var_operador1 = var_operador1 & 7
var_operador2 &= 7
#operador |= es un operador bit a bit  es equivalente a var_operador1 = var_operador1 | 7
var_operador2 |= 7
#operador ^= es equivalente a var_operador1 = var_operador1 ^ 7
var_operador2 ^= 7
#operador >>= es un operador bit a bit  es equivalente a var_operador1 = var_operador1 >>= 7
var_operador2 >>= 7
#operador <<= es es un operador bit a bit  es equivalente a var_operador1 = var_operador1 <<= 7
var_operador2 <<= 7


"""Operadores identidad"""
x = 1
y = x
z = y
print (id(z))# muestra el valor de objeto 140732182763960
print (id(x))# muestra el valor de objeto 140732182763960
print (z is x) # muestra True por que comparten el mismo valor de Objeto, esto no quiere decir que compartan valor asignado.
print (z is not x) # muestra False por que comparten el mismo valor de Objeto, esto no quiere decir que compartan valor asignado.

"""Operadores Pertenencia"""
b = [5,4,3,2,1]
#Esta 3 en la lista a?
print (9 in b) # Muestra True  
#No está 12 en la lista a?
print (12 not in b) # Muestra True

"""Operadores Bit a Bit"""
#AND bit a bit (&): 
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print(a & b)  # Resultado es 12 = 0000 1100
#OR bit a bit (|):
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print(a | b)  # Resultado es 61 = 0011 1101
#XOR bit a bit (^):
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print(a ^ b)  # Resultado es 49 = 0011 0001
#NOT bit a bit (~):
a = 60  # 60 = 0011 1100
print(~a)  # Resultado es -61 = 1100 0011
#Desplazamiento a la izquierda (<<): 
a = 60  # 60 = 0011 1100
print(a << 2)  # Resultado es 240 = 1111 0000
#Desplazamiento a la derecha (>>): 
a = 60  # 60 = 0011 1100
print(a >> 2)  # Resultado es 15 = 0000 1111

#reto