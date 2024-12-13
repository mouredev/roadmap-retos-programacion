# #04 CADENAS DE CARACTERES
'''
Muestra ejemplos de todas las operacines que puedes realizar con cadenas de caracteres:
Acceso a caracteres especificos, subcadenas, longitud, concatenacion, repeticion, recorrido,
conversion a mayusculas y minusculas, reemplazo, division, union, interpolacion, verificacion.
'''

cadena = "HolaMundo"
print(f"String: {cadena}")

# Acceso a caracteres especificos
print("Access to specyfic characters")
print(f"First character: {cadena[0]}")
print(f"Sixth character: {cadena[5]}")
print(f"Last character: {cadena[-1]}")

# Subcadenas
print()

# Longitud
print("\nString Lenght")
print(f"String lenght is: {len(cadena)}")

# Concatenacion
print("\nString Concatenation")
cadena2 = "HolaPython!"
print(cadena + cadena2)

# Repeticion
print("\nString Lenght")
print(cadena * 3)

# Mayusculas
print("\nConvert to uppercase")
print(cadena.upper())

# Minusculas
print("\nConvert to lowercase")
print(cadena.lower())

# Union
print("\nConvert to lowercase")
list_cadena = ["Hola", "mundo", "python"]
join_cadena = " - ".join(cadena)
print(f"Joint String: {cadena}")

# Verificacion
print(f"String is alphanumberic?: {cadena.isalpha()}")

# DIFICULTAD EXTRA
print("\n----------------------------------------------------")
print("EXTRA DIFFICULT")
'''
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palindromos
- Anagramas
- Isogramas
'''
def check(string1, string2):
    # Palindromo
    print(f"{string1} is a palyndrome" if string1 == string1[::-1] else f"{string1} is not a palyndrome")
    print(f"{string2} is a palyndrome" if string2 == string2[::-1] else f"{string2} is not a palyndrome")

    # Anagram
    print(f"{string1} is anagram of {string2}" if sorted(string1) == sorted(string2) else f"{string1} is not anagram of {string2}")

    # Isogram
    print(f"{string1} is an isogram" if len(string1) == len(set(string1)) else f"{string1} is not an isogram")
    print(f"{string2} is an isogram" if len(string2) == len(set(string2)) else f"{string2} is not an isogram")

    print()

def main():
    check("radar", "ana")
    check("amor", "roma")
    check("roma", "python")

if __name__ == "__main__":
    main()

