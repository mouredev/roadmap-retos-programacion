'''
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
'''
# Cadena vacía
cadena_vacía=""

# Cadenas simples
print("Cadena de texto")
print('Cadena de texto')
print("Cadena de 'texto'")

# Cadenas multilínea, tiene en cuenta el vacío tras las tres comillas mostrando una línea en blanco.
poema_Poe = """
Y el Cuervo nunca emprendió el vuelo.
Aún sigue posado, aún sigue posado
en el pálido busto de Palas.
en el dintel de la puerta de mi cuarto.
"""
print(poema_Poe)

# Encontrar la primera ocurrencia de alguna subcadena
print(poema_Poe.find("el"))
print(poema_Poe.index("el"))

# Contabilizar el número de veces que aparece una subcadena
print(poema_Poe.count("el"))

# Reemplazar elementos
print(poema_Poe.replace('posado', 'volando'))

# Separar textos por saltos de línea \n
print("Este texto sale en una línea \ny este en la segunda línea.")
print("Esto no pinta\nnada")

# Formato de cadena de texto sin procesar (raw string)
print(r"Esto no pinta\nada")

# Tabulador
print('Valor = \t40')

# Otra manera de mostrar comilla simple
print('Necesitamos \'escapar\' la comilla simple')

# Barra invertida
print ('Capítulo \\ Sección \\ Encabezado')

# Conversión
print(str(True))
print(str(10))

# Separadores a la hora de imprimir textos
msg1 = '¿Estás ahí?'
msg2 = 'No estoy.'
print(msg1, msg2) # por defecto la coma  hace un espacio
print(msg1, msg2, sep='|')
print(msg2, end='!!')

# Concatenación Unir cadenas de textos
proverb1 = 'Cuando el río suena'
proverb2 = 'agua lleva'
print(proverb1 + proverb2) #los une sin espacio
print(proverb1 + ', ' + proverb2)  # incluimos una coma

# May y min
print(proverb2.capitalize())  # La primera palabra comienza con mayúsculas
print(proverb2.title()) # Todas las palabras cominezan con mayúsculas
print(proverb2.upper()) # Todas las palabras con mayúsculas
print(proverb1.lower()) # Todas las palabras con minúsculas

# Repetir cadenas
reaction = 'Wow'
print(reaction * 4)

# Obtener un carácter
saludo = 'Hola, Mundo'
print(saludo[0]) # muestra un índice concreto
print(saludo[:]) # muestra todo
print(saludo[5:]) # muestra desde la posición 5, incluida
print(saludo[:6]) # muestra hasta la posición 6, incluida
print(saludo[0:3]) # muestra desde la 0 a la 3 incluidas
print(saludo[1:8:3]) # muestra [start:end:step] incluye el 1, excluye el 8 y salta de 3 en 3

# Longitud de la cadena
print(len(saludo))
print(len(cadena_vacía))

# Comprobar que una determinada subcadena se encuentra en una cadena de texto
print("Hola" in saludo)
print("Hola" not in saludo)

# Limpiar cadenas
texto_a_limpiar = "   -Hola mundo-   "
print (texto_a_limpiar)  
print(texto_a_limpiar.strip()) # solo limpia espacios, si empieza con algún símbolo o letra no los borra
print(texto_a_limpiar.lstrip()) #left
print(texto_a_limpiar.rstrip()) #right
print(texto_a_limpiar.strip("-"))  #funciona si está al principo o final
texto_a_limpiar2 = "-   Hola mundo   -"
print(texto_a_limpiar2.strip("-"))  #funciona si está al principo o final

# Empieza o termina por alguna subcadena
print(msg2.startswith("N"))
print(msg2.endswith("."))

# Identificando caracteres
print('R2D2'.isalnum()) # Detectar si todos los caracteres son letras o números
print('C3-PO'.isalnum())
print('314'.isnumeric()) # Detectar si todos los caracteres son números
print('3.14'.isnumeric())
print('abc'.isalpha()) # Detectar si todos los caracteres son letras
print('BIG'.isupper()) # Detectar mayúsculas/minúsculas
print('BIG'.islower()) 
print('Primera Instancia'.istitle())

# Formato
x = 10
print(f'La variable x es = {x}')
print("La variable x es =", x)
print('La variable x es = {}'.format(x))

# Caracteres Unicode
# Fuente: https://symbl.cc/en/unicode/blocks/
rocket_code = 0x1F680
rocket = chr(rocket_code) # La función chr() permite representar un carácter a partir de su código
print (rocket) # cohete

rocket_code = hex(ord(rocket))
print(rocket_code) # La función ord() permite obtener el código (decimal) de un carácter a partir de su representación

print('\N{ROCKET}') #El modificador \N permite representar un carácter a partir de su nombre
print('\N{SNAKE}')


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''

palabra_a_comprobar= ""
palabras_a_comprobar= ""
palabras_a_comprobar2= ""

# Palíndromo, misma palabra que se lee igual al derecho que al revés
def palindromo (palabra_a_comprobar):
    inverso= palabra_a_comprobar[::-1] # Invierto un str
    inverso2 = ''.join(reversed(palabra_a_comprobar)) # Otra forma
    #print(palabra_a_comprobar, inverso, inverso2)
    if palabra_a_comprobar.lower() == inverso.lower():
        print(palabra_a_comprobar, " es un palíndromo.")
        menu()
    else:
        print("Prueba con otra cosa, no lo es.")
        menu()

# Anagrama, dos palabras que se leen igual al derecho que al revés
def anagrama (palabras_a_comprobar, palabras_a_comprobar2):
    ordenado2=sorted(palabras_a_comprobar.lower())  # Devuelve una lista de caracteres ordenados alfabéticamente
    ordenado3=sorted(palabras_a_comprobar2.lower())
    if ordenado2 == ordenado3:  
        print(f"Las palabras {palabras_a_comprobar} y {palabras_a_comprobar2}, son un anagrama.")
        menu()
    else:
        print("Prueba con otra cosa, no lo son.")
        menu()

# Isograma, una palabra o frase en la que no hay letras repetidas
def isograma (palabra_a_comprobar):
    if len(set(palabra_a_comprobar.lower())) == len(palabra_a_comprobar.lower()):  
        # al convertirlo en set elimina lo duplicado y si el largo sigue siendo el mismo, lo es
        print(palabra_a_comprobar, " es un palíndromo.")
        menu()
    else:
        print("Prueba con otra cosa, no lo es.")
        menu()

def menu():
    opcion = input ("1. Comprobar palíndromo\n2. Comprobar Anagrama\n3. Comprobar isograma\n4. Salir\nElige una opción:")

    if opcion == "1":
        palabra_a_comprobar= input("Introduce una palabra para comprobar:")
        print ("Has introducido:", palabra_a_comprobar)
        palindromo(palabra_a_comprobar)
    elif opcion == "2":
        palabras_a_comprobar= input("Introduce una palabra para comprobar:")
        palabras_a_comprobar2= input("Introduce otra palabra para comprobar:")
        print ("Has introducido:", palabras_a_comprobar,"y", palabras_a_comprobar2)
        anagrama (palabras_a_comprobar, palabras_a_comprobar2)
    elif opcion == "3":
        palabra_a_comprobar= input("Introduce una palabra para comprobar:")
        print ("Has introducido:", palabra_a_comprobar)
        isograma(palabra_a_comprobar)
    else:
        print ("¡Hasta luego cocodrilo!")
        quit()

menu()
