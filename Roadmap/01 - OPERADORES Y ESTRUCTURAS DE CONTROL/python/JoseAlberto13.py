'''
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje: Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

#Operadores Aritméticos
print(f"(+) Suma: 8 + 2 = {8 + 2}")
print(f"(-) Resta: 8 - 2 = {8 - 2}")
print(f"(*) Multipicación: 8 * 2 = {8 * 2}")
print(f"(/) División: 8 / 3 = {8 / 3}")
print(f"(//) División Entera 'Int': 8 // 3 = {8 // 3}")
print(f"(%) Modulo o Resto de una División: 8 % 3 = {8 % 3}")
print(f"(**) Potencia: 8 ** 3 = {8 ** 3}")

#Operdores Lógicos
print(f"(and) AND: 8 + 2 == 10 and 8 * 2 == 16 = {8 + 2 == 10 and 8 * 2 == 16}")
print(f"(or) OR: 8 < 2 or 8 > 2 = {8 < 2 or 8 > 2}")
print(f"(or) OR: 8 < 2 or 8 == 2 = {8 < 2 or 8 == 2}")
print(f"(not) NOT: not 8 + 2 == 10 = {not 8 + 2 == 10}")
 
#Operadores de Comparación
print(f"(<) Menor que: 8 < 8 = {8 < 8}")
print(f"(>) Mayor que: 8 > 3 = {8 > 3}")
print(f"(<=) Menor o Igual que: 8 <= 8 = {8 <= 8}")
print(f"(>=) Mayor o Igual que: 8 >= 3 = {8 >= 3}")
print(f"(==) Igual que: 8 == 3 = {8 == 3}")
print(f"(!=) Distinto que: 8 != 3 {8 != 3}")

#Operadores de Asignación
variable = 10
print("(= 10) Asignación variable = ",variable)
variable += 7
print("(+= 7) Suma y aignación variable = ",variable)
variable -= 4
print("(-= 4) Resta y aignación variable = ",variable)
variable *= 4
print("(*= 4) Multiplicación y aignación variable = ",variable)
variable /= 2
print("(/= 2) División y aignación variable = ",variable)
variable %= 3
print("(%= 3) Modulo y aignación variable = ",variable)
variable **= 4
print("(**= 4) Potencia y aignación variable = ",variable)
variable //= 3
print("(//= 3) División Entera y aignación variable = ",variable)

#Operadores de Indentidad
lista1 = ["uno", "dos", "tres"]
lista2 = ["uno", "dos", "tres"]
print("(is) ", lista1 is lista2)
print("(is not) ", lista1 is not lista2)

#Operadores de Pertenencia
print(f"(in) '1' in lista1 = {1 in lista1}")
print(f"(in) '1' not in lista1 = {1 not in lista1}")

#Operadores de Bits
a = 10
b = 3
print(f"a = {bin(a)}\nb = {bin(b)}")
print(f"(&) AND: 10 & 3 = {10 & 3}  resultado en bits {bin(10 & 3)}") #Compara los bits, devolviendo 1 solo cuando ambos bits son 1, de lo contrario es igual a 0.   "1 AND 0 = 0"
print(f"(|) OR : 10 | 3 = {10 | 3}  resultado en bits {bin(10 | 3)}") #Compara los bits, devolviendo 1 si alguno de los bits es 1, de lo contario es igual a 0.      "1 OR  0 = 1"
print(f"(^) XOR: 10 ^ 3 = {10 ^ 3}  resultado en bits {bin(10 ^ 3)}") #Compara los bits, devolviendo 1 si la comparación es diferente, de lo contario es igual a 0.  "1 XOR 1 = 0"
print(f"(>>) Desplazamiento Derecha: 10 >> 3 = {10 >> 3}  resultado en bits {bin(10 >> 3)}") #Desplaza los bits la cantidad de veces que le asignemos a la derecha. "1010  >> 3  = 0101 -> 0010 -> 0001"
print(f"(<<) Desplazamiento Izquierda: 10 << 3 = {10 << 3}  resultado en bits {bin(10 << 3)}") #Desplaza los bits la cantidad de veces que le asignemos a la izquierda, agregando 0. "1010 << 3 = 10100 -> 101000 -> 1010000"

#Estructuras de Control
#--Condicionales
edad = 25
if edad < 18:
    print("La edad es menor a 18 años")
elif edad < 60:
    print("La edad es la de un adulto")
else:
    print("La edad es de un adulto mayor")

#--Iterativas (Bucles)
for i in range (4):
    print(i)

i = 0
while i <= 3:
    print(i)
    i += 1

#--Manejo de Exepciones
try:
    print(10 / 2)
except:
    print("¡ERROR! No se puede dividir entre 0")
finally:
    print("Fin de manejo de exepciones")

'''
EXTRA
'''
i = 10
while i <= 55:
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
    i += 1