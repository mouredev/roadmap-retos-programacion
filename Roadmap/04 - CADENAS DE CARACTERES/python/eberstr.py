# Definición de cadena
cadena = "Hola, mundo!"

# 1. Acceso a caracteres específicos
print("Primer carácter:", cadena[0])        # H
print("Último carácter:", cadena[-1])       # !

# 2. Subcadenas
print("Subcadena (posición 1 a 4):", cadena[1:5])   # ola,

# 3. Longitud de la cadena
print("Longitud de la cadena:", len(cadena))        # 12

# 4. Concatenación
saludo = "Hola" + " " + "mundo!"
print("Concatenación:", saludo)                     # Hola mundo!

# 5. Repetición de cadenas
print("Repetición:", "Hola! " * 3)                  # Hola! Hola! Hola!

# 6. Recorrido de caracteres (iteración)
for caracter in cadena:
    print(caracter, end=" ")                        # H o l a ,   m u n d o !

# 7. Conversión a mayúsculas y minúsculas
print("\nMayúsculas:", cadena.upper())              # HOLA, MUNDO!
print("Minúsculas:", cadena.lower())                # hola, mundo!

# 8. Reemplazo
print("Reemplazo:", cadena.replace("mundo", "Python"))  # Hola, Python!

# 9. División (split)
palabras = cadena.split(", ")
print("División por ', ':", palabras)               # ['Hola', 'mundo!']

# 10. Unión (join)
unidas = " ".join(palabras)
print("Unión de lista en cadena:", unidas)          # Hola mundo!

# 11. Interpolación (f-strings)
nombre = "Eber"
print(f"Hola, {nombre}!")                           # Hola, Eber!

# 12. Verificación de prefijo y sufijo
print("Empieza con 'Hola':", cadena.startswith("Hola"))  # True
print("Termina con '!':", cadena.endswith("!"))          # True

# 13. Buscar posición de subcadena
print("Posición de 'mundo':", cadena.find("mundo"))      # 6

# 14. Contar ocurrencias
print("Ocurrencias de 'o':", cadena.count("o"))          # 2

# 15. Comprobar si es numérica o alfabética
print("Es numérica:", cadena.isdigit())                  # False
print("Es alfabética:", cadena.isalpha())                # False (hay espacios y signos)

# 16. Eliminar espacios en blanco (trim)
cadena_espacios = "   Hola, mundo!   "
print("Sin espacios:", cadena_espacios.strip())          # "Hola, mundo!"

# 17. Capitalización (primera letra en mayúscula)
print("Capitalización:", cadena.capitalize())            # "Hola, mundo!"

# 18. Título (Primera letra de cada palabra en mayúscula)
print("Título:", cadena.title())                         # "Hola, Mundo!"


# Extra

def palindromo(palabra):
    word =""
    for letra in palabra:
        i -= 1
        if letra != palabra[i]:
            break
        else:
            word += letra
    if word == palabra:
        print(f"La palabra {palabra} es un palindromo")
    else:
        print(f"La palabra {palabra} NO es un palindromo")

def anagrama(palabra1, palabra2):
    if palabra1.sorted() == palabra2.sorted()
        print("Anagrama")
    else:
        print("No anagrama")

def isograma(palabra):
    letras  = []
    for letra in palabra:
        if letra not in letras:
            letras.append(letra)
    if letras == list(palabra):
        print(f"La palabra {palabra} es un isograma")
    else:
        print(f"La palabra {palabra} NO es un isograma")

