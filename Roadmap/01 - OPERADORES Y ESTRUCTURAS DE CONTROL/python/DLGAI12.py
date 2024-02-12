"""/*
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
num1 = 14
num2 = 5
""" Operadores Aritmeticos """

print("Operadores Aritmeticos")
print("Suma:num1+num2 =",num1+num2)
print("Resta:num1-num2 =",num1-num2)
print("Multiplicación:num1*num2 =",num1*num2)
print("División:num1/num2 =",num1/num2)
print("Modulo:num1%num2 =",num1%num2)
print("Potencia:num1+num2 =",num1**num2)
print("Divición Entera :num1//num2 =",num1//num2)

""" Operadores Relacionales """

print("Operadores Relacionales")
#Mayor Que >
print(str(num1)+">"+str(num2)+":"+str(num1>num2)) # Devuelve True si el  primer operando es mayor que el segundo si no false

#Menor Que <
print(str(num1)+"<"+str(num2)+":"+str(num1<num2)) # Devuelve True si el  primer operando es menor que el segundo si no false

#Igual que ==
print(str(num1)+"=="+str(num2)+":"+str(num1==num2)) # Devuelve True si el  primer operando es igual que el segundo si no false

#Mayor o Igual Que >=
print(str(num1)+">="+str(num2)+":"+str(num1>=num2)) # Devuelve True si el  primer operando es mayor o igual  que el segundo si no false

#Menor o Igual Que <=
print(str(num1)+"<="+str(num2)+":"+str(num1<=num2)) # Devuelve True si el  primer operando es menor o igual  que el segundo si no false

#Distinto  Que !=
print(str(num1)+"!="+str(num2)+":"+str(num1!=num2)) # Devuelve True si el  primer operando es distinto que el segundo si no false

""" 
    Operadores de Asignación
"""
print("Operadores de Asignación")
#=
i=5
print(i)

#+=5
i+=5
print(i)

#-=5
i-=5
print(i)

#*=5
i*=5
print(i)

#/=5
i/=5
print(i)

#%=5
i=9
i%=5
print(i)

#**=5
i**=5
print(i)

#//=5
i//=5
print(i)

a = 7  # Binario: 111
b = 9  # Binario: 1001

a &= b
print("a &= b =", a)

a |= b
print("a |= b =", a  )

a ^= b
print("a ^= b =", a ) 

a>>=b
print("a >>= b =", a) 

a<<=b
print("a << = b =", a)  

"""
    Operadores Lógicos
"""

print("Operadores Lógicos")
a=True 
b=False

print(a and b) # Devuelve true si a y b son verdaderos si no devuelve false
print(a or b) # Devuelve true si a o b son verdaderos si no devuelve false
print(not a) # Devuelve lo conntrario a lo que recibe si recibe true devuelve false y si recibe false devuelve true

"""
    Operadores de Pertenencia
"""
print("Operadores de Pertenencia")
a = [1,2,3,4,5]
  
#Esta 3 en la lista a?
print(3 in a) # Muestra True 
  
#No está 12 en la lista a?
print(12 not in a) # Muestra True

"""
    Operadores de Identidad
"""
print("Operadores de Identidad")
a = 3
b = 3  
c = 4
print ( a is b) # muestra True
print (a is not b) # muestra False
print (a is not c) # muestra True

x = 1
y = x
z = y
print (z is 1) # muestra True
print (z is x )# muestra True

str1 = "Hola"
str2 = "Hola"

print (str1 is str2 )# muestra True
print ("Codigo" is str2 )# muestra False

a = [10,20,30]
b = [10,20,30]

print (a is b) # muestra False (ya que las listas son objetos mutables en Python)  


""" Estructuras de control"""
print("Estructuras de control")
#condicionales
a=5


if(a>0):
    print("A es positivo")
elif(a<0):
    print("B es negativo")
else:
    print("A es cero")
    
    
print ("for")
for i in range(5):
    print(i)

x=5
print ("while")
while x > 0:
    print (x)
    x-=1

"""Control de flujo dentro de bucles"""
print("Control de flujo dentro de bucles")
# Ejemplo de break
for i in range(10):
    if i == 5:
        break
    print(i)

print("Continue")
# Ejemplo de continue
for i in range(10):
    if i == 5:
        continue
    print(i)


#Manejo de excepciones
print("Excepecion")
try:
    x = 1 / 0 
except ZeroDivisionError:
    print("No se puede dividir por cero!")
finally:
    print("Este código se ejecuta sin importar si hubo un error o no")
   
print("Extra")
for i in range(10,56):
    if (i == 16 or i%2==0 or i%3==0):
        continue
    print(i)

numeros = [i for i in range(10, 56) if i != 16 and i % 2 != 0 and i % 3 != 0]
for numero in numeros:
    print(numero)