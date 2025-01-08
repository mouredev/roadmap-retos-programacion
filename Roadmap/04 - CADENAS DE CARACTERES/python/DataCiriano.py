"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""
 
#Operaciones con cadenas de texto.

#Definición de una cadena
 
mi_cadena = "Hola mundo, estoy haciendo el roadmap de "
mi_cadena2 = "Python"
mi_cadena3 =  "2024"


#Desempaquetado cadena

a,b,c,d,e,f = mi_cadena2
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Concatenación de cadenas

cadena_unida = mi_cadena + mi_cadena2
print(cadena_unida)

#Formateo de una cadena (deferentes formas)
nombre = "Pepito"
saludo = f"Hola, bienvenido a este roadmap {nombre}"
print(saludo)

saludo2 = "Hola, bienvenido a este roadmap {}".format(nombre)
print(saludo2)

año = 2020
lenguaje_programacion = "Python"

mensaje = "Comencé a aprender %s en el año %i" %(lenguaje_programacion, año)
print(mensaje)

#Acceso a cararacteres de una cadena

print(mi_cadena2[0]) #Devueve el primer caracter de la cadena
print(mi_cadena2[-1]) #Devuelve el último caracter de la cadena

#Slicing de una cadena
 
print(mi_cadena[12:]) #Devuele desde el caracter 3n al posiión 12 hasta el final de la cadena
print(mi_cadena[:-3]) #Devuelve desde el principio de la cadena hasta el 4 caracter empezando por el final
print(mi_cadena[18:26]) #Devuelve solo la palabra 'haciendo'
print(mi_cadena[::3]) #Devuelve un caracter de cada 3

#Invertir una cadena

print(mi_cadena[::-1])

#Métodos de las cadenas de carateres

print(mi_cadena.upper()) #Convertir a mayúsculas
print(mi_cadena.lower()) #Convertir a minúculas
print(mi_cadena.capitalize()) #Poner la primera letra de la cadena en mayúsculas
print(mi_cadena.title()) #Poner la primera letra de cada palabra en mayúculas 
print(mi_cadena2.swapcase()) #Invertir mayúsculas y minúculas de una cadena

print(mi_cadena.endswith("python")) #Devuelve True si la cadena acaba por 'python' si no devuelve False
print(mi_cadena.startswith("Hola ")) #Devuelve True si la cadena empeza por 'Hola ' sei no devuelve False

print(mi_cadena.count("o")) #Devuelve el número total de 'o' en la cadena

print(mi_cadena.index("e")) #Devuelve el índice de la priemra 'e' de la cadena
print(mi_cadena.rindex("e")) #Devuelve el índice máxio del caracter buscado

print(mi_cadena.find("estoy")) #Devuelve el índice de los caracteres buscados en la cadena
print(mi_cadena.rfind("e")) #Devuelve el índice de la última ocurrencia del caracter buscado

print(mi_cadena.replace("Hola", "Buenos días")) #Reemplazo de caracteres de una cadena
 
print(mi_cadena.isalnum()) #Devuelve True si todos lso caracters de la cadena son alfanuméricos, si no False
print(mi_cadena.isalpha()) #Devuelve True si todos las caracteres de la cadena son (a-z and A-Z), si no False (el espacio no cuenta)
print(mi_cadena3.isdecimal()) #Devuelve True si todos las caracteres de la cadena son (0-9), si no False
print(mi_cadena3.isdigit()) #Devuelve True si todos las caracteres de la cadena son (0-9), si no False
print(mi_cadena3.isnumeric()) #Igua que .isdigit() pero se aceptan más caracters numérico (por ejemplo ½)
print(mi_cadena.isidentifier()) #Devuelve True si la cadena es un nombre valido para una varaible, si no False
print(mi_cadena.islower()) #Devuelve True si todos los caracteres están en minúsculas, si no False
print(mi_cadena.isupper()) #Devuelve True si todos los caracteres están en mayúsculas, si no False 

#Convertir una lista en una cadena de caracteres separad por espacios

lista_lenguajes = ["Python", "JavaScript", "Java", "HTML", "R"]
lenguajes = " ".join(lista_lenguajes)
print(lenguajes)

#Separa una cadena de caracteres en una lista por un delimitador

lista_palabras = mi_cadena.split(" ")
print(lista_palabras)


#---EXTRA---

def analizar_palabras(word1: str, word2: str): 
    
    #Palíndromo
    print(f"¿La palabra {word1} es palíndromo? {word1 == word1[::-1]}")
    print(f"¿La palabra {word2} es palíndromo? {word2 == word2[::-1]}")
    
    #Anagrama
    print(f"¿La palabra {word1} es anagrama de {word2}? {sorted(word1) == sorted(word2)}")
    
    #Isograma
    print(f"¿Es la palabra {word1} un isograma? {len(word1) == len(set(word1))}")
    print(f"¿Es la palabra {word2} un isograma? {len(word2) == len(set(word2))}")
    
    
analizar_palabras("reconocer", "perro")
analizar_palabras("amor", "roma")
analizar_palabras("radar", "murcielago")


