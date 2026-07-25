#04 CADENAS DE CARACTERES
"""
-Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
-Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
interpolación, verificación...
"""
#CREACION DE CADENAS
primeracadena = "hola compañeros"
segundacadena = "python es genial"
cadena_multilinea = """Escribir un texto muy grande en una cadena es mas facil con las cadenas multilineas, mira todo
el texto que cabe en esta cadena wooow"""

#ACCESO A CARACTERES ESPECIFICOS
acceso_cadena = "pyhton"
print(acceso_cadena[0])
print(acceso_cadena[-1])
print(acceso_cadena[2])

#SUBCADENAS (SLICING)
cadena_subcadenas = "Hola_mi_nombre_es jose_muchisimo gusto"
print(cadena_subcadenas[3:7])
print(cadena_subcadenas[:8])
print(cadena_subcadenas[8:])
print(cadena_subcadenas[::2])
print(cadena_subcadenas[::-1])

#LONGITUD DE UNA CADENA
cadena_longitud = "parangaricutirimicuaro"
print(len(cadena_longitud))

print(cadena_longitud)
#CONCATENACION
concatenadora_1 = "Hola"
concatenadora_2 = " y adios"
print(concatenadora_1+concatenadora_2)

#REPETICION
cadena_repeticion = "osito gominola\n"
print(cadena_repeticion*7)

#RECORRIDO DE CADENAS
cadena_recorridos = "Python"
for caracter in cadena_recorridos:
    print(caracter)

#CONVERSION A MAYUSCULAS Y MINUSCULAS
mayus_minus = "mayusculas_minusculas"
print(mayus_minus.upper())
print(mayus_minus.lower())
print(mayus_minus)
print(mayus_minus.capitalize())
print("hola mundo".title())  

#REEMPLAZO
cadena_reemplazo = "Me gusta la pizza hawaiana"
print(cadena_reemplazo.replace("hawaiana","con peperoni"))

#DIVISION
cadena_division = "Jose,Michel,Enrique,Monica,Monroy"
print("\n".join(cadena_division.split(",")))   #Lo del join viene a continuacion jejeje

#UNION O JOIN
lista = ["Python", "Java", "C++"]
print(", ".join(lista))   

#INTERPOLACION (F-STRINGS)
nombre = "Jose"
edad = "23"
print(f"Mi nombre es {nombre} y tengo {edad} años")

#VERIFICACION
verificadena = "Gallolobo123"
print(verificadena.isalpha())  
print(verificadena.isdigit())
print(verificadena.isalnum())
print(verificadena.startswith("Gallo"))
print(verificadena.endswith("123"))
print("GALLO" in verificadena.upper())

#ELIMINACION DE ESPACIOS
espacio_cadena ="   Gallo   "
print(espacio_cadena.strip())
print(espacio_cadena.rstrip())
print(espacio_cadena.lstrip())

#BUSQUEDA
buscadena = "Programación en python"
print(buscadena.find("python"))
print(buscadena.find("Java"))   
print(buscadena.index("en"))   #INDEX SI NO ENCUENTRA LANZA ERROR  
print(buscadena.count("a"))     
print(buscadena.count("z"))     

#FORMATEO
nombre = "Carlos"
edad = 30
print("Nombre: {}, Edad: {}".format(nombre, edad))  # Formato tradicional
print("Nombre: {1}, Edad: {0}".format(edad, nombre))  # Con índices

#COMPROBACIONES
comprobacion_cadena = "python"
print(comprobacion_cadena.islower())  # False
print(comprobacion_cadena.isupper())  # False
print("123".isnumeric())  # True
print("   ".isspace())   # True

#CODIFICACION Y DECODIFICACION
cadena = "Año"
bytes = cadena.encode('utf-8')  # b'A\xc3\xb1o'
print(bytes.decode('utf-8'))   # 'Año'


"""
            Dificultad extra
"""
print("Este es el programa de dificultad extra, necesitaras ingresar dos palabras")
Primera_palabra = input("Ingresa la primera palabra: ")
Segunda_palabra = input("Ingresa la Segunda palabra: ")

# PALINDROMO CHEQUEO 
if Primera_palabra == Primera_palabra[::-1]:
    print("La primera palabra es un palindromo")
else:
    print("La primera palabra no es un palindromo")
if Segunda_palabra == Segunda_palabra[::-1]:
    print("La segunda palabra es un palindromo")
else:
    print("La segunda palabra no es un palindromo")
    
# ISOGRAMA CHEQUEO
palabra_limpia_1 = Primera_palabra.replace(" ", "").lower()
palabra_limpia_2 = Segunda_palabra.replace(" ", "").lower()

if len(palabra_limpia_1) == len(set(palabra_limpia_1)):
    print("La primera palabra es un isograma")
else: 
    print("La primera palabra no es un isograma")
if len(palabra_limpia_2) == len(set(palabra_limpia_2)):
    print("La segunda palabra es un isograma")
else:
    print("La segunda palabra no es un isograma")

# ANAGRAMA CHEQUEO
if sorted(palabra_limpia_1) == sorted(palabra_limpia_2):
    print("Las palabras son un anagrama")
else: 
    print("Las palabras no son un anagrama") 
    