mi_cadena = "Esto sería una cadena de caracteres"
otra_cadena = "Y esto es otra cadena de caracteres"

print(mi_cadena + " - " + otra_cadena) # Concatenación -> Esto sería una cadena de caracteres - Y esto sería otra cadena de caracteres

print(mi_cadena*2) # Repetición -> Esto sería una cadena de caracteresEsto sería una cadena de caracteres
print(len(mi_cadena)) # Longitud -> 35
print(mi_cadena[0]) # Muestra el primer caracter -> E
print(mi_cadena[0:5]) # Muestra desde la posición 0 hasta la 5 -> Esto
print(mi_cadena[5:]) # Muestra desde la posición 5 hasta el final -> sería una cadena de caracteres
print("sería" in mi_cadena) # Verificar si una cadena contiene sería -> True
print("uno" in mi_cadena) # Verificar si una cadena contiene uno -> False
print(mi_cadena.replace("sería", "es")) # Reemplazo de sería por es -> Esto es una cadena de caracteres
print(mi_cadena.split(" ")) # División de cadena en lista -> ['Esto', 'sería', 'una', 'cadena', 'de', 'caracteres']
print(mi_cadena.upper()) # Mayúsculas -> ESTO SERÍA UNA CADENA DE CARACTERES
print(mi_cadena.lower()) # Minúsculas -> esto sería una cadena de caracteres
print(mi_cadena.title()) # Letras en mayúsculas -> Esto Sería Una Cadena De Caracteres
print(mi_cadena.capitalize()) # Capitalize -> Esto sería una cadena de caracteres
print(mi_cadena.strip()) # Eliminación de espacios al principio y al final
print(mi_cadena.startswith("Es")) # Búsqueda al principio -> True
print(mi_cadena.endswith("res")) # Búsqueda al final -> True
print(mi_cadena.find("sería")) # Búsqueda de posición -> 5
print(mi_cadena.find("Sería")) # Búsqueda de posición -> -1 (No encontrado)
print(mi_cadena.find("esto")) # Búsqueda de posición -> -1 (No encontrado)
print(mi_cadena.lower().find("esto")) # Búsqueda de posición -> 0
print(mi_cadena.count("e")) # Búsqueda de ocurrencias -> 5
print(mi_cadena.count("s")) # Búsqueda de ocurrencias -> 3
print(mi_cadena.isalnum()) # Verificar si la cadena es alfanumérica -> False

nombre = "Marcos"
deporte = "pádel"

print(nombre.center(50)) # Centrado ->                      Marcos


for letra in nombre: # Iteración de la cadena nombre
    print(letra) # Muestra cada letra en una línea
for letra in nombre: # Iteración de la cadena nombre
    print(letra, end="") # Muestra cada letra en la misma línea
print()
for letra in nombre: # Iteración de la cadena nombre
    print(letra, end=".") # Muestra cada letra en la misma línea separada por un punto 
print()

print("Hola {}, deporte: {}".format(nombre, deporte)) # Formateo -> Hola Marcos, deporte: pádel
print("Hola {nombre}, deporte: {deporte}".format(nombre="Juan", deporte="fútbol")) # Formateo -> Hola Juan, deporte: fútbol
print(f"Hola {nombre}, deporte: {deporte}") # Interpolación -> Hola Marcos, deporte: pádel  
print(list(nombre)) # Transformación en lista de caracteres -> ['M', 'a', 'r', 'c', 'o', 's']
mi_join =[nombre, " ", deporte, "!", "!", "!", "!", "!"]
print("".join(mi_join)) # Transformación de lista en cadena -> Marcos pádel!!!!!
mi_otro_join = " - "
print(mi_otro_join.join(["1","2","3"]))

"""
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos 
- Anagramas
- Isogramas
"""
def comprobar(palabra1: str, palabra2: str):

    # PALÍNDROMOS (se lee igual de izquierda a derecha que de derecha a izquierda)
    print(f"¿{palabra1} es un palíndromo?: {palabra1 == palabra1[::-1]}")
    print(f"¿{palabra2} es un palíndromo?: {palabra2 == palabra2[::-1]}")

    # ANAGRAMAS (palabras que tienen las mismas letras pero en distinto orden)
    print(f"¿{palabra1} es anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}")

    # ISOGRAMAS (palabras que no tienen letras repetidas)
    def isograma(palabra):

        palabras_dict = dict() # Diccionario para almacenar las letras de la palabra
        for caracter in palabra: # Iteración de la palabra
            palabras_dict[caracter] = palabras_dict.get(caracter, 0) + 1 # Almacenamiento de las letras

        isograma = True # Inicialización de la variable isograma
        values = list(palabras_dict.values()) # Obtención de los valores del diccionario
        isograma_len = values[0] # Obtención del primer valor
        for word_count in values: # Iteración de los valores
            if word_count != isograma_len: # Comparación de los valores
                isograma = False
                break

        return isograma

    print(f"¿{palabra1} es un isograma?: {isograma(palabra1)}")
    print(f"¿{palabra2} es un isograma?: {isograma(palabra2)}")


comprobar("oso", "casa")
comprobar("oso", "oso")
comprobar("oso", "abcdefghijklmnopqrstuvwxyz")
comprobar("radar", "roma")