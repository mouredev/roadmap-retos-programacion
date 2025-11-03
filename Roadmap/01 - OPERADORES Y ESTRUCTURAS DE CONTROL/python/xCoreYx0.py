#Estos son ejemplos con los tipos de operadores de python

#Usaré estas variables generales para los ejemplos

x = 20
y = 15
primera_ciudad = "Lima"
segunda_ciudad = "Arequipa"
pais = "Perú"

#Operadores Aritméticos:
suma = x + y 
resta = x - y
multiplicacion = x * y

division_entera = x // y
porcentaje = x % y
potenciacion = x ** y

#Operadores de comparación:
igual = primera_ciudad == segunda_ciudad
desigual = primera_ciudad != segunda_ciudad
mayor = x > y
menor = y < x
mayor_igual = x >= y
menor_igual = y <= x

#Operadores Lógicos:
and_logico = primera_ciudad and segunda_ciudad
or_logico = x or y
not_logico = not x

#Operadores de asignación:
z = 12
z += 5
z -= 6
z *= 10
z /= 2
z //= 3
z %= 2
z **= 3

#Operadores de identidad
is_igual = primera_ciudad is pais
is_not_igual = x is not y

#Operadores a nivel de bits
and_bits = x & y
or_bits = x | y
xor_bits = x ^ y
not_bits = ~x
desplaza_izquierda = x << 2
desplaza_derecha = x >> 2

#Ahora pondré un ejemplo de cada tipo de estructura de control de Python con los operadores aprendidos

#Estrucutra condicional if-elif-else
a = 22
if a < 12:
    print("a está entre el 1 y el 11")
elif a == 12:
    print("a es igual 12")
else:
    print("a es un número mayor a 12")

#Estructura de repetición (bucles) while y for

#bucle while
contador = 1   
while contador <= 5:
    print("EL contador subió a: ", contador)
    contador += 1

#bucle for
lista = [20, 2, 13]
for numero in lista:
    print("El número actual en la lista es: ", numero)
for numero in range(1, 3):
    print("El número actual es: ", numero)

#Estructura de control de flujo break, continue y pass

#break
for numero in range(1, 10):
    if numero == 3:
        print("Se encontró el número 3, salimos del bucle")
        break
    print("El número es: ", numero)

#continue
for numero in range(1,10):
    if numero == 5:
        print("Se encontró el cinco, seguimos el bucle")
        continue
    print("Este número es: ", numero)

#pass
for numero in range(1, 6):
    if numero == 3:
        print("No")
        pass
    print("El número ", numero)


#Ahora haré un programa que imprima por consola todos los números comprendidos entre 10 y 55(incluidos),pares, y que no sea 16 ni múltiplos de 3
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)