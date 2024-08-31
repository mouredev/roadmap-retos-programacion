"""EJERCICIO"""

# Acceso a caracteres específicos
cadena = "Hola Python"
print(cadena[0])
print(cadena[-1])


# Sub cadenas
cadena = "Hola Java"
print(cadena[0:4])
print(cadena[5:])


# Longitud
cadena = "Hola C"
print(len(cadena))


# Concatenación
cadena1 = "Hola"
cadena2 = "Mundo"
concatenada = cadena1 + " " + cadena2
print(concatenada)


# Repetición
cadena = "Hola"
repetida = cadena * 3
print(repetida)


# Recorrido
cadena = "Hola Kotlin"
for caracter in cadena:
    print(caracter)


# Conversión a mayúsculas y minúsculas
cadena = "Hola Dart"
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas)
print(minusculas)
print("hola python".title())
print("hola python".capitalize())


# Reemplazo
cadena = "Hola JavaScript"
reemplazo = cadena.replace("JavaScript", "TypeScript")
print(reemplazo)


# División (split)
cadena = "Hola,Python,Java,C"
division = cadena.split(",")
print(division)


# Unión (join)
union = ",".join(division)
print(union)


# Interpolación
nombre = "Marcos"
edad = 17
print(f"Hola, me llamo {nombre} y tengo {edad} años.")


# Verificación
cadena = "Hola Python"
if "Hola" in cadena:
    print("¡Hola está en la cadena!")


"""
DIFICULTAD EXTRA
"""

print("\n")


def palindromos(palabra1: str, palabra2: str):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    print(f"{palabra1} es un palíndromo?: {palabra1 == palabra1[::-1]}")
    print(f"{palabra2} es un palíndromo?: {palabra2 == palabra2[::-1]}")


def anagramas(palabra1: str, palabra2: str):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    print(
        f"{palabra1} es anagrama de {palabra2}? {sorted(palabra1) == sorted(palabra2)}"
    )


def isogramas(palabra1: str, palabra2: str):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    print(f"{palabra1} es isograma?: {len(palabra1) == len(set(palabra1))}")
    print(f"{palabra2} es isograma?: {len(palabra2) == len(set(palabra2))}")


def main():
    palabra1 = input("Ingrese la primer palabra: ")
    palabra2 = input("Ingrese la segundas palabra:")
    palindromos(palabra1, palabra2)
    anagramas(palabra1, palabra2)
    isogramas(palabra1, palabra2)


if __name__ == "__main__":
    main()
