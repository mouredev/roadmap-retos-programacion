"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

texto = "Hola, python"
texto_2 = "2024"
texto_3 = "JUAN ROMAN "
texto_4 = "JRR, JRR, JRR, NJ"

#Acceso a caracter por posiscion - letra l
print(texto[2])

#Longitud de caracteres
print(len(texto))

#Concatenacion
print(texto + " " + texto_2)

#Subcadena
subcadena = texto[6:12]
print(subcadena)

#Mayusculas
print(texto.upper())

#Minusculas
print(texto_3.lower())

#Remplazo
texto_remplazo = texto.replace("Hola", "Adios")
print(texto_remplazo)

#Division - Split
texto_dividido = texto.split()
print(texto_dividido)

#Comprobar si es numero el string
print(texto.isdigit())
print(texto_2.isdigit())

#Recorrido de string
for letra in texto:
    print(letra)

#Repeticion
print(3 * texto_3)

#Verificacion - Las mayusculas importan
contiene = "JUAN" in texto_3
print(contiene)

contiene = "juan" in texto_3
print(contiene)

#Contar subcadenas
cuantas_veces_JRR = texto_4.count("JRR")
print(cuantas_veces_JRR)

#Interpolacion
mensaje = "Hola, soy {} y estamos en el {}.".format(texto_3, texto_2)
print(mensaje)

#f-string
print(f"{texto} es la primera frase que imprimi en {texto_2}")

#Join

#RETO -> Recibe 2 palabras str

#PALINDROMO - Se lee igual de izquierda a derecha que de dercha a izquierda - OK

#ANAGRAMA - 2 Palabras que contiene las mismas letras pero en diferente orden
#Eg. Amor - Roma

#ISOGRAMAS - Palabra en la cual no se repiten letras
#Eg. Murcielago
    
def comprobacion_palabras(txt_1, txt_2):
    txt_1 = txt_1.lower()
    txt_2 = txt_2.lower()
    #Verificar Palindromo
    def palindromo(txt_palindromo):
        vacio = "" #String vacio para reordenar
        for letra in txt_palindromo: #Bucle for que recorre todas las letras de la palabra que se quiere verificar
            vacio = letra + vacio #Asignacion de la letra al string
        if vacio == txt_palindromo: #En casos que la palabra invertida y la normal sean igual se confirma que es un palindromo
            print(f"La palabra {txt_palindromo} es un palindromo")
        else: #En caso de no coincidir se sabe que no es un palindromo 
            print(f"La palabra {txt_palindromo} NO es un palindromo")
    #Aplicar revision a las dos palabras
    palindromo(txt_1)
    palindromo(txt_2)
    #Verificar Anagrama
    longitud_palabra_1 = len(txt_1) #Obetener la longitud de la palabra #1
    longitud_palabra_2 = len(txt_2) #Obetener la longitud de la palabra #2
    cuenta_de_true = 0 #Cuenta para verifica la cantidad de True
    if longitud_palabra_1 == longitud_palabra_2: #Los anagramas deben tener el mismo numero de palabras - Primea verificacion
        for letra in txt_1: #Bucle for para revisar que cada letra de la palabra 1 sea reccorida
            verificacion = letra in txt_2 #Busqueda de la letra perteneciente a la palabra 1 en la palabra 2 
            if verificacion == False: #En caso de que exita un false se sabe que ya no es un anagrama, se rompe el bucle e imprime - Segunda verificacion
                print(f"Las palabras {txt_1} y {txt_2} no son un Anagrama.")
                break
            else:
                cuenta_de_true = cuenta_de_true +1 #Caso de que sea True se suma a la variable global para llevar la cuenta y comparar luego
    else:
        print(f"Las palabras {txt_1} y {txt_2} no son un Anagrama.") #Si no son iguales ya se sabe que no es un anagrama
    if cuenta_de_true == longitud_palabra_1: #Si la cantidad de true es igual a la longitud de las palabras se sabe que es un anagrama - Tercera verificacion
        print(f"las palabras {txt_1} y {txt_2} son un Anagrama.")
    #Verificar Isograma
    def isograma(palabra_isograma):
        isograma_medidor = 0 #Cuenta para verifica cuando acabe el bucle for y poder comprobar que todas las letras este solo una vez 
        longitud_palabra_isograma = len(palabra_isograma) #longitud de la palabra
        for letra in palabra_isograma: #Bucle for para revisar que cada letra de la palabra sea reccorida
            conteo = palabra_isograma.count(letra) #Contar cuantas veces está la palabra
            if conteo != 1: #condicion que determina que no es un isogrma ya que 'x' letra está mas de una vez
                print(f"la palabra {palabra_isograma} no es un isograma.")
                break #Romper el bucle for
            else:
                isograma_medidor = isograma_medidor + 1 #Ir aumentado el contador cada vez que 'x' letra este solo una vez
        if isograma_medidor == longitud_palabra_isograma:
            print(f"la palabra {palabra_isograma} es un isograma.") #ultima verificacion para imprimir que es un isograma
                
    isograma(txt_1)
    isograma(txt_2)

comprobacion_palabras("aMor", "Roma")