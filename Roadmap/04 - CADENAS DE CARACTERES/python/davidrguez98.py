""" # #04 CADENAS DE CARACTERES
> #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio


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

#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**. """

#Concatenación

c1 = "hola"
c2 = "mundo"
c3 = "David Rodríguez @davidrguez98"

print(c1 + " " + c2)

#Repetición

print(c1 * 3)

#Indexación

print(c1[1])

#Longitud

print(len(c2))

#Slicing (porción)

print(c2[2:4])
print(c2[2:])
print(c2[0:2])
print(c2[:2])

#Búsqueda

print("a" in c1)

#Reemplazo

print(c1.replace("o", "a"))

#División

print(c1.split("l"))

#Conversión a mayúsculas, minúsculas y primera en mayúsculas

print(c1.upper())
print(c1.lower())
print("David Rodríguez".title()) 
print("David Rodríguez".capitalize()) #Solo la primera en mayúscula

#Eliminación de espacios al principio y al final

print(" David Rodríguez ".strip())

#Búsqueda al principio y al final

print(c1.startswith("ho"))
print(c1.endswith("la"))

#Búsqueda de posición

print(c3.find("david"))
print(c3.lower().find("david"))

#Búsqueda de ocurrencias

print(c3.lower().count("d"))

#Formateo

print("Saludo: {}, lenguaje: {}!".format(c1, c2))

#Interpolación

print(f"Saludo: {c1}, lenguaje: {c2}!")

# Transformación en lista de caracteres

print(list(c3))

#Transformación de lista en cadena

c4 = [c1, ", ", c2, "!"]
print("".join(c4))

c4 = [c1, ", ", c2, "!"]
print("-".join(c4))

#Transformaciones numéricas

c5 = "123456"
c5 = int(c5)
print(c5)

c6 = "123456.2344"
c6 = float(c6)
print(c6) 

#Comprobaciones varias

print(c1.isalnum())
print(c1.isalpha())
print(c1.isnumeric())


#DIFICULTAD EXTRA

""" 
/*

 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */ """

from collections import Counter

def comparador():

    def palindropo():
        invertir = word_2[::-1].lower()

        if word_1.lower() == invertir:
            print("\nEs un palíndrono")
        else:
            print("\nNo es un palíndrono")

    def anagrama():
        counter1 = Counter(word1.lower())
        counter2 = Counter(word2.lower())

        if counter1 == counter2:
            print(f"\nLas palabra {word1} y {word2} son anagramas")
        else:
            print(f"\nLas palabra {word1} y {word2} no son anagramas")

    while True:

        print("")
        print("1. Comprobar si es un palíndromo.")
        print("2. Comprobar si es un anagrama")
        print("3. Comprobar si es un isograma")
        print("4. Salir de la comprobación.")
        option = input("\nElige una de las anteriores opciones: ")

        match option:

            case("1"): 
                word_1 = input("Palabra 1: ")
                word_2 = input("Palabra 2: ")
                palindropo()
            
            case("2"):
                
                word1 = input("Primera palabra: ")
                word2 = input("Segunda palabra: ")
                anagrama()

            case("3"):
                def isograma(word_3):
                    
                    word_3 = word_3.lower()
                    letras = set(word_3)
                    return len(letras) == len(word_3)

                word_3 = input("Escribe la palabra: ")
                if isograma(word_3):
                    print(f"\n{word_3} es un isograma")
                else:
                    print(f"\n{word_3} no es un isograma")

            case("4"):
                break

comparador()