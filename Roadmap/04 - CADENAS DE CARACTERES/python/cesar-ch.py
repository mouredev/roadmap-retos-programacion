# #04 CADENAS DE CARACTERES

# Ejercicio

# Acceso a caracteres específicos
cadena = "Hola, mundo!"
print("Primer caracter: ", cadena[0])
print("Último caracter: ", cadena[-1])

# Subcadenas
subcadena = cadena[0:4]
print("Subcadena: ", subcadena)

# Longitud de la cadena
longitud = len(cadena)
print("Longitud: ", longitud)

# Concatenación
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + " " + cadena2
print("Concatenación: ", concatenacion)

# Repetición
repetida = cadena1 * 3
print("Repetición: ", repetida)

# Recorrido
for caracter in cadena:
    print(caracter)

# Conversión a mayúsculas y minúsculas
mayusculas = cadena.upper()
minusculas = cadena.lower()
print("Mayúsculas: ", mayusculas)
print("Minúsculas: ", minusculas)

# Reemplazo
reemplazo = cadena.replace("mundo", "Python")
print("Reemplazo: ", reemplazo)

# División
division = cadena.split(",")
print("División: ", division)

# Unión
union = "-".join(["Hola", "Python"])
print("Unión: ", union)

# Interpolación
lenguaje = "Python"
interpolacion = f"El lenguaje es {lenguaje}."
print("Interpolación: ", interpolacion)

# Verificación
contieneHola = "Hola" in cadena
contieneHola2 = cadena.find("Hola") != -1
print("Contiene Hola: ", contieneHola)
print("Contiene Hola: ", contieneHola2)


# Dificultad extra
def comprobar_palabra(palabra1, palabra2):
    def es_palindromo(palabra1, palabra2):
        if len(palabra1) != len(palabra2):
            return False
        return palabra1.lower() == palabra2.lower()[::-1]

    print("Es palindromo: ", es_palindromo(palabra1, palabra2))

    def es_anagrama(palabra1, palabra2):
        if len(palabra1) != len(palabra2):
            return False

        return sorted(palabra1.lower()) == sorted(palabra2.lower())

    print("Es anagrama: ", es_anagrama(palabra1, palabra2))

    def es_isogama(palabra1, palabra2):
        if len(palabra1) != len(palabra2):
            return False

        char_counter = {}
        for char in palabra1:
            if char in char_counter:
                char_counter[char.lower()] += 1
            else:
                char_counter[char.lower()] = 1

        for char in palabra2:
            if char in char_counter:
                char_counter[char.lower()] -= 1
            else:
                return False

        return all(value == 0 for value in char_counter.values())

    print("Es isogama: ", es_isogama(palabra1, palabra2))
