"""
*
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

"""
#SOLUCION

a = 10
b = 2
x = [2, 5, 10]

#Operadores

print("La suma de 10 y 2 es: ", a + b) #Suma

print("La resta de 10 y 2 es: ",a - b) #Resta

print("La multiplicacion de 10 y 2 es: ",a * b)

print("La division de 10 en 2 es: ",a / b)

print("El modulo (Residuo) de 10 / 2 es: ",a % b)

print("10 elevado al 2 es: ",a ** b)

print("La division redondeada de 10 en 3 es: ", a // 3)

b += 3 #otra forma de sumar a una variable

print("La suma de 2 y 3 es: ",b)

b -= 3 #otra forma de restar a una variable

print("La resta de 5 y 3 es: ", b)

a *= 3 #otra forma de multiplicar a una variable

print("La multiplicacion de 10 y 3 es: ",a)

a /= 3 #otra forma de dividir a una variable

print("La divison de 30 entre 3 es: ",a)

a %= 3 #otra forma de sacar el modulo a una variable

print("El modulo (Residuo) de 10 / 3 es: ", a)

b //= 1.2  #otra forma de sacar la division redondeada a una variable

print("El resulatdo redondeado de de 2 / 1.2 es: ",a)

a **= 3 #otra forma de sacar la potencai x de una variable
 
print("El resulatdo de 1 elevado a la 3 es: ", a)

print("1 y 1 son lo mismo?: ", a == b) #Comparacion de igualdad entre dos varibles // True o False

print("1 y 1 son lo diferentes?: ", a != b) #Comparacion de diferncia entre dos varibles // True o False

print ("1 es mayor que 1?: ",a > b) #Comparacion de que valor es más grande > // True o False

print("1 es menor que 2?: ",a < 2) #Comparacion de que valor es más grande < // True o False

print("1 es mayor o igual que 1?: ",a >= b) #Comparacion de que valor es más grande o igualdad (inclusivo) > // True o False

print("1 es menor o igual que 2?: ",a <= 2) #Comparacion de que valor es más grande o igualdad (inclusivo) < // True o False

print(a > b and a < 100) #operador "and" devuelve true si los dos statements son verderos (True) // True o False

print(a < b or a < 100) #operador "or" devuelve true si uno de los dos statements son verderos (True) // True o False

print(not(a > b and a < 100)) #operador "not" invierte el resultado del operador logioo // True o False

print(a in x) #Operador "in" para revisar si un elemento esta en otro // Este caso de variable en lista // True o False

print(b not in x) #Operador "not in" para revisar si un elemento no esta en otro // Este caso de variable en lista // True o False

#Estructuras de Control

#if Else

if a > b:
    print("a es mayor que b!")
elif a < b:
    print("b es mayor que a!")
else:
    print("a y b son iguales!")

#While
    
while a < 5:
    print(a)
    a += 1

#For

for i in x:
  if i == 10:
    break
  print(i)

#Try Except

try:
  print(x)
except:
  print("Un error ocurrió")

#EXTRA
"""
Extra Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

 if x % 2 == 0 | x % 3 != 0 | x != 16:
"""

for x in range(10, 55):
   if  x % 3 != 0 and x % 2 == 0 and x != 16 :
      print(x)

