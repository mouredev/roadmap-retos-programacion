cadena1 = "Ricardo"
cadena2 = "Segundo"

print(cadena1 + " " + cadena2)
print(cadena1[0:3] + " " + cadena2[0:3])
print(len(cadena1))
print(cadena1 * 5)
print(cadena1.upper().count("R"))
print(cadena1.split("a"))
if "R" in cadena1:
    print("La letra R está en la cadena1")
else:   
    print("La letra R no está en la cadena1")
cadena3 = cadena1.replace("R", "r")
print(cadena3)
print(cadena1.find("a"))
print(cadena1.index("a"))
print(cadena1[::-1])
print(set(cadena1.lower()))
cadena1 = "Murcielaga"
print(set(cadena1))

#Palindromo
palabra = "reconocer"
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo")

#Anagrama
palabra1 = "amor"
palabra2 = "roma"
if sorted(palabra1) == sorted(palabra2):
    print("Las palabras son anagramas")

#Isogramas
palabra = "murcielago"
if len(palabra) == len(set(palabra)):
    print("La palabra es un isograma, es decir, no tiene letras repetidas")
else:
    print("La palabra no es un isograma, tiene letras repetidas")   