# 04 - CADENAS DE CARACTERES

mi_cadena = "Hola mi nombre es Javier, estoy aprendiendo Python con retos de programación"

print(mi_cadena[3])
print(mi_cadena[0:4])
print("Longitud de la cadena: " + str(len(mi_cadena)))
print(mi_cadena * 3)

for caracter in mi_cadena:
    print(caracter)

print(mi_cadena.upper())
print(mi_cadena.lower())
print(mi_cadena.capitalize())

print(mi_cadena.replace("javier", "Javier"))

mi_lista = mi_cadena.split(" ")
print(mi_lista)
print(type(mi_lista))
texto=""
for i in mi_lista:
     texto = texto + i + " "
print(texto)

lenguaje = "Python"
print(f"Hola {lenguaje}!")

if lenguaje == "Python":
     print("El lenguaje es Python")

mi_cadena = "AAAAAaaaaa"
if mi_cadena.isalpha():
     print("Cadena contiene sólo caracteres")

mi_cadena = "12345"
if mi_cadena.isnumeric():
     print("Cadena contiene sólo números")
    

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""
primera_palabra = ""
segunda_palabra = ""

while primera_palabra == segunda_palabra:
    print("Introduce dos palabras, tienen que ser distintas")
    primera_palabra = input("Primera palabra: ")
    segunda_palabra = input("Segunda palabra: ")


if primera_palabra == segunda_palabra[::-1]:
     print("Palindromos")

if ''.join(sorted(primera_palabra)) == ''.join(sorted(segunda_palabra)):
     print("Anagramas")

isograma = True
for letra in primera_palabra:
     if primera_palabra.count(letra) > 1:
          isograma = False

if isograma: print("La primera palabra es un isograma")