"""
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
"""

# Operaciones

x1 = "Perro"
x2 = "Conejo"
x3 = "tortuga nadando"

print(x1 + x2)      # Concatenacion (pegar dos o mas cadenas de texto)

print(x1 * 3)       # Repeticion

print(x1[4] + x1[3] + x1[2] + x1[1] + x1[0])    # Indexacion (indicar un solo caracter de la cadena)

print(len(x2))      # Longitud

print(x2[2:6])      # Slicing (porcionar la cadena de texto)
print(x2[2:])
print(x2[:4])

print("e" in x1)    # Busqueda (comprobar si el/los caracteres se encuentran en una cadena de texto)
print("jo" in x2)

print(x2.replace("o","a"))  # Remplazo

print(x2.split("e"))        # Division de una cadena que da como resultado una lista

print(x3.upper())   # Convertir a Mayusculas

print(x1.lower())   # Convertir a minusculas

print(x3.title())   # Primera letra a mayuscula de cada palabra

print(x3.capitalize())  # Primera letra a mayuscula de toda la cadena de texto

print(" Dkp Dev ")
print(" Dkp Dev ".strip())  # Elimincacion de espacios al comienzo y al final de la cadena

print(x3.startswith("Tor")) # Comprueba si la cadena inicia con los caracteres que se especifiquen
print(x3.startswith("tor"))

print(x3.find("ando"))  # Busqueda por posicion del caracter

print(x3.count("a"))    # Busqueda de ocurrencias (cuantas veces aparece el caracter)

print("{}, {} y {}".format(x1,x2,x3))   # Formateo de una cadena eligiendo donde insertare mis cadenas de texto

print(f"{x2}, {x1} y {x3}")     # Interpolacion

print(list(x1))         # Transforma una cadena en lista

l1 = [x1, x2, "y", x3]
print(" ".join(l1))     # Transforma una lista a cadena de texto

x4 = "357"          # Transformar una cadena numerica en un 'int'
x4 = int(x4)
print(x4)

x5 = "35.7"         # Transformar una cadena numerica en un 'float'
x5 = float(x5)
print(x5)

x1 = "Perro"            # Comprobaciones
x6 = "123123"
print(x1.isalpha())     # Si la cadena es alfabetica (solo contiene letras)
print(x6.isalpha())

print(x1.isnumeric())   # Si la cadena es numerica (solo contiene numeros)
print(x6.isnumeric())

print(x1.isalnum())     # Si la cadena es alfanumerica (contiene letras y/o numeros)
print(x6.isalnum())

