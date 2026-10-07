#cadena de caracteres

# ==========================================
# OPERACIONES CON CADENAS EN PYTHON
# ==========================================

texto = "Hola, Python"

# ------------------------------------------
# 1. ACCESO A CARACTERES
# ------------------------------------------

print(texto[0])       # H
print(texto[5])       # ,
print(texto[-1])      # n
print(texto[-2])      # o


# ------------------------------------------
# 2. SUBCADENAS / SLICING
# ------------------------------------------

print(texto[0:4])     # Hola
print(texto[6:])      # Python
print(texto[:4])      # Hola
print(texto[::2])     # Hl,Pto
print(texto[::-1])    # nohtyP ,aloH


# ------------------------------------------
# 3. LONGITUD
# ------------------------------------------

print(len(texto))


# ------------------------------------------
# 4. CONCATENACIÓN
# ------------------------------------------

nombre = "Leandro"
apellido = "Fritz"

nombre_completo = nombre + " " + apellido

print(nombre_completo)


# ------------------------------------------
# 5. REPETICIÓN
# ------------------------------------------

print("Hola " * 3)
print("-" * 30)


# ------------------------------------------
# 6. RECORRIDO
# ------------------------------------------

for caracter in texto:
    print(caracter)


# También podemos obtener posición + carácter
for posicion, caracter in enumerate(texto):
    print(posicion, caracter)


# ------------------------------------------
# 7. MAYÚSCULAS Y MINÚSCULAS
# ------------------------------------------

print(texto.upper())
print(texto.lower())

print(texto.capitalize())
print(texto.title())


# ------------------------------------------
# 8. REEMPLAZO
# ------------------------------------------

print(texto.replace("Python", "Mundo"))

texto2 = "uno uno uno"

print(texto2.replace("uno", "dos"))
print(texto2.replace("uno", "dos", 1))


# ------------------------------------------
# 9. DIVISIÓN / SPLIT
# ------------------------------------------

frase = "Python es un lenguaje de programación"

palabras = frase.split()

print(palabras)

# Separar utilizando un carácter específico
fecha = "2026-10-01"

print(fecha.split("-"))


# ------------------------------------------
# 10. UNIÓN / JOIN LISTA A CADENA DE TEXTO
# ------------------------------------------

palabras = ["Python", "es", "genial"]

print(" ".join(palabras))
print("-".join(palabras))
print(", ".join(palabras))


# ------------------------------------------
# 11. ELIMINAR ESPACIOS
# ------------------------------------------

texto = "   Hola Python   "

print(texto.strip())    # ambos lados
print(texto.lstrip())   # izquierda
print(texto.rstrip())   # derecha


# ------------------------------------------
# 12. BÚSQUEDA
# ------------------------------------------

texto = "Python es genial"

print("Python" in texto)
print("Java" in texto)

print(texto.find("genial"))
print(texto.find("Java"))


# ------------------------------------------
# 13. COMPROBAR SI COMIENZA O TERMINA
# ------------------------------------------

print(texto.startswith("Python"))
print(texto.endswith("genial"))


# ------------------------------------------
# 14. COMPROBAR EL CONTENIDO
# ------------------------------------------

print("Python".isalpha())       # Solo letras
print("12345".isdigit())        # Solo números
print("Python123".isalnum())    # Letras y números
print("   ".isspace())         # Solo espacios


# ------------------------------------------
# 15. COMPARACIÓN
# ------------------------------------------

a = "Python"
b = "Python"
c = "python"

print(a == b)
print(a == c)

print(a != c)


# ------------------------------------------
# 16. REPETICIONES DE UN CARÁCTER / TEXTO
# ------------------------------------------

texto = "banana"

print(texto.count("a"))
print(texto.count("na"))


# ------------------------------------------
# 17. INTERPOLACIÓN
# ------------------------------------------

nombre = "Leandro"
edad = 41

# f-string
print(f"Mi nombre es {nombre} y tengo {edad} años")


# También podemos realizar operaciones
print(f"El año que viene tendré {edad + 1} años")


# ------------------------------------------
# 18. FORMATEAR TEXTO
# ------------------------------------------

precio = 12500.50

print(f"Precio: ${precio:.2f}")


# ------------------------------------------
# 19. CONVERTIR OTROS TIPOS A STRING
# ------------------------------------------

numero = 100
decimal = 10.5

print(str(numero))
print(str(decimal))


# ------------------------------------------
# 20. CONVERTIR STRING A OTROS TIPOS
# ------------------------------------------

numero = "100"
decimal = "10.5"

print(int(numero))
print(float(decimal))


# ------------------------------------------
# 21. INVERTIR UNA CADENA // PALINDROMO
# ------------------------------------------

texto = "Python"

invertido = texto[::-1]

print(invertido)


# ------------------------------------------
# 22. LONGITUD Y CARACTERES
# ------------------------------------------

texto = "Python"

print(f"Primera letra: {texto[0]}")
print(f"Última letra: {texto[-1]}")
print(f"Cantidad de caracteres: {len(texto)}")


# ------------------------------------------
# 22. ANAGRAMA
# ------------------------------------------
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)


print(es_anagrama("roma", "amor"))    # True
print(es_anagrama("python", "java"))  # False


# ------------------------------------------
# 22. isograma, LETRAS APARECEN EL MISMO NUMERO DE VECES
# ------------------------------------------
texto = "MURCIELAGO"

if len(texto) == len(set(texto)):
    print("Es un isograma")
else:
    print("No es un isograma")