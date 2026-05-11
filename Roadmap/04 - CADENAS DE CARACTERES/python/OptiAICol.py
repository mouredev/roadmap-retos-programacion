# Operaciones con cadenas de caracteres
print("Operaciones con cadenas de caracteres")

texto = "Hola, Python!"
print(texto)
# Acceso a caracteres especificos:
print("\nAcceso a caracteres especificos:")
print(texto[0])  # Primer Caracter
print(texto[-1])  # Ultimo Caracter
print(texto[0:4])  # Subcadena "Hola"
print(texto[7:13])  # Subcadena "Python"
print(texto[3:9])  # Subcadena "a, Pyt"

#Longitud
print("\nLongitud:")
print(len(texto))  # Longitud de la cadena

# Concatenacion:
print("\nConcatenacion:")
saludo = "Hola"
nombre = "Mundo"
print(saludo + ", " + nombre + "!") # Concatenacion de cadenas

# Repeticion:
print("\nRepeticion:")
repeticion = "Hola! " * 3
print(repeticion)  # Repeticion de la cadena

# Recorrido:
print("\nRecorrido:")
Abecedario = "ABECEDARIO"
for caracter in Abecedario:
    print(caracter)  # Imprime cada caracter en una nueva linea

Abecedario = "ABECEDARIO"
for caracter in Abecedario:
    print(caracter, end=" ")  # Imprime cada caracter seguido de un espacio

# Mayúsculas y minúsculas:
print("\n\nMayúsculas y minúsculas:")
texto1 = "Hola, mi nombre es Carlos!"
print(texto1)
print(texto1.upper()) # Convierte a mayúsculas
print(texto1.lower()) # Convierte a minúsculas
print(texto1.capitalize()) # Convierte el primer caracter a mayúscula y el resto a minúsculas
print(texto1.title()) # Convierte el primer caracter de cada palabra a mayúscula y el resto a minúsculas

# Remplazo:
print("\nRemplazo:")
print(texto1.replace("Carlos", "Caliche")) # Reemplaza "Carlos" por "Caliche"

# División y unión:
print("\nDivisión y unión:")
lista = texto1.split(",") # Divide la cadena en una lista usando la coma como separador
print(lista) 
print(",".join(lista)) # Une los elementos de la lista en una cadena usando la coma como separador

# Verificación:
print("\nVerificación:")
texto2 = "Buenos días"
print(texto2)
print("Python".isalpha()) # Verifica si todos los caracteres son letras
print("12345".isdigit()) # Verifica si todos los caracteres son dígitos
print("  ".isspace()) # Verifica si todos los caracteres son espacios en blanco
print(texto2.startswith("Hola")) # Verifica si la cadena comienza con "Hola"
print(texto1.startswith("Hola")) 
print(texto2.endswith("!")) # Verifica si la cadena termina con "!"
print(texto1.endswith("!"))
print("Python" in texto2) # Verifica si "Python" está presente en la cadena texto2
print("Buenos" in texto2) # Verifica si "Buenos" está presente en la cadena texto2


# Interpolación
print("\nInterpolación:")
nombre = "Carlos"
edad = 30
ciudad = "Madrid"
print(f"Hola, mi nombre es {nombre} y tengo {edad} años. Vivo en {ciudad}.") # Interpolación usando f-strings

# Otros métodos útiles
print("\nOtros métodos útiles:")
print("  hola  ".strip()) # Elimina los espacios en blanco al inicio y al final de la cadena
print(texto.count("o")) # Cuenta cuántas veces aparece la letra "o" en la cadena texto 
print(texto1.find("Carlos")) #Busca la posición de la primera aparición de "Carlos" en texto1
print(texto1.center(50, "*")) # Centra la cadena texto1 en un campo de ancho 50, rellenando con asteriscos

# Dificultad Extra
print("\nDificultad Extra:")

def analizar_palabras(palabra1, palabra2):
    p1 = palabra1.lower().strip()
    p2 = palabra2.lower().strip()

    print(f"\n'{p1}' es palíndromo: {p1 == p1[::-1]}")
    print(f"'{p2}' es palíndromo: {p2 == p2[::-1]}")

    es_anagrama = sorted(p1) == sorted(p2)
    print(f"\n'{p1}' y '{p2}' son anagramas: {es_anagrama}")

    es_isograma1 = len(p1) == len(set(p1))
    es_isograma2 = len(p2) == len(set(p2))
    print(f"\n'{p1}' es isograma: {es_isograma1}")
    print(f"'{p2}' es isograma: {es_isograma2}")

analizar_palabras("amor", "roma")
analizar_palabras("reconocer", "python")