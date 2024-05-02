"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
"""
palabra = "pera"
numero = 9
print(len(palabra))
print(palabra.find("o") ) # encuentra solo donde aparezca el primer caraacter en la app
print(palabra.count("a") ) # encuentra todo los caracteres dentro de la app 
print(palabra.replace("a", "e") ) #remprazamos los caracteres 
print(palabra.islower() ) # comprobamos si la palabra es minuscuka
print(palabra.isdigit()) # comprobamos si la palabra es un digito
print(palabra + " " +"nueva") #concardenacion de palabras
print(palabra.lower()) # colocamos la palabra en minuscula
print(palabra.split()) # convertimos la palabra en lista
print(palabra.upper()) # colocamos la palabra en mayuscula
print(palabra[::-1]) #reverso de unaa cadena 
print(palabra[3:6]) #cortando cadena
print("hola %s %d" % (palabra,numero)) #interpolacion
print(f"mi palabra es {palabra} mi numero es {numero}")
print("Mi palabrra es {} y mi numero es {}".format(palabra,numero)) #interpolacion









 


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */"""
 
def palidromo():
    palabra = input("Ingrese la palabra para comprobar si es un anagrama: ").lower()
    palabra2 = palabra[::-1]
    if (palabra == palabra2):
        return f"La palabra {palabra}\nEs un palidromo."
    else:
        return f"La palabra {palabra}/nNo es un palidromo."   
#print(palidromo())

def anagrama():
    tx1 = input("Ingrese la primera palabra: ").lower()
    txt2 = input("Ingrese la segunda palabra: ").lower()

    if len(sorted(tx1)) == len(sorted(txt2)):
        return f"La palabra {tx1}y la palabra {txt2}:\nSon un anagrama."
    else:
        return f"La palabra {tx1} y la palabra {txt2}:\nNo son anagrama." 
#print(anagrama())

def isograma():
    palabra = "repeticion"
    nuevaPalabra = set(palabra.lower())
    
    if (len(nuevaPalabra) == len(nuevaPalabra)):
        return "La palabra {} \nEs un Isograma".format(palabra)

print(isograma())

