# Operaciones con Cadena de Caracteres

str1 = "Hola"
str2 = "Mundo"

concatenacion = str1 + " " + str2  # Concatenar Strings
print(concatenacion)

repeticion = str1*3
print(repeticion)  # Repetir Strings

longitud = len(str1)  # Ver la longitud de un String
print(longitud)

indexacion = str1[0]  # Acceder a una posicion del String
print(indexacion)

busqueda = "H" in str1  # Verificar si existe un valor en el String
print(busqueda)

inicio = str1.startswith("Hol")  # Verificar si inicia el String con...
fin = str1.endswith("la")  # Verificar si finaliza el String con...
print(inicio)
print(fin)

posicion = str1.index("o")  # Devuelve la posicion si el valor existe en el String
print(posicion)

minusculas = concatenacion.lower()  # Convierte el String a Minusculas
print(minusculas)

mayusculas = concatenacion.upper()  # Convierte el String a Mayusculas
print(mayusculas)

title = concatenacion.title()  # Convierte la primera letra de cada palabra en Mayuscula
print(title)

capitalize = concatenacion.capitalize()  # Convierte la primera letra de la oracion en Mayuscula
print(capitalize)

ordenar =  sorted(str1)  # Ordena la lista segun su valor unicode
print(ordenar)

print("  hola  ".strip())   # Elimina espacios
print("  hola  ".lstrip())  # Elimina espacios al principio
print("  hola  ".rstrip())  # Elimina espacios al final

remplazo = concatenacion.replace("Mundo", "Python")  # Reemplaza valores en los Strings
print(remplazo)

union = ", ".join(["a", "b", "c"]) # Une datos en un String
print(union)

division = union.split(",")  # Dividir caracteres de un String en una lista
print(division)

formateo = "Python"  # Formatear datos en un String
print(f"Hola {formateo}" ) 

alphanumerico = str1.isalnum()  # Valida si la cadena es Alfanumerica
print(alphanumerico)

letras = str1.isalpha()  # Verifica si la cadena solo contiene letras
print(letras)

numeros = str1.isdigit()  # Verifica si la cadena solo contiene numeros
print(numeros)

minuscula = str1.islower()  # Verifica si la cadena solo contiene minusculas
print(minuscula)

mayuscula = str1.isupper()  # Verifica si la cadena solo contiene mayusuculas
print(mayuscula)

espacios = str1.isspace()  # Verifica si la cadena solo contiene espacios
print(espacios)

codificacion = "año"
bytes = codificacion.encode('utf8')  # Codifica los caracteres
codificacion = bytes.decode('utf8')  # Descodifica los caracteres
print(bytes)
print(codificacion)

invertir = str1[::-1]  # Invertir cadena
print(invertir) 




# Ejercicio: 

palabra1 = "mora"
palabra2 = "amora"

def es_palindromo(palabra):
    
    if palabra == palabra[::-1]:
        print(f"La palabra {palabra} es un palindromo")
    
    else:
        print(f"La palabra {palabra} no es un palindromo")
        
   
def es_anagrama(palabra1, palabra2):
       
    if sorted(palabra1) == sorted(palabra2):
        
        print(f"Las palabras {palabra1} y {palabra2} son anagramas")
    
    else: 
        
        print(f"Las palabras {palabra1} y {palabra2} no son anagramas")
                

def es_isograma(palabra):
    
    if len(palabra) == len(set(palabra)):
        
        print(f"La palabra {palabra} es un isograma")
        
    else:
            
        print(f"La palabra {palabra} no es un isograma")

es_palindromo(palabra1)
es_palindromo(palabra2)
es_anagrama(palabra1, palabra2)
es_isograma(palabra1)
es_isograma(palabra2)