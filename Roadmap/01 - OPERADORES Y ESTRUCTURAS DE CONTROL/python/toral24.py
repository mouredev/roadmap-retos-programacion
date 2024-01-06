#Operadores en python

#Concatenación de cadenas

saludo = "Hola"
lenguaje = "Python"

print("¡"+ saludo + ", " + lenguaje + "!")

#Booleanos

x = True
y = False

print(x or y)
print(x and y)
if not y:
    print("y es falsa")

#Artiméticos
try:

    num1 = int(input("introduce el primer número entero: "))
    num2 = int(input("introduce el segundo número entero: "))

    print("la suma es " + str(num1 + num2))
    print("la resta es: " + str(num1 - num2))
    print("la multiplicación es: " + str(num1 * num2))
    print("la división (con decimales) es: " + str(num1 / num2))
    print("la división (sin decimales) es: " + str(num1 // num2))
    print("la potencia es : " + str(num1 ** num2))
    print("el modulo es : " + str(num1 % num2))

except:
    print("Algo ha salido mal")

#Comparación

letra = "a"
abecedario = []
while letra <= "z":
    abecedario.append(letra)
    letra = chr(ord(letra) + 1)

print("Estas son las primeras 10 letras del abecedario:")
for i in range(10):
    print(abecedario[i], end=" ")

try:
    num = int(input("introduce un número"))
    if num > 0:
        print("has introducido un número positivo")
        if num >= 100:
            print("tu número tiene más de tres cifras")
        elif num < 10:
            print("tu número no tiene dos cifras")
    elif num == 0:
        print("has introducido un cero")
    else:
        print("has introducido un número negitvo")
except:
    print("no has introducido un número")
try:

    numsuerte = 7
    numintroducido = int(input("adivina el número de la suerte"))

    while numsuerte != numintroducido:
        print("vaya no has acertado el número de la suerte prueba otra vez")
except:
    print("no has introducido un número")

#pertenencia e identidad

    vocales = ["a","e","i","o","u"]
    letrausu = str(input("introduce una letra minúscula"))
    if letrausu in abecedario:
        if letrausu not in vocales:
            print("tu letra es una cosonante")
            if letrausu is not "z":
                print("tu letra no es la última del abecedario")
        elif letrausu is "a":
            print("has introducido la primera letra del abecedario")
        
    else:
        print("has introducido una letra mínuscula")

#Operaciones a nivle de bit

x = 5
y = 20

#or 
print(x|y)
#or exclusivo
print(x^y)
#and
print(x&y)
#deplazo de bits
print(x>>2) #dos bits a la derecha
print(y<<5) #cinco bits a la izquierda
#not
print(~x)

#Ejercicio extra

for i in range(10,56):
    if i%2 == 0:
        if i%3 != 0:
            if i != 16:
                print(i, end=" ")
                