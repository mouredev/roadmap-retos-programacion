# Operaciones básicas sobre cadenas de texto
texto = "Hola, mundo!"

# Interpolación de cadenas (uso de plantillas de cadena)
nombre = "Migue"
lenguaje = "PHP"
mensaje = f"Hola, me llamo {nombre} y trabajo con {lenguaje} años."
print(mensaje)

# Longitud de la cadena
longitud = len(texto)
print(f"La longitud de la cadena {texto} es {longitud} caracteres")

# Obtener el carácter en una posición específica
primerCaracter = texto[0]
print(f"El primer carácter de {texto} es {primerCaracter}")

# Concatenar dos cadenas
nuevaCadena = texto + " Python"
print(f"La nueva cadena de unir {texto} con Python es {nuevaCadena}")

# Convertir la cadena a minúsculas
minusculas = texto.lower()
print(f"{texto} en minúsculas es {minusculas}")

# Convertir la cadena a mayúsculas
mayusculas = texto.upper()
print(f"{texto} en mayúsculas es {mayusculas}")

# Obtener una subcadena
subcadena = texto[0:4]
print(f"La subcadena de {texto} entre las posiciones 0 y 4 es {subcadena}")

# Reemplazar parte de la cadena
reemplazada = texto.replace("Hola", "Saludos")
print(f"Vamos a reemplazar Hola por Saludos: {reemplazada}")

# Operaciones adicionales sobre cadenas de texto
textoConEspacios = "   Hola,      mundo!   "

# Eliminar espacios en blanco al principio y al final
sinEspaciosExtremos = textoConEspacios.strip()
print(f"Cadena sin espacios al principio y al final: {sinEspaciosExtremos}")

# Eliminar todos los espacios en blanco
sinEspacios = textoConEspacios.replace(" ", "")
print(f"Cadena sin espacios: {sinEspacios}")

# Unión de dos cadenas
cadena1 = "Moure"
cadena2 = "Dev"
unionCadenas = f"{cadena1} {cadena2}"
print(f"La unión de las cadenas {cadena1} y {cadena2} es {unionCadenas}")

# Intersección de dos cadenas (caracteres comunes)
interseccionCadenas = ''.join(set(cadena1) & set(cadena2))
print(f"Intersección de las cadenas {cadena1} y {cadena2} es {interseccionCadenas}")

# Acceso a caracteres específicos (por posición)
tercerCaracter = texto[2]
print(f"El tercer carácter de {texto} es {tercerCaracter}")

# Repetición de una cadena
cadenaRepetida = "Hola " * 3
print(f"Cadena Hola repetida 3 veces queda {cadenaRepetida}")

# Recorrido de una cadena (usando un bucle)
for i in range(len(texto)):
    print(f"Carácter en posición {i}: {texto[i]}")

# Conversión a título (primera letra en mayúscula)
titulo = texto.lower().title()
print(f"La cadena {texto} como título {titulo}")

# División de una cadena en un array de substrings
palabras = texto.split(" ")
print(f"Palabras en la cadena {texto} son {palabras}")

# Verificación de si una cadena comienza o termina con ciertos caracteres
comienzaCon = texto.startswith("Hola")
print(f"¿La cadena {texto} comienza con 'Hola'? {comienzaCon}")

terminaCon = texto.endswith("mundo!")
print(f"¿La cadena {texto} termina con 'mundo!'? {terminaCon}")

# Verificar si una cadena es palíndromo
def esPalindromo(cadena):
    sinEspacios = ''.join(cadena.split()).lower()
    invertida = sinEspacios[::-1]
    return sinEspacios == invertida

# Verificar si una cadena es un anagrama
def esAnagrama(cadena1, cadena2):
    limpiaCadena = lambda cadena: ''.join(cadena.split()).lower()
    limpiaCadena1 = limpiaCadena(cadena1)
    limpiaCadena2 = limpiaCadena(cadena2)
    return sorted(limpiaCadena1) == sorted(limpiaCadena2)

# Verificar si una cadena es un isograma
def esIsograma(cadena):
    caracteres = set()

    for char in cadena:
        caracter = char.lower()
        if caracter in caracteres:
            return False
        caracteres.add(caracter)

    return True

# Ejemplos de uso de las funciones adicionales
print(f"¿Es '{texto}' un palíndromo? {esPalindromo(texto)}")
print(f"¿Es 'Ana' un palíndromo? {esPalindromo('Ana')}")
print(f"¿Es 'listen' un anagrama de 'silent'? {esAnagrama('listen', 'silent')}")
print(f"¿Es 'programming' un isograma? {esIsograma('programming')}")
