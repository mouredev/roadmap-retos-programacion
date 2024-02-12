# @RoniPG
	
print("Tipo de operadores.")
		
print("Operadores Aritmeticos.")
		
print("Suma +, Resta -, Division /, Multiplicacion *, Resto % (En la division inexacta = lo que sobra)") 
		
print("Ejemplos")

a = 2
b = 3

suma = a + b
print(str(a) + " + " + str(b) + " = " + str(suma))

resta = a - b
print(str(a) + " - " + str(b) + " = " + str(resta))

division = a / b
print(str(a) + " / " + str(b) + " = " + str(division))

multiplicacion = a * b
print(str(a) + " * " + str(b) + " = " + str(multiplicacion))

resto = a % b
print(str(a) + " % " + str(b) + " = " + str(resto))

print("Operadores de Asignacion.")

print(" = para asignar el valor sobrescirbiendolo")
print("+= sumar a la variable el valor dedicidido")
print("-= restar a la variable el valor dedicidido")
print("*= mutilpicar a la variable el valor dedicidido")
print("/= dividir a la variable el valor dedicidido")

print("Ejemplos")

print(a)
print(str(a) + " += 2 ")
a += 2
print(a)
print(str(a) + " -= 2 ")
a -= 2
print(a)
print(str(a) + " *= 2 ")
a *= 2
print(a)
print(str(a) + " /= 2 ")
a /= 2
print(a)

print("Operadores de comparacion")

print("== igual a (para objetos equals(), != difente de, < menor que,") 
print("<= menor o igual que, >= mayor o igual que, > mayor que.") 
print("Todos estos valores devuelven un booleano true o false")

print("Ejemplos")

comparacion = False

a = 2

print(str(a) + " | " + str(b))
comparacion = a == b
print(str(a) + " es igual a " + str(b) + ": " + str(comparacion))
comparacion = a != b
print(str(a) + " no es igual a " + str(b) + ": " + str(comparacion))
comparacion = a < b
print(str(a) + " es menor que " + str(b) + ": " + str(comparacion))
comparacion = a <= b
print(str(a) + " es menor o igual que " + str(b) + ": " + str(comparacion))
comparacion = a >= b
print(str(a) + " es mayor o igual que " + str(b) + ": " + str(comparacion))
comparacion = a > b
print(str(a) + " es mayor que " + str(b) + ": " + str(comparacion))

print("Operadores logicos.")

print("operador or (devuelve true si una de las variables se cumple)")
print("operador and (devuelve true si todas las variables se cumplen)")
print("operador not (invierte el valor de la condici├│n, de true a false y viceversa)")

print("Ejemplos")

logico= True
comparacion=False

print("Operador OR: " + str(comparacion) + " or " + str(logico))

if comparacion or logico: 
    print(logico)
else:
    print(comparacion)

print("Operador AND: " + str(comparacion) + " and " + str(logico))
if comparacion and logico:
    print(logico)
else:
    print(comparacion)

print("Operador NOT: not " + str(comparacion))
if not comparacion:
    print(logico)
else:
    print(comparacion)

print("Operadores ternarios")

print("Tienen la forma: valor_si_verdadero if condicion else valor_si_falso.")

print("Ejemplos")

ternario = False

ternario = logico if comparacion or logico else comparacion
print("Operador OR en ternario: " + str(comparacion) + " or " + str(logico) + " ternario = " + str(ternario))
ternario = logico if comparacion and logico else comparacion
print("Operador AND en ternario: " + str(comparacion) + " and " + str(logico) + " ternario = " + str(ternario))
ternario = logico if not comparacion else comparacion
print("Operador NOT en ternario: not" + str(comparacion) + " ternario = " + str(ternario))

print("Operadores de concatenacion")

print("+ Unir diferentes strings a uno solo.")

print("Ejemplos")

texto1 = "Hola, "
print(texto1)
texto2 = "Python!"
print(texto2)
textoFinal = texto1 + texto2
print(textoFinal)

print("Operadores de conversion de tipo\nNo contiene ya que es un lenguaje debilmente tipado")

print("Ejemplos")

texto1 = "2"
print(type(texto1))
print("Dato en texto = " + texto1)
texto1 = 2
print(type(texto1))
print("Dato convertido a entero = " + str(texto1))
texto1 = "2"
print(type(texto1))
print("Dato convertido a texto = " + texto1)
texto1 = 2.0
print(type(texto1))
print("Dato convertido a flotante = " + str(texto1))

print("Tipo de estucturas.")

print("Estructura if")

print("Se ejecuta el bolque si se cumple la condicion.")

print("Ejemplos")

a = 2
b = 2

print("Si " + str(a) + " = " + str(b))
if a == b:
    print("Se ejecuta el bloque")

print("Estructura if-else")

print("Se ejecuta el bloque if si se cumple la condicion, si no se cumple se ejecuta el else.")

print("Ejemplos")

print("Si " + str(a) + " < (menor que) " + str(b))
if a < b :
    print("Se ejecuta el bloque if")

else :
    print("Se ejecuta el bloque else")

print("Estructura if else-if else")

print("Se ejecuta el bloque if si se cumple la condicion.")
print("Si no se cumple se ejecuta la siguiente condicion else if(asi sucesivamente).")
print("Si no se cumple niguna condicion se ejecuta el else.")

print("Ejemplos")

print("if " + str(a) + " < (menor que) " + str(b) + "\n" + 
                    "else if " + str(a) + " = (igula a) " + str(b))
if a < b :
    print("Se ejecuta el bloque if")

elif a == b :
    print("Se ejecuta el bloque else if")

else :
    print("Se ejecuta el bloque else")

print("Estructura de bucles")

print("Bucle for")
        
print("Se ejecuta un bloque de codigo mientras la condicion sea verdadera.")
print("Esto se controla mediante un iterador que se ira aumentando por cada ejecucion del bucle.")
        
print("Ejemplos")

c=3

for i in range (0, c) :
    print(i)

print("Bucle while")

print("Se ejecuta un bloque de codigo mientras la condicion sea verdadera.")
print("El bucle se ejecutara hasta que se modifique la condicion.")
        
print("Ejemplos")

print("Condicion: " + str(a) + " menor que " + str(c))

while a != c :
    print("La condicion es verdera")
    a += 1
    print(a)

print("DIFICULTAD EXTRA (opcional):")
print("Crea un programa que imprima por consola todos los n├║meros comprendidos")
print("entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni m├║ltiplos de 3.")

for i in range (10,55) : 
    if i%2 != 0:
        None
    elif (i == 16) or (i%3 == 0) :
        None
    else: 
        print (i)
