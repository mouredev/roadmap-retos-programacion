#04 CADENAS DE CARACTERES
'''
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
  conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
'''

if __name__ == '__main__':

    '''
    Operaciones
    '''

    s1 = "Hola"
    s2 = "Python"

    # Concatenación
    print(s1 + ", " + s2 + "!")

    # Repetición
    print(s1 * 3)

    # Indexación
    print(s1[0])

    # Longitud
    print(len(s2))

    # Slicing
    print(s2[2:])

    # Search
    print('a' in s1)
    print('i' in s1)

    # Reemplazo
    print(s1.replace("o", "a"))

    # Division
    print(s2.split("t"))

    # Mayúscula y minúsculas
    print(s1.upper())
    print(s1.lower())
    print("rigo acosta".title())
    print("rigo acosta".capitalize())

    # Eliminación al principio y al final espacio
    # en blanco
    print(" rigo acosta ".strip())

    # Búsqueda al principio y al final
    print(s1.startswith('H'))
    print(s1.endswith('o'))

    s3 = "Rigo Acosta @rigo93acosta"
    # Search position
    print("Rigo Acosta @rigo93acosta".find("Acosta"))
    print("Rigo Acosta @rigo93acosta".find("r"))

    # Search ocurrencia
    print(s3.lower().count("r"))

    # Formateo
    print("Saludo: {}, lenguaje: {}!".format(s1, s2))

    # Interpolación
    print(f"Saludo: {s1}, lenguaje: {s2}!")

    # Transformación en lista
    print(list(s3))

    # Transformación en str
    l1 = [s1, ', ', s2, '!']
    print("".join(l1))
    
    # Transformaciones numéricas
    s4 = "123456"
    s4 = int(s4)
    print(s4)

    s5 = "123456.123"
    s5 = float(s5)
    print(s5)

    # Comprobaciones varias
    s4 = "123456"
    print(s1.isalnum())
    print(s1.isalpha())
    print(s4.isalpha())
    print(s4.isnumeric())

    '''
    EXTRA
    '''

    def isogram(word_test: str) -> bool:
            
        word_dict = {}
        for word in word_test:
            word_dict[word] = word_dict.get(word, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    
    def check_words(word_1: str, word_2: str):

        # Palíndromos
        print(f"¿{word_1} es un palíndromo?: {word_1 == word_1[::-1]}")
        print(f"¿{word_2} es un palíndromo?: {word_2 == word_2[::-1]}")

        # Anagramas entre dos palabras
        print(f"¿{word_1} es anagrama de {word_2}?: {sorted(word_1) == sorted(word_2)}")

        # Isogramas
        print(f"¿{word_1} es un isograma?: {isogram(word_1)}")
        print(f"¿{word_2} es un isograma?: {isogram(word_2)}")


    check_words("pythonpython", "radar")
    check_words("roma", "amor")