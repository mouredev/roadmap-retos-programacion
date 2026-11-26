"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 """

# Creacion de cadenas de caracteres: pueden ser con 3 tipos de comillas: simples, dobles o triples. Las triples permiten crear 
# cadenas multilínea.
print("1. Creación de cadenas de caracteres:")
nombre = "Sergio"
apellido = 'García'
mensaje = """Hola me llamo Sergio García 
y estoy aprendiendo Python"""

# Conversion de datos a otros tipos:
print("2. Conversión de datos a otros tipos:")
edad = 29
print(edad)
print(type(edad))
texto_edad = str(edad) # Convertimos la edad a cadena de caracteres
print(texto_edad)
print(type(texto_edad))

decimal = 3.1416
print(decimal)
print(type(decimal))

decimal_texto = str(decimal) # Convertimos el decimal a cadena de caracteres
print(decimal_texto)
print(type(decimal_texto))

#Acceso a caracteres específicos:
print("3. Acceso a caracteres específicos:")

ejemplo_1 = "Persona"
print(ejemplo_1)  # Muestra la cadena completa
print(ejemplo_1[0])  # Acceso al primer carácter
print(len(ejemplo_1))  # Longitud de la cadena

print(ejemplo_1[-1])  # Acceso al último carácter
print(ejemplo_1[-2])  # Acceso al penúltimo carácter

print("4. Acceso a subcadenas (slicing):") # cadena[inicio:fin:paso], el final no se incluye, el paso es opcional y por defecto es 1.
print(ejemplo_1[:4]) #Desde el inicio hasta el índice 4 (sin incluirlo)
print(ejemplo_1[2:5])  # Acceso a una subcadena
print(ejemplo_1[-1:3:-1])  # Acceso a una subcadena en orden inverso ejemplo_1(desde el final(-1), hasta el índice 3, en reversa (-1))
print(ejemplo_1[::2])  # Acceso a caracteres en posiciones pares
print(ejemplo_1[1:])    #Hasta el final desde el índice 1

print("5. Copiar una cadena:")
ejemplo_2 = ejemplo_1[:]  # Copia la cadena
print(ejemplo_2)
ejemplo_3 = ejemplo_1[1:5]  # Copia una subcadena 
print(ejemplo_3)

print("6 Longitud de la cadena:")
print(len(ejemplo_1))  # Longitud de la cadena
print(len(ejemplo_3))  # Longitud de la subcadena copiada
ejemplo_4 = "Hola Mundo!"
print(len(ejemplo_4))  # Longitud cuenta espacios

print("7. Concatenación de cadenas:")
saludo = "Hola"
nombre = "Sergio"
mensaje = saludo + ", me llamo " + nombre + "." #La concatenación se hace con el operador + y se deben ubicar los espacios manualmente
mensaje_2 = f"{saludo}, me llamo {nombre}." #La concatenación se hace con f-strings y se ubican los espacios automáticamente
print(mensaje)
print(mensaje_2)
print("Hola",saludo,", me llamo",nombre,".") #La concatenación se puede hacer con comas pero no se puede usar +. Ademas los espacios se ubican automáticamente.

print("8. Repetición de cadenas:")
print(ejemplo_1 * 4)  # Repite la cadena 4 veces unidas y sin saltos de linea

print("9. Pertenencia:") #Verificar que algo existe dentro(in) o no(!in) dentro de una cadena de caracteres
ejemplo_5 = "Python"
print("P" in ejemplo_5)  # Verifica si 'P' está en la cadena
print("Pyth" in ejemplo_5)  # Verifica si 'Pyth' está en la cadena
print("taza" in ejemplo_5)  # Verifica si 'taza' está en la cadena
print("ton" in ejemplo_5)  # Verifica si 'ton' está en la cadena

print("taza" not in ejemplo_5)  # Verifica si 'taza' no está en la cadena
print("ton" not in ejemplo_5)  # Verifica si 'ton' no está en la cadena

print("10. Recorrido de cadenas:")

ejemplo_6 = "parangaricutirimícuaro"

for caracter in ejemplo_6:
    print(caracter)  # Imprime cada carácter en una línea separada

print("")
for caracter in ejemplo_6:
    print(caracter, end="")  # Imprime cada carácter en la misma línea

print("")
for i, letra in enumerate(ejemplo_6):
    print(i, letra)  # Imprime cada carácter separado por un guion

print("11. Comparación :")
print("Python" == "python")  # Comparación de igualdad (sensible a mayúsculas y minúsculas)
print("abc" == "ABC")
print("abc" != "ABC")   #Comparación de desigualdad (sensible a mayúsculas y minúsculas)
print("abc" < "ABC")    #Comparación de orden lexicográfico (sensible a mayúsculas y minúsculas)
print("abc" > "ABC")
print("Ana" < "Juan")

print("12. Conversión a mayúsculas y minúsculas:")
ejemplo_7 = "Hellriser"
mensaje_3 = "Hola, me llamo Sergio Menchaca y estoy aprendiendo Python"
print("Mayúsculas:", ejemplo_7.upper())  # Convierte a mayúsculas
print("Minúsculas:", ejemplo_7.lower())  # Convierte a minúsculas
print("Primer letra mayúscula:", ejemplo_7.capitalize())  # Convierte la primera letra a mayúscula
print("Cada palabra con mayúscula:", mensaje_3.title())  # Convierte la primera letra de cada palabra a mayúscula
print("Cambiar caso de las letras:", "PyThOn".swapcase())

print("13. Eliminar espacios:")
print("   Hola   ".strip())  # Elimina espacios al inicio y al final
print("   Hola   ".lstrip())  # Elimina espacios al inicio
print("   Hola   ".rstrip())  # Elimina espacios al final

print("14. Buscar texto")
ejemplo_8 = "Hola, me llamo Sergio Menchaca y estoy aprendiendo Python"
print(ejemplo_8.find("Sergio"))  # Devuelve el índice de la primera aparición de "Sergio"
print(ejemplo_8.find("Python"))  # Devuelve el índice de la primera aparición de "Python"
print(ejemplo_8.find("Java"))  # Devuelve -1 si no se encuentra la subcadena
print(ejemplo_8.index("Sergio"))  # Devuelve el índice de la primera aparición de "Sergio", pero lanza error si no lo encuentra

ejemplo_9 = "Banana"
print(ejemplo_9.find("ana"))  # Devuelve el índice de la primera aparición de "ana"
print(ejemplo_9.find("a"))  # Devuelve el índice de la última aparición de "a"

print("15. Reemplazar texto:")
ejemplo_10 = "Hola, me llamo Sergio Menchaca y estoy aprendiendo Python"
print(ejemplo_10.replace("Sergio", "María"))  # Reemplaza "Sergio" por "María"
print(ejemplo_10.replace("Python", "Java"))  # Reemplaza "Python" por "Java"
ejemplo_11 = "a-a-a-a-a-a-a-a"
print(ejemplo_11.replace("a", "c", 3))  # Reemplaza las primeras 3 apariciones de "a" por "c"

print("16. Dividir cadenas:")
ejemplo_12 = "Joel,Sergio,María,Juan"
lista = ejemplo_12.split(",")  # Divide la cadena en una lista usando la coma como separador
print(lista)

ejemplo_13 = "Joel Sergio María Juan" #Sin separador, por lo que se divide por espacios
print(ejemplo_13.split())  # Divide la cadena en una lista usando el espacio como separador

print("17. Unir cadenas:")
nombres = ["Joel", "Sergio", "María", "Juan"]
resultado = ", ".join(nombres)  # Une la lista en una cadena usando la coma y el espacio como separador
print(resultado)

print("18. Interpolación de cadenas(f-strings):")
nombre = "Sergio"
edad = 30
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
print(f" 2 + 2 = {2 + 2}")  # Se pueden realizar operaciones dentro de las llaves
print("Verificación de cadenas:")


print("19. Verificación de cadenas:")
print("PowerRangers".isalpha())  # Verifica si todos los caracteres son letras == True
print("PowerRangers6".isalpha())  # Verifica si todos los caracteres son letras == False

print("123".isdigit())  # Verifica si todos los caracteres son dígitos == True
print("123a".isdigit())  # Verifica si todos los caracteres son dígitos == False

print("PowerRangers".isalnum())  # Verifica si todos los caracteres son alfanuméricos == True
print("PowerRangers6".isalnum())  # Verifica si todos los caracteres son alfanuméricos == True

print("PowerRangers".islower())  # Verifica si todos los caracteres son minúsculas == False
print("powerrangers".islower())  # Verifica si todos los caracteres son min

print("PowerRangers".isupper())  # Verifica si todos los caracteres son mayúsculas == False
print("POWERRANGERS".isupper())  # Verifica si todos los caracteres son mayúsculas == True

print("   ".isspace())  # Verifica si todos los caracteres son espacios == True

print("20. Verificación de inicio y fin de cadenas:")

ejemplo_14 = "Manjaro Linux"
print(ejemplo_14.startswith("Man"))  # Verifica si la cadena empieza con "Man" == True
print(ejemplo_14.endswith("nux"))  # Verifica si la cadena termina con "nux" == True

print("21. Alineacion de cadenas:")

print("Hola".center(20))  # Centra la cadena en un ancho de 20 caracteres
print("Hola".center(20, "-"))  # Centra la cadena en un ancho de 20 caracteres y rellena con guiones "-"
print("Hola".ljust(20))  # Alinea la cadena a la izquierda en un ancho de 20 caracteres
print("Hola".rjust(20))  # Alinea la cadena a la derecha

print("22. Rellenar con ceros:")
print("17".zfill(5))  # Rellena la cadena con ceros a la izquierda hasta un ancho de 5 caracteres

print("23. Contar apariciones de un carácter o subcadena:")

ejemplo_15 = "Nombre: Sergio Menchaca"
print(ejemplo_15.partition(":"))  # Divide la cadena en una tupla de 3 elementos: antes del separador, el separador y después del separador

print("24. Separar por lineas:")

ejemplo_16 = """Hola Mundo, 
me llamo Sergio Menchaca
y estoy aprendiendo Python"""

print(ejemplo_16.splitlines())  # Separa la cadena por líneas

print("25. Codificación y decodificación de cadenas:")

ejemplo_17 = "Hola Mundo"
# Codificación a bytes
bytes_codificados = ejemplo_17.encode('utf-8')
print(bytes_codificados)  # Muestra los bytes codificados

# Decodificación de bytes a cadena
cadena_decodificada = bytes_codificados.decode('utf-8')
print(cadena_decodificada)  # Muestra la cadena decodificada

print("26. Escapar caracteres especiales:")
ejemplo_18 = "Hola\nMundo\tPython"
print(ejemplo_18)  # Muestra la cadena con caracteres especiales interpretados
"""
Otros escapes:
\n  # salto de línea
\t  # tabulación
\\  # barra invertida
\"  # comilla doble
\'  # comilla simple
"""
print("27. Cadenas inmutables:")
ejemplo_19 = "Python"
#ejemplo_19[0] = "h"  # Esto generará un error porque las cadenas son inmutables

# Pero se puede crear una nueva cadena a partir de la original
ejemplo_20 = "h" + ejemplo_19[1:]  # Crea una nueva cadena con la primera letra cambiada
print(ejemplo_20)  # Muestra la nueva cadena

"""
Las 10 operaciones más importantes con cadenas de caracteres son:
1. Indexación []
2. Slicing [:]
3. len()
4. in
5. for
6. split()
7. join()
8. replace()
9. strip()
10. f-strings
"""

"""
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos: palabras que se leen igual de izquierda a derecha y de derecha a izquierda
 * - Anagramas: palabras que contienen las mismas letras pero en diferente orden
 * - Isogramas: palabras que no contienen letras repetidas
 */
"""

palabra_1 = input("Ingresa la primera palabra: ")
palabra_2 = input("Ingresa la segunda palabra: ")

# Comprobación de palíndromos:
if palabra_1 == palabra_2[::-1]:    # Si la primera palabra es igual al inverso de la segunda palabra, entonces son palíndromos
    print(f"{palabra_1} es un palíndromo de {palabra_2}")   
else:
    print(f"{palabra_1} NO es un palíndromo de {palabra_2}")

# Comprobación de anagramas:
if sorted(palabra_1) == sorted(palabra_2):  # Si la primera palabra ordenada alfabéticamente es igual a la segunda palabra ordenada alfabéticamente, entonces son anagramas
    print(f"{palabra_1} es un anagrama de {palabra_2}")
else:
    print(f"{palabra_1} NO es un anagrama de {palabra_2}")

# Comprobación de isogramas:
if len(set(palabra_1)) == len(palabra_1):   # Si hacemos un set(No se permiten elementos duplicados) de la palabra y comparamos su longitud con la longitud de la palabra original, entonces es un isograma.
    print(f"{palabra_1} es un isograma")
else:
    print(f"{palabra_1} NO es un isograma")

if len(set(palabra_2)) == len(palabra_2):   # Si hacemos un set(No se permiten elementos duplicados) de la palabra y comparamos su longitud con la longitud de la palabra original, entonces es un isograma.
    print(f"{palabra_2} es un isograma")
else:
    print(f"{palabra_2} NO es un isograma")