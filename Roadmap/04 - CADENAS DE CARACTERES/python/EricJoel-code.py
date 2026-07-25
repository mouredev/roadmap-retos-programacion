# Cadenas de caracteres son secuencias de caracteres que se utilizan para representar texto en Python.

## Operaciones 

cadena1 = "Hola"
cadena2 = "Mundo"

# Concatenación
print(cadena1 + ", " + cadena2) 

# Repetición
print(cadena1 * 3)

#Indexación
print(cadena1[0])

#Longitud
print(len(cadena1))
print(len(cadena2))

#Slicing
print(cadena1[1:3]) # no incluye el índice final
print(cadena2[:3])  # desde el inicio hasta el índice 3 (no incluido)
print(cadena2[3:])  # desde el índice 3 hasta el final
print(cadena2[-1])  # último carácter
print(cadena2[-3:]) # últimos tres caracteres

#Busqueda
print(cadena1.find("o")) # índice de la primera ocurrencia de "o"
print(cadena2.find("x")) # devuelve -1 si no se encuentra

print("a" in cadena1) # True
print("x" in cadena2) # False

#Reemplazo
print(cadena1.replace("o", "a")) 
print(cadena2.replace("Mundo", "Python"))
print(cadena2) # la cadena original no cambia

#Division
print(cadena2.split("n")) # divide en una lista

#Conversion a mayusculas y minusculas
print(cadena1.upper())
print(cadena2.lower())

print("eric joel".title()) # Convierte a mayúscula la primera letra de cada palabra
print("eric joel".capitalize()) # Convierte a mayúscula la primera letra de la cadena

#Eliminacion de espacios al inicio y al final
print("  Hola Mundo  ".strip())
print("  Hola Mundo  ".strip() + "!!!") # Concatenación después de eliminar espacios para mostrar el efecto 
print("  Hola Mundo  ".lstrip() + "!!!") # Elimina espacios solo al inicio
print("  Hola Mundo  ".rstrip() + "!!!") # Elimina espacios solo al final

#Busqueda al principio y al final
print(cadena1.startswith("H"))
print(cadena1.startswith("o"))
print(cadena2.endswith("do"))
print(cadena2.endswith("x"))

#Busqueda de posiciones
print(cadena1.index("l")) # index encuentra la primera l de izquierda a derecha
print(cadena1.rindex("l")) # rindex encuentra la última l de derecha a izquierda 
#En este caso ambas devuelven 2 porque la primera l y la última l están en la misma posición

print("Eric Joel @ericcode".find("joel")) # find no distingue entre mayúsculas y minúsculas devuelve -1 
print("Eric Joel @ericcode".find("Joel"))

#Búsqueda de ocurrencias
print("Hola Hola Hola".count("Hola")) # cuenta cuántas veces aparece "Hola"
print("Hola Hola Hola".count("o"))    # cuenta cuántas veces aparece "o"

#Formateo de cadenas
nombre = "Eric"
edad = 30
print("Mi nombre es {} y tengo {} años".format(nombre, edad))

#Interpolacion
print(f"Mi nombre es {nombre} y tengo {edad} años")

#Transformacion en lista de caracteres
print(list(cadena1))

#Transformacion en cadena a partir de lista de caracteres
print(''.join(['H', 'o', 'l', 'a']))
lista = [cadena1, ",", cadena2, "!"]
print(''.join(lista))

#Transformaciones numericas
str_num = "12345"
str_num = int(str_num)
print(str_num)

str_num2 = "123.45"
str_num2 = float(str_num2)
print(str_num2)

#Combinaciones varias
str_num = "12345"
print(cadena1.isalpha()) # True si todos los caracteres son letras
print(cadena2.isdigit())  # True si todos los caracteres son dígitos
print(cadena1.isalnum())  # True si todos los caracteres son letras o dígitos
print("   ".isspace())    # True si todos los caracteres son espacios en blanco 
print(str_num.isnumeric()) # True si todos los caracteres son numéricos
print(cadena2.isidentifier()) # True si es un identificador válido en Python
print(str_num.isupper()) # True si todos los caracteres son mayúsculas como es numérico devuelve False
print(cadena1.islower()) # True si todos los caracteres son minúsculas
print(cadena1.istitle()) # True si cada palabra comienza con mayúscula y el resto son minúsculas


#Cadenas multilínea
cadena_multilinea = """Esta es una cadena
multilinea que ocupa varias lineas.
"""
print(cadena_multilinea)


#Extra
"""Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas"""

def palindormo():
    
    print("Verificador de palindromos")
    
    palabra = input("Ingrese una palabra o frase para verificar si es un palindromo: ")
    
    palabra = palabra.replace(" ", "").lower() # Elimina espacios y convierte a minúsculas  
    
    if palabra == palabra[::-1]: # Compara la palabra con su reverso
        print(f"{palabra} es un palindromo")
    else:
        print(f"{palabra} no es un palindromo")




def anagrama():
    
    print("Verificador de anagramas")
    
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    if sorted(palabra1) == sorted(palabra2): # Compara las palabras ordenadas alfabéticamente
        print(f"{palabra1} y {palabra2} son anagramas")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas")
        



def isograma():
    
    print("Verificador de isogramas")
    
    palabra = input("Ingrese una palabra para verificar si es un isograma: ")
    palabra = palabra.replace(" ", "").lower()
    
    if len(palabra) == len(set(palabra)): # Compara la longitud de la palabra con la longitud del conjunto de caracteres únicos
        print(f"{palabra} es un isograma")
    else:
        print(f"{palabra} no es un isograma")



def menu():
    print("1. Palindromo")
    print("2. Anagrama")
    print("3. Isograma")
    print("4. Salir")
    while True:
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            palindormo()
        elif opcion == "2":
            anagrama()
        elif opcion == "3":
            isograma()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
menu()