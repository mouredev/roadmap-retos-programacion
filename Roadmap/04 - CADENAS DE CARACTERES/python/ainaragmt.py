s1 = "Hello "
s2 = "Python"

# Concatenación
print("\nConcatenación")
print(s1 + " " + s2)
      
# Repetición
print("\nRepetición")
print(s1*3)

# Indexación
print("\nIndexación")
print(s1[0])

# Longitud
print("\nLongitud")
print(len(s1))

# Slicing
print("\nSlicing")
print(s2[2:5]) # del 2 al 5 excluyendo el 5
print(s2[2:]) # del 2 al final

# Búsqueda
print("\nBúsqueda")
print("a" in s1)
print("e" in s1)

# Reemplazo
print("\nReemplazo")
print(s1.replace("e", "a"))

# División
print("\nDivisión")
print(s1.split('l')) # corta por las dos 'l'

# Conversión a mayúsculas
print("\nConversión a mayúsculas y minúsculas")
print(s1.upper())
print(s1.lower())

nombre = "Ainara gmt"
print(nombre.title())
print(nombre.capitalize())

# Eliminación de espacios al principio y al final
print("\nEliminación de espacios al principio y al final")
print(s1.strip() + s2)

# Búsqueda al principio y al final
print("\nBúsqueda al principio y al final")
print(s1.startswith("He"))
print(s1.endswith("He"))

# Búsqueda de posición
print("\nBúsqueda de posición")
print(s1.find("o"))

# Búsqueda de ocurrencias
print("\nBúsqueda de ocurrencias")
print(s1.count("l"))

# Interpolación
print("\nInterpolación")
print(f"Saludo {s1}, lenguaje {s2}")

# Formateo
print("\nFormateo")
print("Saludo {}, lenguaje {}".format(s1,s2))

# Transformación en lista de caracteres
print("\nTransformación en lista de caracteres")
print(list(s1))

# Transformación en lista en cadena
print("\nTransformación en lista en cadena")
l1 = [s1, ", ", s2]
print("".join(l1))
print("-".join(l1))

# Transformaciones numéricas
print("\nTransformaciones numéricas")
s3 = 1234
print(int(s3))

# Comprobaciones varias
print("\nComprobaciones varias")
# Devuelve False por el espacio "Hello "
print(s1.isalnum()) # letras y números
print(s1.isalpha()) # letras
print(s1.isnumeric()) # números

print(s2.isalnum()) # letras y números
print(s2.isalpha()) # letras
print(s2.isnumeric()) # números

'''
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''
print("\nEjercicio de dificultad extra\n")

def programa():
    def palindromo(s1):
        s1 = s1.lower().strip().replace(" ", "")
        for i in range (len(s1)):
            if s1[i] != s1[(len(s1) - 1 - i)]:
                return "No"
        return "Sí"
    
    # Corrección palíndromos
    # Podríamos haber invertido la palabra con s1[::-1]
    # print(f"¿{s1} es un palíndromo?: {s1 == s1[::-1]}")
    
    def anagrama(s1, s2):
        def orden (s1):
            s1 = s1.lower().strip().replace(" ", "")
            lista_ordenada1 = sorted(s1)
            palabra_ordenada1 = "".join(lista_ordenada1)
            return palabra_ordenada1
        s1 = orden (s1)
        s2 = orden (s2)
        if len(s1) != len(s2):
            return "No"
        for i in range (len(s1)):
            if s1[i] != s2[i]:
                return "No"
        return "Sí"
    
    # Corrección anagrama
    # print(f"¿{s1} es anagrama de {s2}?: {sorted(s1) == sorted(s2)}")

    def isograma(s1):
        s1 = s1.lower().strip().replace(" ", "")
        for i in range (len(s1)):
            for j in range (len(s1)):
                if s1[i] == s1[j] and i != j:
                    return "No"
        return "Sí"
    
    # Corrección isograma
    # Comprueba si la longitud de la palabra es igual a
    # la longitud del conjunto de sus letras
    # print(f"¿{s1} es un isograma?: {len(s1) == len(set(s1))}")

    palabra1 = input("Escribe la primera palabra: ")
    palabra2 = input("Escribe la segunda palabra: ")

    pal1 = palindromo(palabra1)
    print("\n¿Es la primera palabra un palíndromo? " + pal1)
    pal2 = palindromo(palabra2)
    print("\n¿Es la segunda palabra un palíndromo? " + pal2)

    ana = anagrama(palabra1, palabra2)
    print("\n¿Son anagramas? " + ana)

    iso1 = isograma(palabra1)
    print("\n¿Es la primera palabra un isograma? " + iso1)
    iso2 = isograma(palabra2)
    print("\n¿Es la segunda palabra un isograma? " + iso2)
    
programa()