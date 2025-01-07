# Cadenas de caracteres
# 1. Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres

# operaciones con cadenas de caracteres
cadena_01 = "hola"
cadena_02 = "mundo"

# concatenacion
concatenacion = cadena_01 + " " + cadena_02
print()
print(concatenacion)

# repeticion
repeticion = cadena_01 * 3
print(repeticion)

# indexacion
indexacion = cadena_01[0] + cadena_01[1] + cadena_01[2] + cadena_01[3]
print(indexacion)
indexacion = cadena_01[0] + cadena_01[3] + cadena_01[0] + cadena_01[3] +cadena_01[0]+ cadena_01[3]
print(indexacion)

# longitud
longitud = len(cadena_01)
print(longitud)

# slicing
slicing = cadena_02[2:6]
print(slicing)
slicing = cadena_02[2:]
print(slicing)
slicing = cadena_02[:4]
print(slicing)

# busqueda
busqueda = "o" in cadena_01
print(busqueda)
busqueda = "i" in cadena_01
print(busqueda)

# remplazo
remplazo = cadena_01.replace("o", "a") 
print(remplazo)
remplazo = cadena_02.replace("o", "i")
print(remplazo)

# division
division = cadena_02.split("n")
print(division)

# mayusculas y minusculas
cadena_03 = "hola caracola"
mayusculas = cadena_01.upper()
print(mayusculas)
minusculas = cadena_01.lower()
print(minusculas)
titulo = cadena_03.title()
print(titulo)
primera_letra_mayuscula = cadena_03.capitalize()
print(primera_letra_mayuscula)

# Eliminar espacios en blanco
cadena_03 = "   hola caracola   "
cadena_03 = cadena_03.strip() # elimina espacios al principio y al final
print(cadena_03)

# Interpolación
nombre = "JacMac45"
edad = 20
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Buqueda al principio y al final
print(cadena_03.startswith("hola"))
print(cadena_03.endswith("ola"))
print(cadena_03.endswith("no"))

# Busqueda de posicion
print(cadena_03.find("hola"))
print(cadena_02.find("n"))
print(cadena_03.lower().find("ola"))

# Busqueda de ocurrencias
cadena_04 = "Es la hora de la fiesta"
print(cadena_04.count("a"))

# Transformación en lista de caracteres
lista_caracteres = list(cadena_03)
print(lista_caracteres)

# Transformación de lista en cadena
lista_caracteres = ["h", "o", "l", "a", " ", "c", "a", "r", "a", "c", "o", "l", "a"]
cadena_03 = "".join(lista_caracteres)
print(cadena_03)

# Casting de cadenas en números
num1 = "123456"
print(type(num1))
nu = int(num1) # A entero
print(type(nu))
print(nu)
num2 = "123456.75"
print(type(num2))
nu2 = float(num2) # A decimal
print(type(nu2))
print(nu2)

# Formateo
print("cadena1 tiene {} y cadena2 tiene {}".format(cadena_01, cadena_02)) # Con format()
print(f"cadena1 tiene {cadena_01} y cadena2 tiene {cadena_02}") # Con f-string 

# Extra
Palabra1 = input("Dime una palabra => ")
Palabra2 = input("Dime otra palabra => ")
print()
# El palindromo se comprueba comparando la palabra con su inversa
print(f"{Palabra1} Es un palindromo") if Palabra1 == Palabra1[::-1] else print(f"{Palabra1} NO es un palindromo")
print(f"{Palabra2} Es un palindromo") if Palabra2 == Palabra2[::-1] else print(f"{Palabra2} NO es un palindromo")
print()

print(f"{Palabra1} y {Palabra2} Son anagramas") if sorted(Palabra1) == sorted(Palabra2) else print(f"{Palabra1} y {Palabra2} NO son anagramas")
print()

print(f"{Palabra1} Es un isograma") if len(Palabra1) == len(set(Palabra1)) else print(f"{Palabra1} NO es un isograma")
print(f"{Palabra2} Es un isograma") if len(Palabra2) == len(set(Palabra2)) else print(f"{Palabra2} NO es un isograma")

