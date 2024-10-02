"""
Operaciones
"""
s1 = "Hola"
s2 = "mundo"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:]) # Hasta el fin
print(s2[:2]) # Desde el principio
print(s2[0:2]) # Desde el principio

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("n"))

# Mayúsculas y minúsculas y primera letra en mayúsculas
print(s1.upper())
print(s1.lower())
print("atila eluno".title())
print("atila eluno".capitalize())

# Eliminación de espacios al principio y al final
print(" atila eluno ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

# Búsqueda de posición
s3 = "Atila Eluno @atieluno"
print(s3.find("ati"))
print(s3.find("Elu"))
print(s3.find("E"))
print(s3.lower().find("a"))

# Búsqueda de ocurrencias
print(s3.lower().count("a"))

# Formateo
print("Saludo: {}, lenguaje: {}".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}")

# Transformación en lista de caracteres
print(list(s3))

# Tranformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Tranformaciónes númericas
s4 = "123456"
s4 = int(s4)
print(s4)

s4 = "123456.123"
s4 = float(s4)
print(s4)

# Comprobaciónes varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
Extra
"""
print("-- Extra --\n")
def imprimir_resultado(titulo: str, function, *args):
    print("")
    print(titulo)
    function(*args)

def palindromo(*words: str):
    for word in words:
        palindromo = word == word[::1]
        print(f"¿{word} es palindromo?: {palindromo}")

def anagrama(w1, w2):
    anagrama = sorted(w1) == sorted(w2)
    print(f"¿{w1} y {w2} son anagramas?: {anagrama}")

def isograma(*words: str):
    for word in words:
        word_dict = dict()
    
        for w in word:
            word_dict[w] = word_dict.get(w, 0) + 1

        isogram = True
        for w_count in word_dict.values():
            if w_count > 1:
                isogram = False
                break
        print(f"¿{word} es un isograma?: {isogram}")



def check(word1: str, word2: str):
    imprimir_resultado("Verificando Palíndromo:", palindromo, word1, word2)
    imprimir_resultado("Verificando Anagrama:", anagrama, word1, word2)
    imprimir_resultado("Verificando Isograma:", isograma, word1, word2)
    

if __name__ == "__main__":
    word1 = input("Ingresa la palabra a verificar: ")
    word2 = input("Ingresa la palabra a verificar: ")
    
    check(word1, word2)
    
