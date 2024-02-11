#Ejercicio
#Acceso a caracter específico
cadena = "Python"
primer_caracter = cadena[0]
ultimo_caracter = cadena[-1]
print(primer_caracter, ultimo_caracter)

#Subcadena
cadena = "Python"
posicion = cadena.find("y")
print(posicion)

#Longitud
cadena = "Python"
longitud = len(cadena)
print(longitud)

#Concatenación
cadena1 = "Hola"
cadena2 = "Mundo"
resultado = cadena1 + " " + cadena2
print(resultado)

#Repetición
cadena = "Python "
resultado = cadena * 3
print(resultado)

#Recorrido
cadena = "Python"
for caracter in cadena:
    print(caracter)


#Conversión Minusculas y Mayusculas
cadena = "Python"
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas, minusculas)

#Reemplazo
cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Mundo", "Python")
print(nueva_cadena)

#División
cadena = "Python es genial"
subcadenas = cadena.split(" ")  # Dividir por espacio en blanco
print(subcadenas)

cadena = "Python es genial"
trozo1 = cadena[:6]  
trozo2 = cadena[7:9]  
trozo3 = cadena[10:]  

print(trozo1, trozo2, trozo3)

#Unión
cadenas = ["Hola", "Python"]
union = " xx ".join(cadenas)
print(union)

#Interpolación con f-strings y método format 
nombre = "Felipe"
edad = 33
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)

mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)

#Verificación con Dígito, Letra, Alfanumérico, Mayúscula, Minúscula y espacio en blanco
caracter = '5'
if caracter.isdigit():
    print(f"{caracter} es un dígito.")
else:
    print(f"{caracter} no es un dígito.")

caracter = 'A'
if caracter.isalpha():
    print(f"{caracter} es una letra.")
else:
    print(f"{caracter} no es una letra.")

caracter = 'X'
if caracter.isalnum():
    print(f"{caracter} es alfanumérico.")
else:
    print(f"{caracter} no es alfanumérico.")

caracter = 'Z'
if caracter.isupper():
    print(f"{caracter} está en mayúsculas.")
else:
    print(f"{caracter} no está en mayúsculas.")

caracter = 'z'
if caracter.islower():
    print(f"{caracter} está en minúsculas.")
else:
    print(f"{caracter} no está en minúsculas.")

caracter = ' '
if caracter.isspace():
    print(f"{caracter} es un espacio en blanco.")
else:
    print(f"{caracter} no es un espacio en blanco.")

#Ejercicio
#Palindromo
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return palabra == palabra[::-1]

def verificar_palindromos(palabra1, palabra2):
    if es_palindromo(palabra1) and es_palindromo(palabra2):
        print(f"Ambas palabras, '{palabra1}' y '{palabra2}', son palíndromos.")
    elif es_palindromo(palabra1):
        print(f"La palabra '{palabra1}' es un palíndromo, pero '{palabra2}' no lo es.")
    elif es_palindromo(palabra2):
        print(f"La palabra '{palabra2}' es un palíndromo, pero '{palabra1}' no lo es.")
    else:
        print(f"Ni '{palabra1}' ni '{palabra2}' son palíndromos.")

# Ejemplo de uso
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

verificar_palindromos(palabra1, palabra2)

#Anagrama
def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    palabra2 = palabra2.lower().replace(" ", "")

    # Verificar si las palabras tienen la misma cantidad de letras
    if len(palabra1) != len(palabra2):
        return False

    # Verificar si ambas palabras contienen las mismas letras
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if son_anagramas(palabra1, palabra2):
    print(f"'{palabra1}' y '{palabra2}' son anagramas.")
else:
    print(f"'{palabra1}' y '{palabra2}' no son anagramas.")