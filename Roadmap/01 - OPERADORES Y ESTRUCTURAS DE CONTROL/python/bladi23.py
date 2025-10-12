"""
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
 
 """
 
 #OPERADORES ARITMÉTICOS
 
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# OPERADORES DE ASIGNACIÓN COMPUESTA
x = 10
x += 5
print("x += 5 →", x)
x *= 2
print("x *= 2 →", x)

# OPERADORES DE IDENTIDAD
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print("lista1 is lista2:", lista1 is lista2)
print("lista1 is lista3:", lista1 is lista3)
print("lista1 is not lista3:", lista1 is not lista3)

# OPERADORES DE PERTENENCIA
print("2 in lista1:", 2 in lista1)
print("4 not in lista1:", 4 not in lista1)

#EJEMPLOS DE OPERADORES LOGICOS 

edad_usuario=int(input("Introduce tu edad: "))
entrada=input("Has pagado la entrada? (si/no): ").lower()
if edad_usuario>=18 and entrada =="si":
    print("Bienvenido a la fiesta ")
else :
    print("Lo siento, no puedes entrar a la fiesta")

edad_cine=int(input("Introduce tu edad: "))
entrada=input("Tiene entrada VIP? (si/no): ").lower()
if edad_cine>=16 or entrada=="si":
    print("Puedes entrar al cine")
else:
    print("Lo siento, no puedes entrar al cine")
    
#OPERADORES DE COMPARACION
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#ESTRUCTURAS DE CONTROL CONDICIONALES
edad=20
if edad>=18:
    print("Eres mayor de edad")
elif edad==17:
    print("Casi eres mayor de edad ")
else:
    print("Eres menor de edad")
    
print("Bucle while:")
i = 0
while i < 5:
    print(i)
    i += 1

print("Bucle for:")
for i in range(5):
    print(i)

# CONTROL DE FLUJO
print("Break:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("Continue:")
for i in range(10):
    if i == 5:
        continue
    print(i)

print("Pass:")
for i in range(3):
    if i == 1:
        pass
    print(i)
# MANEJO DE EXCEPCIONES
try:
    numero = int(input("Introduce un número para dividir: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Por favor, ingresa un número válido.")

# DIFICULTAD EXTRA: imprimir números del 10 al 55, pares, no 16 ni múltiplos de 3
print("Números del 10 al 55 que son pares, no son 16 y no son múltiplos de 3:")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)