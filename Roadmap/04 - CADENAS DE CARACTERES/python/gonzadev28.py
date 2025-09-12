""" EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación..."""

cadena_texto = "Aprendiendo Python con Mouredev"

print(cadena_texto[12]) #Acceso a un caracterter en especifico en la posicion[12] = "P"
print(cadena_texto.find("Mouredev")) #Acceso a posicion de subcadena "Mouredev" = [23]
print(len(cadena_texto)) #Acceso a la longitud de cadena de texto (31)

cadena_texto2 = "en Github y Youtube"

print(cadena_texto + ", " + cadena_texto2) #Concatenacion de 2 cadenas de texto
print(cadena_texto * 5) #Repeticion de cadena de texto

for i in cadena_texto: #Reccorido por caracter de la cadena de texto
    print(i)

print(cadena_texto.upper()) #Convierte la cadena de texto a mayusculas
print(cadena_texto.lower()) #Convierte la cadena de texto a minusculas 
print(cadena_texto.replace("Python", "Java")) #Reemplaza cadena de texto "Python" a "Java"
print(cadena_texto.split(" ")) #Separa cadena de texto donde haya " " (espacio)

#Union
texto_separado = ["Esto", "es", "texto", "separado"]
print(" ".join(texto_separado)) #Une diferentes cadenas de texto en uno solo

#Interpolacion 
print(f"Esta es la primera cadena de texto: {cadena_texto} y esta la segunda: {cadena_texto2}")

#Verificacion
cadena_texto3 = "Python"
print("h" in(cadena_texto3)) #Verifica si caracter "h" se encuentra en cadena de texto
print(cadena_texto3.isalpha()) #Verfica si cadena de texto es alfabetica
print(cadena_texto3.isalnum()) #Verfifica si cadena de texto es alfanumerica
print(cadena_texto3.isdigit()) #Verifica si cadena de texto es numerica 
print(cadena_texto3.istitle()) #Verifica si cadena de texto tiene formato de titulo 

""" DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas """

#Palindromo

def palindromo(palabra1):
    if(palabra1 == palabra1[::-1]):
        print(f"La palabra {palabra1} es palindromo")
    else:
        print(f"La palabra {palabra1} no es palindromo")

palindromo("radar")
palindromo("perro")

#Anagrama

def anagrama(palabra1, palabra2):
    if(sorted(palabra1) == sorted(palabra2)):
        print(f"La palabra {palabra1} es anagrama de {palabra2}")
    else:
        print("No son anagramas")

anagrama("sentido", "destino")
anagrama("programador", "estudiante")

#Isograma

def isograma(palabra1):
    if(len(palabra1) == len(set(palabra1))):
        print(f"La palabra {palabra1} es un isograma")
    else:
        print(f"La palabra {palabra1} no es isograma")

isograma("murcielago")
isograma("isograma")



