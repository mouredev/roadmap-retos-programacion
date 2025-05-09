#Cadena de caracteres

cadena1 = "Hola"
cadena2 = "Amigo"
cadena3 = "Adios\namigo"
cadena4 = "Como estas hoy?"

print(f"esta es la cadena1:", cadena1)
print(f"esta es la cadena multilinea:", cadena3)
print(f"caracter del indice 1:", cadena1[1]) #Acceso a un caracter mediante su indice
print(f"indice del caracter o:", cadena1.index("o")) #Acceso al indice de un caracter
print(f"indice del caracter o:", cadena1.find("o")) #Acceso al indice de un caracter
print(f"rebanado de la cadena1:", cadena1[2:5]) #rebanado
print(cadena1 * 3)           #repeticion
print("longitud de la cadena1:", len(cadena1)) #longitud
print(f"cuenta ocurrencias de a:", cadena1.count("a"))
print(f"verifica el inicio:", cadena1.startswith("Ho"))
print(f"verifica el final:", cadena1.endswith("la"))
print(f"cadena1 en mayusculas:", cadena1.upper()) #convierte todos los caracteres en mayusculas
print(f"cadena1 en minusculas:", cadena1.lower()) #convierte todos los caracteres en minusculas
print(f"union de caracteres de la cadena1 y la cadena2:", cadena1 + " " + cadena2)
print("Ho" in cadena1)          #verificacion o buscar
print(f"reemplazar cadena de caracteres: ", cadena1.replace("Hola", "Hello")) #reemplazar cadena de caracteres
cadena4.strip()
print(cadena4)

#extra

def check():
	#palindromo
	palabra1 = "ana"
	palabra2 = "hola"

	print(f"{palabra1} es un palindromo?, {palabra1 == palabra1[::-1]}")
	print(f"{palabra2} es un palindromo?, {palabra2 == palabra2[::-1]}")

	#anagrama
	print(f"{palabra1} y {palabra2} son anagramas?", sorted(palabra1) == sorted(palabra2))

check()			