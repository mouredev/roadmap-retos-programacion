# 1. Concatenación de caracteres

palabra_1 = "Gato"
palabra_2 = "Perro"

union = palabra_1 + " " + palabra_2

print(union)

# 2. Repetición de caracteres

repeticion = palabra_1 * 4

print(repeticion)

# la función join agrega un espacio al inicio de cada palabra

resultado_2 = " ".join([palabra_1] * 4)

print(resultado_2)

# 3. Acceso e indexación: acceder a un caracter específico con el índice.

print(palabra_1[3]) 
print(palabra_1[0])
print(palabra_1[-2])   #cuenta desde el último caracter

# 4. Slicing: extrae una porción de la cadena de caracteres

frase = "Hoy no tomé desayuno"

print(frase[0:3])   #se excluye el ultimo indice
print(frase[12:])   #si no se indica el fin este llega al final de la cadena

# 5. Longitud: nos entrega la longitud de la cadena de caracteres

print(len(frase))

# 6. Búsqueda de caracteres o subcadenas

print("D" in frase)
print("d" in frase)
print(frase.find("desayuno"))
print(frase.index("desayuno"))

# 7. Reemplazo de subcadenas

nueva_frase = frase.replace("no", "si")

print(nueva_frase)

# Cuando se repite una palabra la va a cambiar, para evitarlo se especifica cuantas veces se quiere cambiar

nueva_frase2 = frase.replace("no", "si", 1)

print(nueva_frase2)

# 8. Conversión a mayúsculas y minúsculas

print(frase.upper())
print(frase.lower())

# 9. Capitalización y formato de título

palabra = "hola gato"

print(palabra.capitalize())   # Solo pone mayuscula la primera letra
print(palabra.title())        # Pone mayuscula en cada palabra

# 10. Eliminar espacios en blanco

cadena = "       Hola Mundo Gatos       "

print(cadena.strip())
print(cadena.lstrip())   # Solo a la izquierda
print(cadena.rstrip())   # Solo a la derecha

# 11. Dividir y unir: se divide con split y se une con join

partes = cadena.split()   # Divide por espacios
print(palabra_1.split("t"))

print(partes)

unir = " ".join(partes)

print(unir)

# 12. Verificación de tipo de caracteres

print(palabra_1.isdigit())   #Falso, son letras
print(palabra_1.isalpha())   #True, son todas letras

palabraConNumeros = "abcd1234"

print(palabraConNumeros.isalnum())  #True, son letras y numeros

# 14. Formato de cadenas

nombre = "Juan"
edad = 45

print(f"Nombre: {nombre}, Edad: {edad}")
print("Nombre: {}, Edad: {}".format(nombre, edad))
print("Nombre: %s, Edad: %d" %(nombre, edad))

# 15. Transformación numérica

num = "012345"
num = int(num)
print(int(num))
print(type(num))

# 16. Transformacion decimales

dec = "1234.123"
dec = float(dec)
print(float(dec))
print(type(dec))


#* DIFICULTAD EXTRA (opcional):
# * Crea un programa que analice dos palabras diferentes y realice comprobaciones
# * para descubrir si son:
# * - Palíndromos
# * - Anagramas
# * - Isogramas

palabra1 = "arenera"
palabra2 = "amor"

def palindromos(palabra1):
    return palabra1 == palabra1[::-1]  # [inicio:fin:paso]

print(palindromos(palabra1)) 

# lo que hace [::-1] es dar vuelta la palabra
# == va a devolver un booleano porque compara los valores

def anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

print(anagramas(palabra1, palabra2)) 

# Isograma: palabra donde ninguna letra se repite.

pal1 = "Murcielago"

# primero separamos la palabra por sus caracteres con set, donde no se muestran repetidos
# se mide el largo de la palabra con len() y se compara con len() del set() de la palabra
# si es distinto significa que alguna letra se repite, por lo que no es isograma
# si son iguales, la palabra no tiene caracteres que se repiten, siendo isograma

if len(pal1) == len(set(pal1)):
    print(f"{pal1}, si es isograma")

else:
    print(f"{pal1}, no es isograma")