"""
Vamos con las cadenas de carácteres
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 """

import os #importamos la libreria del sistema para poder hacer uso del bash
import textwrap
def limpiar(): #creamos la función para limpiar la pantalla para poder aplicarla las veces que necesitemos sin repetir código
    while True:

        pregunta=input("quieres que limpie la pantalla? (si - no): ")
        if pregunta=="si":
        
            if os.name=="posix":
                os.system("clear")
                break
            else:
                os.system("cls")
                break
        elif pregunta=="no":
            break
    
#Pregunto si limpio la consola

limpiar()


#CREO LA VARIABLE CON LA CADENA DE TEXTO

cadena_texto="Acceso a caracteres específicos, subcadenas, longitud, concatenación,"\
     "repetición, recorrido, conversión a mayúsculas y minúsculas, reemplazo, división,"\
     "unión, interpolación, verificación...\n"

print(cadena_texto)

# 1. Longitud de la Cadena

print("#1. LONGITUD DE LA CADENA")
print(len(cadena_texto))
print("\n")

# 2. Acceso a caracteres específicos

print("#2. ACCESO A UN CARÁCTER\n")
print("Vamos acceder a un punto concreto del indice de la cadena. Vamos a pedir que posición quiere el usuario\n")
while True:
    try:
        pregunta=int(input("dame el número del indice en la cadena anterior para mostrar el carácter: "))
        if pregunta<0 or pregunta>= len(cadena_texto):
            raise IndexError
        break
    except ValueError:
        print("\n")
        print("ERROR. Ingresa un valor entero")
    except IndexError:
        print("ERROR. Has puesto un valor fuera del rango de la cadena")

print(f"el carácter es el: {cadena_texto[pregunta]}\n")

# 3. Acceso a subcadenas (slicing)

print("#3. ACCESO A SUBCADENAS (SLICING)\n")
while True:
    try:
        inicio=int(input("ingresa el número de inicio del indice la cadena: \n"))
        final=int(input("ingresa el final del indice de la cadena: \n"))
        if inicio>final:
            print("el primer valor a de ser inferior al segundo\n")
            continue
        break
    except ValueError:
        print("\n")
        print("ERROR. Ingresa un valor entero")
    

print(f"la cadena resultante es: {cadena_texto[inicio:final]}\n")

# 4. Concatenación

print("#4. CONCATENACIÓN")

while True:
    try:
        print("Vamos a concatenar dos candenas\n")
        print("antes decide que tipo de concatenació:\n")
        print("1- enganchar dos palabras como una compuesta\n")
        print("2- concatenar dos palabras individuales con espacio entre ellas\n")
        opcion=int(input("Que opción quieres: \n"))
    except ValueError:
        print("\n")
        print("ERROR. Ingresa un valor entero")
    if opcion==1:
        print("has escogido la opción 1\n")
        primera_cadena=input("escribe la primera cadena :")
        segunda_cadena=input("escribe la segunda cadena: ")
        print("la concatenación es: ")
        print(primera_cadena + segunda_cadena)
        break
    elif opcion==2:
        print("has escogido la opción 2")
        primera_cadena=input("escribe la primera cadena :")
        segunda_cadena=input("escribe la segunda cadena: ")
        print("la concatenación es: ")
        print(primera_cadena + " " + segunda_cadena)
        break
    elif opcion<0 and opcion>1:
        print("ERROR. Introduce 1 o 2\n")

# 5. Repetición de Cadenas. Se trata de repetir la cadena las veces que le indiques

print("\n#5. REPETICIÓN DE CADENAS\n")
print("Vamos a realizar una repetición de la misma cadena, tantas veces le indiques\n")
while True:
    frase=input("dime la cadena a repetir: \n")
    try:
        repeticion=int(input("indica las veces que se ha de repetir la cadena: "))
        cadena=frase*repeticion
        print(cadena+"\n")
        break
    except ValueError:
        print("ERROR. Ingresa un valor entero")
        
# 6. Conversión a Mayúsculas y Minúsculas

print("\n#6. CONVERSIÓN A MAYÚSCULAS Y MINÚSCULAS\n")
print("Empezamos con la conversión de minúsculas a mayúsculas\n")
frase=input("dime la frase: ")
frase2=frase.upper()
print("\n"+frase2+"\n")

print("Empezamos con la conversión de mayúsculsa a minúsculas\n")
frase=input("dime la frase: ")
frase2=frase.lower()
print("\n"+frase2)

# 7. Recorrido por la cadena
print("\n#7. RECORRIDO POR LA CADENA\n")
print(f"cogeremos la frase inicial: {cadena_texto}\n")
print("vamos a imprimir carácter a carácter separado cada uno del otro, haciendo una iteración por toda la cadena\n")
print("para eso, luego vamos a usar la función print(cadena, end=\" \"). Con el parámetro end añadimos despues del string un carácter o espacio")
for i in cadena_texto:
    print(i,end=" ")
print("\n")

# 8. Reemplazo de Subcadenas
print("#8. REEMPLAZO DE SUBCADENAS\n")
cadena=input("que cadena es la muestra donde vamos a realizar el cambio: ")
antigua=input("\nindicame la cadena que quieres substituir: ")
nueva=input("\nindicame la cadena nueva: ")
cadena=cadena.replace(antigua,nueva)
print(f"\nLa cadena ha quedado así: {cadena}\n")

# 9. División de Cadenas
print("\n#9. División de Cadenas\n")
print("Vamos a proceder a realizar una división de una cadena. Lo realizaremos con la función .split()")
cadena=input("pasame la cadena para después dividirla: ")
lista_cadenas=cadena.split()
print("\nHemos creado una lista con las cadenas divididas por un espacio (frases).\
       Si quieres separar por un indicador se ha de proceder indicandolo\n")
print(f"la lista es: {lista_cadenas}")
print("\nAhora vamos a indicar también cual será el separador\n")
separador=input("dame el separador: ")
lista_cadenas2=cadena.split(separador)
print(f"La lista es: {lista_cadenas2}")

# 10. Unión de cadenas
print("# 10. UNIÓN DE CADENAS\n")
print("Esta función (.join()) hace la función inversa a la .splint()\n")
print(f"Vamos a usar la lista anterior que hemos creado: {lista_cadenas}\n")
cadena_nueva=" ".join(lista_cadenas)
print(cadena_nueva)

# 11. Interpolación de cadenas
print("\n# 11. INTERPOLACIÓN DE CADENAS\n")
print("Tenemos diferentes sistemas de interpolación, el más habitual es el F-strings:\n")
print("1. F-strings: print(f\"cadena {variable})\n")
print("2. Str.format()\n")
print("inciamos con la F-str")
frase1=input("dame la primera frase: \n")
frase2=input("dame la segunda frase: \n")
print(f"vamos a añadir al print la primera frase: ({frase1}) y la segunda frase: ({frase2})\n") #usamos la F-Str para introducir cadenas
print("vamos a usar el .format(). Requiere que introduzca los datos según lo siguiente:\n") 
print("variable=\"estoy en {cadena1\} y quiero ir a {cadena2\}.format(cadena1=\"STR\",cadena2=\"STR\")\n")
print("luego imprimimos con un print la variable")
cadena1=input("dame la primera cadena que ha de ser el nombre de una ciudad: \n")
cadena2=input("dame la segunda cadena que ha de ser el nombre de otra ciudad: \n")
mensaje="estoy en {frase1} y quiero ir a {frase2}".format(frase1=cadena1,frase2=cadena2) # usamos la función .format
print(mensaje+"\n")

# 12. VERIFICACIÓN DE PROPIEDADES DE CADENAS
print("# 12. VERIFICACIÓN DE PROPIEDADES DE CADENAS\n")
print("Tipos de verificación: \n")

#Verifico si la cadena es de caracter alfabéticos
print("1. Verifica si los carácteres son letras con la función .isalpha()\n")
cadena=input("introduce una palabra (no una frase o dará error) para verificar si son letras: ") 
verifica=cadena.isalpha()       #compruebo si los carácteres son alfabeto, y si es cierto devuelvo True
if verifica==True:
    print("son carácteres alfabéticos\n")
else:
    print("no es una cadena de carácteres alfabéticos\n")

#si es una frase genero una lista separando las palabras con un .split() y luego lo proceso
print("puedo comprobar si se usa una frase, palabra a palabra. Para eso usaré un bucle y la función all()\n")
cadena=input("introduce una frase para verificar si son letras: ")
frase=cadena.split()
alphabet=all(caracter.isalpha() for caracter in frase)
if alphabet:
    print("son caracteres alfabéticos\n")
else:
    print("no todos son carácteres alfabéticos\n")

#Verifico si la cadena es alfanumérica
print("2. Verifica si los carácteres son alfanuméricos con la función .isalnum()\n")
frase=input("introduce la cadena: \n")
verifica=frase.isalnum()        #realizo la compovación de si los carácteres son alfanumérico
if verifica:
    print("son alfanuméricos\n")
else:
    print("no son alfanuméricos\n")

#vuelvo a separar en una lista mediante un .split()
frase=input("escribe la frase alfanumérica a identificar: \n")
lista=frase.split()
numeros=all(num.isalnum() for num in lista)
if numeros:
    print("todos son alfanúmericos\n")
else:
    print("no todos son alfanúmericos")

#Verifico si la cadena es numérica
print("3. Verifica si los carácteres son numéricos con la función .isdigit()\n")
frase=input("introduce la cadena: \n")
verifica=frase.isdigit()        #realizo la compovación de si los carácteres son numéricos
if verifica:
    print("son numéricos\n")
else:
    print("no son numéricos\n")

#vuelvo a separar en una lista mediante un .split()
frase=input("introduce la cadena separada por espacios\n")
lista=frase.split()
numeros=all(num.isdigit() for num in lista)
if numeros:
    print("todos son números\n")
else:
    print("no todos son números")

#Verifico si la cadena es un espacio en blanco
print("4. Verifica si la cadena es un espacio en blanco con la función .isspace()\n")
frase=input("introduce la cadena: \n")
verifica=frase.isspace()        #realizo la compovación de si es un espacio en blanco
if verifica:
    print("es un espacio en blanco\n")
else:
    print("no es un espacio en blanco\n")

# EJERCICIOS DIFICULTAD EXTRA

#Palíndromos
limpiar() #Iniciamos limpiando la pantalla si el usuario nos lo indica
print("#######################")
print("#                     #")
print("#     PALÍNDROMOS     #")
print("#                     #")
print("#######################")
texto=(
    "Un palíndromo es una palabra, frase, número o cualquier otra secuencia de caracteres"
    "que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando los espacios,"
    "la puntuación y la acentuación. Es decir, su orden se mantiene al revés, lo cual hace que se" 
    "pueda leer de forma idéntica en ambas direcciones."
)
paragrafo=textwrap.fill(texto,80)
print("\n"+paragrafo+"\n")
frase=input("introduce el palíndromo: ")
frase=frase.replace(" ","").lower() #ponemos todos los carácteres en minúsculas y quitamos posibles espacios
palindromo=frase
frase=list(frase)
palindromo=list(palindromo)
palindromo.reverse()
palCert=True
for i in range(len(frase)):
    if frase[i] != palindromo[i]: 
        palCert=False
        break
if palCert:
    print("\nES UN PALÍNDROMO\n")
else:
    print("\nNO ES UN PALÍNDROMO\n")

# ANAGRAMA

limpiar()

print("#################")
print("#               #")
print("#   ANAGRAMA    #")
print("#               #")
print("#################")

texto=(
    "Un anagrama es una palabra o frase formada al reorganizar"
     "las letras de otra palabra o frase, usando todas las letras" 
     "una sola vez. Por ejemplo, \"amor\" es un anagrama de \"Roma\""
)
paragrafo=textwrap.fill(texto,80)
print("\n"+paragrafo+"\n")
print("\nVamos a introducir dos frases y comprobar si la segunda es un anagrama de la segunda\n")
print(textwrap.fill("No se verificará si la frase tiene coherencia o sentido lingüístico, únicamente se evaluará si las letras se reorganizan correctamente en un anagrama",80))

# iniciamos la petición de las frases
while True:    
    primera_frase=input("\nintroduce la primera frase: ")
    anagrama=input("\nintroduce la segunda frase. El anagrama: ")

    primera_frase=primera_frase.replace(" ","").lower() #ponemos en minúsculas los carácteres y quitamos los espacios
    anagrama=anagrama.replace(" ","").lower() #ponemos en minúsculas los carácteres y quitamos los espacios

    # comprobamos que la longitud de las dos cadenas sean iguales
    if len(primera_frase)==len(anagrama):
        break
    else:
        print("\nERROR. Introduce frases del mismo tamaño\n")

#ordenamos las cadenas convirtiendolas en listas ordenadas
primera_frase=sorted(primera_frase)
anagrama=sorted(anagrama)

if primera_frase==anagrama:
    print("\nEs un anagrama\n")
else:
    print("\nNo es un anagrama\n")

# ISOGRAMA

# ANAGRAMA

limpiar()

print("#################")
print("#               #")
print("#    ISOGRAMA   #")
print("#               #")
print("#################")

texto=(
    "Un isograma es una palabra o frase en la que ninguna letra se repite." 
    "Cada letra aparece solo una vez, sin importar si son mayúsculas o minúsculas." 
    "Un ejemplo de isograma es la palabra \"murciélago\", ya que todas sus letras son diferentes."
)

print(textwrap.fill(texto,80))

# Iniciamos con la introducción de la frase
frase=input("introduce la frase a analizar: \n")
frase=frase.replace(" ","").lower()  # quito espacios y lo paso todo a minúsculas para evitar errores en la comparación
isograma=set()
lista=list(frase)

# Iniciamos unta iteración por la lista creada de la frase introducida y añadimos los carácteres en el set()
for car in lista:
    isograma.add(car)
if len(lista)==len(isograma):
    print("\nEs un ISOGRAMA\n")
else:
    print("\nNo es un ISOGRAMA\n")