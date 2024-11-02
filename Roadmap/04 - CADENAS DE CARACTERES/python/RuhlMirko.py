print("Acceso a caracteres especificos:")
cadena_ejemplo = "Hola mundo "
print(cadena_ejemplo[0])
print(cadena_ejemplo[5])

print("\nSubcadenas")
print(cadena_ejemplo[2:5])
print(cadena_ejemplo[:5])
print(cadena_ejemplo[4:])

print("\nLongitud")
longitud_cadena = str(len(cadena_ejemplo))
print("Longitud de la cadena: " + longitud_cadena)
print("Cantidad de letras 'o' encontradas: " + str(cadena_ejemplo.count('o')))

print("\nConcatenacion")
cadena_nueva = "y hola a todos"
cadena_ejemplo = cadena_ejemplo + cadena_nueva
print(cadena_ejemplo)

print("\nRepeticion")
print(cadena_ejemplo * 3)

print("\nRecorrido")
for char in cadena_ejemplo:
    print(char)

print("\nConversion a Mayuscula y Minuscula")
print(cadena_ejemplo.lower())
print(cadena_ejemplo.upper())
print(cadena_ejemplo.capitalize())
print(cadena_ejemplo.title())

print("\nReemplazo")
cadena_ejemplo = cadena_ejemplo.strip(' ')  # Elimina los espacios en blanco
cadena_ejemplo = cadena_ejemplo.replace('mundo', 'Python')  # Reemplaza una palabra con otra
print(cadena_ejemplo)

print("\nDivision")
lista_cadena = cadena_ejemplo.split(' ')
print(lista_cadena)

print("\nUnion")
print("".join(lista_cadena))

print("\nVerificacion")
numero_ejemplo = "12"
print(f"<{cadena_ejemplo}> es una variable alfa-numerica? {cadena_ejemplo.isalnum()}")
print(f"<{numero_ejemplo}> es un numero? {numero_ejemplo.isnumeric()}")

print("\nBusqueda")
print(f"<{cadena_ejemplo}> contiene un hola? {'Hola' in cadena_ejemplo}")
print(f"<{cadena_ejemplo}> contiene python? Indice {cadena_ejemplo.find('Python')}")
print(f"<{cadena_ejemplo}> Empieza con un hola? {cadena_ejemplo.startswith('Hola')}")
print(f"<{cadena_ejemplo}> Empieza con un hola? {cadena_ejemplo.endswith('Hola')}")

print("\nDificlutad Extra: ")

first_word = input("Ingrese una palabra: ").lower()
second_word = input("Ingrese otra palabra: ").lower()


def palindromos(a_str, b_str):
    if a_str == a_str[::-1]:
        print(f"{a_str} es una Palabra palindroma")
    if b_str == b_str[::-1]:
        print(f"{b_str} es una Palabra palindroma")


def anagramas(a_str, b_str):
    result = sorted(a_str) == sorted(b_str)
    if result:
        print(f"{a_str} y {b_str} es un Anagrama")


def isogramas(a_str, b_str):
    def revisar_palabra(palabra_a_revisar):
        dict_palabra = dict()
        for character in palabra_a_revisar:
            dict_palabra[character] = dict_palabra.get(character, 0) + 1

        isograma = True
        valores = list(dict_palabra.values())
        isograma_longitud = valores[0]
        for word_count in valores:
            if word_count != isograma_longitud:
                isograma = False
                break

        return isograma

    if revisar_palabra(a_str):
        print(a_str + " es un Isograma")
    if revisar_palabra(b_str):
        print(b_str + " es un Isograma")


palindromos(first_word, second_word)
anagramas(first_word, second_word)
isogramas(first_word, second_word)
