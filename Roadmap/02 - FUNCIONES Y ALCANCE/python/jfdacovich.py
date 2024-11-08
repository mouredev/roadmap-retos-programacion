# Función si parámetros
def hey():
    print("Hey que tal?")

# Función con un parámetro
def hey_personalizado(nombre):
    print(f"Hey {nombre} que tal?")

# Función con varios parámetros
def suma(a, b):
    return a + b

# Función dentro de otra función
def funcion_outside():
    print("OUT")

    def funcion_inside():
        print("IN")

    funcion_inside()

# Función creada en el lenguaje
def longitud(str):
    return len(str)

# Variables Locales y Globales
global_var = "Global"

def funcion_var():
    local_var = "Local"
    print(local_var)
    print(global_var)

"""
Dificultad Extra
"""

def imprimir_numeros(str1: str, str2: str) -> int:
    count = 0
    for num in range(1, 100+1):
        if num % 3 == 0 and num % 5 == 0:
            print(f"Las dos cadenas: {str1},{str2}")
        elif num % 3 == 0:
            print(f"La cadena 1: {str1}")
        elif num % 5 == 0:
            print(f"La cadena 2: {str2}")
        else:
            print(num)
            count += 1
    return count

print("----------funciones básicas----------")
hey()
hey_personalizado("jfdacovich")
print(suma(11,7))
funcion_outside()
print(longitud("Heyyy people!!"))
funcion_var()
print(imprimir_numeros("buenass", "adiosss"))