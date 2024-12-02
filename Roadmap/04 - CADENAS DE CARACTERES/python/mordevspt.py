"""
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""
# Cadena - String
mi_cadena = "En un lugar de la mancha"
print(f"Cadena a recorrer: {mi_cadena}")

# INDEXACIÓN - Acceso a caracteres específicos
print("\nINDEXACIÓN\n")
print(f"Posición 10 (mi_cadena[10]): {mi_cadena[10]}")

# Subcadenas
print("\nSUBCADENAS\n")
print(f"Posiciones 6 a 10 (mi_cadena[6:10]): {mi_cadena[6:10]}")
print(f"Primeros 10 catracteres (mi_cadena[:10]): {mi_cadena[:10]}")
print(f"Últimos 10 catracteres mi_cadena[10:]: {mi_cadena[10:]}")
print(f"Último caracter de la cadena (mi_cadena[-1]): {mi_cadena[-1]}")

# Saber si una subcadena está en otra cadena
print("\nSaber si una subcadena está en otra cadena\n")
mi_subcadena1 = "mancha"
mi_subcadena2 = "coche"
print(f"Subcadenas: \n\n- mi_subcadena1: {mi_subcadena1}\n- mi_subcadena2: {mi_subcadena2}")

# Búsqueda de posición
print("\nBÚSQUEDA DE POSICIÓN\n")

# Método In devuelve True o False
print("\nMÉTODO IN\n")
print(f"In (mi_subcadena1 in mi_cadena): {mi_subcadena1 in mi_cadena}")
print(f"In (mi_subcadena2 in mi_cadena): {mi_subcadena2 in mi_cadena}")

# Método Find - Devuelve el índice donde empieza la subcadena dentro de la cadena o -1 si no la encuentra
# Devuelve la primera ocurriencia
print("\nMETODO FIND\n")
print(f"Find (mi_cadena.find(mi_subcadena1)): {mi_cadena.find(mi_subcadena1)}")
print(f"Find (mi_cadena.find(mi_subcadena2)): {mi_cadena.find(mi_subcadena2)}")

# Búsqueda de ocurrencias
print("\nBUSCAR OCURRENCIAS\n")
print(f"Cuantas veces aparece una subcadena (mi_cadena.count('a')): {mi_cadena.count("a")}")

# Buscar por el principio o el final
print("\nBUSCAR PRINCIPIO / FINAL\n")
print(f"Principio (mi_cadena.startswith('mancha')): {mi_cadena.startswith("mancha")}")
print(f"Principio (mi_cadena.startswith('En')): {mi_cadena.startswith("En")}")
print(f"Final (mi_cadena.endswith('mancha')): {mi_cadena.endswith("mancha")}")
print(f"Final (mi_cadena.endswith('En')): {mi_cadena.endswith("En")}")

# Longitud
print("\nLONGITUD\n")
print(f"Longitud total (len(mi_cadena)): {len(mi_cadena)}")

# División
print("\nDIVISIÓN\n")
print(f"División (mi_cadena.split()): {mi_cadena.split()}")
print(f"División por alguna de las letras (mi_cadena.split('a')): {mi_cadena.split("a")}")

# Concatenación
print("\nCONCATENACIÓN\n")
print(f"Concatenamos las subcadenas (mi_subcadena1+mi_subcadena2): {mi_subcadena1+mi_subcadena2}")

# Repetición
print("\nREPETICIÓN\n")
repetirCadena= 5
print(f"Repetición de la cadena por una cantidad: {mi_cadena*repetirCadena}")

# Recorrido
print("\nRECORRIDO\n")
print(f"Recorrer de principo a fin (mi_cadena[0::]): {mi_cadena[0::]}")
print(f"Recorrer en saltos de 3 (mi_cadena[::3]): {mi_cadena[::3]}")
print(f"Invertir cadena (mi_cadena[::-1]): {mi_cadena[::-1]}")
print(f"Saltos de dos en dos (mi_cadena[::2]): {mi_cadena[::2]}")

# Conversión a mayúsculas y minúsculas
print("\nCONVERSIÓN A MAYÚSCULAS Y MINÚSCULAS\n")
print(f"Minúsculas (mi_cadena.lower()): {mi_cadena.lower()}")
print(f"Mayúsculas (mi_cadena.upper()): {mi_cadena.upper()}")
print(f"Cambiar mayúsculas a minúsculas y viceversa (mi_cadena.swapcase()): {mi_cadena.swapcase()}")
print(f"Letra capital (mi_cadena.capitalize()): {mi_cadena.capitalize()}")
print(f"Título (mi_cadena.title()): {mi_cadena.title()}")

# Reemplazo 
print("\nREEMPLAZO\n")
print(f"mi_cadena.replace('mancha','llanura'): {mi_cadena.replace("mancha","llanura")}")

# Unión
print("\nUNIÓN\n")
print(f"Unión de las subcadenas mi_subcadena1 + ' ' + mi_subcadena2: {mi_subcadena1 + " " + mi_subcadena2}")

# Eliminar espacios al principio y al final
print("\nELIMINAR ESPACIOS\n")
mi_cadenaConEspacios = " empiezo con espacios y termino con espacios "
print(f"'{mi_cadenaConEspacios}'")
print(f"Eliminar espacios (mi_cadenaConEspacios.strip()): '{mi_cadenaConEspacios.strip()}'")

# Interpolación 
print("\nINTERPOLACION")

# Variables
a = 2001
b = "Hola"
c = "Python"
d = True
e = 3.14

# Módulos %
print("\nMODULOS\n")
# %d = Integer
# %f = Float
# %s = String
# %x = Hexadecimal
# %o = Octal

print("%d + 1000 = 3001" % (a))
print("%s es una web desarrollada en %s" % ("Reflex", c))
print("[%d, %s, %s, %s, %f]" % (a, b, c, d, e))
print("¡%s! Mi lenguaje de programación favorito es %s" % (b, c))
print("El valor de PI o π: %f" % (e))

print("\nFORMAT\n")
print("{} + 1000 = 3001".format(a))
print("{} es una web desarrollada en {}".format("Reflex", c))
print("[{}, {}, {}, {}, {}]".format(a, b, c, d, e))
print("¡{}! Mi lenguaje de programación favorito es {}".format(b, c))
print("El valor de PI o π: {}".format(e))

print("\nF\n")
print(f"{a} + 1000 = 3001")
print(f"Reflex es una web desarrollada en {c}")
print(f"[{a}, {b}, {c}, {d}, {e}]")
print(f"¡{b}! Mi lenguaje de programación favorito es {c}")
print(f"El valor de PI o π: {e}")

# Transformación de String a lista - Todos los caracteres son parte de una lista
print("\nTRANSFORMACIÓN STRING A LISTA\n")
print(f"Transformación a lista list(mi_cadena): {list(mi_cadena)}")

# Transformación de List a String - UNa lista pasa a ser un String
print("\nTRANSFORMACIÓN LISTA A STRING\n")
mi_lista = [mi_subcadena1," y ",mi_subcadena2, "."]
print(mi_lista)
print(f"Pasar de lista a String (''.join(mi_lista)): {"".join(mi_lista)}")

# Transformación numérica
print("\nTRANSFORMACIÓN NUMÉRICA\n")

print("Como string")
mi_telefono = "987456321"
mi_pi = "3.14"
print(mi_telefono)
print(mi_pi)
print(type(mi_telefono))
print(type(mi_pi))

print("\nComo números")
print("Usamos int(<variable>) y float(<variable>)")
mi_telefono = int(mi_telefono)
mi_pi = float(mi_pi)
print(mi_telefono)
print(mi_pi)
print(type(mi_telefono))
print(type(mi_pi))

# Comprobaciones de tipo de dato
print("\nCOMPROBAR TIPO DE DATO\n")
print(f"Es caracter (mi_cadena.isalpha): {mi_cadena.isalpha}")
print(f"Es entero (mi_telefono.is_integer): {mi_telefono.is_integer}")
print(f"Es float (mi_pi.is_integer): {mi_pi.is_integer}")

# Verificación
print("\nVERIFICACIÓN\n")
print(f"Tipo de objeto (type(mi_cadena)): {type(mi_cadena)}")
if type(mi_cadena) == str:
    print("True")
else:
    print("False")
print(f"Es una instancia (isinstance(mi_cadena,str)): {isinstance(mi_cadena,str)}")
if isinstance(mi_cadena, str):
    print("True")
else:
    print("False")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

"""
Palíndromos

Habitualmente se entiende por palíndromo aquel que toma por unidad la letra, es decir, 
cuya última letra es la misma que la primera, la penúltima es la misma que la segunda, etc. 
Es el caso de palabras tales como reconocer o anilina.

Ejemplos
1. aba, 2. Ababa, 3. Abalaba, 4. acá, 5. acurruca, 6. ada, 7. Ada, 8. aérea, 9. agá
"""

"""
Anagramas

Un anagrama es una palabra que resulta de la transposición de todas las letras de otra palabra. 
Dicho de otra forma, una palabra es anagrama de otra si las dos tienen las mismas letras, 
con el mismo número de apariciones, pero en un orden diferente.

Ejemplos
1. Esqueleto / es el toque, 2. Amor / mora, 3. Necesario / escenario, 4. Alfabeto / aabeflot, 5. Roma / Omar
"""

"""
Isogramas

Un isograma es una palabra, frase o secuencia en la que no se repite ninguna letra. 
Es un conjunto de caracteres en el que cada letra aparece solo una vez. 

Ejemplos
1. "Amor" es un isograma, ya que ninguna de sus letras se repite.
2. "Casa" no es un isograma, porque la letra "a" aparece dos veces.
"""

print("\nEJERCICIO\n")

def preguntaFrases():
    primeraPalabra = input("Dame la Primera palabra: ")
    segundaPalabra = input("Dame la Segunda palabra: ")
    
    # Comprobamos que las palabras se nos han pasado
    if len(primeraPalabra) > 0 and len(segundaPalabra) > 0:
        # Revisamos si son Palíndromos
        esPalindromoPrimeraPalabra = esPalindromo(primeraPalabra.lower())
        esPalindromoSegundaPalabra = esPalindromo(segundaPalabra.lower())
        # Imprimimos el resultado
        if esPalindromoPrimeraPalabra and esPalindromoSegundaPalabra:
            print(f"Las palabras {primeraPalabra} y {segundaPalabra} son Palindromos.")
        # Resto de resultados
        else:
            # Solo Primera Palabra
            if esPalindromoPrimeraPalabra:
                print(f"La palabra {primeraPalabra} es un Palíndromo.")
            else:
                print(f"La palabra {primeraPalabra} NO es un Palíndromo.")
            # Solo Segunda Palabra
            if esPalindromoSegundaPalabra:
                print(f"La palabra {segundaPalabra} es un Palíndromo.")
            else:
                print(f"La palabra {primeraPalabra} NO es un Palíndromo.")
        
        # Comprobamos si es un Anagrama
        resultado = esAnagrama(primeraPalabra.lower(),segundaPalabra.lower())
        if resultado:
            print(f"Las palabras {primeraPalabra} y {segundaPalabra} son Anagramas.")
        else: 
            print(f"Las palabras {primeraPalabra} y {segundaPalabra} NO son Anagramas.")
            
        """
        En el ejecrició correguido sería:
        print(f"¿Las palabras {primeraPalabra} y {segundaPalabra} son Anagramas?: {sorted(primeraPalabra) == sorted(segundaPalabra)}")
        """    
        print(f"¿Las palabras {primeraPalabra} y {segundaPalabra} son Anagramas?: {sorted(primeraPalabra) == sorted(segundaPalabra)}")
            
        # Comprobamos si es un Isograma - Hererograma
        comprobarPrimeraPalabra = esIsogramaPrimerOrden(primeraPalabra.lower())
        comprobarSegundaPalabra = esIsogramaPrimerOrden(segundaPalabra.lower())
        if comprobarPrimeraPalabra and comprobarSegundaPalabra:
            print(f"Las palabras {primeraPalabra} y {segundaPalabra} son Isogramas de primer orden.")
        # Resto de resultados
        else:
            # Solo Primera Palabra
            if comprobarPrimeraPalabra:
                print(f"La palabra {primeraPalabra} es un Isogramas de primer orden.")
            else:
                print(f"La palabra {primeraPalabra} NO es un Isogramas de primer orden.")
            # Solo Segunda Palabra
            if comprobarSegundaPalabra:
                print(f"La palabra {segundaPalabra} es un Isogramas de primer orden.")
            else:
                print(f"La palabra {segundaPalabra} NO es un Isogramas de primer orden.")

        # Comprobamos si es un Isograma de segundo orden
        comprobarPrimeraPalabra = esIsogramaSegundoOrden(primeraPalabra.lower())
        comprobarSegundaPalabra = esIsogramaSegundoOrden(segundaPalabra.lower())
        if comprobarPrimeraPalabra and comprobarSegundaPalabra:
            print(f"Las palabras {primeraPalabra} y {segundaPalabra} son Isogramas de segundo orden.")
        # Resto de resultados
        else:
            # Solo Primera Palabra
            if comprobarPrimeraPalabra:
                print(f"La palabra {primeraPalabra} es un Isogramas de segundo orden.")
            else:
                print(f"La palabra {primeraPalabra} NO es un Isogramas de segundo orden.")
            # Solo Segunda Palabra
            if comprobarSegundaPalabra:
                print(f"La palabra {segundaPalabra} es un Isogramas de segundo orden.")
            else:
                print(f"La palabra {segundaPalabra} NO es un Isogramas de segundo orden.")   
            
        # Comprobamos si es un Isograma - Basado en la corrección del ejercicio
        comprobarPrimeraPalabra = esIsogramaContarLetras(primeraPalabra.lower())
        comprobarSegundaPalabra = esIsogramaContarLetras(segundaPalabra.lower())
        if comprobarPrimeraPalabra and comprobarSegundaPalabra:
            print(f"Las palabras {primeraPalabra} y {segundaPalabra} son Isogramas.")
        # Resto de resultados
        else:
            # Solo Primera Palabra
            if comprobarPrimeraPalabra:
                print(f"La palabra {primeraPalabra} es un Isogramas.")
            else:
                print(f"La palabra {primeraPalabra} NO es un Isogramas.")
            # Solo Segunda Palabra
            if comprobarSegundaPalabra:
                print(f"La palabra {segundaPalabra} es un Isogramas.")
            else:
                print(f"La palabra {segundaPalabra} NO es un Isogramas.") 
        
    else:
        print("Palabras no facilitadas para su comprobación")
        
# PALINDROMO             
def esPalindromo(palabra):
    # Recorremos una de las palabras (la segunda) al revés y la comparamos
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# ANAGRAMA
def esAnagrama(primeraPalabra,segundaPalabra):
    letraNoEncontrada = False
    # Recorremos la primera palabra y buscamos si alguna de sus letras no están en la segunda palabra
    for i in range(len(primeraPalabra)):
        if segundaPalabra.count(primeraPalabra[i]) == 0:
            letraNoEncontrada = True
            break
    # Recorremos la segunda palabra y buscamos si alguna de sus letras no están en la primera palabra
    for i in range(len(segundaPalabra)):
        if primeraPalabra.count(segundaPalabra[i]) == 0:
            letraNoEncontrada = True
            break
    # Si hay repetidas no es un Isograma
    if letraNoEncontrada:
        return False
    else:
        return True

# ISOGRAMA - HETEROGRAMA (Isograma de primer orden)
def esIsogramaPrimerOrden(palabra):
    letraRepetida = True
    # Recorremos las diferentes partes de la palabra y comprobamos si esta tiene alguna letra repetida
    for i in range(len(palabra)):
        if palabra.count(palabra[i]) > 1:
            letraRepetida = False
            break
    # Si hay repetidas no es un Isograma
    if letraRepetida:
        return True
    else:
        return False
    
def esIsogramaSegundoOrden(palabra):
    letraRepetida = True
    # Recorremos las diferentes letras y comprobamos si se repiten
    for i in range(len(palabra)):
        if palabra.count(palabra[i]) < 2:
            letraRepetida = False
            break
    # Si hay repetidas no es un Isograma
    if letraRepetida:
        return True
    else:
        return False
    
def esIsogramaContarLetras(palabra):
    # Inicimos un diccionario para almacenar las letras y el número de repeticiones de las mismas
    numeroLetras = {} 
    # Recorremos el string
    for letra in palabra:
        # Por cada letra que recorremos, asignamos en el diccionario la letra como clave y la cantidad como valor
        numeroLetras[letra] = numeroLetras.get(letra,0) + 1
    
    # Comprobamos la recurriencia de cada una de las letras
    esUnIsograma = True
    # Nos quedamos con el valor del primer elemento para comparar
    listaValores = list(numeroLetras.values())
    longitudIsograma = listaValores[0]
    
    # Recorremos el string
    for cantidad_letra in listaValores:
        if cantidad_letra != longitudIsograma:
            esUnIsograma = False
            break
    # Si hay repetidas no es un Isograma
    if esUnIsograma:
        return True
    else:
        return False
    
# Ejecutamos el programa
preguntaFrases()