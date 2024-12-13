''' 04 CADENAS DE CARACTERES'''

### OPERACIONES CON CADENAS DE CARACTERES


'''Strings'''
string = "Hola mundo"
double_string = "hola mundo\nAdios para siempre"

print(double_string)

# 1. Concatenación de cadenas
uno = "holaa"
dos = "mundo"
print(uno + " " + dos)

# 2. Repetición de cadenas
print((uno + " ")* 3)

# 3. Longitud de una cadena
print(len(uno))

# 4. Acceso a un caracter
print(uno[0])

# 5. Acceso a un rango de caracteres
## SLICING
print(uno[:3])
print(uno[1:2])
print(uno[0:])

# 6. Búsqueda de un caracter
print("a" in uno)
print("w" not in uno)

# 7. Reemplazo de caracteres
print(uno.replace("h", "p"))

# 8. División
print(uno.split("a"))

# 9. Mayúsculas y minúsculas, y capilalización
print(uno.upper())
print(uno.lower())
print("hola pepe".title()) # Primera letra en mayúscula
print("hola pepe".capitalize()) # Primera letra en mayúscula de la oración

# 10. Eliminación de espacios al principio y al final
print(" hola pepe    ".strip())

#11. Búsqueda al principio y al final
## Devuelve True o False
print(uno.startswith("ho"))
print(uno.endswith("aa"))

# 12. Búsqueda de posición
print(uno.find("a"))

# 13. Búsqueda de ocurrencias 
## Contar cuantas veces aparece un caracter

print(uno.count("a"))

# 14. Leer al reves
print(uno[::-1])


''' Para printear '''

# 1. Formateo de cadenas
print("Saludos desde {}, {}!".format("latinoamerica", "Colombia"))

# 2. Formateo de cadenas con f-strings
print(f"Saludos desde {uno}")

# 3. Pasar a lista
print(list("hola"))

# 4. Pasar a cadena la lista
lista = ["ok","dlsad", uno, "jeje"]
print(" ".join(lista))

'''Para diferentes tipos de datos'''
hola = 9382195238945
hola = int(hola)
print(hola)

# Comprobacion 
numbers = "123456"
print(uno.isalnum()) #Significa que son alfabeticos y/o numericos
print(uno.isalpha()) #Significa que son alfabeticos
print(numbers.isalpha()) #Significa que son alfabetico
print(numbers.isnumeric()) #Significa que no tiene números

''' DIFICULTAD EXTRA
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

def palabras(palabra1, palabra2):
    igual = lambda x, y: x == y
    if igual(palabra1, palabra2):
        if palabra1 == palabra1[::-1]:
            print(f"{palabra1} es un palíndromo.")
        if sorted(palabra1) == sorted(palabra2):
            print(f"{palabra1} y {palabra2} son anagramas.")
    else: 
        print(f"{palabra1} y {palabra2} no son iguales.")
    print("Finalización de programa")

def isograma(palabra1):
    lista = list(palabra1)
    conjunto = set(lista)
    
    if len(conjunto) == len(lista):
        print(f"{palabra1} es un isograma.")
    else:
        print(f"{palabra1} no es un isograma.")
        
            
palabras("level", "leveeel")
isograma("level")     
        
