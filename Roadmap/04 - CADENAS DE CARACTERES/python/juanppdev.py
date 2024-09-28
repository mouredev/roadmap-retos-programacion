# Definir una cadena de caracteres
cadena = "Hola, mundo!"

# Acceso a caracteres específicos
primer_caracter = cadena[0]
ultimo_caracter = cadena[-1]

print("Acceso a caracteres:")
print("Primer caracter:", primer_caracter)
print("Último caracter:", ultimo_caracter)

# Subcadenas
subcadena = cadena[0:4]
print("\nSubcadena:")
print("Subcadena de los primeros 4 caracteres:", subcadena)

# Longitud de la cadena
longitud = len(cadena)
print("\nLongitud de la cadena:")
print("Longitud de la cadena:", longitud)

# Concatenación
otra_cadena = " ¡Python es genial!"
cadena_concatenada = cadena + otra_cadena
print("\nConcatenación:")
print("Cadena concatenada:", cadena_concatenada)

# Repetición
cadena_repetida = cadena * 3
print("\nRepetición:")
print("Cadena repetida 3 veces:", cadena_repetida)

# Recorrido
print("\nRecorrido:")
for caracter in cadena:
    print(caracter, end=" ")

# Conversión a mayúsculas y minúsculas
print("\n\nConversión a mayúsculas y minúsculas:")
mayusculas = cadena.upper()
minusculas = cadena.lower()
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)

# Reemplazo
cadena_reemplazada = cadena.replace("mundo", "Python")
print("\nReemplazo:")
print("Cadena con reemplazo:", cadena_reemplazada)

# División
palabras = cadena.split(",")
print("\nDivisión:")
print("Cadena dividida por coma:", palabras)

# Unión
nueva_cadena = "-".join(palabras)
print("\nUnión:")
print("Palabras unidas por guión:", nueva_cadena)

# Interpolación
nombre = "Juan"
edad = 25
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print("\nInterpolación:")
print("Mensaje interpolado:", mensaje)

# Verificación
es_digito = cadena.isdigit()
print("\nVerificación:")
print("¿La cadena contiene solo dígitos?:", es_digito)

## Ejercicio Extra
def es_palindromo(palabra):
    reversa = palabra[::-1]
    return palabra == reversa

def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def es_isograma(palabra):
    set_de_caracteres = set()
    for caracter in palabra:
        if caracter in set_de_caracteres:
            return False  # Si se encuentra un carácter repetido, no es un isograma
        set_de_caracteres.add(caracter)
    return True

# Ingresa las dos palabras que deseas analizar
palabra1 = input("Ingresa la primera palabra: ").lower()
palabra2 = input("Ingresa la segunda palabra: ").lower()

# Comprobación de palíndromo
es_palindromo_1 = es_palindromo(palabra1)
es_palindromo_2 = es_palindromo(palabra2)

# Comprobación de anagrama
es_anagrama_resultado = es_anagrama(palabra1, palabra2)

# Comprobación de isograma
es_isograma_1 = es_isograma(palabra1)
es_isograma_2 = es_isograma(palabra2)

# Mostrar resultados
print("\nResultados:")
print(f"Palabra 1 es palíndromo: {es_palindromo_1}")
print(f"Palabra 2 es palíndromo: {es_palindromo_2}")
print(f"Son anagramas: {es_anagrama_resultado}")
print(f"Palabra 1 es isograma: {es_isograma_1}")
print(f"Palabra 2 es isograma: {es_isograma_2}")
